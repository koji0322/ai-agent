# Claude Code スキル・プラグインガイド

## 0. はじめに

このガイドは **Claude Code のスキルとプラグインを使い、再利用可能な知識パッケージとして Claude Code の能力を拡張するための自分用リファレンス** です。

- **想定読者**: プログラミング初心者 — [Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md) を読み終え、プロジェクトの開発・公開・運用を一通り経験した
- **ゴール**: スキルの仕組みを理解して自作できる。プラグインとしてパッケージ化・共有できる。公式スキルを活用できる
- **関連ガイド**:
  - [Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) — カスタマイズ・自動化（レベル 3）
  - [Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md) — 公開・運用（レベル 5）
  - [Claude Code マルチエージェントガイド](16-claude-code-multi-agent-guide.md) — マルチエージェント（次のステップ）

> レベル 3 ではカスタムコマンドやフックで Claude Code をカスタマイズした。
> このガイドでは、その発展形である **スキル（Skills）** と **プラグイン（Plugins）** を使い、
> **専門知識を構造化して、いつでも・誰でも使える形にする** 段階に進む。

<details><summary>VBA 経験者向けの補足</summary>

個人用マクロを整理して汎用アドイン（`.xlam`）にまとめ、社内に配布する段階に相当します。
</details>

---

## 1. スキル（Skills）とは何か

### 概要

スキルは **Claude Code に「専門知識」を持たせる仕組み**。指示書・参照資料・実行スクリプトをまとめたフォルダで、Claude が必要に応じて動的に読み込む。

### カスタムコマンドとの違い

レベル 3 で作ったカスタムスラッシュコマンドとの比較:

| | カスタムコマンド（レベル 3） | スキル（レベル 6） |
|---|---|---|
| 単位 | 1 つの指示テンプレート（`.md` 1 ファイル） | 知識・スクリプト・参照資料のまとまり（フォルダ） |
| 読み込み | コマンド実行時に全文を読み込む | 3 層の段階的読み込み（必要な分だけ） |
| 発動方法 | `/project:review` のように明示的に呼ぶ | Claude が関連性を判断して自動的に読み込む |
| 拡張性 | マークダウン 1 ファイル | 複数ファイル + 実行スクリプト |
| 共有 | ファイルをコピー | プラグインとして配布可能 |

カスタムコマンドが「簡単なショートカット」なら、スキルは「専門家の知識をマニュアルにまとめて配布する」イメージ。

<details><summary>VBA 経験者向けの補足</summary>

カスタムコマンドが「よく使うマクロをボタンに登録する」なら、スキルは「専門家の知識をマニュアルにまとめて配布する」イメージです。
</details>

---

## 2. スキルの 3 層アーキテクチャ

スキルが効率的に動く仕組みの核心。Claude の **コンテキストウィンドウ**（作業メモリ）を無駄遣いしないための設計。

### 3 つの層

```
レベル 1（起動時）: 名前と説明だけ読む → 「いつ使うか」を把握
        ↓ タスクに関連すると判断
レベル 2（必要時）: SKILL.md の本文を読む → 「何をするか」を理解
        ↓ 追加の情報が必要
レベル 3+（動的） : 補足ファイルやスクリプトを読む → 「どう実行するか」を実行
```

**レベル 1（メタデータ）**: `SKILL.md` の YAML フロントマター（`name` と `description`）だけが起動時に読み込まれる。Claude は「このスキルがどんな場面で役立つか」だけを把握する。

**レベル 2（本文）**: タスクに関連すると判断されたとき、`SKILL.md` の本文が読み込まれる。

**レベル 3+（補足資料）**: 本文から参照される追加ファイル（テンプレート、スクリプト等）が必要に応じて動的に読み込まれる。

<details><summary>VBA 経験者向けの補足</summary>

VBA で例えると、レベル 1 は「マクロの名前一覧」、レベル 2 は「マクロのコード本体」、レベル 3 は「マクロが参照する外部データ」に相当します。全部を一度にメモリに載せず、必要なときだけ読み込みます。
</details>

### なぜこの仕組みが重要か

10 個のスキルがあっても、起動時に読み込まれるのは名前と説明だけ（数行 × 10）。実際に使うスキルの詳細だけが読み込まれるので、コンテキストウィンドウを圧迫しない。

---

## 3. 初めてのスキルを作る

### SKILL.md の書き方

スキルの中心は `SKILL.md` ファイル。YAML フロントマター + マークダウン本文で構成する。

```markdown
---
name: code-review
description: コードレビューを実施し、品質・セキュリティ・可読性の観点で指摘する
---

# コードレビュースキル

## レビュー観点

以下の観点でコードをレビューしてください:

1. **バグ・論理エラー**: 意図と異なる動作をする箇所
2. **セキュリティ**: SQL インジェクション、XSS、ハードコードされた秘密情報
3. **可読性**: 変数名が意味を表しているか、処理の流れが追いやすいか
4. **テスト**: テストが十分か、エッジケースがカバーされているか

## 指摘フォーマット

各指摘は以下のフォーマットで報告してください:

- **ファイル**: ファイル名と行番号
- **深刻度**: 高 / 中 / 低
- **内容**: 問題の説明と修正案
```

