# Python 環境構築ガイド

## 0. はじめに

このガイドは **Mac に Python の開発環境を構築するための入門ガイド** です。

- **想定読者**: プログラミング初心者。Mac の基本操作とターミナルの使い方は学習済み
- **ゴール**: Python のバージョン管理・仮想環境・パッケージ管理を理解し、VS Code と Claude Code で Python 開発を始められるようになる
- **前提**: [Mac 基本操作ガイド](01-mac-basics-guide.md) でターミナルの基本操作は学習済み

Python は **汎用プログラミング言語** です。データ分析・Web アプリ・自動化スクリプトなど、幅広い用途に使えます。Mac には最初から Python が入っていますが、開発用にはバージョン管理や仮想環境の設定が必要です。

### 関連ガイド

- **Mac の基本操作**: [Mac 基本操作ガイド](01-mac-basics-guide.md)
- **VS Code**: [VS Code 基本操作ガイド](00-vscode-guide.md)
- **Claude Code**: [Claude Code 基本操作ガイド](10-claude-code-guide.md)、[アプリケーション開発ガイド](13-claude-code-app-dev-guide.md)
- **Python 活用**: [データ分析入門ガイド](27-data-analysis-guide.md)
- **学習ロードマップ**: [開発学習ロードマップ](30-learning-roadmap-guide.md)

---

## 1. Python のバージョンと選び方

### Python 2 と Python 3

Python には大きく **Python 2** と **Python 3** の 2 系統がある。

| 項目 | Python 2 | Python 3 |
|------|----------|----------|
| **状態** | 2020 年にサポート終了 | 現在の主流 |
| **新規開発** | 使ってはいけない | こちらを使う |
| **コマンド** | `python` （古い Mac） | `python3` |

> **結論: 必ず Python 3 を使う。** Python 2 は過去の遺産であり、新しいプロジェクトでは使わない。

### 今の Python バージョンを確認する

```bash
# Python 3 のバージョンを確認
python3 --version
# 出力例: Python 3.13.2

# python コマンドがどこを指しているか確認
which python3
# 出力例: /usr/bin/python3
```

Mac に最初から入っている Python（システム Python）はバージョンが古いことが多い。開発には **pyenv で管理した Python** を使うのがベストプラクティス。

### バージョンの選び方

| 方針 | 説明 |
|------|------|
| **最新の安定版を選ぶ** | `3.13.x` など など、最新のメジャーリリースを使う |
| **マイナーバージョンは最新** | `3.13.1` より `3.13.2` のように、バグ修正が反映された最新を選ぶ |
| **特別な理由がなければ最新** | ライブラリの互換性で古いバージョンが必要なケースは稀 |

```bash
# pyenv でインストール可能なバージョン一覧を確認（後述）
pyenv install --list | grep "^  3\."
```

---

## 2. pyenv で Python バージョン管理

### pyenv とは

**pyenv** は Python のバージョン管理ツール。複数の Python バージョンをインストールし、プロジェクトごとに使うバージョンを切り替えられる。

| 機能 | 説明 |
|------|------|
| 複数バージョンの共存 | 3.12 と 3.13 を両方インストールできる |
| グローバル設定 | デフォルトで使うバージョンを指定 |
| ローカル設定 | プロジェクトごとにバージョンを指定 |

### インストール

```bash
# Homebrew で pyenv をインストール
brew install pyenv
```

### シェルの設定

pyenv を使うには、シェル（zsh）の設定ファイルに初期化コマンドを追加する必要がある。

```bash
# ~/.zshrc に pyenv の設定を追記
echo '' >> ~/.zshrc
echo '# pyenv' >> ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# 設定を反映
source ~/.zshrc
```

### Python のインストールと切り替え

```bash
# インストール可能なバージョンを確認
pyenv install --list | grep "^  3\.12"

# Python 3.13.2 をインストール（例）
pyenv install 3.13.2

# インストール済みのバージョン一覧
pyenv versions

# グローバル（システム全体）のデフォルトを設定
pyenv global 3.13.2

# バージョンを確認
python --version
# 出力: Python 3.13.2
```

### プロジェクトごとのバージョン指定（local）

