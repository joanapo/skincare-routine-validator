from datetime import datetime
from pydantic import BaseModel
from typing import List

class AddProductModel(BaseModel):
    name:str
    category:str
    type:str
    ingredients:List[str]

class AddProductResponseModel(BaseModel):
    id: int
    name: str
    type: str
    ingredients: List[str]
    success:bool
    timestamp: datetime

    class Config:
        from_attributes = True