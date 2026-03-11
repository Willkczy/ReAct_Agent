from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper

search_api = SerpAPIWrapper()

@tool
def Search(query: str) -> str:
    """Useful for searching the web for current information about any topic."""
    return search_api.run(query)