from sqlalchemy.orm import Session

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