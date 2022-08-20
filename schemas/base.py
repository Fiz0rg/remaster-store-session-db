import imp
from typing import Optional
from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class IdBaseModel(OurBaseModel):
    id: Optional[int]