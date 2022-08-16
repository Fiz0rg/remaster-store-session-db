import imp

from pydantic import BaseModel

from .base import OurBaseModel


class CategoryCreate(BaseModel):
    id: int
    name: str
