# ReAct Agent

A Streamlit-based ReAct (Reasoning + Acting) agent powered by Google Gemini and LangChain/LangGraph. The agent can search the web, compare items, and analyze information to answer complex, multi-step questions.

## Project Structure

```
.
├── app.py           # Streamlit UI — chat interface and step-by-step reasoning display
├── agent.py         # Agent factory — creates the ReAct agent with LLM and tools
├── config.py        # LLM configuration (Gemini 3.1 Flash Lite via LangChain)
├── tools/
│   ├── __init__.py  # Exports all tools
│   ├── search.py    # Web search tool using SerpAPI
│   ├── compare.py   # Item comparison tool (LLM-based)
│   └── analyze.py   # Text analysis/summarization tool (LLM-based)
├── pyproject.toml   # Project metadata and dependencies
└── .env             # API keys (not committed)
```

## Tools

| Tool | Description |
|------|-------------|
| **Search** | Searches the web for current information using SerpAPI |
| **Compare** | Compares multiple items in a category, providing pros/cons and recommendations |
| **Analyze** | Analyzes and summarizes text to extract key insights |

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Environment Variables

Create a `.env` file with:

```
GOOGLE_API_KEY=<your-google-api-key>
SERPAPI_API_KEY=<your-serpapi-api-key>
```

### Install Dependencies

```bash
uv sync
```

Or with pip:

```bash
pip install -e .
```

## Usage

```bash
streamlit run app.py
```

Enter a query in the text box (e.g., "Compare Python and Rust for web development") and click **Submit**. The agent will reason through the problem step-by-step, calling tools as needed, and display the final answer along with expandable reasoning traces.
