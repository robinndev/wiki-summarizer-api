import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

class WikipediaScraper:
    def scrape(self, url: str) -> tuple[str, str]:
        url = unquote(url)
        
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise ValueError(f"Erro ao acessar a URL: {url} (status {response.status_code})")
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.title.string.replace(" – Wikipédia", "").strip() if soup.title else "Sem título"
        
        paragraphs = soup.find_all("p")
        full_text = " ".join(p.get_text().strip() for p in paragraphs if p.get_text().strip())
        
        return title, full_text
