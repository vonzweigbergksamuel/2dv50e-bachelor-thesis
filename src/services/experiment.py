import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from deepface.modules.verification import find_threshold

from services import database_service
from services.preprocess_service import UNKNOWN


def run_experiment(model: str, known_subjects: list[dict], unknown_subjects: list[dict]):
    """
    Runs the experiment for a given model, known subjects and unknown subjects.
    """
    db_subjects = database_service.get_all_subjects()
    threshold = find_threshold(model, "cosine")

    db_embeddings = np.array([s["embedding"] for s in db_subjects])
    db_identities = [s["identity"] for s in db_subjects]

    actual = []
    predicted = []

    for subject in known_subjects:
        for embedding in subject["unknown_images"]:
            actual.append(subject["identity"])
            predicted.append(_predict(embedding, db_embeddings, db_identities, threshold))

    for subject in unknown_subjects:
        for embedding in subject["unknown_images"]:
            actual.append(UNKNOWN)
            predicted.append(_predict(embedding, db_embeddings, db_identities, threshold))

    return actual, predicted


def _predict(embedding, db_embeddings, db_identities, threshold):
    distances = 1 - cosine_similarity([embedding], db_embeddings)[0]
    min_idx = np.argmin(distances)

    if distances[min_idx] < threshold:
        return db_identities[min_idx]
    return UNKNOWN
