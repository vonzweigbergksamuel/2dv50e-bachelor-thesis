import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

_raw = os.getenv("DEEPFACE_POSTGRES_URI", "")
if not _raw:
    raise RuntimeError("DEEPFACE_POSTGRES_URI is not set")

POSTGRES_URI = _raw.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(POSTGRES_URI)
