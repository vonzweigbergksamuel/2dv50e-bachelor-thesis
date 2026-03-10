import contextlib
import os
import shutil

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine

load_dotenv()

_raw = os.getenv("DEEPFACE_POSTGRES_URI", "")
POSTGRES_URI = _raw.replace("postgresql://", "postgresql+psycopg://", 1) if _raw else ""
ENGINE = create_engine(POSTGRES_URI) if POSTGRES_URI else None
META = MetaData()

if ENGINE is not None:
    META.reflect(bind=ENGINE)


def clean_up_folder():
    """
    Cleans up the folders created by the preprocess service.
    """
    shutil.rmtree("test_subjects", ignore_errors=True)


def clean_up_database():
    """
    Cleans up the database.
    """
    if ENGINE is None:
        return

    with contextlib.closing(ENGINE.connect()) as con:
        trans = con.begin()
        for table in reversed(META.sorted_tables):
            con.execute(table.delete())
        trans.commit()
