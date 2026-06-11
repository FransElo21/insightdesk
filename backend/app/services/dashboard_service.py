from app.repositories.complaint_repository import (
    ComplaintRepository
)


class DashboardService:

    def __init__(
        self,
        repository: ComplaintRepository
    ):
        self.repository = repository

    def get_summary(
        self
    ):

        total = (
            self.repository.count_all()
        )

        categories = (
            self.repository.count_by_category()
        )

        sentiments = (
            self.repository.count_by_sentiment()
        )

        return {
            "total_complaints": total,
            "categories": categories,
            "sentiments": sentiments
        }
    
    def get_trends(
    self
    ):

        rows = (
            self.repository
            .get_daily_trends()
        )

        return {
            "daily": [
                {
                    "date": str(date),
                    "count": count
                }
                for date, count
                in rows
            ]
        }
    
    def get_top_categories(
    self
    ):

        rows = (
            self.repository
            .get_top_categories()
        )

        return {
            "data": [
                {
                    "category": category,
                    "count": count
                }
                for category, count
                in rows
            ]
        }
    
    def get_sentiment_distribution(
    self
    ):

        rows = (
            self.repository
            .get_sentiment_distribution()
        )

        return {
            "data": [
                {
                    "sentiment": sentiment,
                    "count": count
                }
                for sentiment, count
                in rows
            ]
        }