import os
import shutil
from services.preprocess_service import DB_FOLDER, TEST_SUBJECTS_FOLDER

def clean_up():
  """
  Cleans up the folders created by the preprocess service.
  """
  print("Cleaning up...")
  if os.path.exists(DB_FOLDER):
    shutil.rmtree(DB_FOLDER)
  if os.path.exists(TEST_SUBJECTS_FOLDER):
    shutil.rmtree(TEST_SUBJECTS_FOLDER)