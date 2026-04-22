# This service is used to preprocess the datasets, ie. split them into training and testing sets.
import os
import pathlib
import time

from deepface import DeepFace

from config import DETECTOR_BACKEND, GOOGLE_SHEET_FILE, RESULTS_FILE, IMAGE_EXTENSIONS
from services.print_service import show_progress


def pre_process(dataset_path: pathlib.Path, model: str):
    """
    Preprocesses the dataset by splitting it into a known and unknown set.
    """
    all_subjects = []
    time_per_run = []

    identities = sorted(
        d for d in os.listdir(dataset_path) if (dataset_path / d).is_dir()
    )

    number_of_identities = len(identities)

    completed_identities = 0

    for identity in identities:
        identity_path = dataset_path / identity
        images = sorted(
            f
            for f in os.listdir(identity_path)
            if pathlib.Path(f).suffix.lower() in IMAGE_EXTENSIONS
        )

        if len(images) < 2:
            number_of_identities -= 1
            continue

        embedded_images = []
        for image in images:
            image_path = identity_path / image
            try:
                start_time = time.perf_counter()
                embedded_image = DeepFace.represent(
                    img_path=str(image_path),
                    model_name=model,
                    detector_backend=DETECTOR_BACKEND,
                    enforce_detection=False,
                )
                end_time = time.perf_counter()
                time_per_run.append(end_time - start_time)
                embedded_images.append(embedded_image[0]["embedding"])
            except Exception as e:
                print(f"  [SKIP] Failed to embed {image_path}: {e}")

        if len(embedded_images) < 2:
            number_of_identities -= 1
            continue

        all_subjects.append({"identity": identity, "images": embedded_images})

        completed_identities += 1
        show_progress("Preprocessing", completed_identities, number_of_identities)

    avg_time_per_embedding = (
        sum(time_per_run) / len(time_per_run) if time_per_run else 0.0
    )

    return all_subjects, avg_time_per_embedding


def set_up_directories():
    """
    Sets up the directories for the project.
    """
    # Create result file
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write("")

    # Create google sheet file
    with open(GOOGLE_SHEET_FILE, "w", encoding="utf-8") as f:
        f.write("")
