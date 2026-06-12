from unittest.mock import Mock

from app.services.insight_service import (
    InsightService
)


def test_generate_insight():

    complaint_repository = Mock()

    insight_repository = Mock()

    ai_service = Mock()

    complaint_repository.get_last_days.return_value = [

        Mock(
            description="Wifi lambat"
        ),

        Mock(
            description="Internet putus"
        )

    ]

    ai_service.generate_insight.return_value = (
        "Insight AI"
    )

    insight_repository.create.return_value = Mock(
        id=1
    )

    service = InsightService(
        complaint_repository,
        insight_repository,
        ai_service
    )

    result = (
        service.generate_insight(
            30
        )
    )

    assert result.id == 1

    complaint_repository.get_last_days.assert_called_once()

    ai_service.generate_insight.assert_called_once()

    insight_repository.create.assert_called_once()