### 配置場所

```bash
# プロジェクト内に配置
mkdir -p .claude/skills/code-review
```

```
.claude/skills/code-review/
  SKILL.md          # メインの指示書
```

### YAML フロントマターのポイント

- `name`: スキルの識別名。短くわかりやすく
- `description`: **最も重要**。Claude がこの説明を読んで「このスキルを使うべきか」を判断する。具体的に書く

```
× description: コードレビュー
○ description: コードレビューを実施し、品質・セキュリティ・可読性の観点で指摘する
```

### 動作確認

Claude Code を起動してタスクを依頼するだけ。スキルの `description` に合致するタスクなら自動的に読み込まれる。

```
あなた: 「src/main.py をレビューして」

Claude: （code-review スキルが自動で読み込まれ、定義した観点とフォーマットでレビューする）
```

---

## 4. スキルを実用的にする

### 補足ファイルの追加

`SKILL.md` から参照する追加ファイルを同じフォルダに置ける。

```
.claude/skills/report-generator/
  SKILL.md              # メインの指示書
  templates/
    monthly-report.md   # レポートのテンプレート
    quarterly-report.md # 四半期レポートのテンプレート
  reference.md          # 参照データ（KPI の定義など）
```

`SKILL.md` の中で参照:

```markdown
---
name: report-generator
description: 定型レポートをテンプレートに従って生成する
---

# レポート生成スキル

## 使い方

レポートの種類に応じて `templates/` 内のテンプレートを使用してください。

- 月次レポート: `templates/monthly-report.md`
- 四半期レポート: `templates/quarterly-report.md`

KPI の定義は `reference.md` を参照してください。
```

> テンプレートや参照資料はレベル 3+（必要になったとき）に読み込まれるため、起動時のメモリ消費はゼロ。

### 実行スクリプトの同梱

Python スクリプトをスキルに含めると、Claude がツールとして呼び出せる。

```
.claude/skills/csv-analyzer/
  SKILL.md
  analyze.py            # CSV を分析するスクリプト
```

`analyze.py`:

```python
#!/usr/bin/env python3
import pandas as pd
import sys
import json

file_path = sys.argv[1]
df = pd.read_csv(file_path)

result = {
    "rows": len(df),
    "columns": list(df.columns),
    "summary": df.describe().to_dict()
}

print(json.dumps(result, ensure_ascii=False, indent=2))
```

> スクリプトを同梱すると、Claude がファイルの中身を直接コンテキストに読み込む必要がなくなる。スクリプトが処理して結果だけを受け取るため、効率的。

### `$ARGUMENTS` でパラメータを受け取る

スキルをスラッシュコマンドとしても使える場合、`$ARGUMENTS` で引数を受け取れる。

```markdown
---
name: analyze
description: CSV ファイルを分析して統計情報を出力する
---

対象ファイル: $ARGUMENTS

`analyze.py` を実行して統計情報を取得してください。
```

```
/project:analyze data/sales.csv
```

---

## 5. Anthropic 公式スキルを使う

Anthropic が提供する公式スキルを導入すると、高度な機能をすぐに使える。

### 公式スキルの一覧

| スキル | 機能 |
|-------|------|
| **Excel** | 本格的なスプレッドシート生成（数式・グラフ・書式設定付き） |
| **PowerPoint** | プレゼンテーション作成 |
| **Word** | 文書作成 |
| **PDF** | フォーム入力付き PDF の操作 |

**Excel スキル**は特に便利で、Claude Code から本格的な Excel ファイルを生成・操作できる。

<details><summary>VBA 経験者向けの補足</summary>

VBA ユーザーにとって特に価値が高いのが Excel スキルです。Claude Code から Excel ファイルを生成・操作できます。
</details>

### 導入方法

公式スキルは GitHub リポジトリ（`anthropics/skills`）で公開されている。

```
あなた: 「Anthropic の公式 Excel スキルを導入して」
```

または手動で:

```bash
# リポジトリをクローン
git clone https://github.com/anthropics/skills.git ~/anthropic-skills

# 必要なスキルをプロジェクトにコピー
cp -r ~/anthropic-skills/excel .claude/skills/
```

### 使用例

```
あなた: 「data/sales.csv のデータを元に、月ごとの売上推移グラフ付きの Excel レポートを作って」

Claude: （Excel スキルが自動で読み込まれ、本格的な Excel ファイルを生成する）
```

---

## 6. プラグインとしてパッケージ化する

### プラグインとは

スキル・スラッシュコマンド・フック・MCP サーバーを **1 つの配布可能な単位にまとめたもの**。

