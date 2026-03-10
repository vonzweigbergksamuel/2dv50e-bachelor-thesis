# This service is used to preprocess the datasets, ie. split them into training and testing sets.
import pathlib
from dataclasses import dataclass

from sklearn.model_selection import train_test_split

RESULTS_FILE = "results.txt"
GOOGLE_SHEET_FILE = "google_sheet.txt"

UNKNOWN = "Unknown"


@dataclass(frozen=True)
class ExperimentImage:
    path: pathlib.Path
    label: str


@dataclass(frozen=True)
class ExperimentSplit:
    db: list[ExperimentImage]
    test_known: list[ExperimentImage]
    test_unknown: list[ExperimentImage]


def load_dataset(dataset_path: pathlib.Path) -> dict[str, list[pathlib.Path]]:
    """
    Loads the dataset into a subject -> image paths mapping.
    """
    subjects: dict[str, list[pathlib.Path]] = {}

    for subject_path in sorted(dataset_path.iterdir()):
        if not subject_path.is_dir():
            continue

        images = sorted(path for path in subject_path.iterdir() if path.is_file())
        if images:
            subjects[subject_path.name] = images

    return subjects


def pre_process(
    dataset: dict[str, list[pathlib.Path]], random_state: int
) -> ExperimentSplit:
    """
    Splits the dataset into known DB images and test images.
    """
    valid_identities = sorted(
        subject for subject, images in dataset.items() if len(images) >= 2
    )

    if len(valid_identities) < 2:
        raise ValueError(
            "Dataset must contain at least two identities with two images."
        )

    known_subjects, unknown_subjects = train_test_split(
        valid_identities, test_size=0.5, train_size=0.5, random_state=random_state
    )

    db_images: list[ExperimentImage] = []
    test_known_images: list[ExperimentImage] = []
    test_unknown_images: list[ExperimentImage] = []

    for subject in sorted(known_subjects):
        db, test = train_test_split(
            dataset[subject], test_size=0.5, train_size=0.5, random_state=random_state
        )
        db_images.extend(
            ExperimentImage(path=image_path, label=subject) for image_path in db
        )
        test_known_images.extend(
            ExperimentImage(path=image_path, label=subject) for image_path in test
        )

    for subject in sorted(unknown_subjects):
        _, test = train_test_split(
            dataset[subject], test_size=0.5, train_size=0.5, random_state=random_state
        )
        test_unknown_images.extend(
            ExperimentImage(path=image_path, label=UNKNOWN) for image_path in test
        )

    return ExperimentSplit(
        db=db_images,
        test_known=test_known_images,
        test_unknown=test_unknown_images,
    )


def set_up_directories():
    """
    Resets the output files for the project.
    """
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write("")

    with open(GOOGLE_SHEET_FILE, "w", encoding="utf-8") as f:
        f.write("")
