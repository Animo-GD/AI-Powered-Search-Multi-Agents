import requests
from bs4 import BeautifulSoup
from crewai import LLM

class SimpleScraper:
    def __init__(self, llm: LLM):
        self.llm = llm

    def fetch_html(self, url: str) -> str:
        """Download raw HTML."""
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text

    def parse_text(self, html: str) -> str:
        """Extract clean text from HTML."""
        soup = BeautifulSoup(html, "html.parser")

        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(separator="\n")
        return text.strip()

    def extract_info(self, url: str, query: str) -> str:
        """Fetch -> Parse -> Ask LLM to extract info."""
        html = self.fetch_html(url)
        text = self.parse_text(html)

        prompt = f"""
        You are a data extractor. Extract the following from the website:

        Website: {url}
        User query: {query}

        Content:
        {text[:5000]}  # limit for safety
        """

        response = self.llm.call(prompt)
        return response.output_text

# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    # You can swap Ollama, OpenRouter, or OpenAI
    llm = LLM(
        model="ollama/qwen2.5-coder",
        base_url="http://localhost:11434",
        temperature=0.2,
        max_tokens=1024
    )

    scraper = SimpleScraper(llm)
    result = scraper.extract_info("https://en.wikipedia.org/wiki/Python_(programming_language)", 
                                  "Summarize the history of Python in bullet points.")
    print(result)
