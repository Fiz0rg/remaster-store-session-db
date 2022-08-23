import imp

from pydantic import BaseModel

from .base import OurBaseModel


class CategoryName(OurBaseModel):
    name: str


class CategoryCreate(CategoryName):
    id: int
