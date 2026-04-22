import os
import random
import shutil
from pathlib import Path

IGNORED_FOLDERS = [".DS_Store"]
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif", ".webp"}
PATH_PREFIX = "RFW"


def adapter():
    path = Path(__file__).parent.parent / "data" / PATH_PREFIX

    folders = os.listdir(path)

    for folder in folders:
        folder_path = path / folder
        if folder in IGNORED_FOLDERS or not folder_path.is_dir():
            continue

        all_entries = os.listdir(folder_path)
        subjects = [s for s in all_entries if (folder_path / s).is_dir()]

        for non_dir in set(all_entries) - set(subjects):
            (folder_path / non_dir).unlink()

        for subject in subjects:
            subject_path = folder_path / subject
            all_files = os.listdir(subject_path)
            images = [
                f for f in all_files if Path(f).suffix.lower() in IMAGE_EXTENSIONS
            ]

            for non_image in set(all_files) - set(images):
                (subject_path / non_image).unlink()

            if len(images) < 2:
                shutil.rmtree(subject_path)
                continue

            dest = path / subject
            if dest.exists():
                dest = path / f"{subject}_{random.random()}"

            shutil.move(str(subject_path), str(dest))

        os.removedirs(folder_path)

    print(f"Adapter completed for {PATH_PREFIX}")


adapter()
