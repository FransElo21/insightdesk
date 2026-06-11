from typing import List

from fastapi import APIRouter
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

from app.schemas.complaint_schema import (
    ComplaintCreate,
    ComplaintResponse
)

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


@router.post(
    "",
    response_model=ComplaintResponse
)
def create_complaint(
    request: ComplaintCreate,
    db: Session = Depends(
        get_db
    )
):

    repository = ComplaintRepository(
        db
    )

    service = ComplaintService(
        repository
    )

    return service.create_complaint(
        request
    )


@router.get(
    "",
    response_model=List[
        ComplaintResponse
    ]
)
def get_complaints(
    db: Session = Depends(
        get_db
    )
):

    repository = ComplaintRepository(
        db
    )

    service = ComplaintService(
        repository
    )

    return service.get_complaints()