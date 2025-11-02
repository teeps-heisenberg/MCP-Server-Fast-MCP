# FastAPI MCP Server Integration with Gemini CLI

This project demonstrates how to create a FastAPI application, wrap it with an MCP (Model Context Protocol) server, and integrate it with Gemini CLI for natural language interactions.

## Project Structure

```
.
├── app.py              # FastAPI application with REST endpoints
├── mcp_server.py       # MCP server that exposes FastAPI endpoints as tools
├── requirements.txt    # Python dependencies
├── gemini-config.json  # Gemini CLI configuration file
└── README.md          # This file
```

## Features

### FastAPI Application (`app.py`)
- **User Management**: Create, read, and delete users
- **Task Management**: Create, read, update (complete), and delete tasks
- **Calculations**: Perform mathematical operations (add, subtract, multiply, divide)
- **Health Check**: Monitor application status

### MCP Server (`mcp_server.py`)
Exposes 11 FastAPI endpoints as MCP tools:
- `get_health` - Check API health status
- `get_users` - Retrieve all users
- `get_user` - Get a specific user by ID
- `create_user` - Create a new user
- `delete_user` - Delete a user by ID
- `get_tasks` - Retrieve all tasks
- `get_task` - Get a specific task by ID
- `create_task` - Create a new task
- `complete_task` - Mark a task as completed
- `delete_task` - Delete a task by ID
- `calculate` - Perform mathematical calculations

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI Application

In one terminal, start the FastAPI server:

```bash
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### 3. Install Gemini CLI

Install the Gemini CLI globally using npm:

```bash
npm install -g @google/gemini-cli@latest
```

### 4. Configure Gemini CLI

Add the MCP server to Gemini CLI configuration. The configuration file is typically located at:

- **Windows**: `%APPDATA%\Gemini CLI\config.json`
- **macOS/Linux**: `~/.config/gemini-cli/config.json`

Or use the Gemini CLI command:

```bash
gemini mcp add fastapi-mcp-server python mcp_server.py
```

Alternatively, you can manually add this to your Gemini CLI config file:

```json
{
  "mcpServers": {
    "fastapi-mcp-server": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        "PYTHONPATH": "."
      }
    }
  }
}
```

**Note**: Make sure to provide the full path to `mcp_server.py` if running from a different directory.

### 5. Verify Setup

Verify that the MCP server is properly configured:

```bash
gemini mcp list
```

## Practical Demonstration with Gemini CLI

Once everything is set up, you can interact with your FastAPI application through Gemini CLI using natural language. Here are some examples:

### Example 1: Check API Health

```
gemini> Check the health of the FastAPI application
```

Gemini CLI will call the `get_health` tool and return the API status.

### Example 2: Create a User

```
gemini> Create a new user named John Doe with email john@example.com and age 30
```

This will invoke the `create_user` tool with the provided parameters.

### Example 3: List All Users

```
gemini> Show me all users
```

This uses the `get_users` tool to retrieve all users from the API.

### Example 4: Create a Task

```
gemini> Create a task titled "Complete MCP integration" with description "Integrate MCP server with Gemini CLI"
```

The `create_task` tool will be called to create the task.

### Example 5: Perform Calculation

```
gemini> Calculate 25 multiplied by 4
```

Or:

```
gemini> What is 100 divided by 5?
```

This will use the `calculate` tool to perform the mathematical operation.

### Example 6: Complete a Task

```
gemini> Mark task with ID 1 as completed
```

This will call the `complete_task` tool.

### Example 7: Get Task Details

```
gemini> Show me task number 1
```

Uses the `get_task` tool to retrieve task details.

### Example 8: Delete a User

```
gemini> Delete user with ID 1
```

Invokes the `delete_user` tool.

## Testing the API Directly

You can also test the FastAPI endpoints directly using curl or a REST client:

```bash
# Health check
curl http://localhost:8000/health

# Get all users
curl http://localhost:8000/users

# Create a user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "age": 30}'

# Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Task", "description": "This is a test task"}'

# Perform calculation
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "multiply", "a": 25, "b": 4}'
```

## API Documentation

Once the FastAPI application is running, you can access interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Troubleshooting

### MCP Server Not Found

If Gemini CLI cannot find the MCP server:
1. Ensure you're in the correct directory when starting Gemini CLI
2. Check that the path to `mcp_server.py` in the config is correct
3. Verify Python is in your PATH

### Connection Errors

If you get connection errors:
1. Ensure the FastAPI application is running on port 8000
2. Check that the `API_URL` in `mcp_server.py` matches your FastAPI server URL
3. Verify there are no firewall restrictions

### Import Errors

If you encounter import errors:
1. Make sure all dependencies are installed: `pip install -r requirements.txt`
2. Verify you're using the correct Python environment
3. Check that the `mcp` package is installed correctly

## Requirements

- Python 3.8 or higher
- Node.js and npm (for Gemini CLI)
- All packages listed in `requirements.txt`

## License

This is a sample project for educational purposes.

