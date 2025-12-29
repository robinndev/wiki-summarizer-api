from unittest.mock import MagicMock
from app.services.summary_service import SummaryService


def test_summary_service_returns_summary():
    # mocks
    mock_repo = MagicMock()
    mock_scraper = MagicMock()
    mock_llm = MagicMock()
    mock_db = MagicMock()

    # cenário: não existe cache
    mock_repo.get_by_url.return_value = None

    # scraper retorna título + texto
    mock_scraper.scrape.return_value = (
        "Título de Teste",
        "Texto completo da Wikipedia"
    )

    # llm retorna resumo
    mock_llm.summarize.return_value = "Resumo gerado com sucesso."

    # repository.create retorna entidade simulada
    mock_repo.create.return_value = MagicMock(
        title="Título de Teste",
        summary="Resumo gerado com sucesso."
    )

    service = SummaryService(
        repository=mock_repo,
        scraper=mock_scraper,
        llm_service=mock_llm,
    )

    result = service.get_or_create_summary(
        db=mock_db,
        url="https://pt.wikipedia.org/wiki/Teste",
        max_words=50,
    )

    # asserts de chamadas
    mock_repo.get_by_url.assert_called_once_with(
        mock_db,
        "https://pt.wikipedia.org/wiki/Teste"
    )
    mock_scraper.scrape.assert_called_once_with(
        "https://pt.wikipedia.org/wiki/Teste"
    )
    mock_llm.summarize.assert_called_once_with(
        text="Texto completo da Wikipedia",
        max_words=50,
    )
    mock_repo.create.assert_called_once()

    # assert final
    assert result == {
        "title": "Título de Teste",
        "summary": "Resumo gerado com sucesso.",
        "has_cached": False,
    }
