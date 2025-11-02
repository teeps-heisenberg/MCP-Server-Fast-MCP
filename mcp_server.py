"""
MCP Server for FastAPI Application
Exposes FastAPI endpoints as MCP tools that can be called via Gemini CLI
"""
import asyncio
import json
import httpx
from typing import Any, Dict, List
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Create the MCP server instance
server = Server("fastapi-mcp-server")
API_URL = "http://localhost:8000"


# Define all available tools
@server.list_tools()
async def list_tools() -> List[Tool]:
    """List all available MCP tools"""
    return [
        Tool(
            name="get_health",
            description="Get health status of the FastAPI application",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_users",
            description="Get all users from the FastAPI application",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_user",
            description="Get a specific user by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "The ID of the user to retrieve"
                    }
                },
                "required": ["user_id"]
            }
        ),
        Tool(
            name="create_user",
            description="Create a new user",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the user"
                    },
                    "email": {
                        "type": "string",
                        "description": "Email address of the user"
                    },
                    "age": {
                        "type": "integer",
                        "description": "Age of the user (optional)"
                    }
                },
                "required": ["name", "email"]
            }
        ),
        Tool(
            name="delete_user",
            description="Delete a user by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "The ID of the user to delete"
                    }
                },
                "required": ["user_id"]
            }
        ),
        Tool(
            name="get_tasks",
            description="Get all tasks from the FastAPI application",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_task",
            description="Get a specific task by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "integer",
                        "description": "The ID of the task to retrieve"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="create_task",
            description="Create a new task",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the task"
                    },
                    "description": {
                        "type": "string",
                        "description": "Description of the task (optional)"
                    },
                    "completed": {
                        "type": "boolean",
                        "description": "Whether the task is completed (default: false)"
                    }
                },
                "required": ["title"]
            }
        ),
        Tool(
            name="complete_task",
            description="Mark a task as completed",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "integer",
                        "description": "The ID of the task to complete"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="delete_task",
            description="Delete a task by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "integer",
                        "description": "The ID of the task to delete"
                    }
                },
                "required": ["task_id"]
            }
        ),
        Tool(
            name="calculate",
            description="Perform mathematical calculations (add, subtract, multiply, divide)",
            inputSchema={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "The mathematical operation to perform"
                    },
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls and forward them to FastAPI endpoints"""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            if name == "get_health":
                response = await client.get(f"{API_URL}/health")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "get_users":
                response = await client.get(f"{API_URL}/users")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "get_user":
                user_id = arguments["user_id"]
                response = await client.get(f"{API_URL}/users/{user_id}")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "create_user":
                user_data = {
                    "name": arguments["name"],
                    "email": arguments["email"]
                }
                if "age" in arguments:
                    user_data["age"] = arguments["age"]
                response = await client.post(
                    f"{API_URL}/users",
                    json=user_data
                )
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "delete_user":
                user_id = arguments["user_id"]
                response = await client.delete(f"{API_URL}/users/{user_id}")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "get_tasks":
                response = await client.get(f"{API_URL}/tasks")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "get_task":
                task_id = arguments["task_id"]
                response = await client.get(f"{API_URL}/tasks/{task_id}")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "create_task":
                task_data = {
                    "title": arguments["title"]
                }
                if "description" in arguments:
                    task_data["description"] = arguments["description"]
                if "completed" in arguments:
                    task_data["completed"] = arguments["completed"]
                response = await client.post(
                    f"{API_URL}/tasks",
                    json=task_data
                )
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "complete_task":
                task_id = arguments["task_id"]
                response = await client.put(f"{API_URL}/tasks/{task_id}/complete")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "delete_task":
                task_id = arguments["task_id"]
                response = await client.delete(f"{API_URL}/tasks/{task_id}")
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            elif name == "calculate":
                calc_data = {
                    "operation": arguments["operation"],
                    "a": arguments["a"],
                    "b": arguments["b"]
                }
                response = await client.post(
                    f"{API_URL}/calculate",
                    json=calc_data
                )
                response.raise_for_status()
                result = response.json()
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            
            else:
                return [TextContent(
                    type="text",
                    text=json.dumps({"error": f"Unknown tool: {name}"}, indent=2)
                )]
        
        except httpx.HTTPStatusError as e:
            error_msg = f"HTTP Error {e.response.status_code}: {e.response.text}"
            return [TextContent(type="text", text=json.dumps({"error": error_msg}, indent=2))]
        
        except httpx.RequestError as e:
            error_msg = f"Request failed: {str(e)}"
            return [TextContent(type="text", text=json.dumps({"error": error_msg}, indent=2))]
        
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            return [TextContent(type="text", text=json.dumps({"error": error_msg}, indent=2))]


async def main():
    """Main entry point for the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

