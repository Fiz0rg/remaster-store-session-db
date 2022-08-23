from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from schemas.goods import GoodsCreate


class UserDb(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    password: str

