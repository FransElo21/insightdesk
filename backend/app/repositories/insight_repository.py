from sqlalchemy.orm import Session

from app.models.insight_model import Insight


class InsightRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(
        self,
        content: str
    ):

        insight = Insight(
            content=content
        )

        self.db.add(
            insight
        )

        self.db.commit()

        self.db.refresh(
            insight
        )

        return insight

    def get_all(
        self
    ):

        return (
            self.db.query(
                Insight
            )
            .order_by(
                Insight.generated_at.desc()
            )
            .all()
        )

    def get_latest(
        self
    ):

        return (
            self.db.query(
                Insight
            )
            .order_by(
                Insight.generated_at.desc()
            )
            .first()
        )