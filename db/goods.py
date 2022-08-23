from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from schemas.user import NameUser

from .category import Category


class GoodsDb(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    description: str = Field(default='')
    category_id: int = Field(foreign_key='category.id')

    category: Optional[Category] = Relationship(back_populates='goods')
