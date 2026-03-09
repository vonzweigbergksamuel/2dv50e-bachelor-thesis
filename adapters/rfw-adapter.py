import os
import shutil
from pathlib import Path
import random


def adapter():
    path = Path(__file__).parent.parent / "data" / "RFW"

    folders = os.listdir(path)

    for folder in folders:
        folder_path = path / folder
        subjects = os.listdir(folder_path)

        for subject in subjects:
            subject_path = folder_path / subject
            dest = path / subject
            if dest.exists():
                dest = path / f"{subject}_{random.random()}"
            shutil.move(str(subject_path), str(dest))

        os.removedirs(folder_path)


adapter()
