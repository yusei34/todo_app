from datetime import date
from dataclasses import asdict
from .models import Todo

def add_todo(data:dict, title:str, due:date | None = None, priority : int = 2 ) -> dict : 
    
    new_id = data["next_id"]
    
    todo = Todo(
        id=new_id,
        title=title,
        due=due,
        priority=priority
        )
    
    data["todos"].append(asdict(todo))
    data["next_id"] += 1
    
    return data

def list_todos(data: dict,show_all: bool = False,sort_by: str | None = None) -> list[dict]:
 
    todos = data["todos"]
    
    if not show_all:
        filtered = [todo for todo in todos if not todo["done"]]
        todos = filtered
 
    return todos
            
            
