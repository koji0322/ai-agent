# Claude Code 応用・自動化ガイド

## 0. はじめに

このガイドは **Claude Code をカスタマイズし、繰り返し作業を自動化するための自分用リファレンス** です。

- **想定読者**: [Claude Code 実践ガイド](02-claude-code-practical-guide.md) を読み終え、Git・GitHub の基本操作と実践的な開発フローが身についている
- **ゴール**: 設定ファイル・カスタムコマンド・フック・MCP・ヘッドレスモードを使いこなし、自分の作業スタイルに最適化された環境を構築する
- **関連ガイド**:
  - [Claude Code 基本操作ガイド](01-claude-code-guide.md) — 基本操作（レベル 1）
  - [Claude Code 実践ガイド](02-claude-code-practical-guide.md) — Git・開発フロー（レベル 2）
  - [Claude Code アプリケーション開発ガイド](04-claude-code-app-dev-guide.md) — アプリ開発（次のステップ）

> レベル 2 までは「Claude Code をそのまま使う」段階だった。
> このガイドでは **「Claude Code を自分好みにカスタマイズし、定型作業を仕組み化する」** 段階に進む。
> VBA で例えると、マクロを手動実行する段階から、`Workbook_Open` やユーザーフォームで自動化する段階への移行。

---

## 1. 設定ファイルを理解する

### 設定ファイルの種類

Claude Code の挙動は設定ファイルで制御できる。設定ファイルは **スコープ（適用範囲）** によって使い分ける。

| スコープ | ファイルの場所 | 適用範囲 | Git に含める？ |
|---------|-------------|---------|--------------|
| **ユーザー設定** | `~/.claude/settings.json` | 全プロジェクト共通 | No（個人環境） |
| **プロジェクト共有設定** | `.claude/settings.json` | このプロジェクトのみ | Yes（チーム共有） |
| **プロジェクトローカル設定** | `.claude/settings.local.json` | このプロジェクトのみ | No（個人環境） |

> VBA の対比:
> - ユーザー設定 = `PERSONAL.XLSB`（全ブック共通の個人設定）
> - プロジェクト共有設定 = ブック内の `ThisWorkbook` モジュール（ブック固有、他の人にも共有される）
> - プロジェクトローカル設定 = 自分の PC だけの環境設定

### 設定ファイルの基本構造

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(git status)",
      "Bash(python *)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  },
  "env": {
    "MY_VARIABLE": "値"
  }
}
```

- `permissions.allow`: 自動で許可するコマンド（毎回 `y` を押さなくて済む）
- `permissions.deny`: 常に拒否するコマンド（危険な操作を防ぐ）
- `env`: 環境変数の設定

### 優先順位

設定が重複した場合の優先順位:

```
プロジェクトローカル > プロジェクト共有 > ユーザー設定
```

> 身近な設定が優先される。「プロジェクト固有の設定」は「全体の設定」を上書きする。

---

## 2. CLAUDE.md を使いこなす

レベル 1 では「CLAUDE.md にプロジェクト情報を書く」だけだった。ここではより戦略的に活用する。

### CLAUDE.md の読み込み階層

CLAUDE.md は **複数の場所に置ける**。Claude Code は起動時にこれらを全て読み込む。

| 場所 | 役割 | 例 |
|------|------|-----|
| `~/.claude/CLAUDE.md` | 全プロジェクト共通のルール | 「日本語で回答して」「コミットメッセージは日本語で」 |
| プロジェクトルートの `CLAUDE.md` | プロジェクト固有の情報 | 「Python 3.12 を使用」「テストは pytest で実行」 |
| サブフォルダの `CLAUDE.md` | フォルダ固有の情報 | `src/api/CLAUDE.md` に API 設計ルールを記載 |

### settings.json と CLAUDE.md の使い分け

| | `settings.json` | `CLAUDE.md` |
|---|---|---|
| 役割 | Claude が **できること** を制御 | Claude が **知っておくべきこと** を伝える |
| 内容 | 許可するコマンド、環境変数 | コーディング規約、プロジェクト概要、注意事項 |
| 形式 | JSON | マークダウン |

### 効果的な CLAUDE.md の書き方

```markdown
# プロジェクト概要
顧客管理 Web アプリ。Flask + SQLite で構築。

