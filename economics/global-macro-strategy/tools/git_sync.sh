#!/bin/bash
# git_sync.sh <file_path> <commit_message>
# 自動生成ファイルを GitHub に同期する共通ヘルパー
# 呼び出し側で || true を使うこと（sync失敗でも本体ジョブを止めない）

set -euo pipefail

REPO_ROOT="/Users/matsubarakouji/ai-agent"
FILE_PATH="${1:?引数1: ファイルパスが必要}"
COMMIT_MSG="${2:?引数2: コミットメッセージが必要}"

cd "$REPO_ROOT"

# ステージング
git add "$FILE_PATH"

# 差分がなければスキップ
if git diff --cached --quiet; then
    echo "[GIT]   変更なし、スキップ: $FILE_PATH"
    exit 0
fi

# コミット＆プッシュ
git commit -m "$COMMIT_MSG"
git push origin master
echo "[GIT]   同期完了: $FILE_PATH"
