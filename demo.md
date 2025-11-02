# Practical Demonstration Guide - Using Gemini CLI with FastAPI MCP Server

This guide provides step-by-step practical demonstrations of using the Gemini CLI to interact with your FastAPI application through the MCP server.

## Prerequisites

1. FastAPI application running on `http://localhost:8000`
2. Gemini CLI installed and configured with the MCP server
3. MCP server properly configured in Gemini CLI

## Step-by-Step Demonstration

### Step 1: Start the FastAPI Application

```bash
# Terminal 1 - Start FastAPI
python app.py
```

Expected output:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Verify FastAPI is Running

Open your browser or use curl to verify:
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "users_count": 0,
  "tasks_count": 0
}
```

### Step 3: Start Gemini CLI

```bash
# Terminal 2 - Start Gemini CLI
gemini
```

### Step 4: Demonstration Scenarios

#### Scenario 1: Health Check

**Gemini CLI Prompt:**
```
Check the health status of my FastAPI application
```

**Expected MCP Tool Call:**
- Tool: `get_health`
- Arguments: `{}`

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000",
  "users_count": 0,
  "tasks_count": 0
}
```

---

#### Scenario 2: Create a User

**Gemini CLI Prompt:**
```
Create a new user named Alice Smith with email alice@example.com and age 28
```

**Expected MCP Tool Call:**
- Tool: `create_user`
- Arguments: `{"name": "Alice Smith", "email": "alice@example.com", "age": 28}`

**Expected Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 28
  }
}
```

---

#### Scenario 3: Create Another User

**Gemini CLI Prompt:**
```
Add a user named Bob Johnson with email bob@example.com
```

**Expected MCP Tool Call:**
- Tool: `create_user`
- Arguments: `{"name": "Bob Johnson", "email": "bob@example.com"}`

**Expected Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": 2,
    "name": "Bob Johnson",
    "email": "bob@example.com",
    "age": null
  }
}
```

---

#### Scenario 4: List All Users

**Gemini CLI Prompt:**
```
Show me all the users in the system
```

**Expected MCP Tool Call:**
- Tool: `get_users`
- Arguments: `{}`

**Expected Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice Smith",
      "email": "alice@example.com",
      "age": 28
    },
    {
      "id": 2,
      "name": "Bob Johnson",
      "email": "bob@example.com",
      "age": null
    }
  ],
  "count": 2
}
```

---

#### Scenario 5: Get Specific User

**Gemini CLI Prompt:**
```
What are the details for user ID 1?
```

**Expected MCP Tool Call:**
- Tool: `get_user`
- Arguments: `{"user_id": 1}`

**Expected Response:**
```json
{
  "user": {
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@example.com",
    "age": 28
  }
}
```

---

#### Scenario 6: Create a Task

**Gemini CLI Prompt:**
```
Create a task titled "Complete project documentation" with description "Write comprehensive documentation for the MCP integration"
```

**Expected MCP Tool Call:**
- Tool: `create_task`
- Arguments: `{"title": "Complete project documentation", "description": "Write comprehensive documentation for the MCP integration"}`

**Expected Response:**
```json
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Complete project documentation",
    "description": "Write comprehensive documentation for the MCP integration",
    "completed": false,
    "created_at": "2024-01-01T12:05:00.000000"
  }
}
```

---

#### Scenario 7: Create Multiple Tasks

**Gemini CLI Prompt:**
```
Add a task for "Review code" and another one for "Deploy to production"
```

**Expected MCP Tool Calls:**
- Tool: `create_task` with `{"title": "Review code"}`
- Tool: `create_task` with `{"title": "Deploy to production"}`

---

#### Scenario 8: List All Tasks

**Gemini CLI Prompt:**
```
Show me all tasks
```

**Expected MCP Tool Call:**
- Tool: `get_tasks`
- Arguments: `{}`

**Expected Response:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete project documentation",
      "description": "Write comprehensive documentation for the MCP integration",
      "completed": false,
      "created_at": "2024-01-01T12:05:00.000000"
    },
    {
      "id": 2,
      "title": "Review code",
      "description": null,
      "completed": false,
      "created_at": "2024-01-01T12:06:00.000000"
    },
    {
      "id": 3,
      "title": "Deploy to production",
      "description": null,
      "completed": false,
      "created_at": "2024-01-01T12:06:30.000000"
    }
  ],
  "count": 3
}
```

