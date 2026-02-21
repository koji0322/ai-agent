# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

- **Location**: `economics/global-macro-strategy/` within the parent repo at `/Users/matsubarakouji/ai-agent`
- **Purpose**: グローバルマクロ投資戦略の分析・ナレッジ管理
- **Parent repo**: Contains `dev-learning-guides/` and `gemini-test/` as sibling projects

## Repository Notes

- The git root is `/Users/matsubarakouji/ai-agent` — git commands should target that root, not this subdirectory

---

## このシステムとは

**Claude Code を中核とした個人版グローバルマクロ分析システム**。

世界トップクラスのヘッジファンドが行う「マクロ経済環境の診断 → 市場アノマリーの検知 → 投資シナリオの設計」というインテリジェンス・サイクルを、Claude Code の WebSearch・ファイル読み書き・分析能力を駆使して個人で再現することを目的とする。

分析の核心は **12クロック・ビジネスサイクルモデル** によるレジーム判定であり、「今、世界経済はどのフェーズにあるか」を月次で診断した上で、その文脈の中で日次・週次・月次のレポートを生成する階層的な分析体系を持つ。

---

## システム全体像

```
【月次】 3-monthly-systematic-macro     ← マクロ経済の月次深掘り（GDP・ISM・PCE・金利）
    ↓ 分析結果をインプットに
【月次】 0-12clock-diagnosis            ← 12クロック判定（Clock 1〜12）
    ↓ state/current-clock.md に保存
【週次】 2-7-weekly                     ← 週次マーケット・レジーム分析・来週シナリオ設計
    ↓ 同じ12clockコンテキストを参照
【日次】 1-day                          ← 日次アノマリー検知・CEO向けブリーフィング
```

すべてのレポートは `state/current-clock.md` を共通のコンテキストとして参照し、分析に一貫性を持たせる。

---

## フォルダ構成

```
global-macro-strategy/
├── data/                データ出力先（スクリプトが自動生成）
│   ├── assets/          ETF・資産価格データ  assetdata_YYYYMMDD.csv
│   ├── reports/
│   │   ├── daily/       日次レポート    report_YYYYMMDD.md
│   │   └── weekly/      週次レポート    weekly_YYYYMMDD.md
│   ├── macro/           マクロ経済指標データ（CPI・GDP等）
│   ├── sentiment/       センチメント・フローデータ
│   ├── position/        ポジション・保有状況データ
│   └── clock/           12clock診断結果履歴
├── prompt/
│   ├── pre-review/      精査前プロンプト（原本保管）・サンプルCSV
│   └── refined/         運用中プロンプト（Claude Code専用・磨き済み）
│       ├── 0-12clock-diagnosis.md          12クロック月次診断
│       ├── 1-day.md                        日次アノマリー検知レポート
│       ├── 2-7-weekly.md                   週次ウォーゲーミングブリーフ
│       └── 3-monthly-systematic-macro.md   月次マクロ分析レポート
├── reference/
│   └── pre-review/      参照資料（12clockモデル・フレームワーク等）
│       ├── 12clock/                 12クロックモデル定義・判定基準・運用マニュアル
│       ├── 2025/                    2025年活動ログ・ヘッジファンド研究
│       ├── 5core-strategy/          5コア要素・THE MACRO EDGE 書籍開発
│       ├── economic-regime-and-cycle-analysis/  レジーム×サイクル分析
│       ├── global-macro-investor-handbook/      投資家ハンドブック（第1版）
│       ├── global-macro-investor-handbook02/    投資家ハンドブック（第2版）
│       └── jim-rodgers/             ジム・ロジャーズ戦略研究
├── state/
│   └── current-clock.md 12クロック最新診断結果（全プロンプトが参照）
└── tools/               データ生成・自動化スクリプト
    ├── etf_master.csv              ETF静的メタデータ
    ├── export_csv.py               資産価格エクスポート（→ data/assets/）
    ├── run_export.sh               export_csv.py のラッパー + git sync
    ├── run_daily_report.sh         1-dayレポート自動生成（→ data/reports/daily/）
    ├── run_weekly_report.sh        週次レポート自動生成（→ data/reports/weekly/）
    ├── git_sync.sh                 GitHub 同期ヘルパー
    ├── create_master.py            一回限りの移行スクリプト
    ├── requirements.txt
    ├── com.globalmacrosta.export.plist          launchd: 火〜土 05:55 価格取得
    ├── com.globalmacrosta.daily-report.plist    launchd: 火〜土 06:00 日次レポート生成
    └── com.globalmacrosta.weekly-report.plist   launchd: 土    06:10 週次レポート生成
```

