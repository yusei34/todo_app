from pathlib import Path
import json
from datetime import date
from copy import deepcopy

def load_data(path = "todo.json") :
    """_summary_
        1. ファイルが存在するか確認
            - 無ければ初期データを返す

        2. JSONとして読み込む
            - JSONDecodeError は例外

        3. 読み込んだ dict を整形
            - created_at, due を str -> date に変換
            - next_id, todos があることを最低限確認

        4. dict を返す
    """
    path = Path(path)
    
    # Check there is "todo.json"
    
    # 1. if "todo.json" is nothing , return Initial data 
    if not path.exists():
        return {"next_id": 1, "todos": []}
    
    # 2. There is "todo.json" but It is nothing data 
    
    # Check todo.json is 0byte
    if path.stat().st_size == 0:
        return {"next_id": 1, "todos": []}

    # Open and Read todo.json
    with open(path, "r", encoding="utf-8") as f:
        try:
            # retrieve data from todo.json  
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise e
        for todo in data["todos"]:
            todo["created_at"] = date.fromisoformat(todo["created_at"])
            if todo["due"] is not None:
                todo["due"] = date.fromisoformat(todo["due"])
    return data


def save_data(data: dict, path = "todo.json") :
    path = Path(path)
    
    out = deepcopy(data)
    
    for todo in out["todos"]:
            todo["created_at"] = todo["created_at"].isoformat()  # date -> "YYYY-MM-DD"
            if todo["due"] is not None:
                todo["due"] = todo["due"].isoformat()
                
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        
    

d = load_data()
save_data(d)
print(type(d["todos"][0]["created_at"]))


        

    