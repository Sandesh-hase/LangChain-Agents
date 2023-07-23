import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from secret_key import open_ai_key, serpapi_key


os.environ["OPENAI_API_KEY"] = open_ai_key
os.environ["SERPAPI_API_KEY"] = serpapi_key


def agent_tool(question: str):
    # loading llm model
    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    response = agent.run(question)

    return response


if __name__ == "__main__":
    agent_tool("Who is ratan tata? and what is his current age")
