# 12クロック・ビジネスサイクル診断プロンプト

**バージョン**: 1.0 (Claude Code専用)
**実行タイミング**: 月1回、または市場レジーム転換の疑いが生じた時
**所要時間目安**: 5〜10分

---

## 【Claude Codeへの指示】

あなたは世界トップクラスのマクロ経済アナリストです。
以下の手順に従い、**12クロック・ビジネスサイクルモデル**に基づいて現在の経済環境を診断し、結果をファイルに保存してください。

---

## STEP 0: 参照ドキュメントの読み込み

以下のファイルを読み込み、12クロックモデルの定義と判定基準を把握してください。

```
参照ファイル:
- /Users/matsubarakouji/ai-agent/economics/global-macro-strategy/reference/pre-review/12clock/model/main.md
- /Users/matsubarakouji/ai-agent/economics/global-macro-strategy/reference/pre-review/12clock/model/overview.md
- /Users/matsubarakouji/ai-agent/economics/global-macro-strategy/reference/pre-review/12clock/judgement/12clock-detailed.md
```

**12クロックの構造（概要）**:
| Phase | Clock | 名称 |
|---|---|---|
| Phase I リフレ・回復 | 7 | 大底・政策転換 (The Pivot) |
| Phase I | 8 | 金融相場初期 (Liquidity Rally) |
| Phase I | 9 | 早期回復 (Early Cycle) |
| Phase II ブーム・成長 | 10 | ゴルディロックス (Goldilocks) |
| Phase II | 11 | 成熟・利上げ開始 (Mid Cycle) |
| Phase II | 12 | ユーフォリア・過熱 (Late Cycle) |
| Phase III 過熱・減速 | 1 | インフレショック (Inflation Shock) |
| Phase III | 2 | 引き締め・減速 (Tightening) |
| Phase III | 3 | スタグフレーション (Stagflation Risk) |
| Phase IV 後退・クラッシュ | 4 | 崩壊の予兆 (The Cliff) |
| Phase IV | 5 | リセッション突入 (Recession) |
| Phase IV | 6 | 総悲観・浄化 (Capitulation) |

---

## STEP 1: マクロデータの収集（WebSearch）

以下の各項目について **WebSearch** ツールを使用してデータを収集してください。
各検索は日本語または英語で実行し、**最新の数値と日付を必ず特定**してください。

### 1-1. 実体経済（成長ベクトル）
- `US GDP growth rate latest 2026` → 直近GDP成長率（前期比年率）
- `Atlanta Fed GDPNow latest forecast` → GDPNow最新予測値
- `US nonfarm payrolls latest` → 非農業部門雇用者数（前月比）
- `US unemployment rate latest Sahm rule` → 失業率とサーム・ルール発動状況

### 1-2. 物価・インフレ（インフレベクトル）
- `US CPI latest 2026` → CPI前月比・前年比
- `US PCE core latest` → コアPCE
- `US supercore CPI latest` → スーパーコアCPI（サービス除く住居）

### 1-3. 金融政策・流動性
- `Federal Reserve interest rate decision latest 2026` → FF金利現在水準
- `Fed balance sheet QT quantitative tightening latest` → QTの状況
- `US yield curve 10year 2year spread latest` → 10年-2年金利差（イールドカーブ）

### 1-4. 市場・心理
- `US ISM manufacturing PMI latest 2026` → ISM製造業景況感
- `US ISM services PMI latest` → ISM非製造業
- `S&P 500 latest` → 株価水準とトレンド
- `VIX volatility index latest` → 恐怖指数
- `US high yield credit spread latest` → ハイイールドスプレッド

---

## STEP 2: 4ステップ診断アルゴリズムの実行

収集したデータを使い、以下の4ステップで現在のClockを特定してください。

### Step 2-1: トレンド判定（ベクトル解析）

| 成長ベクトル | インフレベクトル | 暫定フェーズ |
|---|---|---|
| 加速(↗) | 低下・安定(↘) | Phase II: ブーム・適温 → Clock 10, 11 |
| 加速(↗) | 上昇・過熱(↗) | Phase II後期〜III初期 → Clock 12, 1 |
| 減速(↘) | 高止まり・上昇(↗) | Phase III: 過熱・減速 → Clock 2, 3 |
| 減速・マイナス(↘) | 低下・急落(↘) | Phase IV: 後退・クラッシュ → Clock 4, 5, 6 |
| 底打ち・回復(↗) | 低下・緩和(↘) | Phase I: リフレ・回復 → Clock 7, 8, 9 |

**暫定判定フェーズ**: `[記入]`、**候補Clock**: `[記入]`

### Step 2-2: 質の評価（深度補正）

以下の中身を確認し、候補Clockを±1修正する。

