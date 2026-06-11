from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.repositories.insight_repository import (
    InsightRepository
)

from app.services.ai_service import (
    AIService
)

from app.services.insight_service import (
    InsightService
)


def get_insight_service(
    db: Session = Depends(
        get_db
    )
):

    complaint_repository = (
        ComplaintRepository(
            db
        )
    )

    insight_repository = (
        InsightRepository(
            db
        )
    )

    ai_service = AIService()

    return InsightService(
        complaint_repository,
        insight_repository,
        ai_service
    )