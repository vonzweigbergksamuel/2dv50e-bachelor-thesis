from sqlalchemy import JSON, Column, Integer, MetaData, String, Table, select

from lib import engine

metadata = MetaData()

embeddings_table = Table(
    "embeddings",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("identity", String, nullable=False),
    Column("embedding", JSON, nullable=False),
)


def insert_subject(identity: str, embeddings: list[list[float]]):
    metadata.create_all(engine)
    with engine.connect() as conn:
        conn.execute(
            embeddings_table.insert(),
            [{"identity": identity, "embedding": emb} for emb in embeddings],
        )
        conn.commit()


def get_all_subjects() -> list[dict]:
    with engine.connect() as conn:
        rows = conn.execute(select(embeddings_table)).fetchall()
    return [{"identity": row.identity, "embedding": row.embedding} for row in rows]


def clear_database():
    metadata.drop_all(engine)