---

#### Scenario 9: Complete a Task

**Gemini CLI Prompt:**
```
Mark task 1 as completed
```

**Expected MCP Tool Call:**
- Tool: `complete_task`
- Arguments: `{"task_id": 1}`

**Expected Response:**
```json
{
  "message": "Task marked as completed",
  "task": {
    "id": 1,
    "title": "Complete project documentation",
    "description": "Write comprehensive documentation for the MCP integration",
    "completed": true,
    "created_at": "2024-01-01T12:05:00.000000"
  }
}
```

---

#### Scenario 10: Perform Calculations

**Gemini CLI Prompt:**
```
What is 25 multiplied by 4?
```

**Expected MCP Tool Call:**
- Tool: `calculate`
- Arguments: `{"operation": "multiply", "a": 25, "b": 4}`

**Expected Response:**
```json
{
  "operation": "multiply",
  "a": 25,
  "b": 4,
  "result": 100
}
```

**More Calculation Examples:**

```
Calculate 100 divided by 5
```
- Tool: `calculate` with `{"operation": "divide", "a": 100, "b": 5}`

```
Add 42 and 18
```
- Tool: `calculate` with `{"operation": "add", "a": 42, "b": 18}`

```
Subtract 50 from 75
```
- Tool: `calculate` with `{"operation": "subtract", "a": 75, "b": 50}`

---

#### Scenario 11: Get Task Details

**Gemini CLI Prompt:**
```
Show me details for task number 2
```

**Expected MCP Tool Call:**
- Tool: `get_task`
- Arguments: `{"task_id": 2}`

**Expected Response:**
```json
{
  "task": {
    "id": 2,
    "title": "Review code",
    "description": null,
    "completed": false,
    "created_at": "2024-01-01T12:06:00.000000"
  }
}
```

---

#### Scenario 12: Delete a Task

**Gemini CLI Prompt:**
```
Delete task 3
```

**Expected MCP Tool Call:**
- Tool: `delete_task`
- Arguments: `{"task_id": 3}`

**Expected Response:**
```json
{
  "message": "Task deleted successfully",
  "task_id": 3
}
```

---

#### Scenario 13: Delete a User

**Gemini CLI Prompt:**
```
Remove user with ID 2
```

**Expected MCP Tool Call:**
- Tool: `delete_user`
- Arguments: `{"user_id": 2}`

**Expected Response:**
```json
{
  "message": "User deleted successfully",
  "user_id": 2
}
```

---

#### Scenario 14: Complex Workflow

**Gemini CLI Prompt:**
```
Create a user named Charlie Brown with email charlie@example.com, then create a task for him titled "Setup development environment", and finally check the health status
```

**Expected MCP Tool Calls (in sequence):**
1. `create_user` with `{"name": "Charlie Brown", "email": "charlie@example.com"}`
2. `create_task` with `{"title": "Setup development environment"}`
3. `get_health` with `{}`

---

## Troubleshooting Common Issues

### Issue: "MCP tool not found"
**Solution:** Verify that the MCP server is properly configured in Gemini CLI config file.

### Issue: "Connection refused" or "Request failed"
**Solution:** 
1. Ensure FastAPI is running on port 8000
2. Check that `API_URL` in `mcp_server.py` matches your FastAPI URL
3. Verify no firewall is blocking localhost connections

### Issue: "HTTP Error 404"
**Solution:** 
- Check that the resource ID exists
- Verify the FastAPI endpoint is correct
- Check the FastAPI logs for errors

### Issue: "HTTP Error 400"
**Solution:**
- Verify all required parameters are provided
- Check parameter types match expected values
- Review the tool's input schema

## Tips for Best Results

1. **Be Specific**: Provide clear, specific instructions to Gemini CLI
2. **Use Natural Language**: You don't need to know exact tool names - Gemini will map your requests
3. **Check Status First**: Use `get_health` to verify connectivity before complex operations
4. **Chain Operations**: You can ask for multiple operations in one request

## Next Steps

After mastering these basic operations, try:
- Creating complex workflows combining multiple operations
- Using the API directly via curl to understand the underlying structure
- Exploring the FastAPI interactive docs at `http://localhost:8000/docs`
- Extending the API with additional endpoints and corresponding MCP tools

