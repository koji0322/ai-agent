# 開発学習ガイドシリーズ

Mac で Claude Code を中心に、プログラミングの基礎から実践的な開発スキルまで段階的に学べるガイド集。

---

## 対象読者

- プログラミング初心者
- Mac ユーザー
- Claude Code を活用して開発を学びたい方

## ガイドの全体像

```
=== 環境・基盤ガイド (00-05) ===
00  VS Code 基本操作           エディタの使い方
01  Mac 基礎操作               Mac の画面・キーボード・Finder・アプリ管理
02  Mac おすすめアプリ          開発・生産性向上アプリの導入
03  ターミナル CLI ツール       モダンなコマンド代替・開発支援ツール
04  おすすめ Web サイト         学習・AI・開発支援の定番サイト
05  SNS・情報発信              X・YouTube・Discord・ポッドキャスト

=== Claude Code 本編 (10-16) ===
10  基本操作                   ターミナルと Claude Code の基礎
11  実践                       Git・GitHub・開発フロー
12  応用・自動化               設定・コマンド・フック・MCP
13  アプリ開発                 Python・Web アプリ・DB・API
14  公開・運用                 デプロイ・CI/CD・保守
15  スキル・プラグイン          Claude Code の能力を拡張
16  マルチエージェント          複数 AI の協調・SDK

=== 新規テーマ (20-27) ===
20  セキュリティ基礎            API キー管理・SSH・OWASP Top 10
21  テスト入門                 pytest・TDD・カバレッジ・CI 連携
22  Docker 入門                コンテナ・Dockerfile・docker-compose
23  Web 開発基礎               HTML/CSS/JS・React・Next.js
24  データベース入門            SQLite・SQL・PostgreSQL・ORM
25  API 設計・連携             REST・FastAPI・Claude API
26  Python 環境構築            pyenv・venv・pip・VS Code 設定
27  データ分析入門             pandas・matplotlib・Jupyter・CSV/Excel

=== ロードマップ (30) ===
30  開発学習ロードマップ        初心者からプロフェッショナルへの道筋
```

---

## 各ガイドの内容

### 環境・基盤ガイド (00-05)

#### [00 - VS Code 基本操作ガイド](00-vscode-guide.md)

VS Code のインストールから基本操作、Claude Code との連携まで。

| トピック | 内容 |
|---------|------|
| 画面構成 | アクティビティバー・サイドバー・エディタ・ターミナル・ステータスバー |
| 基本操作 | フォルダを開く・ファイル編集・保存・検索 |
| ショートカット | コマンドパレット・ファイル検索・ターミナル開閉 |
| 拡張機能 | Japanese Language Pack・Claude Code・Python |
| Claude Code 連携 | 内蔵ターミナルでの実行・拡張機能 |

---

#### [01 - Mac 基礎操作ガイド](01-mac-basics-guide.md)

Mac の画面構成・キーボード・Finder・トラックパッド・アプリ管理・システム設定を体系的にまとめたガイド。

| トピック | 内容 |
|---------|------|
| 画面構成 | メニューバー・Dock・デスクトップ |
| キーボード | 修飾キー・主要ショートカット |
| Finder | フォルダ構造・基本操作・ナビゲーション・おすすめ設定 |
| トラックパッド | ジェスチャー操作 |
| アプリの基本 | 起動・終了・インストール（App Store / dmg / Homebrew） |
| Dock・Mission Control | 配置・仮想デスクトップ・Split View |
| セキュリティ・バックアップ | FileVault・Gatekeeper・Time Machine |

---

#### [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md)

Mac に導入すべき開発・生産性向上アプリをまとめたガイド。

| トピック | 内容 |
|---------|------|
| ターミナル・シェル | iTerm2・Oh My Zsh・Starship |
| パッケージマネージャー | Homebrew 活用・Brewfile で一括管理 |
| エディタ・IDE | VS Code・Cursor・CotEditor |
| Git・GitHub | GitHub Desktop・GitKraken・gh CLI |
| API・データベース | Postman・Bruno・TablePlus・DB Browser |
| ウィンドウ管理・生産性 | Rectangle・Raycast・Clipy・Karabiner-Elements |

