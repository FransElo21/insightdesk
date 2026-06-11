from pydantic import BaseModel


class DashboardSummaryResponse(
    BaseModel
):

    total_complaints: int

    categories: dict

    sentiments: dict

class TrendItem(
    BaseModel
):
    date: str

    count: int


class DashboardTrendResponse(
    BaseModel
):
    daily: list[TrendItem]

class CategoryItem(
    BaseModel
):
    category: str

    count: int


class TopCategoryResponse(
    BaseModel
):
    data: list[CategoryItem]

class SentimentItem(
    BaseModel
):
    sentiment: str

    count: int


class SentimentDistributionResponse(
    BaseModel
):
    data: list[SentimentItem]