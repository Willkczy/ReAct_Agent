from langchain.agents import initialize_agent, AgentType
from config import llm
from tools import all_tools

def get_agent():
    return initialize_agent(
        all_tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )
