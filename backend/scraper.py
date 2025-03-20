import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts, styles, and unnecessary tags
        for script in soup(["script", "style", "meta", "link", "noscript"]):
            script.extract()

        text = ' '.join(soup.stripped_strings)  # Extract visible text
        return text[:5000]  # Limit text to 5000 characters

    except requests.exceptions.RequestException as e:
        print(f"Scraping failed: {e}")
        return ""

