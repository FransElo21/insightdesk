from app.models.complaint_model import (
    Complaint
)

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.services.ai_service import (
    AIService
)

from app.core.logger import (
    logger
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

        logger.info(
            f"Creating complaint: "
            f"{request.title}"
        )

        try:

            logger.info(
                "Calling AI "
                "for classification"
            )

            category = (
                self.ai_service.classify(
                    request.description
                )
            )

            logger.info(
                f"Category predicted: "
                f"{category}"
            )

            logger.info(
                "Calling AI "
                "for sentiment"
            )

            sentiment = (
                self.ai_service.sentiment(
                    request.description
                )
            )

            logger.info(
                f"Sentiment predicted: "
                f"{sentiment}"
            )

        except Exception as e:

            logger.exception(
                f"AI processing failed: {e}"
            )

            category = (
                "Tidak Diketahui"
            )

            sentiment = (
                "Netral"
            )

        complaint = Complaint(
            title=request.title,
            description=request.description,
            location=request.location,
            category=category,
            sentiment=sentiment
        )

        logger.info(
            "Saving complaint "
            "to database"
        )

        result = (
            self.repository.create(
                complaint
            )
        )

        logger.info(
            f"Complaint created "
            f"successfully "
            f"(id={result.id})"
        )

        return result

    def get_complaints(
        self
    ):

        logger.info(
            "Fetching all complaints"
        )

        return (
            self.repository.get_all()
        )

    def get_complaint_by_id(
        self,
        complaint_id: int
    ):

        logger.info(
            f"Fetching complaint "
            f"id={complaint_id}"
        )

        return (
            self.repository.get_by_id(
                complaint_id
            )
        )