##　使い方
- python -m todo で **__main__.py** を実行

### Issue の作成 (GitHub)
`gh` CLI がインストール・認証済みであることを前提に、GitHub Issue を作成します。

- タイトル必須:
  - `python -m todo create "タイトル"`
- 説明付き:
  - `python -m todo create "タイトル" --description "詳細"`
- リポジトリ指定:
  - `python -m todo create "タイトル" --repo OWNER/REPO`
- ラベル/アサイン付き:
  - `python -m todo create "タイトル" --labels bug urgent --assignees octocat`

### GitHub Issue 一括作成スクリプト
指定された10件の Issue をまとめて作成する場合は、以下を実行します。

- デフォルトリポジトリで作成:
  - `./create_github_issues.sh`
- リポジトリ指定:
  - `./create_github_issues.sh OWNER/REPO`
