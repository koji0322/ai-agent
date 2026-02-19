# Claude Code 学習ガイドシリーズ

Mac で Claude Code を使いこなすための自分用リファレンス集。
VBA（Excel VBE）の経験をベースに、ターミナル操作からマルチエージェントまで段階的に学べる構成。

---

## 対象読者

- VBA（Excel VBE）は使える
- ターミナル操作やモダンな開発ツールは不慣れ
- Mac ユーザー

## ガイドの全体像

```
00  VS Code           エディタの使い方（どのレベルからでも参照）
08  Mac Finder        ファイル管理の基本（どのレベルからでも参照）
09  Mac 基礎操作       Mac の画面・キーボード・アプリ管理（どのレベルからでも参照）
10  Mac おすすめアプリ   開発・生産性向上アプリの導入（どのレベルからでも参照）
11  ターミナル CLI ツール  モダンなコマンド代替・開発支援ツール（どのレベルからでも参照）
12  おすすめ Web サイト   学習・AI・開発支援の定番サイト（どのレベルからでも参照）
13  SNS・情報発信        X・YouTube・Discord・ポッドキャスト（どのレベルからでも参照）
    ─────────────────────────────────────────────
01  基本操作           ターミナルと Claude Code の基礎
02  実践               Git・GitHub・開発フロー
03  応用・自動化        設定・コマンド・フック・MCP
04  アプリ開発          Python・Web アプリ・DB・API
05  公開・運用          デプロイ・CI/CD・保守
06  スキル・プラグイン   Claude Code の能力を拡張
07  マルチエージェント   複数 AI の協調・SDK
    ─────────────────────────────────────────────
20  学習ロードマップ     初心者からプロフェッショナルへの道筋
```

## 各ガイドの内容

### [00 - VS Code 基本操作ガイド](00-vscode-guide.md)

VS Code のインストールから基本操作、Claude Code との連携まで。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| 画面構成 | アクティビティバー・サイドバー・エディタ・ターミナル・ステータスバー |
| 基本操作 | フォルダを開く・ファイル編集・保存・検索 |
| ショートカット | コマンドパレット・ファイル検索・ターミナル開閉 |
| 拡張機能 | Japanese Language Pack・Claude Code・Python |
| Claude Code 連携 | 内蔵ターミナルでの実行・拡張機能 |

---

### [08 - Mac Finder 基本操作ガイド](08-mac-finder-guide.md)

Mac のファイル管理アプリ Finder の使い方。Windows エクスプローラーとの違いを中心に解説。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| 画面構成 | ツールバー・サイドバー・メインエリア・パスバー |
| 基本操作 | 移動・コピー・名前変更・削除・クイックルック |
| ナビゲーション | フォルダ移動・パス指定・サイドバー活用 |
| 検索 | Finder 内検索・Spotlight |
| おすすめ設定 | パスバー表示・拡張子表示・隠しファイル |
| ターミナル連携 | `open .`・パスのドラッグ&ドロップ |

---

### [09 - Mac 基礎操作ガイド](09-mac-basics-guide.md)

Mac の画面構成・キーボード・トラックパッド・アプリ管理・システム設定まで、Mac の基礎知識を体系的にまとめたガイド。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| 画面構成 | メニューバー・Dock・デスクトップ・通知センター |
| キーボード | 修飾キーの対応（Ctrl→Cmd）・記号の読み方・主要ショートカット |
| トラックパッド | ジェスチャー操作（スクロール・ズーム・3本指スワイプ） |
| アプリの基本 | 起動・切替（Cmd+Tab）・終了（×で終了しない）・強制終了 |
| Dock・Mission Control | 配置・仮想デスクトップ・Split View |
| Spotlight・スクリーンショット | 万能ランチャー・画面キャプチャ・画面収録 |
| インストール・設定 | App Store・dmg・Homebrew・おすすめ初期設定 |
| セキュリティ・バックアップ | FileVault・Gatekeeper・Time Machine |
| トラブルシューティング | フリーズ対処・ディスク容量・セーフモード |

---

### [10 - Mac おすすめアプリガイド](10-mac-apps-guide.md)

