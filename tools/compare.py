from langchain_core.tools import tool
from config import llm

@tool
def Compare(input: str) -> str:
    """Compare multiple items in a given category. Input format: 'item1, item2, ..., category: <category>'"""
    try:
        parts = input.split("category:")
        if len(parts) != 2:
            return "Error: Please use format 'item1, item2, category: <category>'"
        items = [item.strip() for item in parts[0].split(",") if item.strip()]
        category = parts[1].strip()
        prompt = f"Compare the following {category}: {', '.join(items)}. Provide key features, pros/cons, and a recommendation. Be concise."
        return llm.invoke(prompt).content
    except Exception as e:
        return f"Error: {str(e)}"