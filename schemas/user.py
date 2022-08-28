from typing import List

from sqlmodel import SQLModel

from db.user import Goods


class IdClass(SQLModel):
    id: int


class UserName(SQLModel):
    name: str


class PasswordUser(SQLModel):
    password: str


class NewUser(UserName, PasswordUser):
    pass


class UserBasket(IdClass, UserName, PasswordUser):
    basket: List[Goods] = []


