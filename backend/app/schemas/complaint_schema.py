from pydantic import BaseModel
from datetime import datetime


class ComplaintCreate(
    BaseModel
):
    title: str
    description: str
    location: str


class ComplaintResponse(
    BaseModel
):
    id: int
    title: str
    description: str
    category: str | None
    sentiment: str | None
    location: str
    created_at: datetime | None

    class Config:
        from_attributes = True