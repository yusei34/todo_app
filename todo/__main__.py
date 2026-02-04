from dataclasses import dataclass, field
from datetime import date

@dataclass
class Todo:
    id : int
    title : str
    done : bool = field(default=False)
    created_at : date = field(default_factory=date.today)
    due : date | None = field(default=None)
    priority : int = field(default=3)
    
def main():
    pass

if __name__ == "__main__":
    main()