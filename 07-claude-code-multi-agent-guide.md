# Claude Code マルチエージェントガイド

## 0. はじめに

このガイドは **複数の Claude Code インスタンスを協調させ、プログラムから Claude Code を制御するための自分用リファレンス** です。

- **想定読者**: [Claude Code スキル・プラグインガイド](06-claude-code-skills-guide.md) を読み終え、スキル・プラグインを自作できる
- **ゴール**: Agent Teams で並列作業ができる。Agent SDK でプログラムから Claude Code を制御できる。状況に応じた使い分けを判断できる
- **関連ガイド**:
  - [Claude Code 応用・自動化ガイド](03-claude-code-advanced-guide.md) — カスタマイズ・自動化（レベル 3）
  - [Claude Code スキル・プラグインガイド](06-claude-code-skills-guide.md) — スキル・プラグイン（レベル 6）

> レベル 6 までは **1 つの Claude Code セッション** が作業の単位だった。
> このガイドでは、**複数の Claude Code を協調させる Agent Teams** と、
> **プログラムから Claude Code を制御する Agent SDK** を使い、より大規模なタスクに対応する。
> VBA の枠を完全に超える段階。複数のマクロを連携させてワークフロー全体を自動化し、さらに Excel の外からマクロを呼び出すイメージ。

> **注意**: Agent Teams は実験的機能（2026 年 2 月時点）。仕様が変更される可能性がある。

---

## 1. サブエージェントの復習と限界

### サブエージェントとは

Claude Code が内部的に使う「部下」のようなもの。メインの Claude Code が複雑なタスクを処理するとき、サブエージェントにサブタスクを委任する。レベル 3 で触れた `Task` ツールがこれにあたる。

### サブエージェントの特徴

- メインの Claude Code が管理する
- サブタスクの結果をメインに返す
- メイン側のコンテキストウィンドウに結果が蓄積される

### 限界

- **一方向**: サブエージェントはメインにしか報告できない。サブエージェント同士は会話できない
- **短命**: 1 つのサブタスクが終わったら消える
- **集中管理**: 全てメインが管理するため、メインのコンテキストが膨張しやすい

### Agent Teams はこの限界を超える

| | サブエージェント | Agent Teams |
|---|---|---|
| コンテキスト | メインに結果を返す | 各メンバーが独立したコンテキストを持つ |
| コミュニケーション | メインにのみ報告 | メンバー間で直接メッセージ交換 |
| 協調方法 | メインが全て管理 | 共有タスクリストで自律的に協調 |
| 寿命 | サブタスク完了まで | セッション終了まで継続 |
| 適するタスク | 調査・検索など短い委任 | 並行開発・複数観点のレビュー |

---

## 2. Agent Teams を有効化する

### 有効化

Agent Teams はデフォルトで無効。設定ファイルで有効化する。

`.claude/settings.json` または `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 基本概念

| 概念 | 役割 |
|------|------|
| **チームリード** | チームを作成し、メンバーを配置し、全体を調整する。自分がやりとりする相手 |
| **チームメイト** | 独立した Claude Code インスタンス。それぞれが自分のコンテキストウィンドウを持つ |
| **共有タスクリスト** | チーム全体の作業項目と依存関係を管理する。全メンバーから見える |
| **メールボックス** | メンバー間のメッセージング。直接やりとりできる |

### 表示モード

| モード | 環境 | 切り替え |
|-------|------|---------|
| **インプロセス** | 1 つのターミナルに全メンバー | `Shift + ↑/↓` でメンバー切り替え |
| **分割ペイン** | tmux や iTerm2 で各メンバーを別ペインに表示 | 各ペインが独立 |

> 最初はインプロセスモードで十分。慣れてきたら分割ペインを試す。

---

## 3. 初めてのチーム作業

### チームを起動する

```
あなた: 「チームを作って。メンバー 2 人で、1 人は実装担当、もう 1 人はテスト担当にして」

チームリード: チームを構成します。
              - 実装担当: src/ のコードを実装
              - テスト担当: tests/ のテストを作成・実行