---

#### [03 - ターミナル CLI ツールガイド](03-terminal-tools-guide.md)

ターミナルで使うモダンな CLI ツール（コマンド代替・開発支援ツール）をまとめたガイド。

| トピック | 内容 |
|---------|------|
| モダンなコマンド代替 | eza(ls)・bat(cat)・fd(find)・ripgrep(grep)・delta(diff) |
| ファイル操作・検索 | fzf・tree・zoxide(cd)・trash-cli |
| JSON・データ処理 | jq・yq・fx |
| ネットワーク・HTTP | curl・httpie・xh |
| バージョン管理 | mise・nvm・fnm・pyenv |
| Git 拡張 | lazygit・tig・git-delta |

---

#### [04 - おすすめ Web サイトガイド](04-web-resources-guide.md)

開発者がブックマークしておくべき Web サイト・オンラインサービスをまとめたガイド。

| トピック | 内容 |
|---------|------|
| 公式ドキュメント | MDN・Python Docs・DevDocs |
| 学習プラットフォーム | freeCodeCamp・The Odin Project・Codecademy |
| AI サービス | Claude・ChatGPT・GitHub Copilot・Perplexity |
| ホスティング・デプロイ | Vercel・Netlify・Render・GitHub Pages |
| 開発支援ツール | regex101・Excalidraw・CodePen・StackBlitz |

---

#### [05 - SNS・情報発信ガイド](05-sns-guide.md)

開発者がフォロー・参加すべき SNS・動画・ポッドキャスト・コミュニティをまとめたガイド。

| トピック | 内容 |
|---------|------|
| X（Twitter）・Bluesky | フォローすべきアカウント・ハッシュタグ |
| YouTube | プログラミング学習チャンネル |
| Discord・Reddit | 開発者コミュニティ |
| ポッドキャスト | テック系ポッドキャスト |

---

### Claude Code 本編 (10-16)

#### [10 - Claude Code 基本操作ガイド](10-claude-code-guide.md)
**レベル 1 — 道具の使い方を覚える**

ターミナルの開き方から Claude Code のインストール・基本的な対話まで。

| トピック | 内容 |
|---------|------|
| ターミナルの基礎 | 開き方・基本コマンド（`pwd`, `ls`, `cd`）・パスの概念 |
| インストール | Node.js・Claude Code の導入・初回ログイン |
| 起動と終了 | プロジェクトフォルダでの起動・`Ctrl+D` で終了・`-c` で再開 |
| 基本的な対話 | 指示 → 提案 → 承認の流れ |
| スラッシュコマンド | `/help`, `/clear`, `/plan`, `/resume` など |
| CLAUDE.md | プロジェクト固有の設定ファイル |

---

#### [11 - Claude Code 実践ガイド](11-claude-code-practical-guide.md)
**レベル 2 — 道具を使って仕事をする**

Git でバージョン管理し、GitHub にバックアップし、実践的な開発フローで作業する。

| トピック | 内容 |
|---------|------|
| Git | `init` / `add` / `commit` の 3 コマンド・履歴確認・差分確認・復元 |
| GitHub | アカウント作成・SSH 設定・`push` でクラウド保管 |
| 開発フロー | 調査 → 計画 → 実装 → 確認 → 記録の 5 フェーズ |
| 拡張思考モード | `Alt+T` で切り替え・使い分けの目安 |
| デバッグ | エラーメッセージの貼り付け・スクリーンショット活用 |

---

#### [12 - Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md)
**レベル 3 — 道具を自分好みにカスタマイズする**

設定ファイル・カスタムコマンド・フック・MCP で Claude Code を最適化する。

| トピック | 内容 |
|---------|------|
| 設定ファイル | ユーザー / プロジェクト共有 / ローカルの 3 スコープ |
| CLAUDE.md 活用 | 読み込み階層・「やってはいけないこと」の明記 |
| カスタムコマンド | `.claude/commands/` にテンプレートを配置・`$ARGUMENTS` |
| フック | `PreToolUse` / `PostToolUse` / `Notification` で自動化 |
| MCP | 外部ツール連携・`.mcp.json` の設定 |
| ヘッドレスモード | `claude -p` でワンショット実行・シェルスクリプト連携 |

