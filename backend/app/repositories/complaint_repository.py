from sqlalchemy.orm import Session
from sqlalchemy import func

from datetime import datetime
from datetime import timedelta

from app.models.complaint_model import (
    Complaint
)


class ComplaintRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(
        self,
        complaint: Complaint
    ):

        self.db.add(
            complaint
        )

        self.db.commit()

        self.db.refresh(
            complaint
        )

        return complaint

    def get_all(self):

        return (
            self.db
            .query(
                Complaint
            )
            .order_by(
                Complaint.id.desc()
            )
            .all()
        )
    
    def get_by_id(
        self,
        complaint_id: int
    ):

        return (
            self.db.query(
                Complaint
            )
            .filter(
                Complaint.id == complaint_id
            )
            .first()
        )
    
    def count_all(
    self
    ):

        return (
            self.db.query(
                Complaint
            )
            .count()
        )
    
    def count_by_category(
    self
    ):

        result = (
            self.db.query(
                Complaint.category,
                func.count(
                    Complaint.id
                )
            )
            .group_by(
                Complaint.category
            )
            .all()
        )

        return {
            category: count
            for category, count
            in result
            if category
        }
    
    def count_by_sentiment(
        self
    ):

        result = (
            self.db.query(
                Complaint.sentiment,
                func.count(
                    Complaint.id
                )
            )
            .group_by(
                Complaint.sentiment
            )
            .all()
        )

        return {
            sentiment: count
            for sentiment, count
            in result
            if sentiment
        }
    
    def get_daily_trends(
    self
    ):

        result = (
            self.db.query(
                func.date(
                    Complaint.created_at
                ),
                func.count(
                    Complaint.id
                )
            )
            .group_by(
                func.date(
                    Complaint.created_at
                )
            )
            .order_by(
                func.date(
                    Complaint.created_at
                )
            )
            .all()
        )

        return result
    
    def get_top_categories(
    self
    ):

        result = (
            self.db.query(
                Complaint.category,
                func.count(
                    Complaint.id
                ).label(
                    "total"
                )
            )
            .filter(
                Complaint.category.isnot(
                    None
                )
            )
            .group_by(
                Complaint.category
            )
            .order_by(
                func.count(
                    Complaint.id
                ).desc()
            )
            .all()
        )

        return result
    
    def get_sentiment_distribution(
    self
    ):

        result = (
            self.db.query(
                Complaint.sentiment,
                func.count(
                    Complaint.id
                ).label(
                    "total"
                )
            )
            .filter(
                Complaint.sentiment.isnot(
                    None
                )
            )
            .group_by(
                Complaint.sentiment
            )
            .order_by(
                func.count(
                    Complaint.id
                ).desc()
            )
            .all()
        )

        return result
    
    def get_last_days(
    self,
        days: int
    ):

        start_date = (
            datetime.utcnow()
            - timedelta(days=days)
        )

        return (
            self.db.query(
                Complaint
            )
            .filter(
                Complaint.created_at >= start_date
            )
            .all()
        )