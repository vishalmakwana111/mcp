# math_server.py

import os
import sys

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Math")

# Define tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    result = a + b
    return result

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    result = a * b
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")