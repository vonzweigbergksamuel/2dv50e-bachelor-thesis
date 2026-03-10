# This service is used to interface with the DeepFace framework.
import pathlib
import time

from deepface import DeepFace
from deepface.modules import verification

from config import DETECTOR_BACKEND, DISTANCE_METRIC
from services.preprocess_service import UNKNOWN, ExperimentImage, ExperimentSplit


def build_embedding_cache(
    dataset: dict[str, list[pathlib.Path]], model: str
) -> dict[pathlib.Path, list[float]]:
    """
    Computes embeddings once for all images in a dataset for a given model.
    """
    embeddings: dict[pathlib.Path, list[float]] = {}

    for image_paths in dataset.values():
        for image_path in image_paths:
            embedding = _extract_embedding(image_path, model)
            if embedding is not None:
                embeddings[image_path] = embedding

    return embeddings


def run_experiment(
    model: str,
    split: ExperimentSplit,
    embedding_cache: dict[pathlib.Path, list[float]],
) -> tuple[list[str], list[str], float, float, float]:
    """
    Runs an experiment against a trial-specific gallery built from known DB images.
    """
    gallery_start = time.perf_counter()
    gallery_labels, gallery_embeddings = _build_gallery(split.db, embedding_cache)
    gallery_time = time.perf_counter() - gallery_start

    threshold = verification.find_threshold(
        model_name=model, distance_metric=DISTANCE_METRIC
    )

    actual_result: list[str] = []
    predicted_result: list[str] = []
    avg_time_per_subject: list[float] = []

    grouped_test_images = _group_test_images(split)

    match_start = time.perf_counter()
    for subject, subject_images in grouped_test_images.items():
        time_per_images = []

        for image in subject_images:
            actual_result.append(subject)

            image_start = time.perf_counter()
            predicted_result.append(
                _match_image(
                    image.path,
                    gallery_labels,
                    gallery_embeddings,
                    embedding_cache,
                    threshold,
                )
            )
            time_per_images.append(time.perf_counter() - image_start)

        if time_per_images:
            avg_time_per_subject.append(sum(time_per_images) / len(time_per_images))

    match_time = time.perf_counter() - match_start
    avg_time = (
        sum(avg_time_per_subject) / len(avg_time_per_subject)
        if avg_time_per_subject
        else 0.0
    )

    return actual_result, predicted_result, avg_time, gallery_time, match_time


def _extract_embedding(image_path: pathlib.Path, model: str) -> list[float] | None:
    try:
        embedding_objs = DeepFace.represent(
            img_path=image_path,
            model_name=model,
            detector_backend=DETECTOR_BACKEND,
        )
    except ValueError:
        return None

    if not embedding_objs:
        return None

    return embedding_objs[0].get("embedding")


def _build_gallery(
    db_images: list[ExperimentImage],
    embedding_cache: dict[pathlib.Path, list[float]],
) -> tuple[list[str], list[list[float]]]:
    gallery_labels: list[str] = []
    gallery_embeddings: list[list[float]] = []

    for image in db_images:
        embedding = embedding_cache.get(image.path)
        if embedding is None:
            continue
        gallery_labels.append(image.label)
        gallery_embeddings.append(embedding)

    return gallery_labels, gallery_embeddings


def _group_test_images(split: ExperimentSplit) -> dict[str, list[ExperimentImage]]:
    grouped_images: dict[str, list[ExperimentImage]] = {}

    for image in [*split.test_known, *split.test_unknown]:
        grouped_images.setdefault(image.label, []).append(image)

    return dict(sorted(grouped_images.items()))


def _match_image(
    image_path: pathlib.Path,
    gallery_labels: list[str],
    gallery_embeddings: list[list[float]],
    embedding_cache: dict[pathlib.Path, list[float]],
    threshold: float,
) -> str:
    query_embedding = embedding_cache.get(image_path)
    if query_embedding is None or not gallery_embeddings:
        return UNKNOWN

    distances = verification.find_distance(
        [query_embedding], gallery_embeddings, DISTANCE_METRIC
    )
    best_index = min(
        range(len(gallery_labels)),
        key=lambda index: float(distances[index][0]),
    )
    best_distance = float(distances[best_index][0])

    if best_distance <= threshold:
        return gallery_labels[best_index]

    return UNKNOWN