---

#### [13 - Claude Code アプリケーション開発ガイド](13-claude-code-app-dev-guide.md)
**レベル 4 — 道具を使って「作品」を作る**

Python・Web アプリ・データベースで実用的なアプリケーションを開発する。

| トピック | 内容 |
|---------|------|
| Python 基礎 | Excel 読み書き・CSV 集計・ファイル一括処理 |
| プロジェクト設計 | Claude Code との壁打ち・モジュール分割 |
| コマンドラインツール | `argparse` で引数受け取り |
| Web アプリ | Streamlit（最も手軽）・Flask（本格的） |
| データベース | SQLite の基本・SQL を Claude Code に書いてもらう |
| API 連携 | `requests` ライブラリ・API キーの安全な管理 |
| テスト | `pytest` の基本・Claude Code にテストを書いてもらう |

---

#### [14 - Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md)
**レベル 5 — 作品を人に届け、維持する**

作ったものを公開し、継続的に保守・改善するための仕組みを整える。

| トピック | 内容 |
|---------|------|
| README | プロジェクトの「顔」を整備 |
| 依存関係管理 | `requirements.txt`・仮想環境（`venv`） |
| GitHub 公開 | ライセンス・Issue 管理 |
| 秘密情報管理 | `.env` / `.env.example` / `.gitignore` |
| デプロイ | Streamlit Cloud・GitHub Pages・Render |
| CI/CD | GitHub Actions でテスト自動実行 |

---

#### [15 - Claude Code スキル・プラグインガイド](15-claude-code-skills-guide.md)
**レベル 6 — Claude Code 自体を拡張する**

スキルとプラグインで専門知識を構造化し、再利用・共有可能にする。

| トピック | 内容 |
|---------|------|
| スキルとは | カスタムコマンドとの違い・自動発動の仕組み |
| 3 層アーキテクチャ | メタデータ → 本文 → 補足資料の段階的読み込み |
| スキル作成 | `SKILL.md` の書き方・YAML フロントマター |
| 公式スキル | Excel・PowerPoint・Word・PDF |
| プラグイン | フォルダ構成・`plugin.json`・名前空間・配布 |
| フックの発展 | `SessionStart` / `UserPromptSubmit` / `prompt` タイプ |

---

#### [16 - Claude Code マルチエージェントガイド](16-claude-code-multi-agent-guide.md)
**レベル 7 — 複数の AI を協調させる**

Agent Teams で並列作業し、Agent SDK でプログラムから制御する。

| トピック | 内容 |
|---------|------|
| Agent Teams | 有効化・チームリード / チームメイト・共有タスクリスト |
| チーム構成パターン | 並行開発・マルチ観点レビュー・仮説検証 |
| 品質管理 | プラン承認・品質ゲート（フック連携） |
| Agent SDK | Python / TypeScript からの制御・`query()` 関数 |
| SDK 実用例 | 自動レビュー・CI/CD 連携・一括処理 |
| 使い分け | 状況別の最適アプローチ判断フロー |

---

### 新規テーマ (20-27)

#### [20 - セキュリティ基礎ガイド](20-security-basics-guide.md)

開発に必要なセキュリティの基礎知識。

| トピック | 内容 |
|---------|------|
| パスワード・アカウント管理 | パスワードマネージャー・2FA・SSH キー |
| API キー管理 | `.env`・`.gitignore`・環境変数 |
| Git とセキュリティ | シークレットのスキャン・git-secrets |
| OWASP Top 10 | XSS・SQL インジェクション・CSRF |
| 依存パッケージ | npm audit・pip audit・Dependabot |

---

#### [21 - テスト入門ガイド](21-testing-intro-guide.md)

テストの書き方と自動化。

