from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from uuid import uuid4

app = FastAPI(title="Tasks API", version="0.1.0")

class Task(BaseModel):
    id: str
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

db: Dict[str, Task] = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return list(db.values())

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    task = Task(id=str(uuid4()), title=payload.title, done=False)
    db[task.id] = task
    return task

@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, done: bool):
    if task_id not in db:
        raise HTTPException(404, "Task not found")
    task = db[task_id]
    task.done = done
    db[task_id] = task
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    if task_id not in db:
        raise HTTPException(404, "Task not found")
    del db[task_id]
    return None