Mac に導入すべき開発・生産性向上アプリをまとめたガイド。Homebrew での一括セットアップ方法も解説。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| ターミナル・シェル | iTerm2・Oh My Zsh・Starship |
| パッケージマネージャー | Homebrew 活用・Brewfile で一括管理 |
| エディタ・IDE | VS Code・Cursor・CotEditor |
| Git・GitHub | GitHub Desktop・GitKraken・gh CLI |
| API・データベース | Postman・Bruno・TablePlus・DB Browser |
| ブラウザ・開発ツール | Chrome（DevTools）・Firefox・Arc |
| ウィンドウ管理・生産性 | Rectangle・Raycast・Clipy・Karabiner-Elements |
| ドキュメント・メモ | Notion・Obsidian・Markdown エディタ |
| その他の便利ツール | AppCleaner・The Unarchiver・Stats・Hidden Bar |

---

### [11 - ターミナル CLI ツールガイド](11-terminal-tools-guide.md)

ターミナルで使うモダンな CLI ツール（コマンド代替・開発支援ツール）をまとめたガイド。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| モダンなコマンド代替 | eza(ls)・bat(cat)・fd(find)・ripgrep(grep)・sd(sed)・dust(du)・duf(df)・delta(diff) |
| ファイル操作・検索 | fzf（あいまい検索）・tree・zoxide(cd)・trash-cli |
| JSON・データ処理 | jq・yq・fx |
| ネットワーク・HTTP | curl・wget・httpie・xh |
| プロセス・システム監視 | htop・btop・procs・watch |
| バージョン管理（言語） | mise(asdf後継)・nvm・fnm・pyenv |
| Git 拡張 | lazygit・tig・git-delta |
| Docker・コンテナ | Docker Desktop・lazydocker・dive |
| その他の便利ツール | tldr・thefuck・neofetch・tokei・hyperfine |

---

### [12 - おすすめ Web サイトガイド](12-web-resources-guide.md)

開発者がブックマークしておくべき Web サイト・オンラインサービスをまとめたガイド。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| 公式ドキュメント・リファレンス | MDN・Python Docs・DevDocs・Can I Use |
| 学習プラットフォーム | freeCodeCamp・The Odin Project・Codecademy・Udemy |
| 技術コミュニティ・Q&A | Stack Overflow・GitHub Discussions・Qiita・Zenn・Dev.to |
| AI サービス・ツール | Claude・ChatGPT・GitHub Copilot・Perplexity・v0 |
| ホスティング・デプロイ | Vercel・Netlify・Render・Cloudflare Pages・GitHub Pages |
| デザイン・UI リソース | Figma・Tailwind CSS・shadcn/ui・Heroicons・Google Fonts |
| API・データ | Public APIs リスト・JSONPlaceholder・Postman API Network |
| 開発支援ツール（Web） | regex101・Excalidraw・CodePen・StackBlitz・readme.so |
| ニュース・トレンド | Hacker News・daily.dev・JavaScript Weekly・GitHub Trending |

---

### [13 - 開発者向け SNS・情報発信ガイド](13-sns-guide.md)

開発者がフォロー・参加すべき SNS・動画・ポッドキャスト・コミュニティをまとめたガイド。
どのレベルからでも参照できる独立したガイド。

| トピック | 内容 |
|---------|------|
| X（Twitter） | フォローすべきアカウント・ハッシュタグ・活用法 |
| YouTube | プログラミング学習チャンネル（日本語・英語） |
| Discord | 開発者コミュニティ・OSS プロジェクトの公式サーバー |
| Reddit | プログラミング系サブレディット |
| LinkedIn | エンジニアのキャリア・ネットワーキング |
| Bluesky・Threads・Mastodon | 新興 SNS のテックコミュニティ |
| ポッドキャスト | テック系ポッドキャスト（日本語・英語） |
| おすすめフォロー戦略 | 情報過多にならないための運用ルール |

---

### [01 - Claude Code 基本操作ガイド](01-claude-code-guide.md)
**レベル 1 — 道具の使い方を覚える**

ターミナルの開き方から Claude Code のインストール・基本的な対話まで。ゼロからのスタート地点。

| トピック | 内容 |
|---------|------|
| ターミナルの基礎 | 開き方・基本コマンド（`pwd`, `ls`, `cd`）・パスの概念 |
| インストール | Node.js・Claude Code の導入・初回ログイン |
| 起動と終了 | プロジェクトフォルダでの起動・`Ctrl+D` で終了・`-c` で再開 |
| 基本的な対話 | 指示 → 提案 → 承認の流れ |
| スラッシュコマンド | `/help`, `/clear`, `/plan`, `/resume` など |
| CLAUDE.md | プロジェクト固有の設定ファイル |

