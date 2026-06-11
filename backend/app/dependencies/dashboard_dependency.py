from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.services.dashboard_service import (
    DashboardService
)


def get_dashboard_service(
    db: Session = Depends(
        get_db
    )
):

    repository = ComplaintRepository(
        db
    )

    return DashboardService(
        repository
    )