| トピック | 内容 |
|---------|------|
| テストの種類 | ユニット・統合・E2E |
| pytest | インストール・assert・fixture・parametrize |
| TDD | Red-Green-Refactor サイクル |
| カバレッジ | pytest-cov・レポートの見方 |
| CI 連携 | GitHub Actions でテスト自動化 |

---

#### [22 - Docker 入門ガイド](22-docker-intro-guide.md)

コンテナ技術の基礎。

| トピック | 内容 |
|---------|------|
| コンテナの概念 | コンテナ vs VM・イメージ vs コンテナ |
| 基本コマンド | run・ps・stop・rm・images |
| Dockerfile | FROM・RUN・COPY・WORKDIR・CMD |
| docker-compose | マルチコンテナ構成・Web + DB の例 |
| Dev Containers | VS Code でコンテナ内開発 |

---

#### [23 - Web 開発基礎ガイド](23-web-basics-guide.md)

Web 開発の基礎技術。

| トピック | 内容 |
|---------|------|
| HTML/CSS/JS | 基本構文・セマンティック HTML・Flexbox |
| DevTools | Elements・Console・Network タブ |
| React | コンポーネント・JSX・props・state・hooks |
| Next.js | ルーティング・SSR vs CSR・API ルート |
| ビルドツール | Vite・バンドリング |

---

#### [24 - データベース入門ガイド](24-database-intro-guide.md)

データベースの基礎。

| トピック | 内容 |
|---------|------|
| DB の種類 | RDB vs NoSQL |
| SQLite | Python での基本操作 |
| SQL 基本 | SELECT・INSERT・UPDATE・DELETE・JOIN |
| テーブル設計 | 主キー・外部キー・正規化 |
| ORM | SQLAlchemy の基本・CRUD |
| マイグレーション | Alembic の基本 |

---

#### [25 - API 設計・連携ガイド](25-api-guide.md)

API の設計と利用。

| トピック | 内容 |
|---------|------|
| HTTP の基礎 | メソッド・ステータスコード・ヘッダー |
| REST API 設計 | リソースベース URL・CRUD マッピング |
| FastAPI | パスパラメータ・リクエストボディ・自動ドキュメント |
| 外部 API | requests ライブラリ・JSON 処理 |
| Claude API | SDK・メッセージ API・ストリーミング |
| API 認証 | API キー・OAuth・Bearer トークン |

---

#### [26 - Python 環境構築ガイド](26-python-setup-guide.md)

Python 環境のセットアップ。

| トピック | 内容 |
|---------|------|
| バージョン管理 | pyenv・mise でバージョンを切り替え |
| 仮想環境 | venv で依存パッケージを分離 |
| パッケージ管理 | pip install・requirements.txt |
| VS Code 設定 | Python 拡張・インタープリタ選択・デバッグ |
| Claude Code 連携 | Python スクリプト生成・CLAUDE.md 設定 |

---

#### [27 - データ分析入門ガイド](27-data-analysis-guide.md)

Python でのデータ分析の基礎。

| トピック | 内容 |
|---------|------|
| pandas | DataFrame・CSV/Excel 読み込み・集計 |
| matplotlib | 棒グラフ・折れ線グラフ・円グラフ |
| Jupyter Notebook | セル操作・VS Code 連携 |
| 実践 | データクリーニング・可視化・結果保存 |
| Claude Code 連携 | データ分析の依頼・コード生成 |

---

### ロードマップ (30)

#### [30 - 開発学習ロードマップ](30-learning-roadmap-guide.md)
**初心者からプロフェッショナルへ**

プログラミング未経験者が Claude Code エコシステムを活用して開発のプロフェッショナルになるまでの学習ロードマップ。

| トピック | 内容 |
|---------|------|
| ロードマップ全体像 | フェーズ別の到達レベル・学習時間の目安 |
| 環境構築フェーズ | Mac 操作・VS Code・ターミナル・Claude Code の基礎 |
| 実践フェーズ | Git・GitHub・Python・Web アプリ・DB・API |
| 応用フェーズ | カスタマイズ・自動化・デプロイ・CI/CD |
| 専門フェーズ | セキュリティ・テスト・Docker・Web 開発・DB・API 設計 |
| マスターフェーズ | スキル・マルチエージェント・フルスタック・チーム開発 |
| キャリアパス | AI 時代の開発者キャリア・職種マップ |