---

### [02 - Claude Code 実践ガイド](02-claude-code-practical-guide.md)
**レベル 2 — 道具を使って仕事をする**

Git でバージョン管理し、GitHub にバックアップし、実践的な開発フローで作業する。

| トピック | 内容 |
|---------|------|
| Git | `init` / `add` / `commit` の 3 コマンド・履歴確認・差分確認・復元 |
| GitHub | アカウント作成・SSH 設定・`push` でクラウド保管 |
| プロジェクトの始め方 | フォルダ構成・CLAUDE.md 整備・`.gitignore` |
| 開発フロー | 調査 → 計画 → 実装 → 確認 → 記録の 5 フェーズ |
| 拡張思考モード | `Alt+T` で切り替え・使い分けの目安 |
| デバッグ | エラーメッセージの貼り付け・スクリーンショット活用 |

---

### [03 - Claude Code 応用・自動化ガイド](03-claude-code-advanced-guide.md)
**レベル 3 — 道具を自分好みにカスタマイズする**

設定ファイル・カスタムコマンド・フック・MCP で Claude Code を自分の作業スタイルに最適化する。

| トピック | 内容 |
|---------|------|
| 設定ファイル | ユーザー / プロジェクト共有 / ローカルの 3 スコープ |
| CLAUDE.md 活用 | 読み込み階層・「やってはいけないこと」の明記 |
| カスタムコマンド | `.claude/commands/` にテンプレートを配置・`$ARGUMENTS` |
| フック | `PreToolUse` / `PostToolUse` / `Notification` で自動化 |
| MCP | 外部ツール連携・`.mcp.json` の設定 |
| ヘッドレスモード | `claude -p` でワンショット実行・シェルスクリプト連携 |
| ブランチ | 分岐・マージ・プルリクエスト |

---

### [04 - Claude Code アプリケーション開発ガイド](04-claude-code-app-dev-guide.md)
**レベル 4 — 道具を使って「作品」を作る**

VBA でやっていた作業を Python・Web アプリ・データベースで再現する。

| トピック | 内容 |
|---------|------|
| VBA → Python | Excel 読み書き・CSV 集計・ファイル一括処理 |
| プロジェクト設計 | Claude Code との壁打ち・モジュール分割の判断 |
| コマンドラインツール | `argparse` で引数受け取り |
| Web アプリ | Streamlit（最も手軽）・Flask（本格的） |
| データベース | SQLite の基本・SQL を Claude Code に書いてもらう |
| API 連携 | `requests` ライブラリ・API キーの安全な管理 |
| テスト | `pytest` の基本・Claude Code にテストを書いてもらう |

---

### [05 - Claude Code 公開・運用ガイド](05-claude-code-deploy-guide.md)
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
| 保守サイクル | Issue 駆動の開発・バージョニング |

---

### [06 - Claude Code スキル・プラグインガイド](06-claude-code-skills-guide.md)
**レベル 6 — Claude Code 自体を拡張する**

スキルとプラグインで専門知識を構造化し、再利用・共有可能にする。

| トピック | 内容 |
|---------|------|
| スキルとは | カスタムコマンドとの違い・自動発動の仕組み |
| 3 層アーキテクチャ | メタデータ → 本文 → 補足資料の段階的読み込み |
| スキル作成 | `SKILL.md` の書き方・YAML フロントマター |
| 実用化 | 補足ファイル・実行スクリプトの同梱 |
| 公式スキル | Excel・PowerPoint・Word・PDF |
| プラグイン | フォルダ構成・`plugin.json`・名前空間・配布 |
| フックの発展 | `SessionStart` / `UserPromptSubmit` / `prompt` タイプ |

---

### [07 - Claude Code マルチエージェントガイド](07-claude-code-multi-agent-guide.md)
**レベル 7 — 複数の AI を協調させる**

Agent Teams で並列作業し、Agent SDK でプログラムから制御する。

