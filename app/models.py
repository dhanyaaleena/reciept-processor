from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str = Field(..., description="The name of the retailer.")
    purchaseDate: str = Field(..., description="Date of purchase in YYYY-MM-DD format.")
    purchaseTime: str = Field(..., description="Time of purchase in HH:MM 24-hour format.")
    items: List[Item]
    total: str = Field(..., description="Total amount paid.")

class PointsResponse(BaseModel):
    points: int
