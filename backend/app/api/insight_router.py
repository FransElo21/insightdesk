from typing import List

from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.insight_dependency import (
    get_insight_service
)

from app.schemas.insight_schema import (
    InsightResponse
)

from app.services.ai_service import AIService
from app.services.insight_service import (
    InsightService
)

router = APIRouter(
    prefix="/insights",
    tags=["Insights"]
)

@router.post(
    "/generate",
    response_model=InsightResponse
)
def generate_insight(
    service: InsightService = Depends(
        get_insight_service
    )
):

    return (
        service.generate_insight()
    )

@router.get(
    "",
    response_model=List[
        InsightResponse
    ]
)
def get_insights(
    service: InsightService = Depends(
        get_insight_service
    )
):

    return (
        service.get_insights()
    )

@router.get(
    "/latest",
    response_model=InsightResponse
)
def get_latest_insight(
    service: InsightService = Depends(
        get_insight_service
    )
):

    return (
        service.get_latest_insight()
    )

# @router.get("/test-ai")
# def test_ai():

#     ai = AIService()

#     category = ai.classify(
#         "Atap di Gedung 9 sering bocor saat hujan"
#     )

#     return {
#         "category": category
#     }

# @router.get("/test-sentiment")
# def test_sentiment():

#     ai = AIService()

#     sentiment = ai.sentiment(
#         "Wifi di Gedung 9 sangat lancar"
#     )

#     return {
#         "sentiment": sentiment
#     }