複数の機能をパッケージとして配布し、誰でも簡単にインストールして使える形式。

<details><summary>VBA 経験者向けの補足</summary>

VBA の `.xlam`（Excel アドイン）ファイルに相当します。複数のモジュール・フォーム・参照設定を 1 つにまとめて配布する仕組みです。
</details>

### プラグインのフォルダ構成

```
my-plugin/
  .claude-plugin/
    plugin.json          # マニフェスト（名前・説明・バージョン）
  skills/                # スキル群
    code-review/
      SKILL.md
    report-generator/
      SKILL.md
      templates/
        monthly-report.md
  commands/              # スラッシュコマンド群
    review.md
    test.md
  hooks/
    hooks.json           # フック設定
  .mcp.json              # MCP サーバー設定
```

### plugin.json の書き方

```json
{
  "name": "my-dev-toolkit",
  "description": "開発作業を効率化するスキル・コマンド・フックのセット",
  "version": "1.0.0",
  "author": {
    "name": "自分の名前"
  }
}
```

### 名前空間

プラグイン内のスキルやコマンドは、プラグイン名がプレフィックスになる。

```
スタンドアロンの場合: /project:review
プラグインの場合:     /my-dev-toolkit:review
```

> 複数のプラグインを同時に使っても名前が衝突しない。

### ローカルでテスト

```bash
claude --plugin-dir ./my-plugin
```

このフラグをつけて起動すると、指定したプラグインが読み込まれた状態で使える。

---

## 7. プラグインを共有する

### Git リポジトリとして配布

プラグインのフォルダをそのまま Git リポジトリにして GitHub に公開する。

```bash
cd my-plugin
git init
git add .
git commit -m "初回リリース: my-dev-toolkit プラグイン"
git remote add origin git@github.com:ユーザー名/my-dev-toolkit.git
git push -u origin main
```

### インストール

```
/plugin install ユーザー名/my-dev-toolkit
```

### Anthropic 公式プラグイン

Anthropic は 11 種の公式プラグインを公開している。

| 分野 | 用途 |
|------|------|
| Productivity | ドキュメント・スプレッドシート作成 |
| Sales | 営業資料・提案書作成 |
| Finance | 財務分析・レポート |
| Data | データ分析・可視化 |
| Legal | 法的文書のレビュー |
| Marketing | マーケティング資料作成 |
| Customer Support | サポート対応の効率化 |

> 必要に応じて公式プラグインを導入し、自分のワークフローに組み込む。

---

## 8. フックの発展（レベル 3 の拡張）

レベル 3 で導入したフックの追加イベントを扱う。

### 追加のフックイベント

| イベント | 発火タイミング | 用途 |
|---------|-------------|------|
| `SessionStart` | セッション開始時 | 環境変数の設定、ワークスペースの準備 |
| `SessionEnd` | セッション終了時 | ログの保存、一時ファイルのクリーンアップ |
| `UserPromptSubmit` | ユーザーが入力を送信したとき | 入力のバリデーション、ログ記録 |
| `Stop` | Claude の応答が完了したとき | 成果物の品質チェック |
| `TeammateIdle` | チームメイトが待機状態になったとき | レベル 7 で活用 |
| `TaskCompleted` | タスクが完了したとき | 品質ゲート、テスト自動実行 |

### prompt タイプのフック

`command` タイプ（シェルコマンドを実行）に加えて、`prompt` タイプ（LLM で判断）も使える。

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "このコマンドが本番データベースに影響を与える可能性があるか判断してください。影響がある場合はブロックしてください。"
          }
        ]
      }
    ]
  }
}
```

> LLM がコマンドの内容を分析して、危険な操作を自動的にブロックできる。

---

## 9. 困ったときは

### よくある問題と対処法

| 症状 | 対処法 |
|------|--------|
| スキルが認識されない | YAML フロントマターの `name` と `description` があるか確認。ファイル名が `SKILL.md`（大文字）か確認 |
| スキルが自動で発動しない | `description` の記述を見直す。タスクとの関連性が Claude に伝わる表現にする |
| プラグインの名前が競合する | `plugin.json` の `name` をユニークにする。名前空間で自動的に分離される |
| フックがエラーになる | コマンドを直接ターミナルで実行してテスト。`timeout` が短すぎないか確認 |
| 公式スキルがうまく動かない | 必要な依存パッケージがインストールされているか確認。Claude Code を再起動 |
| `$ARGUMENTS` が展開されない | スキルをスラッシュコマンドとして呼んでいるか確認。自動発動時は展開されない |

### スキル作成のベストプラクティス

- `description` を具体的に書く（Claude がいつ使うか判断する材料になる）
- 最小構成で作って動作確認 → 徐々に拡張
- 大きな参照資料はレベル 3+（補足ファイル）に分離する
- 定期的に使わなくなったスキルを整理する
