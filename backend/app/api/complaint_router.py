from typing import List

from fastapi import APIRouter
from fastapi import Depends

from app.services.complaint_service import (
    ComplaintService
)

from app.schemas.complaint_schema import (
    ComplaintCreate,
    ComplaintResponse
)

from app.dependencies.complaint_dependency import (
    get_complaint_service
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
    service: ComplaintService = Depends(
        get_complaint_service
    )
):

    return (
        service.create_complaint(
            request
        )
    )


@router.get(
    "",
    response_model=List[
        ComplaintResponse
    ]
)
def get_complaints(
    service: ComplaintService = Depends(
        get_complaint_service
    )
):

    return (
        service.get_complaints()
    )


@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def get_complaint(
    complaint_id: int,
    service: ComplaintService = Depends(
        get_complaint_service
    )
):

    return (
        service.get_complaint_by_id(
            complaint_id
        )
    )