# コーディング規約
- Python 3.12 を使用
- 変数名はスネークケース（例: user_name）
- 関数には docstring を書く
- テストは pytest で実行: `pytest tests/`

# やってはいけないこと
- データベースファイル（app.db）を直接編集しない
- .env ファイルを Git にコミットしない
- 本番用の設定を変更しない

# よく使うコマンド
- テスト実行: `pytest tests/ -v`
- 開発サーバー起動: `flask run --debug`
```

> 「やってはいけないこと」を明記するのが特に重要。Claude Code は指示がなければ最善の判断をするが、プロジェクト固有の禁止事項は伝えないとわからない。

---

## 3. カスタムスラッシュコマンドを作る

### カスタムスラッシュコマンドとは

毎回同じような指示を入力する手間を省く仕組み。マークダウンファイルを所定のフォルダに置くだけで、スラッシュコマンドとして使えるようになる。

> VBA の対比: よく使うマクロをクイックアクセスツールバーに登録するようなもの。ワンクリック（ワンコマンド）で定型作業を実行できる。

### 作り方

`.claude/commands/` フォルダにマークダウンファイルを作成する。

```bash
# プロジェクトフォルダ内で
mkdir -p .claude/commands
```

### 例 1: コードレビューコマンド

`.claude/commands/review.md`:

```markdown
以下のファイルをレビューしてください。

確認観点:
1. バグや論理エラーがないか
2. セキュリティ上の問題がないか
3. コードの読みやすさ
4. テストが十分か

対象: $ARGUMENTS
```

使い方:

```
/project:review src/main.py
```

`$ARGUMENTS` の部分が `src/main.py` に置き換わる。

### 例 2: テスト実行＋結果要約コマンド

`.claude/commands/test.md`:

```markdown
以下の手順でテストを実行し、結果を要約してください。

1. `pytest tests/ -v` を実行
2. テスト結果を確認
3. 失敗したテストがあれば原因を分析
4. 結果を以下のフォーマットで報告:
   - 合計テスト数
   - 成功数 / 失敗数
   - 失敗がある場合は原因の要約
```

使い方:

```
/project:test
```

### 例 3: 今日の変更まとめコマンド

`.claude/commands/summary.md`:

```markdown
今日の Git の変更内容をまとめてください。

1. `git log --oneline --since="today"` を実行
2. 各コミットの内容を確認
3. 以下のフォーマットで報告:
   - 変更したファイル一覧
   - 主な変更内容の要約
   - 残っている TODO があれば記載
```

### ユーザーレベルのコマンド

`~/.claude/commands/` に置くと、全プロジェクトで使えるコマンドになる。

```bash
mkdir -p ~/.claude/commands
```

> プロジェクト固有のコマンドは `.claude/commands/`（`/project:xxx`）、汎用的なコマンドは `~/.claude/commands/`（`/user:xxx`）に置く。

---

## 4. フック（Hooks）で操作を自動化する

### フックとは

Claude Code の特定の操作に **連動して自動実行されるシェルコマンド**。

> VBA の対比: `Workbook_BeforeSave` や `Workbook_Open` のようなイベント駆動マクロ。「ファイルを保存する前に自動でチェックを走らせる」といった動作を実現できる。

### フックの種類

| イベント | 発火タイミング | 用途の例 |
|---------|-------------|---------|
| `PreToolUse` | ツール実行前 | 危険な操作をブロック |
| `PostToolUse` | ツール実行後 | ファイル保存後に自動フォーマット |
| `Notification` | 通知発生時 | 長い処理の完了を通知 |
| `Stop` | Claude の応答完了時 | 品質チェック |

### 設定方法

`.claude/settings.json`（または `~/.claude/settings.json`）の `hooks` セクションに記述する。

### 例 1: ファイル編集後に自動フォーマット

Python ファイルを編集したら、自動で `black`（コードフォーマッター）を実行する。

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path // empty' | grep '\\.py$' | xargs -I {} black {} 2>/dev/null || true",
            "timeout": 10000
          }
        ]
      }
    ]
  }
}
```

