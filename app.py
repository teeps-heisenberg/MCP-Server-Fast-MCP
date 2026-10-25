"""
FastAPI Sample Application
A simple API with multiple endpoints to demonstrate MCP Server integration
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Sample FastAPI App",
    description="A sample FastAPI application for MCP Server integration",
    version="1.0.0"
)


# Data Models
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: Optional[int] = None


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: Optional[str] = None


class CalculationRequest(BaseModel):
    operation: str  # add, subtract, multiply, divide
    a: float
    b: float


# In-memory storage
users_db: List[User] = []
tasks_db: List[Task] = []
next_user_id = 1
next_task_id = 1


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Sample FastAPI App",
        "version": "1.0.0",
        "endpoints": {
            "users": "/users",
            "tasks": "/tasks",
            "calculate": "/calculate",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "users_count": len(users_db),
        "tasks_count": len(tasks_db)
    }


@app.get("/users")
async def get_users():
    """Get all users"""
    return {"users": users_db, "count": len(users_db)}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get a specific user by ID"""
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}


@app.post("/users")
async def create_user(user: User):
    """Create a new user"""
    global next_user_id
    user.id = next_user_id
    next_user_id += 1
    users_db.append(user)
    return {"message": "User created successfully", "user": user}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete a user by ID"""
    global users_db
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users_db = [u for u in users_db if u.id != user_id]
    return {"message": "User deleted successfully", "user_id": user_id}


@app.get("/tasks")
async def get_tasks():
    """Get all tasks"""
    return {"tasks": tasks_db, "count": len(tasks_db)}


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """Get a specific task by ID"""
    task = next((t for t in tasks_db if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}


@app.post("/tasks")
async def create_task(task: Task):
    """Create a new task"""
    global next_task_id
    task.id = next_task_id
    next_task_id += 1
    task.created_at = datetime.now().isoformat()
    tasks_db.append(task)
    return {"message": "Task created successfully", "task": task}


@app.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    """Mark a task as completed"""
    task = next((t for t in tasks_db if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = True
    return {"message": "Task marked as completed", "task": task}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task by ID"""
    global tasks_db
    task = next((t for t in tasks_db if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return {"message": "Task deleted successfully", "task_id": task_id}


@app.post("/calculate")
async def calculate(req: CalculationRequest):
    """Perform mathematical calculations"""
    operation = req.operation.lower()
    
    if operation == "add":
        result = req.a + req.b
    elif operation == "subtract":
        result = req.a - req.b
    elif operation == "multiply":
        result = req.a * req.b
    elif operation == "divide":
        if req.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = req.a / req.b
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid operation. Supported: add, subtract, multiply, divide"
        )
    
    return {
        "operation": operation,
        "a": req.a,
        "b": req.b,
        "result": result
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

