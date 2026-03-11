from langchain.agents import create_agent
from config import llm
from tools import all_tools

def get_agent():
    return create_agent(llm, all_tools)