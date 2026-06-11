from pydantic import BaseModel
from datetime import datetime


class InsightResponse(
    BaseModel
):

    id: int

    content: str

    generated_at: datetime

    class Config:
        from_attributes = True