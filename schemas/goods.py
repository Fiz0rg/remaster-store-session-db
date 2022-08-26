from typing import Optional

from sqlmodel import SQLModel


class GoodsCreate(SQLModel):
    name: str
    describtion: str = ''
    category_id: int


class FullGoodsResponse(GoodsCreate):
    id: Optional[int]