```bash
# プロジェクトフォルダに移動
cd ~/projects/my-app

# このプロジェクトだけ Python 3.12.9 を使う
pyenv local 3.12.9

# .python-version ファイルが作成される
cat .python-version
# 出力: 3.12.9
```

`pyenv local` を実行すると、そのフォルダに `.python-version` ファイルが作成される。以降、このフォルダ内では自動的に指定バージョンの Python が使われる。

### （参考）mise — もう一つのバージョン管理ツール

**mise**（旧 rtx）は Python だけでなく Node.js や Ruby なども一括管理できる統合バージョン管理ツール。

```bash
# mise のインストール
brew install mise

# mise で Python をインストール
mise use python@3.13.2

# mise でバージョン確認
mise current python
```

複数言語を扱うようになったら mise への移行を検討するとよい。このガイドでは pyenv を中心に説明する。

---

## 3. 仮想環境（venv）

### なぜ仮想環境が必要か

Python ではプロジェクトごとに使うライブラリ（パッケージ）が異なる。仮想環境を使わないと、すべてのプロジェクトが同じライブラリ群を共有してしまい、バージョンの衝突が起きる。

| 状態 | 問題 |
|------|------|
| 仮想環境なし | プロジェクト A が pandas 1.5 を必要、プロジェクト B が pandas 2.0 を必要 → 共存できない |
| 仮想環境あり | プロジェクトごとに独立した環境を持つ → それぞれ別バージョンを使える |

### 仮想環境の作成と使い方

```bash
# 1. プロジェクトフォルダに移動
cd ~/projects/my-app

# 2. 仮想環境を作成（.venv という名前のフォルダができる）
python -m venv .venv

# 3. 仮想環境を有効化（activate）
source .venv/bin/activate

# 4. 有効化されるとプロンプトに (.venv) が付く
# (.venv) user@mac my-app %

# 5. この状態で pip install するとこの環境にだけインストールされる
pip install pandas

# 6. 仮想環境を無効化（deactivate）
deactivate
```

### 仮想環境のライフサイクル

```
プロジェクト開始 → venv 作成 → activate → 作業 → deactivate
                                  ↑                    |
                                  └────── 毎回ここから ─┘
```

> **ポイント**: ターミナルを開くたびに `source .venv/bin/activate` を実行する必要がある。VS Code なら自動で有効化する設定ができる（セクション 5 参照）。

### .gitignore に追加

仮想環境のフォルダ（`.venv`）には大量のファイルが含まれるため、Git で管理してはいけない。

```bash
# .gitignore に .venv を追加
echo ".venv/" >> .gitignore
```

`.gitignore` の例:

```
.venv/
__pycache__/
*.pyc
.env
```

### 仮想環境の基本コマンドまとめ

| 操作 | コマンド |
|------|---------|
| 作成 | `python -m venv .venv` |
| 有効化 | `source .venv/bin/activate` |
| 無効化 | `deactivate` |
| 削除（やり直し） | `rm -rf .venv` |
| 確認（どの Python を使っているか） | `which python` |

---

## 4. pip でパッケージ管理

### pip とは

**pip** は Python のパッケージ管理ツール。PyPI（Python Package Index）という公開リポジトリからライブラリをインストールできる。

```bash
# 仮想環境を有効化した状態で実行すること
source .venv/bin/activate

# パッケージをインストール
pip install pandas

# 特定バージョンを指定してインストール
pip install pandas==2.1.0

# インストール済みパッケージの一覧
pip list
```

### requirements.txt で依存関係を管理

チームで開発するとき、あるいは別の環境で同じプロジェクトを動かすとき、**同じパッケージを同じバージョンでインストール** する必要がある。`requirements.txt` はそのための設定ファイル。

```bash
# 現在の環境のパッケージをファイルに書き出す
pip freeze > requirements.txt

# requirements.txt の中身（例）
# numpy==1.26.2
# pandas==2.1.4
# python-dateutil==2.8.2
# ...

# requirements.txt からまとめてインストール（別の環境で）
pip install -r requirements.txt
```

### よく使うパッケージ