---

## 標準的な運用カレンダー

| タイミング | 実行プロンプト | 所要時間 | インプット |
|---|---|---|---|
| **毎月中旬〜下旬** | `3-monthly-systematic-macro` | 10〜15分 | WebSearch（自動） |
| **毎月（月次直後）** | `0-12clock-diagnosis` | 5〜10分 | WebSearch（自動）+ 月次レポート |
| **毎週末（金〜土）** | `2-7-weekly` | 自動（土 06:10） | ETF CSV + WebSearch |
| **毎朝（火〜土）** | `1-day` | 自動（06:00） | ETF CSV + WebSearch |
| **レジーム転換疑い時** | `0-12clock-diagnosis` | 5〜10分 | WebSearch（自動） |

---

## 分析プロンプトの起動方法

### 月次マクロ分析レポート

```
「3-monthlyレポートを作成してください。分析対象月: 202602」
```

- プロンプト: `prompt/refined/3-monthly-systematic-macro.md` を参照して実行
- 全主要経済指標（GDP・ISM・失業率・PCE・FF金利・長期金利）をWebSearchで収集
- ビジネスサイクル分析 → 経済レジーム分析（3ステップ）→ 投資戦略への示唆を生成
- 完了後に `0-12clock-diagnosis` の実行を促す

### 12クロック診断（月1回 or レジーム転換時）

```
「12clock診断をしてください」
```

- プロンプト: `prompt/refined/0-12clock-diagnosis.md` を参照して実行
- 5視点（実体経済・心理PMI・物価・市場金利・金融政策）で現在のクロックを判定
- 4ステップアルゴリズム（トレンド判定 → 質評価 → 乖離確認 → 閾値確認）を実行
- 結果は `state/current-clock.md` に自動保存（1-day・2-7-weeklyが参照）

### 日次レポート（毎朝・自動実行）

```
「1-dayレポートを作成してください。分析対象日: 20260221」

# CSVを明示指定する場合
「1-dayレポートを作成してください。分析対象日: 20260221、CSV: [ファイルパス]」
```

- プロンプト: `prompt/refined/1-day.md` を参照して実行
- CSVを指定しない場合は `data/assets/` 配下の最新 `assetdata_*.csv` を自動使用
- `state/current-clock.md` を自動読み込みし、12clockコンテキストをレポートに反映
- 保存先: `data/reports/daily/report_YYYYMMDD.md`

### 週次レポート（週末・自動実行）

```
「週次レポートを作成してください」

# 週末日付・CSVを明示指定する場合
「週次レポートを作成してください。週末: 20260221、CSV: [ファイルパス]」
```

- プロンプト: `prompt/refined/2-7-weekly.md` を参照して実行
- CSVを指定しない場合は `data/assets/` 配下の最新 `assetdata_*.csv` を自動使用
- `state/current-clock.md` を自動読み込みし、12clockコンテキストをレポートに反映
- 7日間リターンを主軸に、相関分析・12clock整合性チェック・来週シナリオを生成
- 保存先: `data/reports/weekly/weekly_YYYYMMDD.md`

---

## 資産価格データについて

- **出所**: `tools/export_csv.py`（yfinance 経由で自動取得）
- **ファイル命名規則**: `assetdata_YYYYMMDD.csv`（YYYYMMDD = 基準日）
- **保存場所**: `data/assets/`

### 主要カラムと処理規則

| カラム | 内容 | 処理 |
|---|---|---|
| `Current` | 現在価格 | そのまま使用 |
| `Per Yesterday` | 前日比リターン | 小数形式 → ×100 で%換算 |
| `7` / `14` / `30` / `90` / `0101` / `365` | 各期間リターン | 同上 |
| `Yesterday` / `Two days before`（2回目）〜`365`（2回目） | 過去価格 | そのまま使用 |
| `NO` | 行番号 | 空白行（区切り行）は分析から除外 |

