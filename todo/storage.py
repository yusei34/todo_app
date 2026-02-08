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
    if path.exists():
        return "jsonファイルがあります"
    else :
        init_data =  {"next_id" : 1, "todos" : []}
        return init_data




    
    
       
    

def save_data(data: dict, path = "todo.json") :
    pass

data = load_data()



        

    