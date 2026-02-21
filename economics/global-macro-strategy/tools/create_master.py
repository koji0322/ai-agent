#!/usr/bin/env python3
"""
【一回限りの移行スクリプト】
Google Sheets からエクスポートしたサンプルCSVを読み込み、
静的ETFメタデータ (etf_master.csv) を作成する。

Usage:
  python create_master.py
  python create_master.py --source path/to/Export_YYYYMMDD_HHMMSS.csv
"""

import argparse
import csv
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DEFAULT_SOURCE = SCRIPT_DIR.parent / "prompt" / "pre-review" / "sample-data-Export_20260221_065403.csv"
MASTER_CSV = SCRIPT_DIR / "etf_master.csv"

STATIC_COLS = [
    "NO", "名称", "Ticker",
    "カテゴリ1", "カテゴリ2", "カテゴリ3", "カテゴリ4",
    "ETFの特徴", "グローバルマクロ戦略の視点",
]


def main():
    parser = argparse.ArgumentParser(description="ETFマスターCSV作成（一回限り）")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="元CSVファイルのパス")
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"ERROR: ファイルが見つかりません: {source_path}")
        raise SystemExit(1)

    rows = []
    with open(source_path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader)  # ヘッダーをスキップ
        for row in reader:
            # Tickerが空の行（区切り行）はスキップ
            ticker = row[2].strip() if len(row) > 2 else ""
            if not ticker:
                continue
            static_row = row[:9]
            # 不足分を空文字で補完
            while len(static_row) < 9:
                static_row.append("")
            rows.append(static_row)

    with open(MASTER_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(STATIC_COLS)
        writer.writerows(rows)

    print(f"作成完了: {MASTER_CSV}")
    print(f"  ETFエントリ数: {len(rows)} 行（重複Ticker含む）")
    tickers = {r[2] for r in rows}
    print(f"  ユニークTicker数: {len(tickers)}")


if __name__ == "__main__":
    main()