### 例 2: 長い処理が終わったら通知

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code の処理が完了しました\" with title \"Claude Code\"'",
            "timeout": 5000
          }
        ]
      }
    ]
  }
}
```

> macOS のシステム通知が表示される。長いタスクを実行中に別の作業をしているときに便利。

### フックの入力データ

フックのコマンドには **JSON 形式のデータが標準入力（stdin）で渡される**。`jq` コマンドで必要な値を取り出せる。

```bash
# 例: 編集されたファイルのパスを取得
jq -r '.tool_input.file_path'
```

---

## 5. MCP（Model Context Protocol）で外部ツールと連携する

### MCP とは

Claude Code に **新しい「道具」を追加する仕組み**。標準では持っていない能力を外部サーバー経由で拡張できる。

> VBA の対比: Excel から外部の DLL やデータベースに接続するようなもの。Excel 単体ではできないことを、外部ツールとの連携で実現する。

### 仕組みのイメージ

```
Claude Code  ←→  MCP サーバー  ←→  外部サービス
（指示を出す）    （橋渡し役）       （実際の処理）
```

### 設定方法

プロジェクトルートに `.mcp.json` を作成する。

```json
{
  "mcpServers": {
    "サーバー名": {
      "command": "実行コマンド",
      "args": ["引数1", "引数2"]
    }
  }
}
```

### 設定ファイルの場所

| スコープ | ファイル |
|---------|---------|
| プロジェクト共有 | プロジェクトルートの `.mcp.json` |
| プロジェクトローカル | `.claude/settings.local.json` 内の `mcpServers` |
| ユーザー | `~/.claude/settings.local.json` 内の `mcpServers` |

### 例: ファイルシステム拡張

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/matsubarakouji/Documents"]
    }
  }
}
```

### 注意点

- **信頼できるソースの MCP サーバーのみ使う**（不明なサーバーはセキュリティリスク）
- MCP サーバーは Node.js（npx）または Python で実行されるものが多い
- 初めて使うときは Claude Code に「MCP サーバーの設定を手伝って」と頼むのが安全

---

## 6. ヘッドレスモードとスクリプト連携

### ヘッドレスモードとは

**対話なしで** Claude Code を実行する方法。定型処理をバッチ実行するのに使う。

> VBA の対比: タスクスケジューラから `.vbs` スクリプト経由で `Application.Run "マクロ名"` を実行するようなもの。人間が画面を見ていなくても自動で処理が走る。

### 基本的な使い方

```bash
# ワンショットで質問・指示を実行
claude -p "このプロジェクトの README.md を生成して"
```

`-p`（print）フラグをつけると、対話モードに入らず結果を出力して終了する。

### 出力を構造化する

```bash
# JSON 形式で出力
claude -p "main.py のバグを一覧にして" --output-format json
```

他のツールやスクリプトで結果を処理したいときに便利。

### シェルスクリプトとの組み合わせ

```bash
#!/bin/bash
# daily-review.sh — 毎朝のコードレビューを自動実行

cd ~/Documents/my-project

# 昨日からの変更を取得してレビュー
CHANGES=$(git log --oneline --since="yesterday")
claude -p "以下の変更をレビューして問題点を指摘して: $CHANGES"
```

### 実用例

