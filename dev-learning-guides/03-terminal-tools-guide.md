# ターミナル CLI ツールガイド

## 0. はじめに

このガイドは **ターミナルで使うモダンな CLI ツールをまとめた自分用リファレンス** です。

- **想定読者**: プログラミング初心者。ターミナルの基本操作は覚えた。標準コマンドの代替やもっと便利なツールを導入したい
- **ゴール**: モダンな CLI ツールを知り、日常の開発作業を効率化できるようになる
- **前提**: [10 - Claude Code 基本操作ガイド](10-claude-code-guide.md) のターミナル基礎を理解していること
- **関連ガイド**: [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md)

> **02 との棲み分け**: [02](02-mac-apps-guide.md) は **GUI アプリ**（iTerm2・VS Code・Rectangle など）を中心に紹介した。
> このガイドでは **ターミナルの中で使う CLI ツール**（コマンドの代替・開発支援）に特化する。
> 02 でカバー済みの iTerm2・Oh My Zsh・Starship・Homebrew・gh CLI とは重複しない。

> すべて **無料・オープンソース** のツールを紹介する。
> インストールは `brew install` を中心に記載。Homebrew の基本は [01](01-mac-basics-guide.md) を参照。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. モダンなコマンド代替](#1-モダンなコマンド代替) | eza・bat・fd・ripgrep・sd・dust・duf・delta |
| [2. ファイル操作・検索](#2-ファイル操作検索) | fzf・tree・zoxide・trash-cli |
| [3. JSON・データ処理](#3-jsonデータ処理) | jq・yq・fx |
| [4. ネットワーク・HTTP](#4-ネットワークhttp) | curl・wget・httpie・xh |
| [5. プロセス・システム監視](#5-プロセスシステム監視) | htop・btop・procs・watch |
| [6. バージョン管理（言語）](#6-バージョン管理言語) | mise・nvm・fnm・pyenv |
| [7. Git 拡張](#7-git-拡張) | lazygit・tig・git-delta |
| [8. Docker・コンテナ](#8-dockerコンテナ) | Docker Desktop・lazydocker・dive |
| [9. その他の便利ツール](#9-その他の便利ツール) | tldr・thefuck・neofetch・tokei・hyperfine |

---

## 1. モダンなコマンド代替

Unix の標準コマンドには歴史があるが、出力が見づらかったり機能が限定的だったりする。
ここでは **標準コマンドの上位互換** となるモダンなツールを紹介する。

### 標準コマンド vs モダン代替 — 一覧

| 標準コマンド | モダン代替 | 主な改善点 |
|------------|-----------|-----------|
| `ls` | **eza** | カラー表示・Git ステータス・アイコン |
| `cat` | **bat** | シンタックスハイライト・行番号・Git 差分 |
| `find` | **fd** | 直感的な構文・高速・`.gitignore` 対応 |
| `grep` | **ripgrep (rg)** | 超高速・`.gitignore` 対応・再帰検索がデフォルト |
| `sed` | **sd** | 直感的な構文（正規表現がそのまま使える） |
| `du` | **dust** | ビジュアルなディスク使用量表示 |
| `df` | **duf** | テーブル形式のディスク情報表示 |
| `diff` | **delta** | シンタックスハイライト付き差分表示 |

### eza — `ls` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ファイル一覧を見やすく表示。カラー・アイコン・Git ステータス対応 |
| **インストール** | `brew install eza` |
| **Windows での代替** | eza（同じツールが使える） |

```bash
# 基本的な使い方
eza                     # ls と同じ（カラー付き）
eza -l                  # 詳細表示（ls -l の代替）
eza -la                 # 隠しファイルも含めた詳細表示
eza -T                  # ツリー表示（tree の代わりにも使える）
eza -l --git            # Git ステータスを表示
eza --icons             # ファイルタイプに応じたアイコンを表示

# エイリアスの設定（~/.zshrc に追記）
alias ls="eza"
alias ll="eza -l --git --icons"
alias la="eza -la --git --icons"
alias lt="eza -T --icons"
```

**標準 `ls` との比較:**

| 機能 | `ls` | `eza` |
|------|------|-------|
| カラー表示 | `-G` で有効化 | デフォルトで有効 |
| Git ステータス | 非対応 | `--git` で表示 |
| ツリー表示 | 非対応（`tree` が別途必要） | `-T` で対応 |
| アイコン | 非対応 | `--icons` で表示 |
| ヘッダー行 | 非対応 | `-h` で列名を表示 |

### bat — `cat` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ファイル内容をシンタックスハイライト・行番号付きで表示 |
| **インストール** | `brew install bat` |
| **Windows での代替** | bat（同じツールが使える） |

```bash
# 基本的な使い方
bat README.md           # シンタックスハイライト + 行番号で表示
bat -n README.md        # 行番号のみ（枠線なし）
bat -p README.md        # プレーン表示（パイプ向き）
bat -l python script    # 言語を指定してハイライト
bat --diff file1 file2  # 2 ファイルの差分を表示

# 複数ファイルの結合表示
bat header.md content.md footer.md

# エイリアスの設定（~/.zshrc に追記）
alias cat="bat"
```

**標準 `cat` との比較:**

| 機能 | `cat` | `bat` |
|------|-------|-------|
| シンタックスハイライト | なし | 自動検出 |
| 行番号 | なし（`cat -n`） | デフォルトで表示 |
| Git 差分マーク | なし | 変更行にマーク |
| ページャー | なし（全文出力） | 長いファイルは自動ページング |
| テーマ | なし | 多数のテーマから選択可能 |

### fd — `find` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ファイル・ディレクトリの検索。`find` より直感的で高速 |
| **インストール** | `brew install fd` |
| **Windows での代替** | fd（同じツールが使える） |

```bash
# 基本的な使い方
fd pattern              # カレントディレクトリ以下を再帰検索
fd pattern /path        # 指定ディレクトリ以下を検索
fd -e py                # .py ファイルだけを検索
fd -e py -x wc -l       # 見つかったファイルに対してコマンドを実行
fd -H pattern           # 隠しファイルも含めて検索
fd -t f pattern         # ファイルのみ（-t d でディレクトリのみ）
fd -s pattern           # 大文字小文字を区別して検索
```

**標準 `find` との比較:**

| 操作 | `find` | `fd` |
|------|--------|------|
| `.py` ファイルを探す | `find . -name "*.py"` | `fd -e py` |
| 名前にパターンを含むファイル | `find . -name "*test*"` | `fd test` |
| `.gitignore` の尊重 | 非対応 | デフォルトで対応 |
| カラー出力 | なし | デフォルトで有効 |
| 速度 | 遅い | **高速**（並列検索） |

### ripgrep (rg) — `grep` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ファイル内容のテキスト検索。超高速で大規模プロジェクトでも快適 |
| **インストール** | `brew install ripgrep` |
| **Windows での代替** | ripgrep（同じツールが使える） |

```bash
# 基本的な使い方
rg "pattern"            # カレントディレクトリ以下を再帰検索
rg "pattern" src/       # 指定ディレクトリ以下を検索
rg -i "pattern"         # 大文字小文字を無視
rg -w "word"            # 単語単位でマッチ
rg -t py "import"       # .py ファイルのみ検索
rg -l "pattern"         # マッチしたファイル名のみ表示
rg -c "pattern"         # ファイルごとのマッチ数を表示
rg -C 3 "pattern"       # マッチの前後 3 行も表示
rg --replace "new" "old"  # 置換プレビュー（ファイルは変更しない）
```

**標準 `grep` との比較:**

| 機能 | `grep` | `ripgrep` |
|------|--------|-----------|
| 再帰検索 | `-r` オプションが必要 | デフォルト |
| `.gitignore` の尊重 | 非対応 | デフォルトで対応 |
| カラー出力 | `--color` が必要 | デフォルト |
| 速度 | 普通 | **非常に高速** |
| バイナリファイル | 検索してしまう | 自動スキップ |

### sd — `sed` の代替

| 項目 | 内容 |
|------|------|
| **用途** | テキストの検索・置換。`sed` より直感的な構文 |
| **インストール** | `brew install sd` |
| **Windows での代替** | sd（同じツールが使える） |

```bash
# 基本的な使い方
echo "hello world" | sd "world" "Rust"      # パイプで使用
sd "old" "new" file.txt                      # ファイル内を置換（ファイルを直接変更）
sd "foo(\d+)" 'bar$1' file.txt              # 正規表現でキャプチャグループ

# sed との構文比較
# sed: sed -i '' 's/old/new/g' file.txt     # Mac の sed はオプションが独特
# sd:  sd "old" "new" file.txt              # シンプル
```

**標準 `sed` との比較:**

| 比較項目 | `sed` | `sd` |
|---------|-------|------|
| 構文 | `s/old/new/g`（デリミタが必要） | `"old" "new"`（直感的） |
| 正規表現 | 基本正規表現（`-E` で拡張） | デフォルトで最新の正規表現 |
| Mac / Linux 差異 | `-i` オプションの挙動が異なる | 差異なし |

### dust — `du` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ディスク使用量をビジュアルに表示。どのフォルダが容量を使っているか一目でわかる |
| **インストール** | `brew install dust` |
| **Windows での代替** | dust（同じツールが使える） |

```bash
# 基本的な使い方
dust                    # カレントディレクトリの使用量を棒グラフで表示
dust -n 10              # 上位 10 件のみ表示
dust -d 2               # 深さ 2 階層まで表示
dust /path              # 指定ディレクトリを表示
dust -r                 # 逆順（小さい順）で表示
```

### duf — `df` の代替

| 項目 | 内容 |
|------|------|
| **用途** | ディスクの空き容量・マウントポイントをテーブル形式で見やすく表示 |
| **インストール** | `brew install duf` |
| **Windows での代替** | duf（同じツールが使える） |

```bash
# 基本的な使い方
duf                     # 全マウントポイントを表示
duf /                   # 特定のパスのみ表示
duf --only local        # ローカルディスクのみ
```

### delta — `diff` の代替

| 項目 | 内容 |
|------|------|
| **用途** | シンタックスハイライト付きの差分表示。Git の diff 出力を見やすくする |
| **インストール** | `brew install git-delta` |
| **Windows での代替** | delta（同じツールが使える） |

```bash
# Git と連携（~/.gitconfig に追記）
[core]
    pager = delta

[interactive]
    diffFilter = delta --color-only

[delta]
    navigate = true
    side-by-side = true    # 左右比較表示（好みで）
    line-numbers = true

[merge]
    conflictstyle = diff3

[diff]
    colorMoved = default
```

```bash
# 単体でも使用可能
delta file1 file2       # 2 ファイルの差分を表示
```

> **まとめ**: まずは **eza**（ls）・**bat**（cat）・**fd**（find）・**ripgrep**（grep）の 4 つを導入するのがおすすめ。
> 日常的に最もよく使うコマンドの体験が劇的に向上する。

---

## 2. ファイル操作・検索

ファイルの移動・検索をもっと賢くするツール。

### fzf — あいまい検索（ファジーファインダー）

| 項目 | 内容 |
|------|------|
| **用途** | あらゆるリスト（ファイル・履歴・プロセスなど）をインタラクティブに絞り込み検索 |
| **インストール** | `brew install fzf` |
| **Windows での代替** | fzf（同じツールが使える） |

```bash
# インストール後のセットアップ（キーバインドと補完を有効化）
$(brew --prefix)/opt/fzf/install

# 基本的な使い方
fzf                     # カレントディレクトリ以下のファイルを検索
vim $(fzf)              # 検索結果のファイルを vim で開く
cat $(fzf)              # 検索結果のファイルの内容を表示

# パイプと組み合わせ
history | fzf            # コマンド履歴から検索
ps aux | fzf             # プロセスリストから検索
brew list | fzf          # インストール済みパッケージから検索
```

**有効化されるキーバインド:**

| キーバインド | 機能 |
|------------|------|
| `Ctrl + T` | ファイルを検索して入力に挿入 |
| `Ctrl + R` | コマンド履歴をあいまい検索 |
| `Option + C` | ディレクトリを検索して `cd` |

**他のツールとの連携:**

```bash
# fd と組み合わせ（fzf のデフォルト検索に fd を使う）
# ~/.zshrc に追記
export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"

# bat でプレビュー付き検索
fzf --preview "bat --color=always {}"

# ripgrep + fzf で内容検索
rg --line-number "" | fzf --delimiter : --preview 'bat --color=always --highlight-line {2} {1}'
```

> **fzf は「接着剤」**: 単体でも便利だが、他のツール（fd・bat・ripgrep）と組み合わせると真価を発揮する。

### tree — ディレクトリ構造の表示

| 項目 | 内容 |
|------|------|
| **用途** | ディレクトリ構造をツリー形式で表示 |
| **インストール** | `brew install tree` |
| **Windows での代替** | `tree` コマンド（標準搭載だが機能が限定的） |

```bash
# 基本的な使い方
tree                    # カレントディレクトリのツリーを表示
tree -L 2               # 深さ 2 階層まで表示
tree -a                 # 隠しファイルも表示
tree -d                 # ディレクトリのみ表示
tree -I "node_modules|.git"  # 除外パターンを指定
tree --gitignore        # .gitignore のルールに従う
```

> **Tips**: `eza -T` でもツリー表示ができる。eza を導入済みなら tree は不要な場合もある。

### zoxide — `cd` の代替（スマートディレクトリ移動）

| 項目 | 内容 |
|------|------|
| **用途** | 過去に訪れたディレクトリを学習し、部分的なキーワードでジャンプ |
| **インストール** | `brew install zoxide` |
| **Windows での代替** | zoxide（同じツールが使える） |

```bash
# セットアップ（~/.zshrc に追記）
eval "$(zoxide init zsh)"

# 基本的な使い方（z コマンドとして使う）
z projects              # ~/Documents/projects にジャンプ（過去の履歴から推測）
z ai-agent              # ~/ai-agent にジャンプ
zi                      # fzf を使ったインタラクティブ選択

# 使い方のイメージ
# 初回: cd ~/Documents/my-long-project-name
# 2回目以降: z my-long  ← これだけでジャンプ
```

**標準 `cd` との比較:**

| 操作 | `cd` | `zoxide (z)` |
|------|------|-------------|
| フルパス移動 | `cd ~/Documents/projects/ai-agent` | `z ai-agent` |
| 学習機能 | なし | 頻度と最終訪問時刻を学習 |
| あいまい検索 | 非対応 | 部分一致でジャンプ |

### trash-cli — 安全なファイル削除

| 項目 | 内容 |
|------|------|
| **用途** | `rm` の代わりにファイルをゴミ箱に移動。誤削除を防ぐ |
| **インストール** | `brew install trash-cli` |
| **Windows での代替** | `recycle-bin`（npm パッケージ） |

```bash
# 基本的な使い方
trash file.txt          # ファイルをゴミ箱に移動
trash *.log             # パターンで複数ファイルをゴミ箱に移動
trash dir/              # ディレクトリをゴミ箱に移動

# エイリアスの設定（~/.zshrc に追記）
alias rm="trash"        # rm をゴミ箱送りに置き換え（好みで）
```

> **`rm` vs `trash`**: `rm` は即座に削除して復元不可。`trash` ならゴミ箱から取り出せるので安全。
> 特に `rm -rf` の事故防止に有効。

---

## 3. JSON・データ処理

API のレスポンスや設定ファイルなど、JSON / YAML を扱う場面は多い。

### jq — JSON プロセッサ

| 項目 | 内容 |
|------|------|
| **用途** | コマンドラインで JSON を整形・フィルタ・変換。API 開発に必須 |
| **インストール** | `brew install jq` |
| **Windows での代替** | jq（同じツールが使える） |

```bash
# 基本的な使い方
echo '{"name":"Alice","age":30}' | jq .          # 整形表示
echo '{"name":"Alice","age":30}' | jq .name       # 特定のキーを抽出 → "Alice"
echo '{"name":"Alice","age":30}' | jq -r .name    # 生の値（引用符なし）→ Alice

# 配列の操作
echo '[1,2,3,4,5]' | jq '.[]'                     # 各要素を展開
echo '[1,2,3,4,5]' | jq 'map(. * 2)'              # 各要素を 2 倍 → [2,4,6,8,10]
echo '[1,2,3,4,5]' | jq '[.[] | select(. > 3)]'   # 3 より大きい要素 → [4,5]

# API レスポンスの加工例
curl -s https://api.example.com/users | jq '.[] | {name: .name, email: .email}'

# ファイルの加工
jq '.dependencies | keys' package.json            # package.json の依存パッケージ一覧
```

**よく使うフィルタ:**

| フィルタ | 説明 | 例 |
|---------|------|-----|
| `.key` | キーの値を取得 | `.name` → Alice |
| `.[]` | 配列の各要素を展開 | `[1,2,3]` → 1, 2, 3 |
| `.[0]` | 配列のインデックス指定 | `.[0]` → 最初の要素 |
| `\| ` | パイプ（次のフィルタに渡す） | `.users[] \| .name` |
| `select()` | 条件でフィルタ | `select(.age > 20)` |
| `length` | 長さを取得 | `.users \| length` |
| `keys` | オブジェクトのキー一覧 | `. \| keys` |
| `map()` | 配列の各要素を変換 | `map(. + 1)` |

### yq — YAML プロセッサ

| 項目 | 内容 |
|------|------|
| **用途** | jq と同様の構文で YAML を操作。Docker Compose や CI/CD 設定の編集に便利 |
| **インストール** | `brew install yq` |
| **Windows での代替** | yq（同じツールが使える） |

```bash
# 基本的な使い方
yq '.services' docker-compose.yml               # 特定のキーを取得
yq '.services | keys' docker-compose.yml         # サービス名の一覧
yq -i '.version = "3.9"' docker-compose.yml      # YAML ファイルを直接編集
yq -o json docker-compose.yml                    # YAML → JSON 変換
yq -P config.json                                # JSON → YAML 変換
```

### fx — インタラクティブ JSON ビューア

| 項目 | 内容 |
|------|------|
| **用途** | JSON をインタラクティブに展開・折りたたみ・検索。大きな JSON の探索に最適 |
| **インストール** | `brew install fx` |
| **Windows での代替** | fx（同じツールが使える） |

```bash
# 基本的な使い方
cat data.json | fx       # インタラクティブモードで開く
curl -s api_url | fx     # API レスポンスをそのまま閲覧

# インタラクティブモードの操作
# e / E     — 展開 / 折りたたみ
# / + 入力  — 検索
# q         — 終了
```

> **使い分け**: JSON を加工・変換するなら **jq**。大きな JSON を目で追って探索するなら **fx**。

---

## 4. ネットワーク・HTTP

API のテストやファイルのダウンロードに使うネットワーク系ツール。

### curl — HTTP リクエスト（標準搭載）

| 項目 | 内容 |
|------|------|
| **用途** | コマンドラインから HTTP リクエストを送信。Mac に標準搭載 |
| **インストール** | 標準搭載（最新版: `brew install curl`） |
| **Windows での代替** | curl（Windows 10 以降は標準搭載） |

```bash
# 基本的な使い方
curl https://example.com                              # GET リクエスト
curl -o file.zip https://example.com/file.zip         # ファイルをダウンロード
curl -X POST -H "Content-Type: application/json" \
     -d '{"key":"value"}' https://api.example.com     # POST リクエスト
curl -s https://api.example.com | jq .                # サイレント + jq で整形
curl -I https://example.com                           # ヘッダーのみ取得
curl -v https://example.com                           # 詳細なデバッグ情報
```

### wget — ファイルダウンロード

| 項目 | 内容 |
|------|------|
| **用途** | ファイルのダウンロードに特化。再帰ダウンロードやリジューム対応 |
| **インストール** | `brew install wget` |
| **Windows での代替** | wget（Windows 版あり） |

```bash
# 基本的な使い方
wget https://example.com/file.zip                     # ファイルをダウンロード
wget -c https://example.com/large-file.zip            # 中断したダウンロードの再開
wget -r -l 2 https://example.com                      # 再帰的にダウンロード（深さ 2）
wget -i urls.txt                                       # URL リストから一括ダウンロード
```

> **curl vs wget**: API のテストには **curl**。ファイルのダウンロードには **wget** が向いている。

### HTTPie (http) — 人間に優しい HTTP クライアント

| 項目 | 内容 |
|------|------|
| **用途** | curl より直感的な構文で HTTP リクエストを送信。レスポンスが自動で整形・カラー表示 |
| **インストール** | `brew install httpie` |
| **Windows での代替** | HTTPie（同じツールが使える） |

```bash
# 基本的な使い方
http GET https://api.example.com/users                # GET リクエスト
http POST https://api.example.com/users name=Alice    # POST（JSON 自動送信）
http PUT https://api.example.com/users/1 age:=30      # := で数値を指定
http -d GET https://api.example.com                   # ダウンロードモード
http -a user:pass https://api.example.com             # Basic 認証

# curl との構文比較
# curl: curl -X POST -H "Content-Type: application/json" -d '{"name":"Alice"}' URL
# http: http POST URL name=Alice
```

### xh — HTTPie 互換の高速 HTTP クライアント

| 項目 | 内容 |
|------|------|
| **用途** | HTTPie と同じ構文で、Rust 製のため起動が高速 |
| **インストール** | `brew install xh` |
| **Windows での代替** | xh（同じツールが使える） |

```bash
# HTTPie と同じ構文で使える
xh GET https://api.example.com/users
xh POST https://api.example.com/users name=Alice
```

> **使い分け**: 普段使いは **xh**（高速起動）。HTTPie のプラグインが必要な場合は **HTTPie**。
> curl は最も汎用的で、スクリプトやドキュメントでよく使われるため覚えておくと便利。

---

## 5. プロセス・システム監視

システムの状態やプロセスを監視するツール。

### htop — `top` の代替

| 項目 | 内容 |
|------|------|
| **用途** | プロセス一覧・CPU / メモリ使用率をインタラクティブに表示。`top` の上位互換 |
| **インストール** | `brew install htop` |
| **Windows での代替** | Process Explorer（Sysinternals） |

```bash
# 基本的な使い方
htop                    # インタラクティブモードで起動

# 操作キー
# F5         — ツリー表示
# F6         — ソート項目を変更
# F9         — プロセスを kill
# /          — プロセス名で検索
# q          — 終了
```

### btop — さらに高機能なシステムモニタ

| 項目 | 内容 |
|------|------|
| **用途** | CPU・メモリ・ディスク・ネットワークを美しいUIで一括監視。htop のさらに上位互換 |
| **インストール** | `brew install btop` |
| **Windows での代替** | btop（Windows 版あり） |

```bash
btop                    # 起動（マウス操作も可能）
```

**htop vs btop:**

| 比較項目 | htop | btop |
|---------|------|------|
| CPU / メモリ | グラフ表示 | より詳細なグラフ |
| ネットワーク | 非対応 | リアルタイム表示 |
| ディスク I/O | 非対応 | リアルタイム表示 |
| テーマ | 限定的 | 複数テーマ対応 |
| マウス操作 | 非対応 | 対応 |

### procs — `ps` の代替

| 項目 | 内容 |
|------|------|
| **用途** | プロセス一覧をカラー表示・キーワードハイライトで見やすくする |
| **インストール** | `brew install procs` |
| **Windows での代替** | procs（同じツールが使える） |

```bash
# 基本的な使い方
procs                   # 全プロセスを表示
procs node              # "node" を含むプロセスのみ
procs --sortd cpu       # CPU 使用率順にソート
procs --tree            # ツリー表示
```

### watch — コマンドの定期実行

| 項目 | 内容 |
|------|------|
| **用途** | 指定したコマンドを定期的に実行し、結果の変化を監視 |
| **インストール** | `brew install watch` |
| **Windows での代替** | `watch`（Git Bash に同梱） |

```bash
# 基本的な使い方
watch -n 2 "ls -la"                # 2 秒ごとに ls -la を実行
watch -n 5 "docker ps"             # 5 秒ごとにコンテナ状態を確認
watch -d "date"                    # 変更部分をハイライト
watch -n 1 "curl -s localhost:3000/health"  # ヘルスチェックの監視
```

---

## 6. バージョン管理（言語）

プロジェクトごとに異なるバージョンの言語ランタイムを使い分けるためのツール。

### mise — 統一バージョン管理ツール（asdf 後継）

| 項目 | 内容 |
|------|------|
| **用途** | Node.js・Python・Ruby・Go など複数言語のバージョンを一元管理。asdf の高速な後継 |
| **インストール** | `brew install mise` |
| **Windows での代替** | mise（Windows 版あり） |

```bash
# セットアップ（~/.zshrc に追記）
eval "$(mise activate zsh)"

# 基本的な使い方
mise use node@22         # Node.js 22 LTS を使用
mise use python@3.13     # Python 3.13 を使用
mise install node@22     # Node.js 22 をインストール
mise ls                  # インストール済みバージョン一覧
mise current             # 現在使用中のバージョン

# プロジェクトごとの設定（.mise.toml）
mise use --path node@20  # カレントディレクトリに .mise.toml を作成
```

**.mise.toml の例:**

```toml
[tools]
node = "20"
python = "3.13"
```

> **なぜ mise?**: 以前は asdf が定番だったが、mise は Rust 製で高速・設定がシンプル・エラーメッセージがわかりやすい。
> asdf のプラグインとも互換性がある。

### nvm / fnm — Node.js バージョン管理

Node.js だけを管理するなら専用ツールもある。

#### fnm（おすすめ）

| 項目 | 内容 |
|------|------|
| **用途** | Node.js のバージョン管理。nvm より高速（Rust 製） |
| **インストール** | `brew install fnm` |
| **Windows での代替** | fnm（同じツールが使える） |

```bash
# セットアップ（~/.zshrc に追記）
eval "$(fnm env --use-on-cd)"

# 基本的な使い方
fnm install 22          # Node.js 22 LTS をインストール
fnm use 22              # Node.js 22 LTS に切り替え
fnm default 22          # デフォルトバージョンを設定
fnm list                # インストール済み一覧
fnm list-remote         # インストール可能なバージョン一覧
```

#### nvm

| 項目 | 内容 |
|------|------|
| **用途** | Node.js バージョン管理の定番。ドキュメントや記事で最も多く参照される |
| **インストール** | `brew install nvm` |
| **Windows での代替** | nvm-windows |

```bash
# セットアップ（~/.zshrc に追記）
export NVM_DIR="$HOME/.nvm"
[ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && \. "$(brew --prefix)/opt/nvm/nvm.sh"

# 基本的な使い方
nvm install 22          # Node.js 22 LTS をインストール
nvm use 22              # Node.js 22 LTS に切り替え
nvm alias default 22    # デフォルトバージョンを設定
nvm ls                  # インストール済み一覧
```

> **nvm vs fnm**: 新規ユーザーには **fnm** がおすすめ（高速・セットアップが簡単）。
> nvm は歴史が長く情報が多いが、シェル起動が遅くなる欠点がある。
> 複数言語を管理するなら **mise** が最も効率的。

### pyenv — Python バージョン管理

| 項目 | 内容 |
|------|------|
| **用途** | 複数バージョンの Python をインストール・切り替え |
| **インストール** | `brew install pyenv` |
| **Windows での代替** | pyenv-win |

```bash
# セットアップ（~/.zshrc に追記）
eval "$(pyenv init -)"

# 基本的な使い方
pyenv install 3.13.0    # Python 3.13.0 をインストール
pyenv global 3.13.0     # グローバルバージョンを設定
pyenv local 3.12.0      # カレントディレクトリのバージョンを設定（.python-version 作成）
pyenv versions          # インストール済み一覧
pyenv install --list    # インストール可能なバージョン一覧
```

---

## 7. Git 拡張

Git の操作をもっと便利にするツール。gh CLI については [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md) を参照。

### lazygit — ターミナル Git UI

| 項目 | 内容 |
|------|------|
| **用途** | ターミナル内で Git をビジュアルに操作。ステージング・コミット・ブランチ操作がキーボードだけで完結 |
| **インストール** | `brew install lazygit` |
| **Windows での代替** | lazygit（同じツールが使える） |

```bash
# 基本的な使い方
lazygit                 # Git リポジトリ内で起動

# 主要な操作キー
# スペース    — ファイルのステージ / アンステージ
# c          — コミット
# p / P      — プッシュ / プル
# b          — ブランチ一覧
# [/]        — タブ切り替え（ステータス・ファイル・ブランチ・コミット・スタッシュ）
# ?          — ヘルプ
# q          — 終了
```

**主な機能:**

| 機能 | 説明 |
|------|------|
| ステージング | ファイル単位・行単位でステージ / アンステージ |
| コミット | メッセージ入力 → コミットがワンフロー |
| ブランチ | 作成・切替・マージ・リベースをキーボード操作 |
| インタラクティブリベース | コミット順の入れ替え・squash・edit |
| stash | stash の保存・適用・削除 |
| 差分表示 | ファイルの変更内容をリアルタイムプレビュー |

### tig — Git ログビューア

| 項目 | 内容 |
|------|------|
| **用途** | Git のログ・差分・blame をターミナルで閲覧。読み取り専用の Git ブラウザ |
| **インストール** | `brew install tig` |
| **Windows での代替** | tig（同じツールが使える） |

```bash
# 基本的な使い方
tig                     # コミットログを表示
tig blame file.py       # ファイルの各行が誰によって変更されたかを表示
tig log --oneline       # 1 行ログ表示
tig refs                # ブランチ・タグの一覧
tig stash               # stash の一覧

# 操作キー
# Enter      — コミットの詳細を表示
# j/k        — 上下移動
# q          — 戻る / 終了
```

> **lazygit vs tig**: Git 操作（コミット・ブランチ管理）を TUI でやりたいなら **lazygit**。
> ログや blame を快適に閲覧したいなら **tig**。両方入れておくと便利。

### git-delta（再掲）

セクション 1 で紹介した **delta** は Git の diff 出力を見やすくするツール。
`~/.gitconfig` に設定するだけで `git diff` / `git log -p` / `git show` の出力が劇的に改善される。
設定方法は [セクション 1 の delta](#delta--diff-の代替) を参照。

---

## 8. Docker・コンテナ

コンテナ技術を使った開発環境の構築に使うツール。

### Docker Desktop — Docker のGUIツール

| 項目 | 内容 |
|------|------|
| **用途** | Docker エンジン + GUI 管理ツール。コンテナ・イメージ・ボリュームをビジュアルに管理 |
| **インストール** | `brew install --cask docker` |
| **Windows での代替** | Docker Desktop（同じアプリが使える） |

```bash
# Docker CLI の基本コマンド
docker run -it ubuntu bash          # Ubuntu コンテナを起動
docker ps                            # 実行中のコンテナ一覧
docker images                        # イメージ一覧
docker compose up -d                 # docker-compose.yml からサービス起動
docker compose down                  # サービスを停止・削除
docker build -t myapp .              # Dockerfile からイメージをビルド
```

> **注意**: Docker Desktop は個人利用は無料。従業員 250 人以上 or 年間収益 $10M 以上の企業は有料。
> 代替として **OrbStack**（Mac 専用・軽量）や **Colima**（無料・CLI ベース）がある。

### lazydocker — ターミナル Docker UI

| 項目 | 内容 |
|------|------|
| **用途** | ターミナル内で Docker をビジュアルに管理。コンテナ・イメージ・ログの確認が簡単 |
| **インストール** | `brew install lazydocker` |
| **Windows での代替** | lazydocker（同じツールが使える） |

```bash
# 基本的な使い方
lazydocker              # 起動

# 画面構成
# 左パネル: コンテナ・イメージ・ボリューム一覧
# 右パネル: 選択項目の詳細（ログ・設定・統計情報）

# 操作キー
# [/]        — パネル切り替え
# Enter      — 詳細表示
# d          — コンテナを停止・削除
# r          — コンテナを再起動
# q          — 終了
```

### dive — Docker イメージの解析

| 項目 | 内容 |
|------|------|
| **用途** | Docker イメージのレイヤー構成を可視化。無駄なファイルを見つけてイメージを最適化 |
| **インストール** | `brew install dive` |
| **Windows での代替** | dive（同じツールが使える） |

```bash
# 基本的な使い方
dive myapp:latest       # 既存イメージを解析
dive build -t myapp .   # ビルドしながら解析

# 画面構成
# 左パネル: 各レイヤーの内容（追加・変更・削除されたファイル）
# 右パネル: ファイルツリー
# 下部: イメージの効率スコア（無駄なファイルの割合）
```

> **使い分け**: Docker の日常管理は **lazydocker**。イメージサイズの最適化は **dive**。

---

## 9. その他の便利ツール

カテゴリに収まりきらない、でも入れておくと便利なツール。

### tldr — `man` の代替（実用的なコマンド例）

| 項目 | 内容 |
|------|------|
| **用途** | コマンドの使い方を実用的な例で簡潔に表示。`man` ページの長い説明を読む必要がなくなる |
| **インストール** | `brew install tldr` |
| **Windows での代替** | tldr（同じツールが使える） |

```bash
# 基本的な使い方
tldr tar                # tar コマンドの使い方を表示
tldr docker run         # docker run の使い方を表示
tldr git stash          # git stash の使い方を表示
tldr --update           # ページデータを更新
```

**man vs tldr:**

| 比較項目 | `man` | `tldr` |
|---------|-------|--------|
| 情報量 | 全オプションを網羅 | よく使うパターンに絞った例 |
| 読みやすさ | 長くて読みにくい | 短く実用的 |
| 学習コスト | 高い | 低い |

> **Tips**: まず `tldr` で概要を掴み、詳細が必要なときだけ `man` を使うのが効率的。

### thefuck — コマンドミスの自動修正

| 項目 | 内容 |
|------|------|
| **用途** | タイプミスしたコマンドを自動で修正して再実行 |
| **インストール** | `brew install thefuck` |
| **Windows での代替** | thefuck（同じツールが使える） |

```bash
# セットアップ（~/.zshrc に追記）
eval $(thefuck --alias)

# 使い方の例
$ git brnach             # タイプミス → エラー
$ fuck                   # 自動で「git branch」に修正して実行

$ apt install vim        # Mac では apt は使えない → エラー
$ fuck                   # 自動で「brew install vim」に修正

$ cd /ect                # 存在しないパス → エラー
$ fuck                   # 自動で「cd /etc」に修正
```

### fastfetch — システム情報の表示（neofetch 後継）

| 項目 | 内容 |
|------|------|
| **用途** | OS・カーネル・CPU・メモリ・シェルなどのシステム情報をアスキーアート付きで表示 |
| **インストール** | `brew install fastfetch` |
| **Windows での代替** | fastfetch（同じツールが使える） |

```bash
fastfetch               # システム情報を表示
```

> neofetch はメンテナンスが終了しているため、fastfetch の使用を推奨。

### tokei — コード行数カウント

| 項目 | 内容 |
|------|------|
| **用途** | プロジェクトのコード・コメント・空行の行数を言語別に集計 |
| **インストール** | `brew install tokei` |
| **Windows での代替** | tokei（同じツールが使える） |

```bash
# 基本的な使い方
tokei                   # カレントディレクトリのコード行数を集計
tokei src/              # 特定のディレクトリを集計
tokei --sort code       # コード行数順にソート
```

**出力例:**

```
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Python                 12          850          620           95          135
 Markdown                3          240            0          180           60
 TOML                    2           45           35            5            5
===============================================================================
 Total                  17         1135          655          280          200
===============================================================================
```

### hyperfine — コマンドのベンチマーク

| 項目 | 内容 |
|------|------|
| **用途** | コマンドの実行時間を正確に計測・比較。複数コマンドの性能比較に最適 |
| **インストール** | `brew install hyperfine` |
| **Windows での代替** | hyperfine（同じツールが使える） |

```bash
# 基本的な使い方
hyperfine "sleep 0.3"                                    # 実行時間を計測
hyperfine "fd -e py" "find . -name '*.py'"              # 2 つのコマンドを比較
hyperfine --warmup 3 "grep -r pattern ." "rg pattern"   # ウォームアップ 3 回後に比較
hyperfine --export-markdown result.md "command"           # 結果を Markdown で出力
```

> **活用例**: 「ripgrep は grep より本当に速いのか？」を `hyperfine` で実測して確認できる。

---

## まとめ — おすすめ導入ステップ

すべてを一度に入れる必要はない。以下の順序で段階的に導入するのがおすすめ。

### ステップ 1: まず入れるべき 4 ツール

```bash
brew install eza bat fd ripgrep
```

日常的に最もよく使う `ls` / `cat` / `find` / `grep` の体験が劇的に向上する。

### ステップ 2: 検索・移動を強化

```bash
brew install fzf zoxide
# fzf のキーバインドを有効化
$(brew --prefix)/opt/fzf/install
```

### ステップ 3: Git 体験を向上

```bash
brew install lazygit git-delta
```

### ステップ 4: 開発に応じて追加

```bash
# JSON を扱うなら
brew install jq

# API テストをするなら
brew install httpie    # または xh

# Docker を使うなら
brew install lazydocker dive

# 言語バージョン管理
brew install mise      # または fnm + pyenv

# システム監視
brew install btop

# その他
brew install tldr thefuck tokei
```

### 一括インストール（Brewfile に追記）

```ruby
# CLI ツール — モダンなコマンド代替
brew "eza"
brew "bat"
brew "fd"
brew "ripgrep"
brew "sd"
brew "dust"
brew "duf"
brew "git-delta"

# CLI ツール — ファイル操作・検索
brew "fzf"
brew "tree"
brew "zoxide"
brew "trash-cli"

# CLI ツール — データ処理
brew "jq"
brew "yq"
brew "fx"

# CLI ツール — ネットワーク
brew "httpie"
brew "xh"
brew "wget"

# CLI ツール — システム監視
brew "btop"
brew "procs"
brew "watch"

# CLI ツール — バージョン管理
brew "mise"

# CLI ツール — Git 拡張
brew "lazygit"
brew "tig"

# CLI ツール — Docker
brew "lazydocker"
brew "dive"

# CLI ツール — その他
brew "tldr"
brew "thefuck"
brew "neofetch"
brew "tokei"
brew "hyperfine"
```

### エイリアス設定のまとめ（~/.zshrc に追記）

```bash
# モダンなコマンド代替
alias ls="eza"
alias ll="eza -l --git --icons"
alias la="eza -la --git --icons"
alias lt="eza -T --icons"
alias cat="bat"

# 安全な削除
alias rm="trash"

# zoxide の有効化
eval "$(zoxide init zsh)"

# thefuck の有効化
eval $(thefuck --alias)

# mise の有効化
eval "$(mise activate zsh)"
```
