from fastapi import FastAPI
from typing import Optional


api = FastAPI()

all_todos = [
    {"todo_id": 1, "todo_name": "Sports", "todo_description": "Go to the gym"},
    {
        "todo_id": 2,
        "todo_name": "Study",
        "todo_description": "Read FastAPI documentation",
    },
    {
        "todo_id": 3,
        "todo_name": "Work",
        "todo_description": "Finish API endpoint implementation",
    },
    {
        "todo_id": 4,
        "todo_name": "Groceries",
        "todo_description": "Buy fruits and vegetables",
    },
    {
        "todo_id": 5,
        "todo_name": "Relax",
        "todo_description": "Watch a movie in the evening",
    },
]


# GET, POST, PUT, DELETE
@api.get("/")
def index():
    return {"message": "Hello World"}


@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {"result": todo}


@api.get("/todos")
def get_todos(first_n: Optional[int] = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
