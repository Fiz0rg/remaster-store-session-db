import imp
from pydoc import describe
from typing import Optional

from .base import OurBaseModel


class GoodsCreate(OurBaseModel):
    name: str
    describtion: str = ''
    category_id: int


class FullGoodsResponse(GoodsCreate):
    id: Optional[int]
