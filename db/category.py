from typing import Optional
from sqlmodel import SQLModel, Field, Relationship



class Category(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    name: str = Field()

