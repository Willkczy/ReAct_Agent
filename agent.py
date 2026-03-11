from langgraph.prebuilt import create_react_agent
from config import llm
from tools import all_tools

def get_agent():
    return create_react_agent(llm, all_tools)