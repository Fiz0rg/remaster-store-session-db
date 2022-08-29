from typing import Optional

from sqlmodel import SQLModel, Field


class GoodsCreate(SQLModel):
    name: str
    describtion: str = ''
    category_id: int = Field(foreign_key='category.id')
    user_id: Optional[int] = Field(default=None, foreign_key="userdb.id")


class FullGoodsResponse(GoodsCreate):
    id: Optional[int]




