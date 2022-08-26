# from typing import Optional, List

# from sqlmodel import Field, SQLModel, Relationship
# from db.user import UserDb

# from schemas.user import UserName

# class GoodsDb(SQLModel, table=True):
#     id: Optional[int] = Field(primary_key=True, default=None)
#     name: str
#     description: str = Field(default='')
#     category_id: int = Field(foreign_key='category.id')

#     user: Optional[UserDb] = Relationship(back_populates="basket")