| トピック | 内容 |
|---------|------|
| サブエージェントの限界 | Agent Teams との比較 |
| Agent Teams | 有効化・チームリード / チームメイト・共有タスクリスト |
| チーム構成パターン | 並行開発・マルチ観点レビュー・仮説検証 |
| 品質管理 | プラン承認・品質ゲート（フック連携） |
| Agent SDK | Python / TypeScript からの制御・`query()` 関数 |
| SDK 実用例 | 自動レビュー・CI/CD 連携・一括処理 |
| Cowork | コーディング以外のナレッジワーク向け |
| 使い分け | 状況別の最適アプローチ判断フロー |

---

### [20 - 開発学習ロードマップ](20-learning-roadmap-guide.md)
**初心者からプロフェッショナルへ**

プログラミング未経験者が Claude Code エコシステムを活用して開発のプロフェッショナルになるまでの学習ロードマップ。全 7 フェーズで、本シリーズの全ガイド（00〜13）を体系的に学ぶ道筋を示す。

| トピック | 内容 |
|---------|------|
| ロードマップ全体像 | 7 フェーズ・到達レベル・学習時間の目安 |
| Phase 1〜2 | Mac 操作・VS Code・ターミナル・Claude Code の基礎 |
| Phase 3〜4 | Git・GitHub・Python・Web アプリ・DB・API |
| Phase 5〜6 | カスタマイズ・自動化・デプロイ・CI/CD・ポートフォリオ |
| Phase 7 | スキル・マルチエージェント・フルスタック・チーム開発 |
| キャリアパス | AI 時代の開発者キャリア・職種マップ・転職戦略 |
| 学習習慣 | 挫折対策・Claude Code 活用学習法・継続のコツ |

---

## 読み進め方

### 推奨ルート

> **初心者の方へ**: まず [20 - 開発学習ロードマップ](20-learning-roadmap-guide.md) を読み、全体像を把握してから各ガイドに進むことをおすすめする。

```
01（基本操作）→ 02（実践）→ 03（応用）→ 04（アプリ開発）→ 05（公開）→ 06（スキル）→ 07（マルチエージェント）
```

- **00（VS Code）**・**08（Finder）**・**09（Mac 基礎）**・**10（おすすめアプリ）**・**11（CLI ツール）**・**12（Web サイト）**・**13（SNS・情報発信）** はどのタイミングで読んでも OK。01 と並行して参照するのがおすすめ
- 各ガイドの「はじめに」に前提条件と関連ガイドへのリンクがあるので、順番通りでなくても前後関係がわかる

### 目的別ショートカット

| やりたいこと | 読むべきガイド |
|------------|-------------|
| Mac の基本操作を知りたい | 09 |
| Mac に便利なアプリを入れたい | 10 |
| ターミナルをもっと便利にしたい | 11 |
| 開発に役立つサイトを知りたい | 12 |
| 開発者向け SNS を知りたい | 13 |
| Claude Code をとりあえず動かしたい | 01 |
| Git / GitHub を使いたい | 02 |
| 毎回同じ指示を打つのが面倒 | 03（カスタムコマンド・フック） |
| Python で Excel 集計を自動化したい | 04 |
| 作ったツールを公開したい | 05 |
| Claude Code に専門知識を持たせたい | 06 |
| 大規模タスクを並列で処理したい | 07 |
| 学習の全体像とロードマップを知りたい | 20 |
| AI 時代のキャリアパスを知りたい | 20（セクション 10） |
| 学習リソースをフェーズ別に探したい | 20（セクション 9） |

### VBA との対比で全体を捉える

| レベル | VBA でやっていたこと | このシリーズで学ぶこと |
|-------|-------------------|-------------------|
| 1 | VBE を開いてコードを書く | ターミナルを開いて Claude Code を使う |
| 2 | マクロを書いて業務を処理する | Git で管理しながら開発フローで作業する |
| 3 | 自動実行マクロ・ユーザーフォーム | カスタムコマンド・フック・MCP で自動化 |
| 4 | Excel アドインや独立ツールの開発 | Python・Web アプリ・DB でアプリを作る |
| 5 | ツールを共有フォルダで配布・保守 | GitHub で公開・CI/CD で自動テスト・保守 |
| 6 | 汎用アドインを整備して社内配布 | スキル・プラグインで知識を構造化・共有 |
| 7 | （VBA の枠を超える） | 複数 AI の協調・SDK でパイプライン構築 |
