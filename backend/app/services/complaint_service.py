from app.models.complaint_model import (
    Complaint
)

from app.repositories.complaint_repository import (
    ComplaintRepository
)


class ComplaintService:

    def __init__(
        self,
        repository: ComplaintRepository
    ):
        self.repository = repository

    def create_complaint(
        self,
        request
    ):

        complaint = Complaint(
            title=request.title,
            description=request.description,
            location=request.location
        )

        return self.repository.create(
            complaint
        )

    def get_complaints(
        self
    ):

        return self.repository.get_all()