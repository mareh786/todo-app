from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App API")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=List[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)) -> List[schemas.TaskResponse]:
    tasks = db.query(models.Task).order_by(models.Task.id).all()
    return tasks


@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task_create: schemas.TaskCreate, db: Session = Depends(get_db)) -> schemas.TaskResponse:
    if not task_create.task.strip():
        raise HTTPException(status_code=400, detail="Task text must not be empty")
    task = models.Task(task=task_create.task.strip())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.put("/tasks/{task_id}/done", response_model=schemas.TaskResponse)
def mark_task_done(task_id: int, db: Session = Depends(get_db)) -> schemas.TaskResponse:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.done = True
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> None:
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return None
