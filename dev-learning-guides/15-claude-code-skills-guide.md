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

---

## 1. スキル（Skills）とは何か

### 概要

スキルは **Claude Code に「専門知識」を持たせる仕組み**。指示書・参照資料・実行スクリプトをまとめたフォルダで、Claude が必要に応じて動的に読み込む。

### カスタムコマンドとの関係

最新の Claude Code では、**スキルとカスタムコマンドが統合** されている。レベル 3 で作ったカスタムコマンド（`.claude/commands/` の `.md` ファイル）に **YAML フロントマター** を追加することで、スキルとしての高度な機能を持たせられる。

| 機能 | フロントマターなし（レベル 3） | フロントマターあり（レベル 6） |
|------|---|---|
| 基本動作 | 指示テンプレートを実行 | 同左 + 高度な制御 |
| 起動方法 | `/project:xxx` で明示的に呼ぶ | 同左 + Claude が自動で読み込むことも可能 |
| 使えるツール | 全ツール | `allowed-tools` で制限可能 |
| 実行方式 | メインセッション内 | `context: fork` でサブエージェントとして実行可能 |
| エージェント化 | 不可 | `agent` フィールドで専門エージェント化 |

つまり、レベル 3 で作ったコマンドを **そのまま発展** させられる。

---

## 2. YAML フロントマターの仕組み

### 基本構造

スキル（高度なカスタムコマンド）は、マークダウンファイルの先頭に **YAML フロントマター** を書いて機能を制御する。

```markdown
---
name: review
description: コードレビューを実施する
allowed-tools:
  - Read
  - Glob
  - Grep
---

（ここに指示内容を書く）
```

### 主要なフロントマターフィールド

| フィールド | 説明 | 例 |
|-----------|------|-----|
| `name` | スキルの識別名 | `code-review` |
| `description` | スキルの説明（Claude が読み込み判断に使う） | `コードレビューを実施する` |
| `allowed-tools` | 使用可能なツールを制限 | `["Read", "Glob", "Grep"]` |
| `context` | 実行コンテキスト（`fork` でサブエージェント化） | `fork` |
| `agent` | エージェントの種類を指定 | `true` |
| `model` | 使用するモデルを指定 | `claude-sonnet-4-6` |
| `user-invocable` | `/project:xxx` で呼び出し可能にするか | `true`（デフォルト） |
| `argument-hint` | 引数のヒント表示 | `<ファイルパス>` |

### 段階的読み込み

スキルが効率的に動く仕組み:

```
起動時: name と description だけ読む → 「いつ使うか」を把握
  ↓ タスクに関連すると判断
必要時: 本文を読む → 「何をするか」を理解
  ↓ 追加の情報が必要
動的:   補足ファイルやスクリプトを読む → 「どう実行するか」を実行
```

10 個のスキルがあっても、起動時に読み込まれるのは名前と説明だけ。コンテキストウィンドウを圧迫しない。

---

## 3. 初めてのスキルを作る

### 基本的なスキルの書き方

`.claude/commands/` にフロントマター付きのマークダウンファイルを作成する。

```bash
# プロジェクトフォルダ内で
mkdir -p .claude/commands
```

`.claude/commands/review.md`:

```markdown
---
description: コードレビューを実施し、品質・セキュリティ・可読性の観点で指摘する
allowed-tools:
  - Read
  - Glob
  - Grep
argument-hint: <ファイルパス>
---

以下のファイルをレビューしてください: $ARGUMENTS

## レビュー観点

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

### 使い方

```
/project:review src/main.py
```

### description のポイント

`description` は **最も重要**。Claude がこの説明を読んで「このスキルを使うべきか」を判断する。

```
× description: コードレビュー
○ description: コードレビューを実施し、品質・セキュリティ・可読性の観点で指摘する
```

### ユーザーレベルのスキル

`~/.claude/commands/` に置くと全プロジェクトで使える（`/user:xxx` で呼び出し）。

### スキルの一覧を確認

```
/skills
```

利用可能なスキルを一覧表示できる。

---

## 4. スキルを実用的にする

### サブエージェントとして実行（context: fork）

`context: fork` を指定すると、スキルがメインセッションとは **別のサブエージェント** として実行される。メインのコンテキストウィンドウを消費しない。

```markdown
---
description: CSV ファイルを分析して統計レポートを生成する
context: fork
allowed-tools:
  - Read
  - Bash
