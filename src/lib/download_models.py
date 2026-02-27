from deepface import DeepFace
from config import MODELS, DETECTOR_BACKEND
from services.print_service import show_progress

def download_models():
  """
  Downloads the models and detector backend.
  """
  print("Downloading models and detector backend...")
  total_models = len(MODELS) + 1
  completed_models = 0
  
  for model in MODELS:
      DeepFace.build_model(model, task="facial_recognition")
      completed_models += 1
      show_progress(completed_models, total_models)

  DeepFace.build_model(DETECTOR_BACKEND, task="face_detector")
  completed_models += 1
  show_progress(completed_models, total_models)

  print("Models and detector backend downloaded!")