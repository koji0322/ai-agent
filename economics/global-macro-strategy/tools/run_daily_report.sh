#!/bin/bash
# run_daily_report.sh
# 1-day アノマリー検知レポートを自動生成する
# launchd から毎朝（火〜土）6:00 に呼び出される

set -euo pipefail

PROJECT_DIR="/Users/matsubarakouji/ai-agent/economics/global-macro-strategy"
DATA_DIR="$PROJECT_DIR/data/assets"
REPORT_DIR="$PROJECT_DIR/data/reports/daily"
CLAUDE="/Users/matsubarakouji/.local/bin/claude"

mkdir -p "$REPORT_DIR"

# ── 最新の assetdata CSV を取得 ──────────────────────────────────────────────
LATEST_CSV=$(ls -t "$DATA_DIR"/assetdata_*.csv 2>/dev/null | head -1 || true)

if [ -z "$LATEST_CSV" ]; then
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') assetdata CSV が見つかりません: $DATA_DIR" >&2
    exit 1
fi

# ファイル名から基準日を抽出（assetdata_YYYYMMDD.csv → YYYYMMDD）
BASE_DATE=$(basename "$LATEST_CSV" .csv | sed 's/assetdata_//')
REPORT_PATH="$REPORT_DIR/report_${BASE_DATE}.md"

echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') 基準日: $BASE_DATE"
echo "[INFO]  CSV: $LATEST_CSV"
echo "[INFO]  出力先: $REPORT_PATH"

# ── すでにレポートが存在する場合はスキップ ─────────────────────────────────
if [ -f "$REPORT_PATH" ]; then
    echo "[SKIP]  $REPORT_PATH は既に存在します"
    exit 0
fi

# ── Claude Code でレポート生成 ──────────────────────────────────────────────
# --allowedTools: 使用を許可するツールを明示（WebSearch・Read・Glob のみ）
# --output-format text: Markdown テキストとして取得
cd "$PROJECT_DIR"

"$CLAUDE" -p \
    "1-dayレポートを作成してください。分析対象日: ${BASE_DATE}、CSV: ${LATEST_CSV}" \
    --allowedTools "Read,Glob,WebSearch,WebFetch" \
    --output-format text \
    > "$REPORT_PATH"

echo "[DONE]  $(date '+%Y-%m-%d %H:%M:%S') レポート保存: $REPORT_PATH"

# ── GitHub 同期 ───────────────────────────────────────────────────────────────
bash "$PROJECT_DIR/tools/git_sync.sh" \
    "$REPORT_PATH" \
    "auto: report_${BASE_DATE} [日次レポート]" \
    || echo "[WARN]  $(date '+%Y-%m-%d %H:%M:%S') git 同期に失敗しました"