| パッケージ | 用途 | インストール |
|-----------|------|-------------|
| **pandas** | データ分析・CSV/Excel 操作 | `pip install pandas` |
| **requests** | HTTP リクエスト（API 呼び出し） | `pip install requests` |
| **flask** | Web アプリケーション | `pip install flask` |
| **pytest** | テストフレームワーク | `pip install pytest` |
| **python-dotenv** | 環境変数の管理（`.env` ファイル） | `pip install python-dotenv` |
| **openpyxl** | Excel ファイルの読み書き | `pip install openpyxl` |
| **matplotlib** | グラフ描画 | `pip install matplotlib` |

### pip のアップグレード

pip 自体も定期的にアップグレードする。

```bash
# pip のアップグレード
pip install --upgrade pip

# 特定パッケージのアップグレード
pip install --upgrade pandas
```

---

## 5. VS Code での Python 開発設定

### 必須の拡張機能

VS Code で Python を快適に書くには、以下の拡張機能をインストールする。

| 拡張機能 | 説明 | インストール方法 |
|----------|------|-----------------|
| **Python** | Python の基本サポート（実行・デバッグ） | `Cmd + Shift + X` → 「Python」で検索 |
| **Pylance** | 高速な型チェック・コード補完 | Python 拡張機能と一緒に自動インストール |

> **Python 拡張機能をインストールすると Pylance も自動で入る。** 追加で何かする必要はない。

### Python インタープリタの選択

VS Code がどの Python を使うかを設定する。仮想環境を使っている場合、その Python を選択する。

1. `Cmd + Shift + P` でコマンドパレットを開く
2. 「Python: Select Interpreter」と入力
3. `.venv` 内の Python（例: `./.venv/bin/python`）を選択

> フォルダ内に `.venv` があれば、VS Code が自動的に検出して候補に表示する。

### settings.json の設定例

プロジェクトフォルダに `.vscode/settings.json` を作成して、Python 関連の設定を記述する。

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "basic",
  "editor.formatOnSave": true,
  "python.analysis.autoImportCompletions": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.tabSize": 4
  }
}
```

| 設定 | 説明 |
|------|------|
| `defaultInterpreterPath` | 使用する Python のパス（仮想環境内を指定） |
| `activateEnvironment` | ターミナルを開いたとき自動で仮想環境を有効化 |
| `typeCheckingMode` | 型チェックのレベル（`off` / `basic` / `strict`） |
| `formatOnSave` | 保存時に自動フォーマット |
| `defaultFormatter` | Python のフォーマッター（Black を推奨） |

### フォーマッター（Black）の導入

```bash
# Black をインストール
pip install black

# VS Code 拡張機能もインストール
# Cmd + Shift + X → 「Black Formatter」で検索してインストール
```

Black は Python のコードフォーマッター。保存時に自動でコードを整形してくれる。チーム内のコードスタイルを統一するのに便利。

### デバッグ設定

VS Code の Python デバッグ機能を使うと、コードを 1 行ずつ実行して変数の中身を確認できる。

1. デバッグしたい行の左側（行番号の左）をクリックして **ブレークポイント** を設定（赤い丸が表示される）
2. `F5` キーを押してデバッグを開始
3. 初回は「デバッグ構成の選択」が表示されるので「Python File」を選択
4. ブレークポイントでプログラムが一時停止する
5. 左側の「変数」パネルで変数の値を確認

| 操作 | ショートカット |
|------|--------------|
| デバッグ開始 | `F5` |
| ステップオーバー（次の行へ） | `F10` |
| ステップイン（関数の中に入る） | `F11` |
| 続行（次のブレークポイントまで） | `F5` |
| デバッグ停止 | `Shift + F5` |

---

## 6. Claude Code と Python

### Claude Code に Python スクリプトを生成してもらう

Claude Code は Python のコード生成が得意。以下の流れで効率的に開発できる。

```
1. プロジェクトフォルダを作成
2. 仮想環境を作成・有効化
3. Claude Code を起動
4. 自然言語で指示を出す
5. 生成されたコードを実行・確認
6. フィードバックして改善
```

### 実際の流れ

```bash
# 1. プロジェクトフォルダを作成
mkdir ~/projects/csv-analyzer && cd ~/projects/csv-analyzer

# 2. 仮想環境を作成・有効化
python -m venv .venv
source .venv/bin/activate

# 3. Claude Code を起動
claude
```

Claude Code の中での指示例:

```
あなた: 「CSV ファイルを読み込んで、列ごとの統計情報（平均・最大・最小）を表示する
        Python スクリプトを作って。pandas を使ってください」