---

## 読み進め方

### 推奨ルート

> **初心者の方へ**: まず [30 - 開発学習ロードマップ](30-learning-roadmap-guide.md) を読み、全体像を把握してから各ガイドに進むことをおすすめします。

```
環境構築:    00（VS Code）→ 01（Mac 基礎）
Claude Code: 10（基本）→ 11（実践）→ 12（応用）→ 13（アプリ開発）→ 14（公開）→ 15（スキル）→ 16（マルチエージェント）
新規テーマ:  20〜27 は興味・必要に応じていつでも
```

- **00〜05**（環境・基盤ガイド）はどのタイミングで読んでも OK
- **20〜27**（新規テーマ）は独立しているので、必要になったときに参照
- 各ガイドの「はじめに」に前提条件と関連ガイドへのリンクあり

### 目的別ショートカット

| やりたいこと | 読むべきガイド |
|------------|-------------|
| Mac の基本操作を知りたい | [01](01-mac-basics-guide.md) |
| Mac に便利なアプリを入れたい | [02](02-mac-apps-guide.md) |
| ターミナルをもっと便利にしたい | [03](03-terminal-tools-guide.md) |
| 開発に役立つサイトを知りたい | [04](04-web-resources-guide.md) |
| 開発者向け SNS を知りたい | [05](05-sns-guide.md) |
| Claude Code をとりあえず動かしたい | [10](10-claude-code-guide.md) |
| Git / GitHub を使いたい | [11](11-claude-code-practical-guide.md) |
| 毎回同じ指示を打つのが面倒 | [12](12-claude-code-advanced-guide.md)（カスタムコマンド・フック） |
| Python でアプリを作りたい | [13](13-claude-code-app-dev-guide.md) |
| 作ったツールを公開したい | [14](14-claude-code-deploy-guide.md) |
| Claude Code に専門知識を持たせたい | [15](15-claude-code-skills-guide.md) |
| 大規模タスクを並列で処理したい | [16](16-claude-code-multi-agent-guide.md) |
| セキュリティの基礎を知りたい | [20](20-security-basics-guide.md) |
| テストの書き方を学びたい | [21](21-testing-intro-guide.md) |
| Docker を始めたい | [22](22-docker-intro-guide.md) |
| Web 開発を始めたい | [23](23-web-basics-guide.md) |
| データベースを学びたい | [24](24-database-intro-guide.md) |
| API を設計・利用したい | [25](25-api-guide.md) |
| Python の環境を構築したい | [26](26-python-setup-guide.md) |
| データ分析を始めたい | [27](27-data-analysis-guide.md) |
| 学習の全体像とロードマップを知りたい | [30](30-learning-roadmap-guide.md) |

<details>
<summary>VBA 経験者向けの対比表</summary>

| レベル | VBA でやっていたこと | このシリーズで学ぶこと |
|-------|-------------------|-------------------|
| 1 | VBE を開いてコードを書く | ターミナルを開いて Claude Code を使う |
| 2 | マクロを書いて業務を処理する | Git で管理しながら開発フローで作業する |
| 3 | 自動実行マクロ・ユーザーフォーム | カスタムコマンド・フック・MCP で自動化 |
| 4 | Excel アドインや独立ツールの開発 | Python・Web アプリ・DB でアプリを作る |
| 5 | ツールを共有フォルダで配布・保守 | GitHub で公開・CI/CD で自動テスト・保守 |
| 6 | 汎用アドインを整備して社内配布 | スキル・プラグインで知識を構造化・共有 |
| 7 | （VBA の枠を超える） | 複数 AI の協調・SDK でパイプライン構築 |

</details>

---

## データサイエンティスト向けガイド

データサイエンス・機械学習に特化したガイドシリーズは [data-science/](data-science/) ディレクトリに収録しています。

詳細は [data-science/README.md](data-science/README.md) を参照してください。
