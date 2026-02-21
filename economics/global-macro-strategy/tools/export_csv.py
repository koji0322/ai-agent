#!/usr/bin/env python3
"""
グローバルマクロ戦略 ETFデータ CSVエクスポートスクリプト

Google Sheets + GAS の代替。yfinance で価格を取得し、
同一フォーマットの assetdata_YYYYMMDD.csv を生成する。

Usage:
  python export_csv.py                      # 直近の取引日を自動検出
  python export_csv.py --date 20260221      # 基準日を指定
  python export_csv.py --date 20260221 --verbose
"""

import argparse
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

# --- パス定義 ---
SCRIPT_DIR = Path(__file__).parent
MASTER_CSV = SCRIPT_DIR / "etf_master.csv"
OUTPUT_DIR = SCRIPT_DIR.parent / "data" / "assets"

# --- 出力カラム定義（サンプルCSVと同一） ---
OUTPUT_HEADER = [
    "NO", "名称", "Ticker",
    "カテゴリ1", "カテゴリ2", "カテゴリ3", "カテゴリ4",
    "ETFの特徴", "グローバルマクロ戦略の視点",
    "Current", "Per Yesterday", "Yesterday",
    "Two days before", "7", "14", "30", "90", "0101", "365",
    "Two days before", "7", "14", "30", "90", "0101", "365",
]


def prev_trading_date(ref: date) -> date:
    """ref の直前の取引日（土日を除く）を返す。祝日は yfinance が自動処理。"""
    d = ref - timedelta(days=1)
    while d.weekday() >= 5:  # 5=土、6=日
        d -= timedelta(days=1)
    return d


def get_price_at_or_before(series: pd.Series, target: date) -> float | None:
    """target 以前で最も直近の終値を返す。データなければ None。"""
    ts = pd.Timestamp(target)
    subset = series[series.index <= ts]
    if subset.empty:
        return None
    val = float(subset.iloc[-1])
    return val if not pd.isna(val) else None


def get_ytd_price(series: pd.Series, base: date) -> float | None:
    """前年12月31日（または最終取引日）の価格を返す。"""
    dec31 = date(base.year - 1, 12, 31)
    return get_price_at_or_before(series, dec31)


def safe_return(current: float, base_price: float | None) -> float | None:
    """(current - base) / base を計算。base が None / 0 なら None。"""
    if base_price is None or base_price == 0:
        return None
    return (current - base_price) / base_price


def fmt_price(val: float | None) -> str:
    """価格を小数点2桁に丸めて文字列化。None なら空文字。"""
    if val is None:
        return ""
    return f"{round(val, 2)}"


def fmt_return(val: float | None) -> str:
    """リターン（割合）をフル精度で文字列化。None なら空文字。"""
    if val is None:
        return ""
    return repr(val)