Claude: analyze.py を作成します...
        必要なパッケージ: pandas
        pip install pandas を実行しますか？
```

### 仮想環境のベストプラクティス

Claude Code と Python を組み合わせる際のポイント:

| ベストプラクティス | 理由 |
|-------------------|------|
| プロジェクトごとに仮想環境を作る | 依存関係の衝突を防ぐ |
| `.venv` はプロジェクトルートに置く | VS Code が自動検出できる |
| `requirements.txt` を常に更新する | 環境の再現性を確保 |
| `.gitignore` に `.venv/` を入れる | 仮想環境は Git 管理しない |

### CLAUDE.md に Python バージョンを明記する

プロジェクトの `CLAUDE.md` に Python のバージョンや使用パッケージを記載しておくと、Claude Code がプロジェクトの状況を正しく理解できる。

```markdown
# CLAUDE.md

## 環境情報
- Python: 3.13.2（pyenv で管理）
- 仮想環境: .venv（venv で作成）
- パッケージ管理: pip + requirements.txt

## 開発ルール
- コードフォーマッター: Black
- テストフレームワーク: pytest
- 新しいパッケージを追加したら requirements.txt を更新すること

## プロジェクト構造
- src/ — メインのソースコード
- tests/ — テストコード
- data/ — データファイル（Git 管理外）
```

### Claude Code への指示テンプレート

よく使う指示パターン:

```
# 新規スクリプト作成
「○○を行う Python スクリプトを作って。pandas と matplotlib を使ってください」

# 既存コードの改善
「analyze.py にエラーハンドリングを追加して。ファイルが見つからない場合の処理も入れて」

# テスト作成
「analyze.py のテストを pytest で書いて。正常系と異常系の両方をカバーして」

# requirements.txt の更新
「現在の仮想環境のパッケージを requirements.txt に書き出して」
```

---

## 7. 困ったときは

### よくある問題と対処法

| 症状 | 原因 | 対処法 |
|------|------|--------|
| `python` コマンドが見つからない | pyenv の設定が反映されていない | `source ~/.zshrc` を実行、またはターミナルを再起動 |
| `pip install` で権限エラー | 仮想環境の外でインストールしようとしている | `source .venv/bin/activate` で仮想環境を有効化してから実行 |
| `ModuleNotFoundError` | パッケージがインストールされていない | `pip install パッケージ名` でインストール |
| `ModuleNotFoundError`（インストール済みなのに） | 仮想環境が有効化されていない | `which python` で確認。`.venv` 内を指していなければ activate する |
| `pyenv install` でビルドエラー | 依存ライブラリが不足 | `brew install openssl readline sqlite3 xz zlib` を実行してから再試行 |
| VS Code が仮想環境を認識しない | `.venv` が別の場所にある | コマンドパレット → 「Python: Select Interpreter」で手動選択 |
| `pip freeze` の出力が多すぎる | 依存パッケージも含まれている | `pip install pip-tools` → `pip-compile` で直接の依存だけを管理 |
| Black が動かない | 拡張機能がインストールされていない | VS Code で「Black Formatter」拡張機能をインストール |

### 環境構築チェックリスト

新しいプロジェクトを始めるとき、以下を確認する:

```bash
# 1. pyenv で正しい Python バージョンが使われているか
python --version

# 2. 仮想環境が有効化されているか
which python
# → .venv/bin/python を指していれば OK

# 3. 必要なパッケージがインストールされているか
pip list

# 4. requirements.txt があるか
cat requirements.txt
```

---

## 関連ガイド

- [VS Code 基本操作ガイド](00-vscode-guide.md) — エディタの基本操作
- [Mac 基本操作ガイド](01-mac-basics-guide.md) — ターミナル・Homebrew の基本
- [Claude Code 基本操作ガイド](10-claude-code-guide.md) — Claude Code の基本
- [アプリケーション開発ガイド](13-claude-code-app-dev-guide.md) — Claude Code で実際にアプリを作る
- [データ分析入門ガイド](27-data-analysis-guide.md) — pandas を使ったデータ分析
- [開発学習ロードマップ](30-learning-roadmap-guide.md) — 学習の全体像