argument-hint: <CSVファイルパス>
---

$ARGUMENTS を分析して、以下のレポートを生成してください:
- 行数・列数
- 各列の統計情報
- 欠損値の有無
```

> `context: fork` はコンテキストウィンドウを節約したいときや、独立した処理を実行したいときに使う。結果だけがメインに返される。

### 補足ファイルの活用

スキルから参照するテンプレートや参照資料を同じフォルダに置ける。

```
.claude/commands/report/
  report.md             # メインのスキルファイル
  templates/
    monthly-report.md   # レポートのテンプレート
  reference.md          # 参照データ（KPI の定義など）
```

> テンプレートや参照資料は必要になったときに読み込まれるため、起動時のメモリ消費はゼロ。

### 動的コンテキスト注入

バッククォートと `!` を使うと、コマンドの実行結果をスキルに動的に注入できる。

```markdown
---
description: 現在のブランチの変更をレビューする
---

以下の変更をレビューしてください:

!`git diff main...HEAD`
```

> `!` + バッククォートで囲んだコマンドが実行され、その出力がスキルの内容に展開される。

### `$ARGUMENTS` でパラメータを受け取る

`$ARGUMENTS` で引数全体を、`$1`, `$2` で個別の引数を受け取れる。

```markdown
---
description: 指定ファイルのテストを生成する
argument-hint: <ファイルパス> [テストフレームワーク]
---

対象: $1
フレームワーク: $2（指定がなければ pytest を使用）

上記ファイルのテストを作成してください。
```

```
/project:test-gen src/main.py pytest
```

### セッションID等の組み込み変数

スキル内では以下の変数も使える:

| 変数 | 内容 |
|------|------|
| `$ARGUMENTS` | 引数全体 |
| `$1`, `$2`, ... | 個別の引数 |
| `${CLAUDE_SESSION_ID}` | 現在のセッション ID |

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

## 8. スキルとフックの連携

### スキルのフロントマターでフックを定義

スキル固有のフックをフロントマター内に定義できる。settings.json に書くグローバルフックと異なり、そのスキルが有効なときだけ動作する。

```markdown
---
description: Python プロジェクトの開発を支援する
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: "jq -r '.tool_input.file_path // empty' | grep '\\.py$' | xargs -I {} black {} 2>/dev/null || true"
          timeout: 10000
---

Python コードを編集する際は PEP 8 に準拠してください。
```

> スキル内にフックを書くことで、「このスキルが使われているときだけ」自動フォーマットが走る、といった細かい制御ができる。

### フックイベントの全一覧

フックイベントの詳細は [Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) のセクション 4 を参照。15 種類のイベント（PreToolUse, PostToolUse, SessionStart, SessionEnd, UserPromptSubmit, Stop, Notification, PermissionRequest, PostToolUseFailure, SubagentStart, SubagentStop, TeammateIdle, TaskCompleted, PreCompact, ConfigChange）が利用可能。

---

## 9. 困ったときは

### よくある問題と対処法

| 症状 | 対処法 |
|------|--------|
| スキルが認識されない | YAML フロントマターの `description` があるか確認。`.claude/commands/` に `.md` ファイルとして配置されているか確認 |
| スキルが自動で発動しない | `description` の記述を見直す。タスクとの関連性が Claude に伝わる表現にする。`/skills` で一覧を確認 |
| プラグインの名前が競合する | `plugin.json` の `name` をユニークにする。名前空間で自動的に分離される |
| フックがエラーになる | コマンドを直接ターミナルで実行してテスト。`timeout` が短すぎないか確認 |
| 公式スキルがうまく動かない | 必要な依存パッケージがインストールされているか確認。Claude Code を再起動 |
| `$ARGUMENTS` が展開されない | スキルをスラッシュコマンドとして呼んでいるか確認。自動発動時は展開されない |

### スキル作成のベストプラクティス

- `description` を具体的に書く（Claude がいつ使うか判断する材料になる）
- 最小構成で作って動作確認 → 徐々に拡張
- 大きな参照資料はレベル 3+（補足ファイル）に分離する
- 定期的に使わなくなったスキルを整理する