```

### タスクの流れ

1. **リードがタスクを作成**: 共有タスクリストに作業項目を登録
2. **メンバーがタスクを受け取る**: 各メンバーが自分の担当タスクを確認
3. **並行作業**: 実装担当がコードを書いている間に、テスト担当がテスト設計を進める
4. **メッセージ交換**: 「この関数のインターフェースはこうなった」と実装担当がテスト担当に連絡
5. **完了報告**: 各メンバーがタスク完了を報告

### メンバーの切り替え（インプロセスモード）

```
Shift + ↑    # 前のメンバーに切り替え
Shift + ↓    # 次のメンバーに切り替え
```

### 直接メッセージ

特定のメンバーに直接話しかけることもできる。

```
あなた: 「テスト担当に伝えて: calculate_total の引数に tax_rate を追加したので、テストも更新して」
```

---

## 4. チーム構成のパターン

### パターン 1: 並行開発

```
チームリード
├── フロントエンド担当  → HTML/CSS/JavaScript
├── バックエンド担当    → Python/API
└── テスト担当          → テストコードの作成・実行
```

各メンバーが独立して作業し、インターフェース（API の仕様など）だけを共有する。

### パターン 2: マルチ観点レビュー

```
チームリード
├── セキュリティ担当  → 脆弱性・認証・認可のチェック
├── パフォーマンス担当 → 実行速度・メモリ使用量のチェック
└── コード品質担当    → 可読性・保守性・テストカバレッジ
```

同じコードを異なる観点で同時にレビューし、結果を統合する。

### パターン 3: 仮説検証

```
チームリード
├── メンバー A  → 仮説 1 を検証（「原因はデータベースの接続数制限」）
└── メンバー B  → 仮説 2 を検証（「原因はメモリリーク」）
```

バグの原因調査など、複数の仮説を並行して検証する。

### デリゲートモード

チームリードがコーディングせず、調整に専念するモード。

```
Shift + Tab  → デリゲートモードに切り替え
```

リードは方針を決めてメンバーに指示を出すだけ。メンバーがコードを書く。

---

## 5. チーム作業の品質管理

### プラン承認

チームメイトが実装前に計画を提出し、リード（または自分）が承認してから実装を開始する設定。

```
あなた: 「各メンバーは実装前に計画を提出して。承認してから着手するようにして」
```

### 品質ゲート（フックとの連携）

レベル 6 で学んだフックを使い、タスク完了時に自動チェックを走らせる。

```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "pytest tests/ -v --tb=short",
            "timeout": 60000
          }
        ]
      }
    ]
  }
}
```

タスクが完了するたびにテストが自動実行される。テストが失敗したらメンバーに差し戻し。

### TeammateIdle フック

メンバーが待機状態になったときの処理を設定できる。

```json
{
  "hooks": {
    "TeammateIdle": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "待機中のメンバーに、未着手のタスクがあれば割り当ててください。"
          }
        ]
      }
    ]
  }
}
```

---

## 6. Agent SDK の基本

### Agent SDK とは

Claude Code を **プログラムから呼び出す** ための開発キット。Python と TypeScript で利用できる。

| 使い方 | 方法 |
|-------|------|
| 対話的な開発 | CLI（`claude` コマンド）— これまで通り |
| 定型処理の自動実行 | **Agent SDK** |
| CI/CD パイプライン | **Agent SDK** |
| ワンショットの質問 | CLI（`claude -p "質問"`）— レベル 3 で学習済み |

> CLI のヘッドレスモード（`claude -p`）との違い: SDK は **プログラムの中に Claude Code を組み込める**。結果を受け取って次の処理に渡す、条件分岐する、ループする、といった制御が可能。

### インストール

```bash
# Python
pip install claude-agent-sdk

# TypeScript
npm install @anthropic-ai/claude-agent-sdk
```

### 認証

```bash
# Anthropic API キーを設定
export ANTHROPIC_API_KEY=your-api-key
```

---

## 7. SDK でエージェントを作る

### 基本的な使い方（Python）

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="src/main.py のバグを修正して",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Bash"]
        ),
    ):
        print(message)

asyncio.run(main())
```

### 利用できるツール

| ツール | 機能 |
|-------|------|
| `Read` | ファイルを読む |
| `Write` | ファイルを作成する |
| `Edit` | ファイルを編集する |
| `Bash` | ターミナルコマンドを実行する |
| `Glob` | パターンでファイルを検索する |
| `Grep` | ファイル内容を正規表現で検索する |
| `WebSearch` | Web 検索をする |
| `WebFetch` | Web ページを取得して解析する |
| `Task` | サブエージェントにタスクを委任する |

### カスタムサブエージェントの定義

SDK 内で専門のサブエージェントを定義できる。

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Glob", "Grep", "Task"],
    agents={
        "code-reviewer": AgentDefinition(
            description="コード品質を分析し改善点を提案する専門家",
            prompt="コードの品質・可読性・セキュリティを分析してください。",
            tools=["Read", "Glob", "Grep"],
        ),
        "test-writer": AgentDefinition(
            description="テストコードを作成する専門家",
            prompt="pytest を使ったテストコードを作成してください。",
            tools=["Read", "Write", "Bash"],
        ),
    },
)
```

### セッションの継続

```python
# 最初のクエリ
result = await query(prompt="プロジェクトの構成を確認して", options=options)
session_id = result.session_id

# 続きのクエリ（前の会話の文脈を引き継ぐ）
result = await query(
    prompt="見つかった問題を修正して",
    options=options,
    resume=session_id,
)
```

### MCP サーバーとの連携

```python
options = ClaudeAgentOptions(
    mcp_servers={
        "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"]
        }
    }
)
```

---

## 8. SDK の実用例

### 例 1: 毎朝の自動コードレビュー

```python
#!/usr/bin/env python3
"""daily_review.py — 昨日からの変更を自動レビューする"""

