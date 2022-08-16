from sqlmodel import create_engine, SQLModel


DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)