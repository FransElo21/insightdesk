from unittest.mock import Mock

from app.services.complaint_service import (
    ComplaintService
)


class DummyRequest:

    title = (
        "Wifi Kampus Lambat"
    )

    description = (
        "Internet sering putus"
    )

    location = (
        "Gedung 9"
    )


def test_create_complaint():

    repository = Mock()

    ai_service = Mock()

    ai_service.classify.return_value = (
        "Jaringan"
    )

    ai_service.sentiment.return_value = (
        "Negatif"
    )

    repository.create.return_value = Mock(
        id=1
    )

    service = ComplaintService(
        repository,
        ai_service
    )

    result = (
        service.create_complaint(
            DummyRequest()
        )
    )

    assert result.id == 1

    ai_service.classify.assert_called_once()

    ai_service.sentiment.assert_called_once()

    repository.create.assert_called_once()