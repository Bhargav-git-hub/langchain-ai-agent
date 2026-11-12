
import time
from ddgs.exceptions import DDGSException
from datetime import datetime
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

search = DuckDuckGoSearchRun()

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": "ResearchAssistant/1.0 (contact: bhargavtammineedi249@gmail.com)"
}

@tool
def save_to_txt(data: str, filename: str = "output.txt") -> str:
    """Save research data to a text file."""
    timestamp = datetime.now().isoformat()

    formatted_data = f"--- Research Output ---\n{timestamp}\n\n{data}"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(formatted_data)

    return f"Successfully saved to {filename}"


@tool
def search_tool(query: str) -> str:
    """Search the web using DuckDuckGo with automatic retries."""

    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            print(f"DuckDuckGo attempt {attempt}/{max_retries}")

            return search.run(query)

        except DDGSException as exc:
            print(f"Search failed: {exc}")

            if attempt == max_retries:
                return (
                    f"DuckDuckGo search failed after "
                    f"{max_retries} attempts: {exc}"
                )

            time.sleep(2)

        except Exception as exc:
            return f"Unexpected search error: {exc}"


@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia and return relevant results."""

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 2
    }

    try:
        response = requests.get(
            WIKIPEDIA_API,
            params=params,
            headers=HEADERS,
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            return f"No Wikipedia results found for: {query}"

        return "\n\n".join(
            f"Title: {item['title']}\nSnippet: {item['snippet']}"
            for item in results
        )

    except requests.RequestException as exc:
        return f"Wikipedia request failed: {exc}"

    except ValueError as exc:
        return f"Wikipedia returned invalid JSON: {exc}"