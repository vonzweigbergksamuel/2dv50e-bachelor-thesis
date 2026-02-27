# This service is used to preprocess the datasets, ie. split them into training and testing sets.
import os
import shutil
import pathlib
from sklearn.model_selection import train_test_split
from lib.generate_random_state import generate_random_state

DB_FOLDER = "db"
TEST_SUBJECTS_FOLDER = "test_subjects"

def pre_process(dataset_path: pathlib.Path, random_state: int = generate_random_state()):
  """
  Preprocesses the dataset by splitting it into a known and unknown set.
  """
  print("Preprocessing dataset from: ", dataset_path)
  # Create the folders if they don't exist
  os.makedirs(DB_FOLDER, exist_ok=True)
  os.makedirs(TEST_SUBJECTS_FOLDER, exist_ok=True)
  
  identities = os.listdir(dataset_path)
  
  # Split the identities into known and unknown
  known, unkown = train_test_split(identities, test_size=0.5, train_size=0.5, random_state=random_state)
  
  # Split the known subjects into known and unknown images.
  for subject in known:
    subject_path = dataset_path / subject
    
    images = os.listdir(subject_path)
    
    db, test = train_test_split(images, test_size=0.5, train_size=0.5, random_state=random_state)

    # Copy the known images to the DB folder
    for image in db:
      img_path = subject_path / image
      
      dest = dataset_path.parent.parent / DB_FOLDER / subject
      copy_to_folder(img_path, dest)
      
    # Copy the known images to the TEST_SUBJECTS folder
    for image in test:
      img_path = subject_path / image
      
      dest = dataset_path.parent.parent / TEST_SUBJECTS_FOLDER / subject
      copy_to_folder(img_path, dest)
      
  # Split the unknown subjects into unknown images.
  for subject in unkown:
    subject_path = dataset_path / subject
    
    images = os.listdir(subject_path)
    
    _, test = train_test_split(images, test_size=0.5, train_size=0.5, random_state=random_state)
    
    # Copy the unknown images to the TEST_SUBJECTS folder
    for image in test:
      img_path = subject_path / image
      
      dest = dataset_path.parent.parent / TEST_SUBJECTS_FOLDER / subject
      copy_to_folder(img_path, dest)
      
  return random_state

def copy_to_folder(src: pathlib.Path, dest_dir: pathlib.Path):
  os.makedirs(dest_dir, exist_ok=True)
  shutil.copyfile(src, dest_dir / src.name)
  