import asyncio
import subprocess
from claude_agent_sdk import query, ClaudeAgentOptions

async def daily_review():
    # 昨日からの変更を取得
    diff = subprocess.run(
        ["git", "diff", "HEAD~1"],
        capture_output=True, text=True
    ).stdout

    if not diff:
        print("変更なし")
        return

    async for message in query(
        prompt=f"以下の変更をレビューして、問題点があれば指摘して:\n\n{diff}",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Glob", "Grep"]),
    ):
        print(message)

asyncio.run(daily_review())
```

### 例 2: プルリクエスト作成時の自動レビュー（CI/CD 連携）

GitHub Actions から SDK を呼び出して、プルリクエストに自動でレビューコメントをつける。

```yaml
# .github/workflows/auto-review.yml
name: 自動コードレビュー

on:
  pull_request:
    branches: [main]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install claude-agent-sdk
      - run: python scripts/auto_review.py
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### 例 3: 複数ファイルへの定型処理

```python
"""全 Python ファイルに docstring を追加する"""

import asyncio
import glob
from claude_agent_sdk import query, ClaudeAgentOptions

async def add_docstrings():
    py_files = glob.glob("src/**/*.py", recursive=True)

    for file_path in py_files:
        print(f"処理中: {file_path}")
        async for message in query(
            prompt=f"{file_path} の全関数に docstring を追加して。既にある場合はスキップ。",
            options=ClaudeAgentOptions(allowed_tools=["Read", "Edit"]),
        ):
            pass  # 処理完了を待つ

asyncio.run(add_docstrings())
```

---

## 9. Cowork を知る

### Cowork とは

Claude Desktop で動く、**コーディング以外のナレッジワーク** 向けエージェント。Claude Code と同じ技術基盤だが、対象が異なる。

| | Claude Code | Cowork |
|---|---|---|
| 対象 | コーディング・開発作業 | 文書作成・リサーチ・データ分析 |
| 動作環境 | ターミナル / VS Code | Claude Desktop アプリ |
| 実行場所 | ローカルマシン | 仮想マシン上 |
| プラグイン | 対応 | 対応（同じプラグインシステム） |

### どんなときに使うか

- レポートや提案書の作成
- 大量のドキュメントの調査・要約
- データ分析（コーディングが主目的でないもの）
- 複数の情報源から知見を統合する作業

> コーディングが絡むタスクは Claude Code、それ以外のナレッジワークは Cowork、と使い分ける。

---

## 10. 使い分けの判断基準

レベル 1〜7 の全機能を俯瞰した選択ガイド。

| 状況 | 最適なアプローチ | レベル |
|------|---------------|-------|
| 簡単な修正・質問 | 1 セッションで対話 | 1〜2 |
| 定型的な開発フロー | カスタムコマンド + フック | 3 |
| 専門知識が必要な繰り返し作業 | スキル + プラグイン | 6 |
| 大規模な並行開発 | Agent Teams | 7 |
| 自動化パイプライン・CI/CD | Agent SDK | 7 |
| 非コーディングの知的作業 | Cowork | 7 |

### 判断のフローチャート

```
タスクは 1 人で完結する？
  ├── Yes → 1 セッションで OK（レベル 1〜3）
  │         定型処理？ → カスタムコマンド / スキル（レベル 3・6）
  │         プログラムから制御？ → SDK / ヘッドレス（レベル 3・7）
  └── No → 並行作業が必要
            ├── 人間が対話しながら → Agent Teams（レベル 7）
            └── 自動で回したい → SDK でマルチエージェント（レベル 7）
```

---

## 11. 困ったときは

### よくある問題と対処法

| 症状 | 対処法 |
|------|--------|
| Agent Teams が起動しない | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` が `"1"` に設定されているか確認 |
| チームメイトが期待通りに動かない | タスクの記述を具体的にする。曖昧な指示は誤解の原因 |
| SDK で認証エラー | `ANTHROPIC_API_KEY` が設定されているか確認。有効期限切れでないか確認 |
| SDK の処理が途中で止まる | `timeout` パラメータを設定。ネットワーク接続を確認 |
| コンテキストウィンドウが一杯になる | チームメンバーごとに `clear` でリセット。タスクを細かく分割 |
| メンバー間の連携がうまくいかない | 共有タスクリストの記述を明確にする。インターフェースの仕様を先に決める |
| Cowork のプラグインが動かない | Claude Desktop アプリのバージョンを確認。プラグインの互換性を確認 |

### Agent Teams のベストプラクティス

- **タスクを明確に定義する**: 各メンバーが何をすべきか、完了条件は何か
- **インターフェースを先に決める**: メンバー間で共有するデータの形式を最初に合意
- **品質ゲートを設定する**: フックでテスト自動実行、レビュー必須化
- **小さく始める**: 2 人チームから始めて、うまくいったら人数を増やす
