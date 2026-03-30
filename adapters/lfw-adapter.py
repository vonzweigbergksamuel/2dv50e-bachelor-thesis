import os
import shutil
from pathlib import Path

IGNORED_FOLDERS = [".DS_Store"]
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}
PATH_PREFIX = "lfw-deepfunneled"


def adapter():
    path = Path(__file__).parent.parent / "data" / "LFW"
    entry_path = path # / PATH_PREFIX / PATH_PREFIX

    subjects = os.listdir(entry_path)

    for subject in subjects:
        subject_path = entry_path / subject
        if subject in IGNORED_FOLDERS or not subject_path.is_dir():
            continue

        all_files = os.listdir(subject_path)
        images = [f for f in all_files if Path(f).suffix.lower() in IMAGE_EXTENSIONS]

        for non_image in set(all_files) - set(images):
            (subject_path / non_image).unlink()

        if len(images) < 2:
            shutil.rmtree(subject_path)
            continue

    #     shutil.move(subject_path, path)

    # os.removedirs(entry_path)
    print(f"Adapter completed for {PATH_PREFIX}")


adapter()
