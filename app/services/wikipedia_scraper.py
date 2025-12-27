import requests
from bs4 import BeautifulSoup

class WikipediaScraper:

    @staticmethod
    def scrape(url: str) -> str:
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Erro ao acessar a URL: {url}")

        soup = BeautifulSoup(response.text, "lxml")

        content = soup.find("div", {"id": "mw-content-text"})
        if not content:
            return ""

        paragraphs = content.find_all("p")
        text = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())
        return text
