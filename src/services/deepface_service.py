# This service is used to interface with the DeepFace framework.
import os
import pathlib
import time

from deepface import DeepFace

from config import DETECTOR_BACKEND, DISTANCE_METRIC
from services.preprocess_service import TEST_SUBJECTS_FOLDER, UNKNOWN


def run_experiment(model: str):
    """
    Runs an experiment with the given model and seed.
    """
    project_root = pathlib.Path(__file__).parent.parent.parent
    TEST_SUBJECTS_PATH = project_root / TEST_SUBJECTS_FOLDER

    TEST_SUBJECTS = os.listdir(TEST_SUBJECTS_PATH)

    TEST_SUBJECTS = sorted(TEST_SUBJECTS)

    COMPLETED_SUBJECTS = 0

    # print(f"TEST_SUBJECTS_IMAGES: {TEST_SUBJECTS}")

    actual_result = []
    predicted_result = []
    avg_time_per_subject = []

    for subject in TEST_SUBJECTS:
        subject_images = sorted(os.listdir(TEST_SUBJECTS_PATH / subject))

        # print(subject_images)

        time_per_images = []

        unknown_completed_images = 0

        for image in subject_images:
            actual_result.append(subject)

            image_path = TEST_SUBJECTS_PATH / subject / image

            start_time = time.perf_counter()
            search_result = DeepFace.search(
                img=image_path,
                model_name=model,
                distance_metric=DISTANCE_METRIC,
                detector_backend=DETECTOR_BACKEND,
            )
            end_time = time.perf_counter()

            time_per_images.append(end_time - start_time)

            if subject == UNKNOWN:
                unknown_completed_images += 1
                print(
                    f"Completed {unknown_completed_images} of {len(subject_images)} unknown images"
                )

            # DeepFace.search may return a DataFrame or a list of DataFrames
            if isinstance(search_result, list):
                if not search_result:
                    predicted_result.append(UNKNOWN)
                    continue
                df = search_result[0]
            else:
                df = search_result

            if len(df) == 0:
                predicted_result.append(UNKNOWN)
            else:
                top_match = df.iloc[0]
                predicted_result.append(top_match["img_name"])

        COMPLETED_SUBJECTS += 1
        print(f"Completed {COMPLETED_SUBJECTS} of {len(TEST_SUBJECTS)} subjects")

        avg_time_per_subject.append(sum(time_per_images) / len(time_per_images))

    avg_time = sum(avg_time_per_subject) / len(avg_time_per_subject)

    return actual_result, predicted_result, avg_time
