#!/bin/bash
# run_weekly_report.sh
# 週次ウォーゲーミング・ブリーフを自動生成する
# launchd から土曜 6:10 に呼び出される（daily report 完了後）

set -euo pipefail

PROJECT_DIR="/Users/matsubarakouji/ai-agent/economics/global-macro-strategy"
DATA_DIR="$PROJECT_DIR/data/assets"
REPORT_DIR="$PROJECT_DIR/data/reports/weekly"
CLAUDE="/Users/matsubarakouji/.local/bin/claude"

mkdir -p "$REPORT_DIR"

# ── 最新の assetdata CSV を取得 ──────────────────────────────────────────────
LATEST_CSV=$(ls -t "$DATA_DIR"/assetdata_*.csv 2>/dev/null | head -1 || true)

if [ -z "$LATEST_CSV" ]; then
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') assetdata CSV が見つかりません: $DATA_DIR" >&2
    exit 1
fi

# ファイル名から週末日付を抽出（assetdata_YYYYMMDD.csv → YYYYMMDD）
WEEKEND_DATE=$(basename "$LATEST_CSV" .csv | sed 's/assetdata_//')
REPORT_PATH="$REPORT_DIR/weekly_${WEEKEND_DATE}.md"

echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') 週末日付: $WEEKEND_DATE"
echo "[INFO]  CSV: $LATEST_CSV"
echo "[INFO]  出力先: $REPORT_PATH"

# ── すでにレポートが存在する場合はスキップ ─────────────────────────────────
if [ -f "$REPORT_PATH" ]; then
    echo "[SKIP]  $REPORT_PATH は既に存在します"
    exit 0
fi

# ── Claude Code でレポート生成 ──────────────────────────────────────────────
cd "$PROJECT_DIR"

"$CLAUDE" -p \
    "週次レポートを作成してください。週末: ${WEEKEND_DATE}、CSV: ${LATEST_CSV}" \
    --allowedTools "Read,Glob,WebSearch,WebFetch" \
    --output-format text \
    > "$REPORT_PATH"

echo "[DONE]  $(date '+%Y-%m-%d %H:%M:%S') レポート保存: $REPORT_PATH"

# ── GitHub 同期 ───────────────────────────────────────────────────────────────
bash "$PROJECT_DIR/tools/git_sync.sh" \
    "$REPORT_PATH" \
    "auto: weekly_${WEEKEND_DATE} [週次レポート]" \
    || echo "[WARN]  $(date '+%Y-%m-%d %H:%M:%S') git 同期に失敗しました"
