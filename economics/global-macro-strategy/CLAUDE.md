# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

- **Location**: `investing/global-macro-strategy/` within the parent repo at `/Users/matsubarakouji/ai-agent`
- **Purpose**: グローバルマクロ投資戦略の分析・ナレッジ管理
- **Parent repo**: Contains `dev-learning-guides/` and `gemini-test/` as sibling projects

## Repository Notes

- The git root is `/Users/matsubarakouji/ai-agent` — git commands should target that root, not this subdirectory

---

## フォルダ構成

```
global-macro-strategy/
├── prompt/
│   ├── pre-review/      精査前プロンプト（原本保管）
│   └── refined/         運用中プロンプト（Claude Code専用・磨き済み）
│       ├── 0-12clock-diagnosis.md   12クロック月次診断
│       ├── 1-day.md                 日次アノマリー検知レポート
│       └── 2-7-weekly.md            週次ウォーゲーミングブリーフ
├── reference/
│   └── pre-review/      参照資料（12clockモデル・フレームワーク等）
└── state/
    └── current-clock.md 12クロック最新診断結果（自動更新）
```

---

## 分析プロンプトの起動方法

### 12クロック診断（月1回 or レジーム転換時）

```
"12clock診断をしてください"
```

- プロンプト: `prompt/refined/0-12clock-diagnosis.md` を参照して実行
- WebSearch でマクロ経済指標を自動収集し、4ステップで現在のClock（1〜12）を診断
- 結果は `state/current-clock.md` に自動保存（1-day・2-7-weeklyが参照）

### 日次レポート（毎朝）

```
"1-dayレポートを作成してください。分析対象日: 20260221"

# CSVを明示指定する場合
"1-dayレポートを作成してください。分析対象日: 20260221、CSV: [ファイルパス]"
```

- プロンプト: `prompt/refined/1-day.md` を参照して実行
- CSVを指定しない場合は `prompt/pre-review/` 配下の最新 `Export_*.csv` を自動使用
- `state/current-clock.md` を自動読み込みし、12clockコンテキストをレポートに反映

### 週次レポート（週末）

```
"週次レポートを作成してください"

# 週末日付・CSVを明示指定する場合
"週次レポートを作成してください。週末: 20260221、CSV: [ファイルパス]"
```

- プロンプト: `prompt/refined/2-7-weekly.md` を参照して実行
- 7日間リターンを主軸に、相関分析・12clock整合性チェック・来週シナリオを生成

---

## CSVデータについて

- **出所**: Google Sheets から手動エクスポート
- **ファイル命名規則**: `Export_YYYYMMDD_HHMMSS.csv`
- **保存場所**: `prompt/pre-review/`
- **主要カラム**:
  - `Per Yesterday`: 前日比リターン（小数形式、×100で%換算）
  - `7`, `14`, `30`, `90`, `0101`, `365`: 各期間リターン（同上）
  - `Current`: 現在価格
  - `Yesterday` / `Two days before`（2回目）〜`365`（2回目）: 過去価格
- **処理上の注意**: `NO`列が空白の区切り行は除外。同一Tickerは最初の出現を使用

---

## 12クロック・ビジネスサイクルモデルについて

| Phase | Clock | 名称 |
|---|---|---|
| Phase I リフレ・回復 | 7 | 大底・政策転換 |
| Phase I | 8 | 金融相場初期 |
| Phase I | 9 | 早期回復 |
| Phase II ブーム・成長 | 10 | ゴルディロックス |
| Phase II | 11 | 成熟・利上げ開始 |
| Phase II | 12 | ユーフォリア・過熱 |
| Phase III 過熱・減速 | 1 | インフレショック |
| Phase III | 2 | 引き締め・減速 |
| Phase III | 3 | スタグフレーション |
| Phase IV 後退・クラッシュ | 4 | 崩壊の予兆 |
| Phase IV | 5 | リセッション突入 |
| Phase IV | 6 | 総悲観・浄化 |

詳細定義: `reference/pre-review/12clock/model/main.md`
判定基準: `reference/pre-review/12clock/judgement/12clock-detailed.md`
