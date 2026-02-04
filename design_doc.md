了解。いま確定している仕様（MVP A / サブコマンド / JSON / due+priority / 詳細表示 / due未設定はソート最後）を前提に、**最終設計図**をまとめます。
（これを“実装の憲法”にして、以降はここからブレないように進める）

---

# CLI TODO アプリ 最終設計図（v1.0）

## 0. 目的・非目的

### 目的

* Python基礎の総復習として、**CLIで操作できるTODO管理**を実装する
* 学習観点：argparse / データ構造 / 例外 / ファイルI/O / 関数分割 / テスト容易性

### 非目的（v1.0ではやらない）

* ユーザー管理、同期、クラウド、GUI
* 複雑な検索（タグ/プロジェクト/全文検索）
* リマインダー通知

---

## 1. 仕様スコープ（MVP A + 拡張属性）

### ユースケース

* 追加：TODOを追加する（title必須、due/priority任意）
* 一覧：TODOを表示（デフォルト未完了のみ、詳細複数行）
* 完了：ID指定で完了にする
* 削除：ID指定で削除する

---

## 2. CLI I/F（コマンド仕様）

### 2.1 コマンド一覧（サブコマンド方式）

* `todo add "title" [--due YYYY-MM-DD] [--priority 1|2|3]`
* `todo list [--all] [--sort due|priority]`
* `todo done <id>`
* `todo delete <id>`

### 2.2 引数の意味・制約

#### add

* `title`：必須、空/空白のみは禁止
* `--due`：任意、形式は `YYYY-MM-DD`
* `--priority`：任意、`1..3`（1が最優先）

  * 未指定時デフォルト：`2`

#### list

* `--all`：完了済みも含めて表示
* `--sort`：

  * `due`：due昇順。`due=None` は**最後**に並べる
  * `priority`：`1→2→3` の順（昇順）

#### done/delete

* `<id>`：正の整数
* 存在しない場合：エラー

---

## 3. 表示仕様（list）

### 3.1 デフォルト表示（未完了のみ）

1件を複数行で表示する：

例：

```
#3 [ ] Buy milk
  priority : P1 (High)
  due      : 2026-02-01
  created  : 2026-01-29T19:10:00+09:00
```

* done の場合は `[x]`
* due未設定は `due : -`
* priority 表示は `P1/P2/P3` と括弧で `High/Mid/Low`

### 3.2 表示順

* `--sort` 指定なし：`id` 昇順（または追加順）※実装簡易優先
* `--sort due`：due昇順、dueなし最後
* `--sort priority`：priority昇順（P1→P3）

---

## 4. データモデル

### 4.1 Todo（1件）

| フィールド      | 型          | 必須 | 例                           | 備考           |
| ---------- | ---------- | -: | --------------------------- | ------------ |
| id         | int        |  ✅ | 3                           | 一意           |
| title      | str        |  ✅ | "Buy milk"                  | 空禁止          |
| done       | bool       |  ✅ | false                       |              |
| created_at | str        |  ✅ | "2026-02-01T22:00:00+09:00" | ISO 8601     |
| due        | str | null |  ❌ | "2026-02-10" / null         | `YYYY-MM-DD` |
| priority   | int        |  ✅ | 2                           | 1..3（未指定は2）  |

### 4.2 ストレージ全体（JSON）

トップレベルは以下：

```json
{
  "next_id": 4,
  "todos": [
    {
      "id": 3,
      "title": "Buy milk",
      "done": false,
      "created_at": "2026-02-01T22:00:00+09:00",
      "due": "2026-02-10",
      "priority": 1
    }
  ]
}
```

* `next_id` を採用：削除後もID衝突しない
* `todos` は配列

---

## 5. 永続化（ファイル）

### 保存先

* 既定：`./todo.json`（プロジェクト直下）

### 初期化

* `todo.json` が無い場合：以下で開始

```json
{"next_id": 1, "todos": []}
```

### I/O方針

* 読み込み失敗（JSON壊れている等）は「明示的にエラー」推奨
  ※学習目的：壊れたデータを黙って上書きしない

---

## 6. モジュール構成（最終形）

まずは1ファイルで動かしてから、最終的に下記へ分割。

```
todo/
  __init__.py
  __main__.py      # CLI entry
  cli.py           # argparse、表示、エラーハンドリング
  models.py        # Todoのデータ構造（dataclass or TypedDict）
  storage.py       # JSON load/save
  service.py       # add/list/done/deleteのユースケース
  validators.py    # due/priority/titleの検証
```

### 責務

* `cli.py`：引数→service呼び出し、表示、例外をユーザー向け文言に変換
* `service.py`：ビジネスルール（ID採番、状態変更、並び替え）
* `storage.py`：ファイルI/Oのみ（ロジックは持たない）
* `validators.py`：入力検証・正規化

---

## 7. エラー設計

### エラー種別（最低限）

* NotFound: `Not found: <id>`
* Validation:

  * `title is required`
  * `Invalid due date (YYYY-MM-DD)`
  * `priority must be 1-3`
* Storage:

  * `Failed to read todo.json`（JSON破損など）

### CLIの終了コード（任意だが推奨）

* 正常：0
* バリデーション/存在しないID：2
* ストレージ：3

---

## 8. 実装順（確定）

1. storage（load/save）
2. validators（title/due/priority）
3. service（add→list→done→delete）
4. cli（argparseでサブコマンド）
5. README（スモーク手順）

---

## 9. 完成判定（スモーク）

次が全部通れば v1.0 完了：

* `todo add "A" --due 2026-02-01 --priority 1`
* `todo add "B"`
* `todo list`（未完了だけ・詳細表示）
* `todo done 1`
* `todo list`（1が消える or doneが含まれない）
* `todo list --all`（1が[x]で見える）
* `todo delete 2`
* `todo list --all`（2が消える）

---

