# This service is used to interface with the DeepFace framework.
import os
import pathlib
from deepface import DeepFace
from services.preprocess_service import TEST_SUBJECTS_FOLDER, UNKNOWN
from config import DISTANCE_METRIC, DETECTOR_BACKEND

def run_experiment(model: str):
  """
  Runs an experiment with the given model and seed.
  """  
  project_root = pathlib.Path(__file__).parent.parent.parent
  TEST_SUBJECTS_PATH = project_root / TEST_SUBJECTS_FOLDER
  
  TEST_SUBJECTS = os.listdir(TEST_SUBJECTS_PATH)
  
  # print(f"TEST_SUBJECTS_IMAGES: {TEST_SUBJECTS}")

  actual_result = []
  predicted_result = []
  
  for subject in TEST_SUBJECTS:    
    subject_images = os.listdir(TEST_SUBJECTS_PATH / subject)
    
    # print(subject_images)
    
    for image in subject_images:
      actual_result.append(subject)
      
      image_path = TEST_SUBJECTS_PATH / subject / image
      
      search_result = DeepFace.search(
        img=image_path,
        model_name=model,
        distance_metric=DISTANCE_METRIC,
        detector_backend=DETECTOR_BACKEND,
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
  
  return actual_result, predicted_result