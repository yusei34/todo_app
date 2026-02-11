from pathlib import Path
import json
from datetime import date

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
    
    if not path.exists():
        return {"next_id": 1, "todos": []}
    
    if path.stat().st_size == 0:
        return {"next_id": 1, "todos": []}

    with open(path, "r", encoding="utf-8") as f:
        try:
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
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    

data = load_data()
save_data(data)


        

    