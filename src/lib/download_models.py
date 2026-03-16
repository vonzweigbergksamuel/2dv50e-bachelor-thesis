from deepface import DeepFace

from config import DETECTOR_BACKEND, MODELS
from services.print_service import print_current_status, show_progress


def download_models():
    """
    Downloads the models and detector backend.
    """
    print_current_status("Downloading models and detector backend...")
    total_models = len(MODELS) + 1
    completed_models = 0

    for model in MODELS:
        DeepFace.build_model(model, task="facial_recognition")
        completed_models += 1
        show_progress("Downloading models", completed_models, total_models)

    DeepFace.build_model(DETECTOR_BACKEND, task="face_detector")
    completed_models += 1
    show_progress("Downloading models", completed_models, total_models)

    print_current_status("Models and detector backend downloaded!")