| 用途 | コマンド例 |
|------|----------|
| README の自動生成 | `claude -p "README.md を生成して"` |
| コードレビュー | `claude -p "src/ のコードをレビューして"` |
| テスト結果の要約 | `pytest tests/ 2>&1 \| claude -p "このテスト結果を要約して"` |
| Git コミットメッセージの生成 | `git diff --staged \| claude -p "この差分に適したコミットメッセージを提案して"` |

---

## 7. 複数セッションの活用

### セッションとは

Claude Code との一連の会話のこと。会話が長くなりすぎると **コンテキストウィンドウ**（Claude の「作業メモリ」）が一杯になり、精度が下がることがある。

### セッションの使い分け

目的別にセッションを切り分けると効率がよい。

| セッション | 用途 | 寿命 |
|----------|------|------|
| セッション A | 新機能の開発 | 数時間〜数日（長期） |
| セッション B | バグ修正 | 短時間で完了（短期） |
| セッション C | コードレビュー・調査 | 都度（随時） |

### 操作方法

```bash
# 前回のセッションを続ける
claude -c

# 過去のセッションを選んで再開
claude /resume
```

### コンテキストのリセット

会話が長くなって回答の精度が落ちてきたと感じたら:

```
/clear
```

> 履歴をリセットして新しいセッションとして始める。CLAUDE.md の情報は再読み込みされるので、プロジェクトの基本情報は失われない。

---

## 8. Git の実践テクニック

### ブランチの概念

レベル 2 では `main` ブランチだけで作業していた。ブランチを使うと、**本体に影響を与えずに実験できる**。

> VBA の対比: ブックをコピーして実験 → うまくいったら本体に反映。Git のブランチはこの「コピーして実験」をより軽量に行える仕組み。

### 基本操作

```bash
# 新しいブランチを作成して切り替え
git checkout -b feature/add-login

# ブランチ上で作業してコミット
git add .
git commit -m "ログイン機能を追加"

# main ブランチに戻る
git checkout main

# ブランチの変更を main に取り込む
git merge feature/add-login
```

### Claude Code にブランチ操作を任せる

```
あなた: 「新しいブランチ feature/add-export を作って、CSV エクスポート機能を実装して」

Claude: ブランチを作成して実装します。
        1. git checkout -b feature/add-export
        2. エクスポート機能の実装
        3. テストの追加
        → 承認しますか？ [y/n]
```

### プルリクエスト

GitHub 上で「この変更を本体に取り込んでいいか」をレビューしてもらう仕組み。個人開発でも、変更内容を整理する習慣として使うと便利。

```bash
# ブランチを GitHub に push
git push -u origin feature/add-login

# プルリクエストを作成（GitHub CLI を使う場合）
gh pr create --title "ログイン機能を追加" --body "ログイン画面とパスワード認証を実装"
```

> これも Claude Code に「プルリクエストを作成して」と頼める。

---

## 9. 困ったときは

### よくある問題と対処法

| 症状 | 対処法 |
|------|--------|
| カスタムコマンドが認識されない | `.claude/commands/` フォルダの位置を確認。ファイル名が `.md` で終わっているか確認 |
| フックがエラーになる | `timeout` が短すぎないか確認。コマンドを直接ターミナルで実行してエラーを確認 |
| MCP サーバーが動かない | `npx` や `python` のパスが通っているか確認。Claude Code を再起動してみる |
| ヘッドレスモードで結果が途中で切れる | 指示を具体的にする。出力が長い場合は「要約して」と指示に加える |
| ブランチが混乱した | `git branch` で一覧を確認。Claude Code に「ブランチの状態を整理して」と相談 |
| 設定が反映されない | 設定ファイルの JSON 構文エラーを確認。Claude Code を再起動する |
| `jq` がインストールされていない | `brew install jq` でインストール |

### 設定で迷ったら

Claude Code に相談するのが最も手軽。

```
あなた: 「Python ファイルを編集したら自動で black を実行するフックを設定して」

Claude: .claude/settings.json にフックを追加します...
```
