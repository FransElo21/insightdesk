from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Insight(Base):

    __tablename__ = "insights"

    id = Column(
        Integer,
        primary_key=True
    )

    content = Column(
        Text,
        nullable=False
    )

    generated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )