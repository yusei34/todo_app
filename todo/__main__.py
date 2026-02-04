from dataclasses import dataclass, field
from datetime import date

class Todo:
    id : int
    title : str
    done : bool = field(default=False)
    created_at : date
    due : date | None
    priority : int | None = field(default=None)
    
def __post_init__(self):
    self.created_at = date.today()
  
def main():
    print("start")

if __name__ == "__main__":
    main()