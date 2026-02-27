import os
import shutil
from services.preprocess_service import TEST_SUBJECTS_FOLDER

def clean_up():
  """
  Cleans up the folders created by the preprocess service.
  """
  print("Cleaning up...")
  if os.path.exists(TEST_SUBJECTS_FOLDER):
    shutil.rmtree(TEST_SUBJECTS_FOLDER)
    
  # TODO: Add a cleaner for postgres database