from sklearn.model_selection import train_test_split

from config import UNKNOWN


def splitting_service(subjects: list[dict], random_state: int):
    """
    Splits the subjects into a known and unknown set.
    """

    known, unknown = _split(subjects, random_state)
    known_subjects = []
    unknown_subjects = []

    for subject in known:
        known_images, unknown_images = _split(subject["images"], random_state)
        known_subjects.append(
            {
                "identity": subject["identity"],
                "known_images": known_images,
                "unknown_images": unknown_images,
            }
        )

    for subject in unknown:
        unknown_images, _ = _split(subject["images"], random_state)
        unknown_subjects.append({"identity": UNKNOWN, "unknown_images": unknown_images})

    return known_subjects, unknown_subjects


def _split(array: list, random_state: int):
    """
    Splits the array into a training and testing set.
    """
    return train_test_split(
        array, test_size=0.5, train_size=0.5, random_state=random_state
    )
