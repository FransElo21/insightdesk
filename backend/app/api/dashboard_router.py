from fastapi import APIRouter
from fastapi import Depends

from app.schemas.dashboard_schema import (
    DashboardSummaryResponse
)

from app.dependencies.dashboard_dependency import (
    get_dashboard_service
)

from app.services.dashboard_service import (
    DashboardService
)

from app.schemas.dashboard_schema import (
    DashboardTrendResponse
)

from app.schemas.dashboard_schema import (
    TopCategoryResponse
)

from app.schemas.dashboard_schema import (
    SentimentDistributionResponse
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/summary",
    response_model=DashboardSummaryResponse
)

def get_summary(
    service: DashboardService = Depends(
        get_dashboard_service
    )
):

    return (
        service.get_summary()
    )

@router.get(
    "/trends",
    response_model=DashboardTrendResponse
)
def get_trends(
    service: DashboardService = Depends(
        get_dashboard_service
    )
):

    return (
        service.get_trends()
    )

@router.get(
    "/top-categories",
    response_model=TopCategoryResponse
)
def get_top_categories(
    service: DashboardService = Depends(
        get_dashboard_service
    )
):

    return (
        service.get_top_categories()
    )

@router.get(
    "/sentiment-distribution",
    response_model=SentimentDistributionResponse
)
def get_sentiment_distribution(
    service: DashboardService = Depends(
        get_dashboard_service
    )
):

    return (
        service.get_sentiment_distribution()
    )
