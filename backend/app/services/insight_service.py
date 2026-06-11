from app.repositories.complaint_repository import (
    ComplaintRepository
)

from app.repositories.insight_repository import (
    InsightRepository
)

from app.services.ai_service import (
    AIService
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
        self
    ):

        complaints = (
            self.complaint_repository
            .get_all()
        )

        if not complaints:

            raise ValueError(
                "Belum ada complaint untuk dianalisis"
            )

        complaint_texts = []

        for complaint in complaints:

            complaint_texts.append(
                f"""
Judul: {complaint.title}
Kategori: {complaint.category}
Sentimen: {complaint.sentiment}
Deskripsi: {complaint.description}
"""
            )

        insight = (
            self.ai_service
            .generate_insight(
                complaint_texts
            )
        )

        return (
            self.insight_repository
            .create(
                insight
            )
        )

    def get_insights(
        self
    ):

        return (
            self.insight_repository
            .get_all()
        )

    def get_latest_insight(
        self
    ):

        return (
            self.insight_repository
            .get_latest()
        )