def load_master() -> list[dict]:
    if not MASTER_CSV.exists():
        print(f"ERROR: {MASTER_CSV} が見つかりません。先に create_master.py を実行してください。", file=sys.stderr)
        raise SystemExit(1)
    with open(MASTER_CSV, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def fetch_prices(tickers: list[str], start: date, end: date, verbose: bool) -> pd.DataFrame:
    """yfinance で一括ダウンロード。終値DataFrameを返す（列=Ticker）。"""
    if verbose:
        print(f"  価格取得: {len(tickers)} Ticker, {start} 〜 {end}")

    raw = yf.download(
        tickers,
        start=start.strftime("%Y-%m-%d"),
        end=(end + timedelta(days=1)).strftime("%Y-%m-%d"),
        auto_adjust=True,
        progress=False,
    )

    if raw.empty:
        print("ERROR: yfinance からデータを取得できませんでした。", file=sys.stderr)
        raise SystemExit(1)

    # Close カラムを抽出
    if isinstance(raw.columns, pd.MultiIndex):
        closes = raw["Close"]
    else:
        closes = raw[["Close"]]
        closes.columns = tickers[:1]

    # 単一 Ticker の場合 Series になることがある
    if isinstance(closes, pd.Series):
        closes = closes.to_frame(name=tickers[0])

    return closes


def build_row(etf: dict, prices: pd.DataFrame, base: date, verbose: bool) -> list[str]:
    """ETF 1行分の出力データを構築する。"""
    ticker = etf["Ticker"].strip()
    meta = [
        etf["NO"], etf["名称"], ticker,
        etf["カテゴリ1"], etf["カテゴリ2"], etf["カテゴリ3"], etf["カテゴリ4"],
        etf["ETFの特徴"], etf["グローバルマクロ戦略の視点"],
    ]

    if ticker not in prices.columns:
        if verbose:
            print(f"  WARN: {ticker} のデータなし — 数値列を空欄で出力")
        return meta + [""] * 17

    series = prices[ticker].dropna()

    # --- 価格取得 ---
    current = get_price_at_or_before(series, base)
    if current is None:
        if verbose:
            print(f"  WARN: {ticker} の Current 価格なし")
        return meta + [""] * 17

    p_yesterday = get_price_at_or_before(series, base - timedelta(days=1))
    p_2d = get_price_at_or_before(series, base - timedelta(days=2))
    p_7d = get_price_at_or_before(series, base - timedelta(days=7))
    p_14d = get_price_at_or_before(series, base - timedelta(days=14))
    p_30d = get_price_at_or_before(series, base - timedelta(days=30))
    p_90d = get_price_at_or_before(series, base - timedelta(days=90))
    p_ytd = get_ytd_price(series, base)
    p_365d = get_price_at_or_before(series, base - timedelta(days=365))

    # --- リターン計算: (Current - period_price) / period_price ---
    per_yesterday = safe_return(current, p_yesterday)
    r_2d = safe_return(current, p_2d)
    r_7d = safe_return(current, p_7d)
    r_14d = safe_return(current, p_14d)
    r_30d = safe_return(current, p_30d)
    r_90d = safe_return(current, p_90d)
    r_ytd = safe_return(current, p_ytd)
    r_365d = safe_return(current, p_365d)

    dynamic = [
        fmt_price(current),
        fmt_return(per_yesterday),
        fmt_price(p_yesterday),
        fmt_return(r_2d),
        fmt_return(r_7d),
        fmt_return(r_14d),
        fmt_return(r_30d),
        fmt_return(r_90d),
        fmt_return(r_ytd),
        fmt_return(r_365d),
        fmt_price(p_2d),
        fmt_price(p_7d),
        fmt_price(p_14d),
        fmt_price(p_30d),
        fmt_price(p_90d),
        fmt_price(p_ytd),
        fmt_price(p_365d),
    ]

    return meta + dynamic


def main():
    parser = argparse.ArgumentParser(description="ETFマーケットデータ CSVエクスポート")
    parser.add_argument("--date", help="基準日 YYYYMMDD（省略時: 直近取引日）")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    # --- 基準日の決定 ---
    if args.date:
        base = datetime.strptime(args.date, "%Y%m%d").date()
    else:
        base = prev_trading_date(date.today())

    print(f"基準日: {base}")

    # --- マスターデータ読み込み ---
    etfs = load_master()
    tickers = sorted({e["Ticker"].strip() for e in etfs if e["Ticker"].strip()})
    print(f"Ticker数: {len(tickers)} ユニーク / {len(etfs)} 行（重複含む）")

    # --- 価格データ取得（基準日から400日前まで） ---
    start = base - timedelta(days=400)
    prices = fetch_prices(tickers, start, base, args.verbose)

    if args.verbose:
        print(f"  取得済み Ticker: {list(prices.columns)}")

    # --- 行ごとにデータ構築 ---
    output_rows = [OUTPUT_HEADER]
    for etf in etfs:
        row = build_row(etf, prices, base, args.verbose)
        output_rows.append(row)

    # --- CSV 書き出し ---
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"assetdata_{base.strftime('%Y%m%d')}.csv"

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(output_rows)

    print(f"出力完了: {output_path}")
    print(f"  行数: {len(output_rows) - 1} ETF")


if __name__ == "__main__":
    main()
