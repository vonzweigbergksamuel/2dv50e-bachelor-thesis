# This service is used to preprocess the datasets, ie. split them into training and testing sets.
import os
import pathlib
import shutil

from deepface import DeepFace
from sklearn.model_selection import train_test_split

from config import DETECTOR_BACKEND

##############################
# FOLDERS & FILES
##############################
TEST_SUBJECTS_FOLDER = "test_subjects"
RESULTS_FILE = "results.txt"
GOOGLE_SHEET_FILE = "google_sheet.txt"


##############################
# CONSTANTS
##############################
UNKNOWN = "Unknown"
NUMBER_OF_UNKNOWN_IMAGES = 0


def pre_process(dataset_path: pathlib.Path, random_state: int):
    """
    Preprocesses the dataset by splitting it into a known and unknown set.
    """
    img_to_db = []

    # Create the folders if they don't exist
    os.makedirs(TEST_SUBJECTS_FOLDER, exist_ok=True)

    identities = sorted(os.listdir(dataset_path))
    print(f"Identities: {identities}")

    # Split the identities into known and unknown
    known, unkown = train_test_split(
        identities, test_size=0.5, train_size=0.5, random_state=random_state
    )

    # Split the known subjects into known and unknown images.
    for subject in known:
        subject_path = dataset_path / subject

        images = sorted(os.listdir(subject_path))
        print(f"Images: {images}")

        if len(images) < 2:
            # remove the subject from the known list
            known.remove(subject)
            continue

        db, test = train_test_split(
            images, test_size=0.5, train_size=0.5, random_state=random_state
        )

        # Copy the known images to the DB folder
        for image in db:
            img_path = subject_path / image

            img_to_db.append({"path": img_path, "name": subject})

        # Copy the known images to the TEST_SUBJECTS folder
        for image in test:
            img_path = subject_path / image

            dest = dataset_path.parent.parent / TEST_SUBJECTS_FOLDER / subject
            copy_to_test_subjects_folder(img_path, dest)

    # Split the unknown subjects into unknown images.
    for subject in unkown:
        subject_path = dataset_path / subject

        images = sorted(os.listdir(subject_path))

        if len(images) < 2:
            # remove the subject from the unknown list
            unkown.remove(subject)
            continue

        _, test = train_test_split(
            images, test_size=0.5, train_size=0.5, random_state=random_state
        )

        # Copy the unknown images to the TEST_SUBJECTS folder
        for image in test:
            img_path = subject_path / image

            dest = dataset_path.parent.parent / TEST_SUBJECTS_FOLDER / UNKNOWN
            copy_to_test_subjects_folder(img_path, dest)

    print(f"Known: {known}")
    print(f"Unknown: {unkown}")

    return img_to_db


def copy_to_test_subjects_folder(src: pathlib.Path, dest_dir: pathlib.Path):
    """
    Copies a file to the test subjects folder.
    """
    global NUMBER_OF_UNKNOWN_IMAGES
    NUMBER_OF_UNKNOWN_IMAGES += 1

    os.makedirs(dest_dir, exist_ok=True)

    shutil.copyfile(src, dest_dir / f"{NUMBER_OF_UNKNOWN_IMAGES}{src.suffix}")


def insert_into_database(img_to_db: list[dict], model: str):
    """
    Inserts the images into the database.
    """
    for img in img_to_db:
        DeepFace.register(
            img=img["path"],
            img_name=img["name"],
            model_name=model,
            detector_backend=DETECTOR_BACKEND,
        )


def set_up_directories():
    """
    Sets up the directories for the project.
    """
    os.makedirs(TEST_SUBJECTS_FOLDER, exist_ok=True)

    # Create result file
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write("")

    # Create google sheet file
    with open(GOOGLE_SHEET_FILE, "w", encoding="utf-8") as f:
        f.write("")
