from datetime import date
from dataclasses import asdict
from .models import Todo

def add_todo(data:dict, title:str, due:date | None = None, priority : int = 2 ) -> dict : 
    return data

