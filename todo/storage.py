from pathlib import Path
import json

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

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise e
    return data




    
       
    

def save_data(data: dict, path = "todo.json") :
    pass

data = load_data()
print(data)


        

    