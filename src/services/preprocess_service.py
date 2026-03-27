# This service is used to preprocess the datasets, ie. split them into training and testing sets.
import os
import pathlib
import time

from deepface import DeepFace

from config import DETECTOR_BACKEND, GOOGLE_SHEET_FILE, RESULTS_FILE
from services.print_service import show_progress

##############################
# CONSTANTS
##############################
UNKNOWN = "Unknown"


def pre_process(dataset_path: pathlib.Path, model: str):
    """
    Preprocesses the dataset by splitting it into a known and unknown set.
    """
    all_subjects = []
    time_per_run = []

    identities = sorted(os.listdir(dataset_path))

    completed_identities = 0

    for identity in identities:
        identity_path = dataset_path / identity
        images = sorted(os.listdir(identity_path))

        if len(images) < 2:
            continue

        embedded_images = []
        for image in images:
            image_path = identity_path / image
            start_time = time.perf_counter()
            embedded_image = DeepFace.represent(
                img_path=image_path, model_name=model, detector_backend=DETECTOR_BACKEND
            )
            end_time = time.perf_counter()
            time_per_run.append(end_time - start_time)

            embedded_images.append(embedded_image[0]["embedding"])

        all_subjects.append({"identity": identity, "images": embedded_images})

        completed_identities += 1
        show_progress("Preprocessing", completed_identities, len(identities))

    avg_time_per_embedding = sum(time_per_run) / len(time_per_run)

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
