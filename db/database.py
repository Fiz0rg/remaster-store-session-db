from sqlmodel import create_engine, SQLModel

from .category import *
from .user import *


DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/post"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)