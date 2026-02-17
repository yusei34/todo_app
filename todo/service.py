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

