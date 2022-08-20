from typing import Optional
from .base import OurBaseModel


class IdUser(OurBaseModel):
    id: Optional[int]


class PasswordUser(OurBaseModel):
    password: str


class NameUser(OurBaseModel):
    name: str


class NewUser(NameUser, PasswordUser):
    pass


class FullUser(NewUser, IdUser):
    pass 


class UserNameId(NameUser, IdUser):
    pass


class FullUser(IdUser, NameUser, PasswordUser):
    pass