from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.services.complaint_service import (
    ComplaintService
)

from app.services.ai_service import (
    AIService
)


def get_complaint_service(
    db: Session = Depends(
        get_db
    )
):

    repository = ComplaintRepository(
        db
    )

    ai_service = AIService()

    return ComplaintService(
        repository,
        ai_service
    )