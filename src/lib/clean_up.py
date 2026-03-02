import os
import shutil
from services.preprocess_service import TEST_SUBJECTS_FOLDER
import contextlib
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

_raw = os.getenv("DEEPFACE_POSTGRES_URI", "")
POSTGRES_URI = _raw.replace("postgresql://", "postgresql+psycopg://", 1) if _raw else ""

def clean_up_folder():
  """
  Cleans up the folders created by the preprocess service.
  """
  if os.path.exists(TEST_SUBJECTS_FOLDER):
    shutil.rmtree(TEST_SUBJECTS_FOLDER)
    
  
def clean_up_database():
  """
  Cleans up the database.
  """
  if not POSTGRES_URI:
    return
  engine = create_engine(POSTGRES_URI)
  meta = MetaData()
  meta.reflect(bind=engine)
  with contextlib.closing(engine.connect()) as con:
    trans = con.begin()
    for table in reversed(meta.sorted_tables):
      con.execute(table.delete())
    trans.commit()