| チェック項目 | 確認内容 | 補正 |
|---|---|---|
| 雇用の質 | フルタイム増減、パート比率 | フルタイム減・パート増 → +1時間進める |
| 消費の質 | 実質賃金 vs クレジットカード延滞率 | 借金依存の消費増 → +1時間進める |
| 流動性の質 | FRB QT vs 隠れ緩和（RRP放出等） | 隠れ緩和あり → -1時間戻す |

**修正後Clock候補**: `[記入]`

### Step 2-3: 乖離の確認（歪み検知）

市場（株価）が実体経済より何時間先を織り込んでいるかを確認する。
通常は半年先（+2クロック分）を先行するが、それ以上は「歪み」。

- **実体経済の時計**: Clock `[記入]`
- **市場の時計**（株価が示すClock）: Clock `[記入]`
- **乖離の評価**: `[ブル・トラップ / ベア・トラップ / 正常範囲]`
- **含意**: `[記入]`

### Step 2-4: 閾値の確認（フェーズ移行トリガー）

| 移行 | トリガー | 発動状況 |
|---|---|---|
| → Phase II | ISM > 50定着、銅価格上昇トレンド | `[Yes/No/接近中]` |
| → Phase III | 10年金利ブレイク、逆イールド発生、CPI前月比+0.3%定着 | `[Yes/No/接近中]` |
| → Phase IV | **逆イールド解消（順イールド化）**、SLOOS悪化、サーム・ルール発動 | `[Yes/No/接近中]` |
| → Phase I | FRBピボット（利下げ開始）、M2急増、VIXピークアウト | `[Yes/No/接近中]` |

**次フェーズ移行トリガーの発動状況**: `[記入]`

---

## STEP 3: 診断結果の確定と出力

以下のフォーマットで診断結果を出力してください。

---

```
【12クロック・ビジネスサイクル診断レポート】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
診断日      : YYYY-MM-DD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

■ 現在地判定
  Clock [X]「[名称]」(Phase [I/II/III/IV]: [フェーズ名])

■ 5視点サマリー
  ① 実体経済  : [判定と根拠、数値を引用]
  ② 心理・PMI : [判定と根拠、数値を引用]
  ③ 物価     : [判定と根拠、数値を引用]
  ④ 市場・金利: [判定と根拠、数値を引用]
  ⑤ 金融政策 : [判定と根拠、数値を引用]

■ 乖離（歪み）分析
  実体 Clock [X] vs 市場 Clock [Y] → [乖離の性質と含意]

■ 次フェーズ移行予測
  [期間]以内に Clock [Z] へ移行する可能性 [高/中/低]
  移行トリガー: [具体的な指標と閾値]

■ Current Watch（今見るべきトリガー）
  [箇条書き 3〜5項目]

■ Next Portfolio（先取り投資の方向性）
  [現フェーズの推奨スタンス + 次フェーズへの仕込み方針]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## STEP 4: 結果をファイルに保存

診断完了後、**以下のファイルを上書き保存**してください。

**保存先**: `/Users/matsubarakouji/ai-agent/economics/global-macro-strategy/state/current-clock.md`

**保存内容フォーマット**:

```markdown
# 12クロック・ビジネスサイクル 現在地診断

> このファイルは `0-12clock-diagnosis` プロンプト実行時に自動更新されます。
> `1-day` および `2-7-weekly` プロンプトが起動時に自動参照します。

---

## 最終診断

**診断日**: YYYY-MM-DD
**Clock**: [X]「[名称]」
**Phase**: [I/II/III/IV]「[フェーズ名]」

## 5視点サマリー

| 視点 | 判定 | 主要指標・根拠 |
|---|---|---|
| ① 実体経済 | [↗/→/↘] | [数値と概要] |
| ② 心理・PMI | [↗/→/↘] | [数値と概要] |
| ③ 物価 | [↗/→/↘] | [数値と概要] |
| ④ 市場・金利 | [↗/→/↘] | [数値と概要] |
| ⑤ 金融政策 | [緩和/中立/引締] | [概要] |

## 乖離（歪み）分析

実体 Clock [X] vs 市場 Clock [Y] → [性質と含意]

## 次フェーズ移行予測

[期間]以内に Clock [Z] へ → 可能性 [高/中/低]
トリガー: [具体的指標と閾値]

## Current Watch

- [項目1]
- [項目2]
- [項目3]

## Next Portfolio

[推奨スタンスと仕込み方針]
```

ファイル保存後、「診断完了・`state/current-clock.md` を更新しました」と報告してください。

---

## 注意事項

- WebSearchで数値が取得できない場合は、取得できなかった旨を明記し、「不明」と記載して診断を続行する
- 診断はあくまで**現時点のスナップショット**であり、重要な経済指標発表後は再診断を推奨する
- `current-clock.md` の内容は他のプロンプトが自動参照するため、**必ず保存まで完了**させること
