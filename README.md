# AI Agent - LangChain

An AI-powered research assistant built using **LangChain**, **Anthropic Claude**, **DuckDuckGo**, and **Wikipedia**. The agent researches user queries using external search tools, generates structured responses, and saves research results to a text file.

## Features

- **LLM-powered research:** Uses Anthropic Claude to understand queries and synthesize research.
- **Web search:** Retrieves relevant information using DuckDuckGo.
- **Wikipedia integration:** Searches Wikipedia through its MediaWiki API.
- **Structured responses:** Uses Pydantic models to generate consistent research output.
- **Retry mechanism:** Automatically retries failed DuckDuckGo searches up to a configured number of attempts.
- **File storage:** Saves generated research results to `output.txt`.

## Tech Stack

- Python
- LangChain
- LangGraph
- Anthropic Claude
- DuckDuckGo Search (`ddgs`)
- Wikipedia MediaWiki API
- Pydantic
- Requests
- Python-dotenv

## Project Structure

```text
AI Agent Tutorial/
│
├── main.py              # Agent initialization and execution
├── tools.py             # Search, Wikipedia, and file-saving tools
├── requirements.txt     # Python dependencies
├── .env                 # API credentials (not committed)
├── .gitignore           # Excludes sensitive and unnecessary files
└── output.txt           # Generated research output (not committed)
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-agent-tutorial.git
cd ai-agent-tutorial
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
```

Replace the placeholder with your actual Anthropic API key.

### 5. Run the application

```bash
python main.py
```

Enter a research query when prompted.

Example:

```text
Enter your query: South India population
```

The agent searches available sources, generates a structured response, and saves the result to `output.txt`.

## Structured Response

The research output follows this Pydantic schema:

```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
```

This provides a consistent format for research results.

## Configuration

You can customize the following:

- **LLM model:** Change the Anthropic model in `main.py`.
- **Search retries:** Adjust the maximum retry attempts and delay in `tools.py`.
- **Wikipedia results:** Modify the search result limit in the Wikipedia API parameters.
- **Output filename:** Change the filename passed to the file-saving function.

## Security

- Store API credentials in `.env`.
- Never commit API keys or secrets.
- Keep `.env` and your virtual environment excluded through `.gitignore`.

## Future Improvements

- Add additional search providers and fallback mechanisms.
- Retrieve full Wikipedia article extracts.
- Support PDF and Markdown research reports.
- Add source citations and reference validation.
- Introduce conversational memory for multi-turn research.
- Build a web interface for interacting with the research agent.

---

**Author:** YOUR_NAME

**Project:** AI Agent Tutorial