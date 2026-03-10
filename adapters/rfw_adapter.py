import os
import random
import shutil
from pathlib import Path

IGNORED_FOLDERS = [".DS_Store"]


def adapter():
    path = Path(__file__).parent.parent / "data" / "RFW"

    folders = os.listdir(path)

    for folder in folders:
        folder_path = path / folder
        if folder in IGNORED_FOLDERS or not folder_path.is_dir():
            continue

        subjects = os.listdir(folder_path)

        for subject in subjects:
            subject_path = folder_path / subject
            dest = path / subject
            if dest.exists():
                dest = path / f"{subject}_{random.random()}"
            shutil.move(str(subject_path), str(dest))

        os.removedirs(folder_path)


adapter()
