import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    """Extract the main text content from a news article URL"""
    if not url or not url.startswith(('http://', 'https://')):
        print(f"Invalid URL: {url}")
        return ""
        
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
        
        # Get text
        text = soup.get_text(separator=' ', strip=True)
        
        # Clean up text (remove extra whitespace)
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit text length for API constraints
        return text[:4000]  # Limit to 4000 chars to avoid token limits
    except Exception as e:
        print(f"Error extracting content from {url}: {e}")
        return "" 