from app.models.complaint_model import (
    Complaint
)

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.services.ai_service import (
    AIService
)


class ComplaintService:

    def __init__(
        self,
        repository: ComplaintRepository,
        ai_service: AIService
    ):

        self.repository = repository
        self.ai_service = ai_service

    def create_complaint(
        self,
        request
    ):

        try:

            category = (
                self.ai_service.classify(
                    request.description
                )
            )

            sentiment = (
                self.ai_service.sentiment(
                    request.description
                )
            )

        except Exception as e:

            print(
                f"AI Error: {e}"
            )

            category = "Tidak Diketahui"
            sentiment = "Netral"

        complaint = Complaint(
            title=request.title,
            description=request.description,
            location=request.location,
            category=category,
            sentiment=sentiment
        )

        return (
            self.repository.create(
                complaint
            )
        )

    def get_complaints(
        self
    ):

        return (
            self.repository.get_all()
        )

    def get_complaint_by_id(
        self,
        complaint_id: int
    ):

        return (
            self.repository.get_by_id(
                complaint_id
            )
        )