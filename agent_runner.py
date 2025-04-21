from langchain_community.chat_models import ChatOllama
from langchain.agents import AgentExecutor
from langchain_mcp import FastMCPTool
from langchain.agents.agent_toolkits import create_react_agent
from langchain.agents import Tool

llm = ChatOllama(model="qwen2:7b")
mcp_toolkit = FastMCPTool.from_mcp_server("http://localhost:3333")
tools: list[Tool] = mcp_toolkit.to_langchain_tools()
agent = create_react_agent(llm, tools, verbose=True)
executor = AgentExecutor(agent=agent, tools=tools)

response = executor.invoke({"input": "List files in ./docs and summarize the first one"})
print(response)