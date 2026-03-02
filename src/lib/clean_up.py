import os
import shutil
from services.preprocess_service import TEST_SUBJECTS_FOLDER

def clean_up_folder():
  """
  Cleans up the folders created by the preprocess service.
  """
  print("Cleaning up...")
  if os.path.exists(TEST_SUBJECTS_FOLDER):
    shutil.rmtree(TEST_SUBJECTS_FOLDER)
    
  
def clean_up_database():
  """
  Cleans up the database.
  """
  # TODO: Add a cleaner for postgres database
  pass