from fastapi import HTTPException

from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.repositories.insight_repository import (
    InsightRepository
)

from app.services.ai_service import (
    AIService
)

from app.core.logger import (
    logger
)


class InsightService:

    def __init__(
        self,
        complaint_repository: ComplaintRepository,
        insight_repository: InsightRepository,
        ai_service: AIService
    ):

        self.complaint_repository = (
            complaint_repository
        )

        self.insight_repository = (
            insight_repository
        )

        self.ai_service = ai_service

    def generate_insight(
        self,
        days: int = 30
    ):

        logger.info(
            f"Generating insight "
            f"for last {days} days"
        )

        complaints = (
            self.complaint_repository
            .get_last_days(days)
        )

        logger.info(
            f"Found "
            f"{len(complaints)} "
            f"complaints"
        )

        if not complaints:

            logger.warning(
                f"No complaints found "
                f"for last {days} days"
            )

            raise HTTPException(
                status_code=404,
                detail=(
                    f"Tidak ada complaint "
                    f"dalam {days} hari terakhir"
                )
            )

        complaint_texts = [
            complaint.description
            for complaint
            in complaints
        ]

        logger.info(
            "Sending complaints "
            "to AI service"
        )

        insight_content = (
            self.ai_service
            .generate_insight(
                complaint_texts,
                days
            )
        )

        logger.info(
            "Insight generated "
            "successfully"
        )

        result = (
            self.insight_repository
            .create(
                insight_content
            )
        )

        logger.info(
            f"Insight saved "
            f"(id={result.id})"
        )

        return result

    def get_insights(
        self
    ):

        logger.info(
            "Fetching all insights"
        )

        return (
            self.insight_repository
            .get_all()
        )

    def get_latest_insight(
        self
    ):

        logger.info(
            "Fetching latest insight"
        )

        return (
            self.insight_repository
            .get_latest()
        )