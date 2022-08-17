from typing import Optional
from .base import OurBaseModel


class NewUser(OurBaseModel):
    name: str
    password: str


class FullUser(NewUser):
    id: Optional[int] 