from langchain_core.tools import tool
from config import llm

@tool
def Analyze(input: str) -> str:
    """Analyze and summarize information to extract key insights."""
    try:
        prompt = f"Analyze the following and provide key findings, patterns, and an actionable summary. Be concise.\n\n{input}"
        return llm.invoke(prompt).content
    except Exception as e:
        return f"Error: {str(e)}"