# Global Macro Strategy — README

> パス: `/Users/matsubarakouji/ai-agent/economics/global-macro-strategy/`
> 最終更新: 2026-02-21

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

## 標準的な運用カレンダー

| タイミング | 実行プロンプト | 所要時間 | インプット |
|---|---|---|---|
| **毎月中旬〜下旬** | `3-monthly-systematic-macro` | 10〜15分 | WebSearch（自動） |
| **毎月（月次直後）** | `0-12clock-diagnosis` | 5〜10分 | WebSearch（自動）+ 月次レポート |
| **毎週末（金〜土）** | `2-7-weekly` | 10〜15分 | ETF CSV + WebSearch |
| **毎朝（平日）** | `1-day` | 5〜10分 | ETF CSV + WebSearch |
| **レジーム転換疑い時** | `0-12clock-diagnosis` | 5〜10分 | WebSearch（自動） |

---

## 起動コマンド

### 月次マクロ分析レポート
```
「3-monthlyレポートを作成してください。分析対象月: 202602」
```
- 全主要経済指標（GDP・ISM・失業率・PCE・FF金利・長期金利）をWebSearchで収集
- ビジネスサイクル分析 → 経済レジーム分析（3ステップ）→ 投資戦略への示唆を生成
- 完了後に `0-12clock-diagnosis` の実行を促す
- 保存先: `reports/monthly/YYYYMMDD-systematic-macro-report.md`

### 12クロック診断
```
「12clock診断をしてください」
```
- 5視点（実体経済・心理PMI・物価・市場金利・金融政策）で現在のクロックを判定
- 4ステップアルゴリズム（トレンド判定 → 質評価 → 乖離確認 → 閾値確認）を実行
- 結果を `state/current-clock.md` に自動上書き保存

### 日次レポート
```
「1-dayレポートを作成してください。分析対象日: 20260221」
「1-dayレポートを作成してください。分析対象日: 20260221、CSV: [ファイルパス]」
```
- ETF CSVの全銘柄を対象に3種のアノマリーを検知（相関ブレイク・ボラティリティスパイク・トレンド反転）
- CSVを省略した場合は `prompt/pre-review/` 配下の最新 `Export_*.csv` を自動使用
- 保存先: `reports/daily/YYYYMMDD-1day-report.md`

### 週次レポート
```
「週次レポートを作成してください」
「週次レポートを作成してください。週末: 20260221、CSV: [ファイルパス]」
```
- 7日間リターンを主軸にマーケット・レジームを判定し、来週の複数シナリオと戦術プランを設計
- 保存先: `reports/weekly/YYYYMMDD-DDDD-weekly-report.md`

---

## 12クロック・ビジネスサイクルモデル

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

## ETFデータ（CSV）について

### 入手方法
Google Sheets から手動でエクスポートし、`prompt/pre-review/` に配置する。

### ファイル命名規則
```
Export_YYYYMMDD_HHMMSS.csv
```

### 主要カラムと処理規則

| カラム | 内容 | 処理 |
|---|---|---|
| `Per Yesterday` | 前日比リターン | 小数形式 → ×100 で%換算 |
| `7` / `14` / `30` / `90` / `0101` / `365` | 各期間リターン | 同上 |
| `Current` | 現在価格 | そのまま使用 |
| `NO` | 行番号 | 空白行（区切り行）は分析から除外 |

- 同一 Ticker が複数行ある場合は**最初の出現のみ**使用
- `Per Yesterday` が `-1.0` 以下、または価格が `0` / `1` の銘柄はデータ異常として除外

---

## ディレクトリ構成

```
global-macro-strategy/
│
├── README.md                        ← このファイル
├── CLAUDE.md                        ← Claude Code 向けガイド（起動方法・技術仕様）
├── overview.md                      ← 全ファイルの概要インデックス
│
├── state/
│   └── current-clock.md             ← 12クロック最新診断結果（全プロンプトが参照）
│
├── prompt/
│   ├── refined/                     ← 【運用中】Claude Code 専用プロンプト
│   │   ├── 0-12clock-diagnosis.md   月次 12クロック診断
│   │   ├── 1-day.md                 日次 アノマリー検知レポート
│   │   ├── 2-7-weekly.md            週次 ウォーゲーミングブリーフ
│   │   └── 3-monthly-systematic-macro.md  月次 マクロ分析レポート
│   │
│   └── pre-review/                  ← 【原本保管】精査前プロンプト（GitHub からの取り込み）
│       ├── .0/                      GitHub: koji0322/eco / prompt/.0
│       │   ├── 11-Systematic-Macro-Analysis-Framework.md  ← 3-monthly の元ファイル
│       │   ├── 00-adaptive-fractal-position-trader-prompt.md
│       │   ├── 21-vix-divergence-strategy-prompt-vix-only-sqeeze.md
│       │   ├── 22-Volatility-Phase-analysis-prompt.md
│       │   ├── Pythia-DX.md
│       │   ├── divergence-strategy-prompt.md
│       │   ├── mtf-chart-analysis-prompt.md
│       │   ├── archive/             旧版プロンプト
│       │   └── doc/                 補足ドキュメント（clock.md・VIX手引き等）
│       ├── 1-day.md 〜 9-the-apex-*.md   時間軸別プロンプト（Ver.3.0体系）
│       ├── ver3.0.md                Ver.3.0 システム設計書
│       ├── 99-application-guide.md  活用ガイド
│       └── sample-data-Export_*.csv ETFサンプルデータ
│
├── reports/                         ← 生成されたレポートの保管庫
│   ├── daily/                       YYYYMMDD-1day-report.md
│   ├── weekly/                      YYYYMMDD-DDDD-weekly-report.md
│   └── monthly/                     YYYYMMDD-systematic-macro-report.md
│
└── reference/
    └── pre-review/                  ← 参照資料・ナレッジベース
        ├── 12clock/                 12クロックモデル定義・判定基準・運用マニュアル
        ├── 2025/                    2025年活動ログ・ヘッジファンド研究
        ├── 5core-strategy/          5コア要素・THE MACRO EDGE 書籍開発
        ├── economic-regime-and-cycle-analysis/  レジーム×サイクル分析
        ├── global-macro-investor-handbook/      投資家ハンドブック（第1版）
        ├── global-macro-investor-handbook02/    投資家ハンドブック（第2版）
        └── jim-rodgers/             ジム・ロジャーズ戦略研究
```

---

## 運用上の重要ルール

### レポートの命名と保存
すべてのレポートは `reports/` 配下に保存し、ファイル名に日付を含める。命名規則は上表のとおり。

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

---

*このシステムは継続的に進化する。新しいプロンプトや分析手法は `prompt/pre-review/` で検証後、`prompt/refined/` に昇格させる。*
