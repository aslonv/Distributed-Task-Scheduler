# app/tasks.py
from uuid import uuid4
from asyncio import sleep
from typing import Dict

# Simulating a database of tasks
task_db: Dict[str, Dict] = {}

async def create_task(task_data: dict, current_user: dict) -> str:
    task_id = str(uuid4())
    task_db[task_id] = {
        "id": task_id,
        "user_id": current_user["id"],
        "data": task_data,
        "status": "pending"
    }
    # Simulate task processing
    await sleep(5)
    task_db[task_id]["status"] = "completed"
    return task_id

async def get_task_status(task_id: str) -> str:
    if task_id not in task_db:
        return "not_found"
    return task_db[task_id]["status"]
