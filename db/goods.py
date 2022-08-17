import imp

from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from .category import Category


class GoodsDb(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    description: str = ''

    category : Optional[Category] = Relationship(back_populates='goods')
    category_id: int = Field(foreign_key='category.id')
