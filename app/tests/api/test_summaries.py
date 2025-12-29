from unittest.mock import MagicMock
from fastapi import status

from app.api.routes.summaries import get_summary_service


def test_create_summary_success(client, app):
    mock_service = MagicMock()
    mock_service.get_or_create_summary.return_value = {
        "title": "Teste",
        "summary": "Resumo da API.",
        "has_cached": False,
    }

    app.dependency_overrides[get_summary_service] = lambda: mock_service

    response = client.post(
        "/summaries/",
        json={
            "url": "https://pt.wikipedia.org/wiki/Teste",
            "max_words": 30,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "url": "https://pt.wikipedia.org/wiki/Teste",
        "title": "Teste",
        "summary": "Resumo da API.",
        "has_cached": False,
    }

    mock_service.get_or_create_summary.assert_called_once()
