#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-}"

create_issue() {
  local title="$1"
  local body="$2"

  if [[ -n "$REPO" ]]; then
    gh issue create --repo "$REPO" --title "$title" --body "$body"
  else
    gh issue create --title "$title" --body "$body"
  fi
}

read -r -d '' ISSUE_1_BODY <<'EOF'
## 🎯 Milestone 0: Project Setup

### Goal
`python -m todo` が実行できる

### Done 条件
- プロジェクト構成が確定
- 実行するとメッセージが出る

### Tasks
- [ ] ディレクトリ作成（`todo/`）
- [ ] `__main__.py` 作成
- [ ] `README.md` に起動方法を記載
EOF

read -r -d '' ISSUE_2_BODY <<'EOF'
## 💾 Milestone 1: Core（データ & 永続化）

### Goal
Todo 1件の構造を固定する

### Done 条件
- 以下の属性が揃っている
  `id, title, done, created_at, due, priority`

### Tasks
- [ ] dict or dataclass でモデル定義
- [ ] サンプル Todo を1件作成
EOF

read -r -d '' ISSUE_3_BODY <<'EOF'
## 💾 Milestone 1: Core（データ & 永続化）

### Goal
`./todo.json` に永続化できる

### Done 条件
- ファイルが無くても初期化される
- `next_id` を使った ID 管理

### Tasks
- [ ] `load_data()` 実装
- [ ] `save_data(data)` 実装
- [ ] 手動で read → write 確認
EOF

read -r -d '' ISSUE_4_BODY <<'EOF'
## ⚙️ Milestone 2: Service（ユースケース）

### Goal
TODO を1件追加できる

### Done 条件
- title 必須
- due は `YYYY-MM-DD`
- priority は 1〜3（未指定は2）
- next_id が進む

### Tasks
- [ ] title バリデーション
- [ ] due バリデーション
- [ ] priority バリデーション
- [ ] `add_todo()` 実装
EOF

read -r -d '' ISSUE_5_BODY <<'EOF'
## ⚙️ Milestone 2: Service（ユースケース）

### Goal
TODO を詳細表示できる

### Done 条件
- デフォルト：未完了のみ
- `--all` で完了含む
- `--sort due|priority`
  - due=None は最後

### Tasks
- [ ] フィルタ処理
- [ ] ソート処理
- [ ] 複数行フォーマット表示
EOF

read -r -d '' ISSUE_6_BODY <<'EOF'
## ⚙️ Milestone 2: Service（ユースケース）

### Goal
ID指定で完了にできる

### Done 条件
- done=True になる
- 存在しないIDはエラー

### Tasks
- [ ] ID 検索
- [ ] done フラグ更新
- [ ] 保存
EOF

read -r -d '' ISSUE_7_BODY <<'EOF'
## ⚙️ Milestone 2: Service（ユースケース）

### Goal
ID指定で削除できる

### Done 条件
- 対象が削除される
- ID衝突しない

### Tasks
- [ ] ID 検索
- [ ] 削除
- [ ] 保存
EOF

read -r -d '' ISSUE_8_BODY <<'EOF'
## 🖥 Milestone 3: CLI（argparse）

### Goal
CLI から全操作が可能

### Done 条件
- `add / list / done / delete` が使える
- `-h` でヘルプ表示

### Tasks
- [ ] argparse サブコマンド定義
- [ ] 引数 → service 呼び出し
- [ ] エラーをユーザー向け表示に変換
EOF

read -r -d '' ISSUE_9_BODY <<'EOF'
## 🧹 Milestone 4: Quality & Finish

### Goal
失敗時の挙動が一貫している

### Done 条件
- バリデーション / NotFound / Storage エラーが区別される

### Tasks
- [ ] 例外クラス定義（任意）
- [ ] CLI 側で一括ハンドリング
EOF

read -r -d '' ISSUE_10_BODY <<'EOF'
## 🧹 Milestone 4: Quality & Finish

### Goal
完成判定が明確

### Done 条件
- README の手順通りで期待結果になる

### Tasks
- [ ] add → list → done → delete の例を書く
EOF

create_issue "Issue #1: プロジェクト雛形と実行確認" "$ISSUE_1_BODY"
create_issue "Issue #2: Todo データモデル定義" "$ISSUE_2_BODY"
create_issue "Issue #3: JSON ストレージ（load / save）" "$ISSUE_3_BODY"
create_issue "Issue #4: add（追加）" "$ISSUE_4_BODY"
create_issue "Issue #5: list（一覧表示）" "$ISSUE_5_BODY"
create_issue "Issue #6: done（完了）" "$ISSUE_6_BODY"
create_issue "Issue #7: delete（削除）" "$ISSUE_7_BODY"
create_issue "Issue #8: CLI サブコマンド実装" "$ISSUE_8_BODY"
create_issue "Issue #9: エラー設計の統一" "$ISSUE_9_BODY"
create_issue "Issue #10: README にスモークテスト記載" "$ISSUE_10_BODY"