- 同一 Ticker が複数行ある場合は**最初の出現のみ**使用
- `Per Yesterday` が `-1.0` 以下、または価格が `0` / `1` の銘柄はデータ異常として除外

---

## 12クロック・ビジネスサイクルモデルについて

経済サイクルを4フェーズ・12クロックに分類し、各クロックに最適な投資行動を紐づける独自フレームワーク。

| Phase | Clock | 名称 | 実体経済 | インフレ | 金融政策 |
|---|---|---|---|---|---|
| **I リフレ・回復** | 7 | 大底・政策転換 (The Pivot) | 収縮底 | 低下 | 急激緩和 |
| | 8 | 金融相場初期 (Liquidity Rally) | 底打ち | 低位安定 | 緩和継続 |
| | 9 | 早期回復 (Early Cycle) | 回復開始 | 緩やか上昇 | 緩和維持 |
| **II ブーム・成長** | 10 | ゴルディロックス (Goldilocks) | 加速 | 安定 | 中立 |
| | 11 | 成熟・利上げ開始 (Mid Cycle) | 強い成長 | 上昇傾向 | 引締め開始 |
| | 12 | ユーフォリア・過熱 (Late Cycle) | ピーク | 高インフレ | 積極引締め |
| **III 過熱・減速** | 1 | インフレショック (Inflation Shock) | 減速開始 | 急騰 | 強力引締め |
| | 2 | 引き締め・減速 (Tightening) | 減速 | 高止まり | 引締め継続 |
| | 3 | スタグフレーション (Stagflation Risk) | 停滞 | 根強い | 板挟み |
| **IV 後退・クラッシュ** | 4 | 崩壊の予兆 (The Cliff) | 急減速 | 低下開始 | 転換検討 |
| | 5 | リセッション突入 (Recession) | マイナス成長 | 急低下 | 緩和開始 |
| | 6 | 総悲観・浄化 (Capitulation) | 底割れ | 低位 | 強力緩和 |

**現在の診断**: `state/current-clock.md` を参照
**詳細定義**: `reference/pre-review/12clock/model/main.md`
**判定基準**: `reference/pre-review/12clock/judgement/12clock-detailed.md`

---

## 運用上の重要ルール

### レポートの保存場所と命名規則

| レポート種別 | 保存先 | ファイル名 |
|---|---|---|
| 日次レポート | `data/reports/daily/` | `report_YYYYMMDD.md` |
| 週次レポート | `data/reports/weekly/` | `weekly_YYYYMMDD.md` |

### プロンプト修正の方針

- `prompt/refined/` のファイルを直接修正する（運用プロンプトの正本）
- `prompt/pre-review/` のファイルは原本として保管し、原則として修正しない
- GitHub から新しいプロンプトを取り込む場合は `prompt/pre-review/` に配置し、`refined/` 化するか判断する

### 12clock診断の更新タイミング

- **必須**: 月次マクロレポート生成後（精度向上のため月次分析を先に実施）
- **推奨**: 重要経済指標（GDP・CPI・FOMC）の発表後
- **任意**: 週次レポートでClockとの大きな乖離が検出された場合

### パス参照

すべての絶対パスは `/Users/matsubarakouji/ai-agent/economics/global-macro-strategy/` を起点とする。

---

## 参照すべき主要リファレンス

| 目的 | 参照先 |
|---|---|
| 12clockモデルの定義を理解したい | `reference/pre-review/12clock/model/main.md` |
| 各クロックの詳細な指標挙動を知りたい | `reference/pre-review/12clock/judgement/12clock-detailed.md` |
| 経済レジーム×アセットパフォーマンスの早見表 | `reference/pre-review/economic-regime-and-cycle-analysis/economic-regime-and-cycle-phase-asset-performance-matrix.md` |
| プロンプト体系全体の設計思想 | `prompt/pre-review/ver3.0.md` |
| 各プロンプトの活用タイミング・目的 | `prompt/pre-review/99-application-guide.md` |
| 現在の12clock診断結果 | `state/current-clock.md` |
