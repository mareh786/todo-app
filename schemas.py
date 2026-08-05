from pydantic import BaseModel


class TaskCreate(BaseModel):
    task: str


class TaskResponse(BaseModel):
    id: int
    task: str
    done: bool

    class Config:
        orm_mode = True
