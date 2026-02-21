#!/bin/bash
# run_export.sh
# 資産価格CSVを取得し、GitHub に同期する
# launchd から火〜土 05:55 に呼び出される

set -euo pipefail

PROJECT_DIR="/Users/matsubarakouji/ai-agent/economics/global-macro-strategy"
PYTHON="/opt/homebrew/bin/python3"

echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') === 資産価格エクスポート 開始 ==="

# ── CSV 生成 ──────────────────────────────────────────────────────────────────
"$PYTHON" "$PROJECT_DIR/tools/export_csv.py"

# ── 生成されたファイルを特定 ─────────────────────────────────────────────────
LATEST_CSV=$(ls -t "$PROJECT_DIR/data/assets"/assetdata_*.csv 2>/dev/null | head -1 || true)
if [ -z "$LATEST_CSV" ]; then
    echo "[ERROR] CSVが見つかりません" >&2
    exit 1
fi

BASE_DATE=$(basename "$LATEST_CSV" .csv | sed 's/assetdata_//')

# ── GitHub 同期 ───────────────────────────────────────────────────────────────
bash "$PROJECT_DIR/tools/git_sync.sh" \
    "$LATEST_CSV" \
    "auto: assetdata_${BASE_DATE} [価格取得]" \
    || echo "[WARN]  $(date '+%Y-%m-%d %H:%M:%S') git 同期に失敗しました"

echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') === 資産価格エクスポート 完了 ==="
