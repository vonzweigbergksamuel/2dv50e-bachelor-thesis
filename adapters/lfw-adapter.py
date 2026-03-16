import os
import shutil
from pathlib import Path

IGNORED_FOLDERS = [".DS_Store"]
PATH_PREFIX = "lfw-deepfunneled"


def adapter():
    path = Path(__file__).parent.parent / "data" / "LFW"
    entry_path = path  # / PATH_PREFIX / PATH_PREFIX

    subjects = os.listdir(entry_path)

    for subject in subjects:
        subject_path = entry_path / subject
        if subject in IGNORED_FOLDERS or not subject_path.is_dir():
            continue

        images = os.listdir(subject_path)
        if len(images) < 2:
            shutil.rmtree(subject_path)
            continue

        # shutil.move(subject_path, path)

    # os.removedirs(entry_path)


adapter()

# import os
# import shutil
# from pathlib import Path


# def adapter():
#     path_prefix = "lfw-deepfunneled"
#     path = Path(__file__).parent.parent / "data" / "LFW"
#     entry_path = path / path_prefix / path_prefix

#     subjects = os.listdir(entry_path)

#     for subject in subjects:
#         subject_path = entry_path / subject

#         shutil.move(subject_path, path)

#     os.removedirs(entry_path)


# adapter()
