from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class UnionAttributes(SQLModel):
    """
    Базовая общая модель с id и name, которая есть в двух моделях.
    Так как там есть друг на друга ссылки, то расположение моделей в отдельных директориях вызовет циркулярный импорт.
    Пока оставил так
    """


    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str


class User(UnionAttributes):
    password: str


class UserDb(User, table=True):
    """
    Модель для пользователей, которая ссылается на модель товаров и выдаёт их список.
    Именно эта модель выдаёт ошибку, что такой атрибут, как "goods" в этой модели не найдет.
    """


    goods: List["GoodsDb"] = Relationship(back_populates="users")



class Goods(UnionAttributes):
    description: str = Field(default='')
    category_id: int = Field(foreign_key='category.id', default=None)
    user_id: Optional[int] = Field(default=None, foreign_key="userdb.id")


class GoodsDb(Goods, table=True):
    """
    Модель товаров.
    """

    users: Optional[UserDb] = Relationship(back_populates="goods")
