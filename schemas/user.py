from typing import List

from sqlmodel import SQLModel

from db.user import Goods, User


class IdClass(SQLModel):
    id: int


class UserName(SQLModel):
    name: str


class PasswordUser(SQLModel):
    password: str


class NewUser(UserName, PasswordUser):
    pass


class IdUser(IdClass, UserName):
    pass 


class UserBasket(User):
    goods: List["Goods"] = []

