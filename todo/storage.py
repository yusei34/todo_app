from pathlib import Path
import json

def load_data(path = "todo.json") :
        path = Path(path)
        if path.exists():
            print("jsonファイルがあります")
            # ここでjsonファイルの読み込み処理
        else :
            init_data =  {"next_id" : 1, "todos" : []}
            return init_data

#以下コードはファイルがない場合の動作確認用テスト関数 
# def test_load_data(path = "test.json") :
#         path = Path(path)
#         if path.exists():
#             print("jsonファイルがあります")
#             # ここでjsonファイルの読み込み処理
#         else :
#             init_data =  {"next_id" : 1, "todos" : []}
#             return print(init_data)


    
    
        """
        1. ファイルが存在するか確認
            - 無ければ初期データを返す

        2. JSONとして読み込む
            - JSONDecodeError は例外

        3. 読み込んだ dict を整形
            - created_at, due を str -> date に変換
            - next_id, todos があることを最低限確認

        4. dict を返す
        """ 
    
    

def save_data(data: dict, path = "todo.json") :
    pass

data = load_data()
# data = test_load_data()

