# agent.py

import asyncio
import os
from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")

# Initialize the language model
model = ChatOpenAI(model="gpt-4o", api_key=api_key)

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["my_tools/server.py"],  
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            response = await agent.ainvoke({"messages": "What's (7 + 3) x 5?"})
            print("🤖 Agent Response log:", response)

if __name__ == "__main__":
    asyncio.run(main())
