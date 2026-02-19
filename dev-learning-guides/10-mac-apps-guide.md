# Mac おすすめアプリガイド

## 0. はじめに

このガイドは **Mac に導入すべきおすすめアプリを開発者目線でまとめた自分用リファレンス** です。

- **想定読者**: Windows から Mac に移行した開発者。基本操作は覚えたので、便利なアプリを導入したい
- **ゴール**: 開発・生産性向上に役立つアプリを知り、Homebrew で効率的にセットアップできるようになる
- **前提**: [09 - Mac 基礎操作ガイド](09-mac-basics-guide.md) のアプリインストール方法（App Store / dmg / Homebrew）を理解していること
- **関連ガイド**: [00 - VS Code ガイド](00-vscode-guide.md)、[09 - Mac 基礎操作ガイド](09-mac-basics-guide.md)

> このガイドでは **無料アプリを優先** して紹介する。有料の場合は明記する。
> インストール方法は `brew install --cask` を中心に記載。Homebrew の基本は [09 のインストールセクション](09-mac-basics-guide.md) を参照。

### インストール方法の早見表

| 方法 | コマンド / 操作 | 用途 |
|------|----------------|------|
| Homebrew（CLI ツール） | `brew install パッケージ名` | ターミナルで使うツール |
| Homebrew（GUI アプリ） | `brew install --cask アプリ名` | ウィンドウで動くアプリ |
| App Store | App Store で検索 → 入手 | Apple 審査済みアプリ |
| dmg / pkg | 公式サイトからダウンロード | Homebrew にないアプリ |

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. ターミナル・シェル](#1-ターミナルシェル) | iTerm2・Oh My Zsh・Starship |
| [2. パッケージマネージャー](#2-パッケージマネージャー) | Homebrew の活用・brew bundle |
| [3. エディタ・IDE](#3-エディタide) | VS Code・Cursor・CotEditor |
| [4. Git・GitHub](#4-gitgithub) | GitHub Desktop・GitKraken・gh CLI |
| [5. API・データベース](#5-apiデータベース) | Postman・Bruno・TablePlus・DB Browser |
| [6. ブラウザ・開発ツール](#6-ブラウザ開発ツール) | Chrome・Firefox・Arc |
| [7. ウィンドウ管理・生産性](#7-ウィンドウ管理生産性) | Rectangle・Raycast・Clipy・Karabiner |
| [8. ドキュメント・メモ](#8-ドキュメントメモ) | Notion・Obsidian・Markdown エディタ |
| [9. その他の便利ツール](#9-その他の便利ツール) | AppCleaner・The Unarchiver・Stats 他 |

---

## 1. ターミナル・シェル

Mac 標準の「ターミナル.app」でも十分だが、より快適な環境を構築できるツールがある。

### iTerm2 — 高機能ターミナル

| 項目 | 内容 |
|------|------|
| **用途** | Mac 標準ターミナルの上位互換。分割ペイン・検索・プロファイルなど機能が豊富 |
| **料金** | 無料 |
| **インストール** | `brew install --cask iterm2` |
| **Windows での代替** | Windows Terminal |

**主な機能:**

| 機能 | 説明 | ショートカット |
|------|------|-------------|
| 画面分割（水平） | ターミナルを上下に分割 | `Cmd + D` |
| 画面分割（垂直） | ターミナルを左右に分割 | `Cmd + Shift + D` |
| ペイン間移動 | 分割したペイン間を移動 | `Cmd + Option + 矢印` |
| 検索 | ターミナルの出力内を検索 | `Cmd + F` |
| ホットキーウィンドウ | 画面上部からスライド表示 | 設定でキーを割り当て |
| プロファイル | 配色・フォント・起動コマンドを保存 | 設定 → Profiles |

### Oh My Zsh — Zsh の設定フレームワーク

| 項目 | 内容 |
|------|------|
| **用途** | Zsh にテーマ・プラグイン・便利なエイリアスを追加 |
| **料金** | 無料 |
| **インストール** | 下記コマンドを実行 |
| **Windows での代替** | Oh My Posh |

```bash
# Oh My Zsh のインストール
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**便利なプラグイン:**

| プラグイン | 効果 | 有効化 |
|-----------|------|--------|
| `git` | Git コマンドの短縮エイリアス（`gst` = `git status`） | デフォルトで有効 |
| `zsh-autosuggestions` | 過去の入力履歴から補完候補を灰色で表示 | 別途インストール |
| `zsh-syntax-highlighting` | コマンドの構文をリアルタイムでハイライト | 別途インストール |

```bash
# プラグインのインストール例
brew install zsh-autosuggestions zsh-syntax-highlighting

# ~/.zshrc に追記（Oh My Zsh のプラグイン設定）
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

### Starship — クロスプラットフォーム対応プロンプト

| 項目 | 内容 |
|------|------|
| **用途** | ターミナルのプロンプト（入力行の表示）をカスタマイズ。Git ブランチ・言語バージョンなどを表示 |
| **料金** | 無料 |
| **インストール** | `brew install starship` |
| **Windows での代替** | Starship（同じツールが使える） |

```bash
# ~/.zshrc の末尾に追記
eval "$(starship init zsh)"
```

> **まとめ**: iTerm2 + Oh My Zsh + Starship の組み合わせが定番。
> 見た目も機能も大幅に向上するので、Mac セットアップ時の最初の一歩としておすすめ。

---

## 2. パッケージマネージャー

### Homebrew の活用

Homebrew のインストール自体は [09 - Mac 基礎操作ガイド](09-mac-basics-guide.md) を参照。ここでは日常的な活用方法を紹介する。

#### よく使うコマンド

| コマンド | 説明 |
|---------|------|
| `brew search キーワード` | パッケージを検索 |
| `brew info パッケージ名` | パッケージの詳細情報を表示 |
| `brew install パッケージ名` | CLI ツールをインストール |
| `brew install --cask アプリ名` | GUI アプリをインストール |
| `brew list` | インストール済み一覧 |
| `brew outdated` | 更新可能なパッケージを表示 |
| `brew upgrade` | すべてを最新に更新 |
| `brew upgrade パッケージ名` | 特定のパッケージだけ更新 |
| `brew uninstall パッケージ名` | アンインストール |
| `brew cleanup` | 古いバージョンを削除して容量を節約 |
| `brew doctor` | Homebrew 環境の問題を診断 |

#### `brew install` と `brew install --cask` の違い

| 種別 | コマンド | 対象 | 例 |
|------|---------|------|-----|
| Formula | `brew install` | CLI ツール・ライブラリ | `git`, `node`, `python` |
| Cask | `brew install --cask` | GUI アプリケーション | `visual-studio-code`, `google-chrome` |

### Brewfile — 一括インストール

`Brewfile` を作っておけば、新しい Mac でも一発で環境を再構築できる。

```ruby
# Brewfile の例
# CLI ツール
brew "git"
brew "node"
brew "python"
brew "starship"
brew "zsh-autosuggestions"
brew "zsh-syntax-highlighting"

# GUI アプリ
cask "iterm2"
cask "visual-studio-code"
cask "google-chrome"
cask "rectangle"
cask "raycast"
cask "notion"

# App Store アプリ（mas コマンドが必要）
# mas "Xcode", id: 497799835
```

```bash
# 現在のインストール済みパッケージから Brewfile を自動生成
brew bundle dump

# Brewfile からすべてインストール
brew bundle

# Brewfile にないパッケージを表示（整理に便利）
brew bundle cleanup
```

> **Windows との比較**: Windows には Homebrew のような標準的なパッケージマネージャーがない。
> `winget` や `chocolatey` が近いが、Mac の Homebrew ほど普及していない。
> Brewfile は Windows の「アプリ一覧をメモしておいて手動で入れ直す」を完全に自動化するもの。

---

## 3. エディタ・IDE

### VS Code — 定番コードエディタ

| 項目 | 内容 |
|------|------|
| **用途** | コードエディタの定番。拡張機能で何でもできる |
| **料金** | 無料 |
| **インストール** | `brew install --cask visual-studio-code` |
| **Windows での代替** | VS Code（同じアプリが使える） |

> 詳しくは [00 - VS Code 基本操作ガイド](00-vscode-guide.md) を参照。

### Cursor — AI 特化エディタ

| 項目 | 内容 |
|------|------|
| **用途** | VS Code ベースの AI コーディングエディタ。AI による補完・編集が強力 |
| **料金** | 無料プランあり（Pro: $20/月） |
| **インストール** | `brew install --cask cursor` |
| **Windows での代替** | Cursor（同じアプリが使える） |

**VS Code との違い:**

| 比較項目 | VS Code | Cursor |
|---------|---------|--------|
| AI 補完 | 拡張機能で追加 | 標準搭載（Tab で補完） |
| AI チャット | 拡張機能で追加 | 標準搭載（`Cmd + L`） |
| AI による編集 | 拡張機能で追加 | 標準搭載（`Cmd + K`） |
| 拡張機能 | 豊富 | VS Code の拡張機能がそのまま使える |
| 設定の移行 | — | VS Code の設定をインポート可能 |

### CotEditor — 軽量テキストエディタ

| 項目 | 内容 |
|------|------|
| **用途** | 軽量で高速な日本語対応テキストエディタ。設定ファイルの編集やログの閲覧に便利 |
| **料金** | 無料 |
| **インストール** | `brew install --cask coteditor` または App Store |
| **Windows での代替** | サクラエディタ・秀丸エディタ |

> CotEditor は日本製のエディタで、文字コード・改行コードの自動判別が優秀。
> コードを書くのは VS Code、ちょっとしたテキスト編集は CotEditor という使い分けがおすすめ。

---

## 4. Git・GitHub

Git のコマンドラインが苦手なうちは GUI クライアントを使うと直感的に操作できる。

### GitHub Desktop — GitHub 公式 GUI クライアント

| 項目 | 内容 |
|------|------|
| **用途** | Git 操作を GUI で行える。コミット・プッシュ・ブランチ切替がクリック操作で完結 |
| **料金** | 無料 |
| **インストール** | `brew install --cask github` |
| **Windows での代替** | GitHub Desktop（同じアプリが使える） |

**主な機能:**

| 機能 | 説明 |
|------|------|
| 変更の確認 | ファイルごとの差分をビジュアルで表示 |
| コミット | チェックボックスでファイルを選択 → メッセージ入力 → コミット |
| プッシュ / プル | ボタン 1 つで GitHub と同期 |
| ブランチ | GUI でブランチを作成・切替・マージ |
| コンフリクト解消 | マージコンフリクトをエディタで解消するガイド付き |

### GitKraken — 高機能 Git GUI クライアント

| 項目 | 内容 |
|------|------|
| **用途** | Git のブランチツリーをビジュアルで表示。複雑なブランチ構成も一目で把握 |
| **料金** | 無料プランあり（Pro: $4.95/月。公開リポジトリは無料） |
| **インストール** | `brew install --cask gitkraken` |
| **Windows での代替** | GitKraken（同じアプリが使える） |

### gh CLI — GitHub 公式コマンドラインツール

| 項目 | 内容 |
|------|------|
| **用途** | ターミナルから GitHub の操作（PR 作成・Issue 管理・リポジトリ作成）ができる |
| **料金** | 無料 |
| **インストール** | `brew install gh` |
| **Windows での代替** | gh CLI（同じツールが使える） |

```bash
# 初回認証
gh auth login

# よく使うコマンド
gh repo create          # リポジトリを作成
gh pr create            # プルリクエストを作成
gh pr list              # PR 一覧を表示
gh issue create         # Issue を作成
gh issue list           # Issue 一覧を表示
gh repo clone owner/repo  # リポジトリをクローン
```

> **使い分け**: Git 初心者は **GitHub Desktop** から始めるのがおすすめ。
> 慣れてきたらコマンドライン + `gh` CLI に移行すると効率が上がる。
> ブランチが複雑なプロジェクトでは **GitKraken** のビジュアル表示が役立つ。

---

## 5. API・データベース

### Postman — API 開発・テストツール

| 項目 | 内容 |
|------|------|
| **用途** | REST API のリクエスト送信・レスポンス確認・テスト。API 開発のデファクトスタンダード |
| **料金** | 無料プランあり（チーム向けは有料） |
| **インストール** | `brew install --cask postman` |
| **Windows での代替** | Postman（同じアプリが使える） |

**主な機能:**

| 機能 | 説明 |
|------|------|
| リクエスト送信 | GET / POST / PUT / DELETE などをGUIで構築・送信 |
| レスポンス表示 | JSON を整形表示・ヘッダー確認 |
| コレクション | リクエストをフォルダ分けして管理 |
| 環境変数 | 開発 / 本番で URL やトークンを切り替え |
| テスト | レスポンスの自動検証スクリプト |

### Bruno — 軽量 API クライアント（オープンソース）

| 項目 | 内容 |
|------|------|
| **用途** | Postman の軽量代替。ファイルベースで Git 管理しやすい |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask bruno` |
| **Windows での代替** | Bruno（同じアプリが使える） |

**Postman との違い:**

| 比較項目 | Postman | Bruno |
|---------|---------|-------|
| データ保存 | クラウド（アカウント必要） | ローカルファイル（Git 管理可能） |
| 動作速度 | やや重い | 軽量 |
| オフライン | 一部制限 | 完全対応 |
| 価格 | 無料プラン + 有料 | 完全無料 |

### TablePlus — データベース GUI クライアント

| 項目 | 内容 |
|------|------|
| **用途** | SQLite・PostgreSQL・MySQL など複数 DB をGUIで操作 |
| **料金** | 無料プランあり（制限付き。ライセンス: $89 買い切り） |
| **インストール** | `brew install --cask tableplus` |
| **Windows での代替** | HeidiSQL・DBeaver |

### DB Browser for SQLite — SQLite 専用 GUI

| 項目 | 内容 |
|------|------|
| **用途** | SQLite データベースの閲覧・編集に特化。学習用にも最適 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask db-browser-for-sqlite` |
| **Windows での代替** | DB Browser for SQLite（同じアプリが使える） |

> **使い分け**: SQLite だけなら **DB Browser for SQLite**（無料・シンプル）。
> 複数の DB を使うなら **TablePlus**（対応 DB が多く UI が洗練されている）。

---

## 6. ブラウザ・開発ツール

### Google Chrome — Web 開発の定番ブラウザ

| 項目 | 内容 |
|------|------|
| **用途** | Web 開発に必須の DevTools を搭載。拡張機能も豊富 |
| **料金** | 無料 |
| **インストール** | `brew install --cask google-chrome` |
| **Windows での代替** | Google Chrome（同じアプリが使える） |

**DevTools の主な機能（`Cmd + Option + I` で開く）:**

| タブ | 用途 |
|------|------|
| Elements | HTML / CSS の確認・リアルタイム編集 |
| Console | JavaScript の実行・エラー確認 |
| Network | 通信内容の確認・API レスポンスの検証 |
| Application | Cookie・LocalStorage・Service Worker |
| Performance | ページの描画パフォーマンス計測 |
| Lighthouse | パフォーマンス・アクセシビリティの自動監査 |

### Firefox — プライバシー重視のブラウザ

| 項目 | 内容 |
|------|------|
| **用途** | Chrome とは異なるレンダリングエンジン（Gecko）。クロスブラウザテストに必要 |
| **料金** | 無料 |
| **インストール** | `brew install --cask firefox` |
| **Windows での代替** | Firefox（同じアプリが使える） |

> Firefox の DevTools も優秀。特に CSS Grid / Flexbox のデバッグツールは Chrome より使いやすい場面もある。

### Arc — 新世代ブラウザ

| 項目 | 内容 |
|------|------|
| **用途** | タブ管理を根本から再設計したブラウザ。サイドバー型タブ・スペース機能で整理がしやすい |
| **料金** | 無料 |
| **インストール** | `brew install --cask arc` |
| **Windows での代替** | Arc（Windows 版あり） |

**特徴的な機能:**

| 機能 | 説明 |
|------|------|
| サイドバータブ | タブを左サイドバーに配置。ピン留めで常駐タブを管理 |
| スペース | 用途別のタブグループ（仕事・個人・プロジェクトなど） |
| Split View | 2 つのタブを左右に並べて表示 |
| Boost | Web サイトの見た目をカスタマイズ（CSS / JS の注入） |

> **おすすめの使い分け**: Web 開発の検証は **Chrome**（DevTools が業界標準）。
> 日常のブラウジングは **Arc**（タブ管理が快適）。
> クロスブラウザテストに **Firefox**。

---

## 7. ウィンドウ管理・生産性

Mac にはウィンドウのスナップ機能（Windows の `Win + 矢印`）が標準では弱いので、外部アプリで補う。

### Rectangle — ウィンドウ配置ツール

| 項目 | 内容 |
|------|------|
| **用途** | キーボードショートカットでウィンドウを画面の半分・1/3 などに配置 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask rectangle` |
| **Windows での代替** | Windows 標準のスナップ機能（`Win + 矢印`） |

**主なショートカット:**

| 操作 | ショートカット |
|------|-------------|
| 左半分 | `Ctrl + Option + ←` |
| 右半分 | `Ctrl + Option + →` |
| 上半分 | `Ctrl + Option + ↑` |
| 下半分 | `Ctrl + Option + ↓` |
| 最大化 | `Ctrl + Option + Return` |
| 左上 1/4 | `Ctrl + Option + U` |
| 中央に配置 | `Ctrl + Option + C` |
| 次のディスプレイへ移動 | `Ctrl + Option + Cmd + →` |

> **macOS Sequoia 以降**: macOS 15 Sequoia からはウィンドウタイリングが標準搭載された。
> ただし Rectangle のほうがショートカットが豊富で柔軟性が高い。

### Alfred / Raycast — ランチャー・生産性ツール

Mac 標準の Spotlight を大幅に強化するランチャーアプリ。

#### Raycast（おすすめ）

| 項目 | 内容 |
|------|------|
| **用途** | アプリ起動・計算・スニペット・ウィンドウ管理・クリップボード履歴など万能ランチャー |
| **料金** | 無料（Pro: $8/月。AI 機能など） |
| **インストール** | `brew install --cask raycast` |
| **Windows での代替** | PowerToys Run |

**主な機能:**

| 機能 | 説明 |
|------|------|
| アプリ起動 | Spotlight より高速なアプリ検索・起動 |
| スニペット | よく使うテキストをキーワードで展開 |
| クリップボード履歴 | コピー履歴を検索・貼り付け |
| ウィンドウ管理 | Rectangle 相当の機能が内蔵 |
| 計算機 | ランチャーから直接計算 |
| 拡張機能（Extensions） | GitHub・Jira・Notion など豊富な連携 |

> Raycast のウィンドウ管理機能を使えば Rectangle は不要になる場合もある。

#### Alfred

| 項目 | 内容 |
|------|------|
| **用途** | 老舗のランチャーアプリ。Workflow（自動化）が強力 |
| **料金** | 無料（Powerpack: £34 買い切り。Workflow 機能を解放） |
| **インストール** | `brew install --cask alfred` |
| **Windows での代替** | Keypirinha |

> **Alfred vs Raycast**: 新規ユーザーには **Raycast** がおすすめ（無料で機能が充実・UI がモダン）。
> Alfred は Workflow の資産がある既存ユーザー向け。

### Clipy — クリップボードマネージャー

| 項目 | 内容 |
|------|------|
| **用途** | クリップボードの履歴を保持し、過去にコピーしたテキストを再利用 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask clipy` |
| **Windows での代替** | Windows 標準のクリップボード履歴（`Win + V`） |

> **注意**: Raycast にもクリップボード履歴機能があるため、Raycast を使う場合は Clipy は不要。

### Karabiner-Elements — キーボードカスタマイズ

| 項目 | 内容 |
|------|------|
| **用途** | キーの割り当てを自由に変更。CapsLock を Ctrl にする、外部キーボードの配列変更など |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask karabiner-elements` |
| **Windows での代替** | AutoHotkey・PowerToys |

**よく使う設定例:**

| 変更内容 | 説明 |
|---------|------|
| CapsLock → Ctrl | ターミナル操作で Ctrl を多用するため |
| CapsLock → Cmd（単押し）/ Ctrl（長押し） | Complex Modifications で実現 |
| 英数 / かな → Cmd（押しながら）/ 英数・かな（単押し） | IME 切替とモディファイアを兼用 |
| 外部キーボードの Alt ↔ Cmd | Windows 用キーボードを Mac に合わせる |

```
設定手順:
1. Karabiner-Elements を起動
2. Simple Modifications タブ → キーの変更を追加
3. Complex Modifications タブ → Add rule → Import more rules from the Internet
4. 検索して好みのルールをインポート
```

---

## 8. ドキュメント・メモ

### Notion — オールインワンドキュメント

| 項目 | 内容 |
|------|------|
| **用途** | メモ・ドキュメント・タスク管理・データベースが一体化。個人〜チームまで対応 |
| **料金** | 無料プランあり（Plus: $10/月） |
| **インストール** | `brew install --cask notion` |
| **Windows での代替** | Notion（同じアプリが使える） |

**主な用途:**

| 用途 | 説明 |
|------|------|
| 技術メモ | コードブロック・テーブル対応のリッチなメモ |
| プロジェクト管理 | Kanban ボード・カレンダー・タイムライン |
| Wiki | チームの知識ベースを構築 |
| データベース | テーブル・リスト・ギャラリーなど多様なビュー |

### Obsidian — ローカルファースト Markdown メモ

| 項目 | 内容 |
|------|------|
| **用途** | ローカルの Markdown ファイルをベースにしたナレッジ管理。リンクでメモ同士をつなげる |
| **料金** | 個人利用は無料（Sync: $4/月、Publish: $8/月） |
| **インストール** | `brew install --cask obsidian` |
| **Windows での代替** | Obsidian（同じアプリが使える） |

**Notion との違い:**

| 比較項目 | Notion | Obsidian |
|---------|--------|----------|
| データ保存 | クラウド | ローカルファイル（`.md`） |
| オフライン | 制限あり | 完全対応 |
| 共同編集 | 対応 | 非対応（Publish でウェブ公開は可能） |
| カスタマイズ | テンプレート | プラグイン（コミュニティ製が豊富） |
| バックリンク | あり | **強力**（グラフビューでメモの関係を可視化） |
| Git 連携 | 困難 | 容易（ファイルベースなので `git` で管理可能） |

### Markdown エディタの選択肢

| アプリ | 特徴 | 料金 | インストール |
|-------|------|------|------------|
| **Typora** | WYSIWYG 型の Markdown エディタ。書きながらプレビュー | 有料（$14.99 買い切り） | `brew install --cask typora` |
| **MacDown** | 左右分割プレビューのシンプルなエディタ | 無料 | `brew install --cask macdown` |
| **Mark Text** | オープンソースの WYSIWYG Markdown エディタ | 無料 | `brew install --cask mark-text` |

> **おすすめ**: VS Code + Markdown Preview 拡張機能でも十分。
> Markdown に特化した体験がほしい場合は Typora（有料だがUI が美しい）や Mark Text（無料）を検討。

---

## 9. その他の便利ツール

日常的に使う小さいけれど便利なユーティリティアプリ。

### AppCleaner — アプリの完全削除

| 項目 | 内容 |
|------|------|
| **用途** | アプリをアンインストールする際に関連ファイル（設定・キャッシュ）もまとめて削除 |
| **料金** | 無料 |
| **インストール** | `brew install --cask appcleaner` |
| **Windows での代替** | Revo Uninstaller |

> Mac は Finder でアプリをゴミ箱に入れるだけではアンインストールが不完全。
> 設定ファイルやキャッシュが `~/Library` に残る。AppCleaner はこれらも検出して一括削除してくれる。

### The Unarchiver — 圧縮ファイル解凍

| 項目 | 内容 |
|------|------|
| **用途** | zip 以外の圧縮形式（rar・7z・tar.gz など）にも対応する解凍ツール |
| **料金** | 無料 |
| **インストール** | `brew install --cask the-unarchiver` または App Store |
| **Windows での代替** | 7-Zip |

### MonitorControl — 外部ディスプレイの輝度調整

| 項目 | 内容 |
|------|------|
| **用途** | 外部ディスプレイの輝度・音量を Mac のキーボードで調整 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask monitorcontrol` |
| **Windows での代替** | Monitorian |

> 外部ディスプレイを使う場合は必須。Mac 標準ではキーボードの輝度キーが外部ディスプレイに効かないが、MonitorControl を入れれば内蔵ディスプレイと同じ感覚で操作できる。

### Stats — システムモニタ

| 項目 | 内容 |
|------|------|
| **用途** | メニューバーに CPU・メモリ・ディスク・ネットワーク・バッテリーの使用状況を表示 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask stats` |
| **Windows での代替** | タスクマネージャー（標準機能） |

**表示できる情報:**

| モジュール | 表示内容 |
|-----------|---------|
| CPU | 使用率・温度 |
| メモリ | 使用量・圧縮量 |
| ディスク | 読み書き速度・使用量 |
| ネットワーク | アップロード / ダウンロード速度 |
| バッテリー | 残量・充電サイクル・温度 |

### Hidden Bar — メニューバー整理

| 項目 | 内容 |
|------|------|
| **用途** | メニューバーのアイコンを折りたたんで整理。普段使わないアイコンを隠す |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask hiddenbar` または App Store |
| **Windows での代替** | Windows 標準の通知領域の管理 |

> Stats・MonitorControl などを入れるとメニューバーがアイコンだらけになる。
> Hidden Bar で普段見ないアイコンを隠しておくと見た目がすっきりする。

---

## まとめ — おすすめセットアップ手順

新しい Mac のセットアップは以下の順序がおすすめ。

### ステップ 1: 基盤ツール

```bash
# Homebrew をインストール（09 参照）後、基盤ツールを導入
brew install --cask iterm2
brew install starship zsh-autosuggestions zsh-syntax-highlighting
```

### ステップ 2: 開発ツール

```bash
brew install --cask visual-studio-code
brew install --cask google-chrome
brew install gh
brew install --cask github
```

### ステップ 3: 生産性ツール

```bash
brew install --cask rectangle
brew install --cask raycast
brew install --cask karabiner-elements
```

### ステップ 4: ユーティリティ

```bash
brew install --cask appcleaner
brew install --cask the-unarchiver
brew install --cask stats
brew install --cask hiddenbar
```

### ステップ 5: 必要に応じて追加

```bash
# API 開発をするなら
brew install --cask postman       # または bruno

# データベースを扱うなら
brew install --cask tableplus     # または db-browser-for-sqlite

# ドキュメント管理
brew install --cask notion        # または obsidian

# 外部ディスプレイを使うなら
brew install --cask monitorcontrol
```

### 一括インストール（Brewfile）

上記すべてを `Brewfile` にまとめておけば、`brew bundle` の一発で環境構築が完了する。

```bash
# Brewfile を作成して一括インストール
brew bundle
```

> **ポイント**: すべてを一度に入れる必要はない。
> まずステップ 1〜3 を入れて、必要になったタイミングで追加していくのがおすすめ。
