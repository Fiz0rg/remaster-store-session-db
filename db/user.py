from typing import Optional

from sqlmodel import Field, SQLModel


class UserDb(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    password: str