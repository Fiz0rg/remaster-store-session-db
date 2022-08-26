from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class UnionAttributes(SQLModel):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str


class User(UnionAttributes):
    password: str


class TestUser(User):
    pass


class UserDb(TestUser, table=True):
    goods: List["GoodsDb"] = Relationship(back_populates='users')



class Goods(UnionAttributes):
    description: str = Field(default='')
    category_id: int = Field(foreign_key='category.id', default=None)


class TestGoods(Goods):
    user_id: Optional[int] = Field(default=None, foreign_key="userdb.id")


class GoodsDb(TestGoods, table=True):
    users: Optional[UserDb] = Relationship(back_populates="goods")


class FuckIt(SQLModel):
    name: str
    description: str = Field(default='')
    category_id: int = Field(foreign_key='category.id')
    user_id: Optional[int] = Field(default=None, foreign_key="userdb.id")


class FuckId(FuckIt):
    id: int