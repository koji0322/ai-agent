# DS 向けターミナル CLI ツールガイド

## 0. はじめに

このガイドは **データサイエンティスト（DS）がターミナルで使う CLI ツールをまとめた自分用リファレンス** です。

- **想定読者**: Python でデータ分析・機械学習を行う人。ターミナルでの作業効率を上げたい
- **ゴール**: DS に必要な CLI ツールを知り、Python 環境管理・データ処理・実験管理を効率化できるようになる
- **前提**: ターミナルの基本操作ができること。Python の基礎を理解していること
- **関連ガイド**: [10 - DS 向け Mac アプリガイド](10-mac-apps-guide.md)、[12 - DS 向け Web サイトガイド](12-web-resources-guide.md)

> **元ガイドとの棲み分け**: [11 - ターミナル CLI ツールガイド](../11-terminal-tools-guide.md) は **Web 開発者向け** のモダン CLI ツール（eza・bat・ripgrep 等）を紹介している。
> このガイドでは **データサイエンス・機械学習に特化した CLI ツール** に絞って紹介する。
> 汎用的な CLI ツール（eza・bat・fd・fzf 等）は元ガイドを参照。

> すべて **無料・オープンソース** のツールを紹介する。
> インストールは `brew install` / `pip install` / `conda install` を中心に記載。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. Python パッケージ管理](#1-python-パッケージ管理) | pip・conda・uv・poetry・pipx |
| [2. 仮想環境・バージョン管理](#2-仮想環境バージョン管理) | venv・conda env・pyenv・mise |
| [3. Jupyter 関連 CLI](#3-jupyter-関連-cli) | jupyter・nbconvert・papermill・nbstripout |
| [4. データ処理 CLI](#4-データ処理-cli) | csvkit・xsv・jq・duckdb CLI |
| [5. ML 実験・モデル管理](#5-ml-実験モデル管理) | mlflow・wandb CLI・dvc |
| [6. クラウド CLI](#6-クラウド-cli) | aws cli・gcloud・az cli |
| [7. Docker・コンテナ](#7-dockerコンテナ) | docker・docker compose・lazydocker |
| [8. コード品質・Lint](#8-コード品質lint) | ruff・mypy・black・isort |
| [9. まとめ — おすすめ導入ステップ](#9-まとめ--おすすめ導入ステップ) | 段階的インストール・設定 |

---

## 1. Python パッケージ管理

DS は大量の Python パッケージを扱う。パッケージマネージャーの選択は作業効率に直結する。

### パッケージマネージャー一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **pip** | https://pip.pypa.io | Python 標準のパッケージマネージャー | 無料 |
| **conda** | https://docs.conda.io | Python + 非 Python パッケージの管理。環境管理も一体化 | 無料 |
| **uv** | https://github.com/astral-sh/uv | Rust 製の超高速 pip / venv 代替 | 無料 |
| **poetry** | https://python-poetry.org | 依存関係の解決・ロックファイル・パッケージ公開を統合 | 無料 |
| **pipx** | https://pipx.pypa.io | CLI ツールを隔離環境にインストール | 無料 |

### pip — 基本のパッケージマネージャー

| 項目 | 内容 |
|------|------|
| **用途** | PyPI からパッケージをインストール。最も基本的な Python パッケージ管理 |
| **インストール** | Python に同梱 |

```bash
# 基本操作
pip install pandas                 # パッケージのインストール
pip install pandas==2.2.0          # バージョン指定
pip install -r requirements.txt    # requirements.txt から一括インストール
pip freeze > requirements.txt      # 現在の環境をファイルに出力
pip list                           # インストール済みパッケージ一覧
pip show pandas                    # パッケージの詳細情報
pip install --upgrade pandas       # アップグレード
```

### conda — DS のデファクトスタンダード

| 項目 | 内容 |
|------|------|
| **用途** | Python パッケージ + C/Fortran ライブラリ（BLAS・LAPACK 等）を統合管理 |
| **インストール** | Miniconda / Anaconda に同梱 |
| **pip との違い** | conda は Python 以外の依存（C ライブラリ等）も自動解決。科学計算パッケージのインストールが確実 |

```bash
# 基本操作
conda install numpy pandas scikit-learn   # パッケージのインストール
conda install -c conda-forge lightgbm     # conda-forge チャンネルから
conda update --all                         # すべてのパッケージを更新
conda list                                 # インストール済み一覧
conda search tensorflow                    # パッケージを検索

# 環境のエクスポート・復元
conda env export > environment.yml
conda env create -f environment.yml
```

**pip vs conda — 使い分け:**

| 比較項目 | pip | conda |
|---------|-----|-------|
| パッケージソース | PyPI | conda チャンネル（defaults・conda-forge） |
| 非 Python 依存 | 手動で対応 | 自動解決 |
| 環境管理 | venv を別途使用 | conda env で一体管理 |
| 速度 | 普通 | やや遅い（依存解決が厳密） |
| DS パッケージ | 対応 | 最適化済みバイナリを配布 |

### uv — 次世代の高速パッケージマネージャー

| 項目 | 内容 |
|------|------|
| **用途** | pip + venv の代替。Rust 製で 10〜100 倍高速 |
| **インストール** | `brew install uv` |
| **特徴** | pip と同じコマンド体系で学習コスト低。ロックファイル（`uv.lock`）にも対応 |

```bash
# pip の代替として使う
uv pip install pandas numpy scikit-learn
uv pip install -r requirements.txt
uv pip freeze

# プロジェクト管理
uv init my-project
uv add pandas numpy
uv sync                  # ロックファイルから環境を再現

# 仮想環境の作成
uv venv
source .venv/bin/activate
```

### poetry — プロジェクトの依存管理

| 項目 | 内容 |
|------|------|
| **用途** | 依存関係の厳密な解決・ロックファイル管理・パッケージの公開 |
| **インストール** | `pipx install poetry` |
| **適したユーザー** | DS パッケージやツールを PyPI に公開したい人。厳密な依存管理が必要なプロジェクト |

```bash
# プロジェクトの初期化
poetry init

# パッケージの追加
poetry add pandas numpy scikit-learn
poetry add --group dev pytest ruff

# 依存のインストール
poetry install

# 仮想環境内でコマンド実行
poetry run python train.py
poetry run jupyter lab
```

### pipx — CLI ツールの隔離インストール

| 項目 | 内容 |
|------|------|
| **用途** | Python 製の CLI ツールを隔離された仮想環境にインストール。システムの Python を汚さない |
| **インストール** | `brew install pipx && pipx ensurepath` |

```bash
# CLI ツールのインストール例
pipx install ruff           # Linter
pipx install black          # フォーマッター
pipx install mlflow         # 実験管理
pipx install cookiecutter   # プロジェクトテンプレート
```

> **おすすめ**: DS の日常作業には **conda**（科学計算パッケージの互換性が高い）。
> 速度を重視するなら **uv** を試す。CLI ツールは **pipx** で隔離インストールする。

---

## 2. 仮想環境・バージョン管理

プロジェクトごとに環境を分離することで、依存の衝突を防ぐ。

### 仮想環境ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **venv** | https://docs.python.org/3/library/venv.html | Python 標準の仮想環境 | 無料 |
| **conda env** | https://docs.conda.io | conda の仮想環境管理 | 無料 |
| **pyenv** | https://github.com/pyenv/pyenv | Python バージョンの管理 | 無料 |
| **mise** | https://mise.jdx.dev | 複数言語のバージョンを一元管理 | 無料 |

### venv — Python 標準の仮想環境

| 項目 | 内容 |
|------|------|
| **用途** | プロジェクトごとに独立した Python 環境を作成 |
| **インストール** | Python に標準搭載 |

```bash
# 仮想環境の作成・有効化
python -m venv .venv
source .venv/bin/activate

# パッケージのインストール
pip install pandas numpy scikit-learn

# 環境の無効化
deactivate
```

### conda env — conda の仮想環境

| 項目 | 内容 |
|------|------|
| **用途** | プロジェクトごとに Python バージョンとパッケージを分離 |
| **インストール** | conda に同梱 |

```bash
# 環境の作成
conda create -n ml-project python=3.12 pandas scikit-learn

# 環境の有効化・無効化
conda activate ml-project
conda deactivate

# 環境の一覧
conda env list

# 環境のエクスポート・復元
conda env export > environment.yml
conda env create -f environment.yml

# 環境の削除
conda env remove -n ml-project
```

**environment.yml の例:**

```yaml
name: ml-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - jupyter
  - pip:
    - wandb
    - lightgbm
```

### pyenv — Python バージョン管理

| 項目 | 内容 |
|------|------|
| **用途** | 複数バージョンの Python をインストール・切り替え |
| **インストール** | `brew install pyenv` |

```bash
# セットアップ（~/.zshrc に追記）
eval "$(pyenv init -)"

# バージョンのインストール・切り替え
pyenv install 3.12.0
pyenv install 3.11.0
pyenv global 3.12.0           # グローバルバージョン
pyenv local 3.11.0            # プロジェクト固有バージョン（.python-version 作成）
pyenv versions                 # インストール済み一覧
```

> **venv vs conda env**: pip + venv で管理する場合は **venv**。conda で管理する場合は **conda env**。
> 混在させると依存の衝突が起きやすいので、プロジェクトごとにどちらか一方に統一する。

---

## 3. Jupyter 関連 CLI

Jupyter ノートブックの操作を CLI で自動化するツール。

### Jupyter CLI ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **jupyter** | https://jupyter.org | JupyterLab / Notebook の起動・管理 | 無料 |
| **nbconvert** | https://nbconvert.readthedocs.io | ノートブックを HTML・PDF・Python スクリプトに変換 | 無料 |
| **papermill** | https://papermill.readthedocs.io | ノートブックをパラメータ付きで自動実行 | 無料 |
| **nbstripout** | https://github.com/kynan/nbstripout | ノートブックの出力セルを Git コミット前に自動削除 | 無料 |

### jupyter — 起動・カーネル管理

```bash
# JupyterLab の起動
jupyter lab
jupyter lab --port 8889              # ポート指定

# Jupyter Notebook の起動
jupyter notebook

# カーネルの管理
jupyter kernelspec list              # 利用可能なカーネル一覧
jupyter kernelspec remove kernel_name  # カーネルの削除

# 拡張機能の管理
jupyter labextension list            # インストール済み拡張一覧
```

### nbconvert — ノートブックの形式変換

| 項目 | 内容 |
|------|------|
| **用途** | .ipynb を HTML・PDF・Markdown・Python スクリプトなど様々な形式に変換 |
| **インストール** | `pip install nbconvert` |

```bash
# HTML に変換
jupyter nbconvert --to html analysis.ipynb

# Python スクリプトに変換
jupyter nbconvert --to script analysis.ipynb

# PDF に変換（LaTeX が必要）
jupyter nbconvert --to pdf analysis.ipynb

# Markdown に変換
jupyter nbconvert --to markdown analysis.ipynb

# 出力セルを除去して変換
jupyter nbconvert --to html --no-input analysis.ipynb
```

### papermill — ノートブックの自動実行

| 項目 | 内容 |
|------|------|
| **用途** | ノートブックにパラメータを渡して自動実行。バッチ処理・パイプラインに組み込める |
| **インストール** | `pip install papermill` |

```bash
# パラメータ付きで実行
papermill input.ipynb output.ipynb -p learning_rate 0.01 -p epochs 100

# 複数のパラメータセットで実行
papermill input.ipynb output_lr001.ipynb -p learning_rate 0.01
papermill input.ipynb output_lr005.ipynb -p learning_rate 0.05
```

**ノートブック側の設定:**

```python
# ノートブックのセルにタグ "parameters" を付ける
# デフォルト値を定義
learning_rate = 0.001
epochs = 10
```

### nbstripout — Git 向けの出力セル削除

| 項目 | 内容 |
|------|------|
| **用途** | Git コミット時にノートブックの出力セル・実行カウントを自動削除。差分をクリーンに保つ |
| **インストール** | `pip install nbstripout` |

```bash
# リポジトリに設定（Git フィルターとして登録）
nbstripout --install

# 手動で出力を削除
nbstripout notebook.ipynb

# 設定の解除
nbstripout --uninstall
```

> **なぜ nbstripout が重要か**: ノートブックの出力セル（グラフ・テーブル・ログ）は
> バイナリデータとして .ipynb に埋め込まれる。これが Git の差分を膨大にし、レビューを困難にする。
> nbstripout をリポジトリに設定しておけば、コミット時に自動で出力が除去される。

---

## 4. データ処理 CLI

ターミナルでデータの前処理・探索を行うツール。

### データ処理 CLI 一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **csvkit** | https://csvkit.readthedocs.io | CSV ファイルの操作・変換・分析 | 無料 |
| **xsv** | https://github.com/BurntSushi/xsv | Rust 製の高速 CSV 処理 | 無料 |
| **jq** | https://jqlang.github.io/jq/ | JSON の整形・フィルタ・変換 | 無料 |
| **DuckDB CLI** | https://duckdb.org | ファイル（CSV・Parquet）に直接 SQL を実行 | 無料 |

### csvkit — CSV のスイスアーミーナイフ

| 項目 | 内容 |
|------|------|
| **用途** | CSV ファイルの変換・結合・集計・SQL クエリをコマンドラインで実行 |
| **インストール** | `pip install csvkit` |

```bash
# CSV の概要を表示
csvstat data.csv                    # 各列の統計情報
csvlook data.csv                    # ターミナルでテーブル表示
csvcut -c name,age data.csv         # 特定の列を抽出

# 形式変換
in2csv data.xlsx > data.csv         # Excel → CSV
csvjson data.csv > data.json        # CSV → JSON

# SQL でクエリ
csvsql --query "SELECT name, AVG(age) FROM data GROUP BY name" data.csv

# CSV の結合
csvjoin -c id file1.csv file2.csv   # id 列で結合
csvstack file1.csv file2.csv        # 縦に結合
```

**csvkit のコマンド一覧:**

| コマンド | 用途 |
|---------|------|
| `csvlook` | CSV をテーブル形式で表示 |
| `csvstat` | 各列の統計情報を表示 |
| `csvcut` | 列の選択・並べ替え |
| `csvgrep` | 行のフィルタリング |
| `csvsort` | ソート |
| `csvjoin` | CSV ファイルの結合 |
| `csvstack` | CSV ファイルの縦結合 |
| `csvsql` | SQL でクエリ |
| `in2csv` | Excel・JSON などから CSV に変換 |

### xsv — 高速な CSV 処理

| 項目 | 内容 |
|------|------|
| **用途** | 大規模な CSV ファイルを高速に処理。数 GB のファイルでも快適に操作 |
| **インストール** | `brew install xsv` |

```bash
# 基本操作
xsv headers data.csv               # 列名の一覧
xsv stats data.csv                  # 各列の統計情報
xsv count data.csv                  # 行数
xsv select name,age data.csv        # 列の選択
xsv search -s name "Alice" data.csv # 検索
xsv sort -s age data.csv            # ソート
xsv frequency -s category data.csv  # 値の出現頻度
xsv sample 100 data.csv             # ランダムサンプリング
```

### jq — JSON プロセッサ

| 項目 | 内容 |
|------|------|
| **用途** | JSON データの整形・フィルタ・変換。API レスポンスや設定ファイルの操作に |
| **インストール** | `brew install jq` |

```bash
# 基本操作
cat data.json | jq .                # 整形表示
cat data.json | jq '.results[]'     # 配列を展開
cat data.json | jq '.results[] | {name: .name, score: .score}'  # フィールド抽出

# DS での活用例
# API から取得した JSON を CSV に変換
cat results.json | jq -r '.[] | [.name, .accuracy, .loss] | @csv' > results.csv
```

### DuckDB CLI — ファイルに直接 SQL

| 項目 | 内容 |
|------|------|
| **用途** | CSV・Parquet・JSON ファイルに直接 SQL を実行。インメモリ分析エンジン |
| **インストール** | `brew install duckdb` |
| **特徴** | DB のセットアップ不要。ファイルに対して即座に SQL が書ける |

```bash
# DuckDB CLI を起動
duckdb

# CSV ファイルに SQL を実行
duckdb -c "SELECT * FROM 'data.csv' LIMIT 10"
duckdb -c "SELECT category, COUNT(*), AVG(price) FROM 'sales.csv' GROUP BY category"

# Parquet ファイルに SQL を実行
duckdb -c "SELECT * FROM 'data.parquet' WHERE age > 30"

# 複数ファイルの結合
duckdb -c "SELECT a.*, b.score FROM 'users.csv' a JOIN 'scores.csv' b ON a.id = b.user_id"

# ワイルドカードで複数ファイルを読み込み
duckdb -c "SELECT * FROM 'logs/*.csv'"

# 結果を Parquet に出力
duckdb -c "COPY (SELECT * FROM 'data.csv' WHERE age > 30) TO 'filtered.parquet'"
```

> **DuckDB は DS 必携**: pandas を起動するほどでもない軽いデータ探索に最適。
> CSV を直接 SQL で分析でき、Parquet の読み書きも高速。大規模データの前処理にも使える。

---

## 5. ML 実験・モデル管理

実験の追跡・モデルの管理・データパイプラインの構築を CLI で行う。

### ML 管理ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **MLflow** | https://mlflow.org | 実験追跡・モデルレジストリ・デプロイ | 無料（OSS） |
| **wandb CLI** | https://wandb.ai | 実験管理・可視化・レポート作成 | 個人: 無料 |
| **DVC** | https://dvc.org | データ・モデルのバージョン管理・パイプライン | 無料（OSS） |

### MLflow — OSS の実験管理

| 項目 | 内容 |
|------|------|
| **用途** | 実験パラメータ・メトリクス・成果物の記録。モデルのバージョン管理とデプロイ |
| **インストール** | `pip install mlflow` |

```bash
# MLflow Tracking UI を起動
mlflow ui
# ブラウザで http://localhost:5000 を開く

# CLI からの実験実行
mlflow run . -P learning_rate=0.01 -P epochs=100

# モデルの管理
mlflow models serve -m "models:/my-model/Production" -p 5001
```

### wandb CLI — クラウドベースの実験管理

| 項目 | 内容 |
|------|------|
| **用途** | W&B の操作をコマンドラインから。ログイン・同期・レポート作成 |
| **インストール** | `pip install wandb` |

```bash
# 初回ログイン
wandb login

# オフラインモードで実行した結果を同期
wandb sync ./wandb/offline-run-*

# プロジェクトの状態を確認
wandb status
```

### DVC — データパイプライン

| 項目 | 内容 |
|------|------|
| **用途** | データの前処理 → 特徴量作成 → 学習 → 評価のパイプラインを定義・再現 |
| **インストール** | `pip install dvc` または `brew install dvc` |

```bash
# パイプラインの定義
dvc run -n preprocess \
  -d src/preprocess.py -d data/raw.csv \
  -o data/processed.csv \
  python src/preprocess.py

dvc run -n train \
  -d src/train.py -d data/processed.csv \
  -o models/model.pkl \
  -m metrics.json \
  python src/train.py

# パイプラインの再実行（変更があったステージのみ）
dvc repro

# パイプラインの可視化
dvc dag
```

**dvc.yaml の例:**

```yaml
stages:
  preprocess:
    cmd: python src/preprocess.py
    deps:
      - src/preprocess.py
      - data/raw.csv
    outs:
      - data/processed.csv

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/processed.csv
    outs:
      - models/model.pkl
    metrics:
      - metrics.json:
          cache: false
```

---

## 6. クラウド CLI

クラウド上のデータ・計算リソースを操作するための CLI。

### クラウド CLI 一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **AWS CLI** | https://aws.amazon.com/cli/ | S3・SageMaker・EC2 等の操作 | 無料 |
| **Google Cloud CLI** | https://cloud.google.com/sdk | GCS・Vertex AI・BigQuery 等の操作 | 無料 |
| **Azure CLI** | https://learn.microsoft.com/cli/azure/ | Blob Storage・Azure ML 等の操作 | 無料 |

### AWS CLI — S3 とデータ連携

| 項目 | 内容 |
|------|------|
| **用途** | S3 のデータ操作・SageMaker のジョブ管理・EC2 インスタンスの操作 |
| **インストール** | `brew install awscli` |

```bash
# 初回設定
aws configure

# S3 操作（DS で最もよく使う）
aws s3 ls s3://my-bucket/data/
aws s3 cp data.csv s3://my-bucket/data/
aws s3 cp s3://my-bucket/data/result.csv ./
aws s3 sync ./data s3://my-bucket/data/    # ディレクトリの同期
aws s3 rm s3://my-bucket/data/old.csv

# 大きなファイルの転送
aws s3 cp large-file.parquet s3://my-bucket/ --storage-class INTELLIGENT_TIERING

# SageMaker の操作
aws sagemaker list-training-jobs
aws sagemaker describe-training-job --training-job-name my-job
```

### Google Cloud CLI — BigQuery とデータ分析

| 項目 | 内容 |
|------|------|
| **用途** | GCS のデータ操作・BigQuery の SQL 実行・Vertex AI のジョブ管理 |
| **インストール** | `brew install --cask google-cloud-sdk` |

```bash
# 初回ログイン
gcloud auth login
gcloud config set project my-project

# GCS 操作
gsutil ls gs://my-bucket/
gsutil cp data.csv gs://my-bucket/data/
gsutil -m cp -r ./data gs://my-bucket/     # 並列コピー

# BigQuery（bq コマンド）
bq query --use_legacy_sql=false "SELECT * FROM dataset.table LIMIT 10"
bq extract dataset.table gs://my-bucket/export.csv
bq load --source_format=CSV dataset.table gs://my-bucket/data.csv
```

### Azure CLI

| 項目 | 内容 |
|------|------|
| **用途** | Blob Storage のデータ操作・Azure ML のジョブ管理 |
| **インストール** | `brew install azure-cli` |

```bash
# 初回ログイン
az login

# Blob Storage 操作
az storage blob list --container-name data --account-name mystorage
az storage blob upload --file data.csv --container-name data --name data.csv
```

---

## 7. Docker・コンテナ

分析環境の再現性を確保するためのコンテナツール。

### Docker CLI ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **docker** | https://www.docker.com | コンテナの構築・実行・管理 | 無料 |
| **docker compose** | https://docs.docker.com/compose/ | 複数コンテナの一括管理 | 無料 |
| **lazydocker** | https://github.com/jesseduffield/lazydocker | Docker のターミナル UI | 無料 |

### docker — DS 向けの使い方

```bash
# DS 向け Docker イメージの利用例
docker run -it --rm -p 8888:8888 jupyter/scipy-notebook   # Jupyter + SciPy
docker run -it --rm -p 8888:8888 jupyter/tensorflow-notebook  # Jupyter + TensorFlow

# GPU 付きコンテナ（NVIDIA Container Toolkit が必要）
docker run --gpus all -it pytorch/pytorch:latest

# カスタム環境のビルド
docker build -t my-ds-env .
docker run -it --rm -v $(pwd):/app -p 8888:8888 my-ds-env
```

### docker compose — 複数サービスの管理

```yaml
# docker-compose.yml の例（Jupyter + PostgreSQL）
services:
  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
    environment:
      - JUPYTER_ENABLE_LAB=yes

  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: analytics
      POSTGRES_USER: ds
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

```bash
# サービスの起動・停止
docker compose up -d
docker compose down
docker compose logs jupyter
```

### lazydocker — ターミナルで Docker を管理

| 項目 | 内容 |
|------|------|
| **用途** | コンテナ・イメージ・ログをターミナルの TUI で管理 |
| **インストール** | `brew install lazydocker` |

```bash
lazydocker    # 起動
```

---

## 8. コード品質・Lint

DS のコードも品質を保つ。ノートブックから本番コードに移行する際に特に重要。

### コード品質ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Ruff** | https://github.com/astral-sh/ruff | 超高速の Python Linter + Formatter | 無料 |
| **mypy** | https://mypy-lang.org | Python の静的型チェック | 無料 |
| **Black** | https://black.readthedocs.io | Python コードフォーマッター | 無料 |
| **isort** | https://pycqa.github.io/isort/ | import 文のソート | 無料 |

### Ruff — Linter + Formatter の統合ツール

| 項目 | 内容 |
|------|------|
| **用途** | Flake8・isort・pyupgrade 等の機能を統合。Rust 製で超高速 |
| **インストール** | `pip install ruff` または `brew install ruff` |
| **特徴** | Black + isort + Flake8 の代替を 1 つのツールで。10〜100 倍高速 |

```bash
# Lint チェック
ruff check .
ruff check --fix .              # 自動修正

# コードフォーマット
ruff format .
ruff format --check .           # フォーマットの確認のみ
```

**ruff.toml の設定例（DS プロジェクト向け）:**

```toml
line-length = 120
target-version = "py312"

[lint]
select = ["E", "F", "W", "I", "UP", "B", "SIM"]
ignore = ["E501"]  # 行の長さは line-length で制御

[lint.isort]
known-third-party = ["numpy", "pandas", "sklearn", "torch", "tensorflow"]

[format]
quote-style = "double"
```

### mypy — 型チェック

| 項目 | 内容 |
|------|------|
| **用途** | Python コードの型アノテーションをチェック。バグの早期発見に有効 |
| **インストール** | `pip install mypy` |

```bash
# 型チェック
mypy src/
mypy src/ --ignore-missing-imports  # サードパーティの型スタブがない場合
```

### Black — コードフォーマッター

| 項目 | 内容 |
|------|------|
| **用途** | Python コードを統一的にフォーマット。「議論不要のフォーマッター」 |
| **インストール** | `pip install black` |

```bash
# フォーマット
black .
black --check .                  # チェックのみ
black --line-length 120 .        # 行の長さを指定
```

> **おすすめ**: **Ruff** 1 つで Linter + Formatter + isort をカバーできる。
> 新規プロジェクトでは Ruff だけ導入すれば十分。

---

## 9. まとめ — おすすめ導入ステップ

### ステップ 1: パッケージ管理・環境

```bash
# Miniconda をインストール（10 参照）後
conda create -n my-project python=3.12
conda activate my-project
conda install numpy pandas scikit-learn matplotlib jupyter
```

### ステップ 2: Jupyter 関連

```bash
pip install nbstripout papermill nbconvert
nbstripout --install   # Git フィルターとして設定
```

### ステップ 3: データ処理

```bash
brew install duckdb jq xsv
pip install csvkit
```

### ステップ 4: コード品質

```bash
pip install ruff mypy
# または
brew install ruff
```

### ステップ 5: 実験管理・バージョン管理

```bash
pip install mlflow wandb dvc
```

### ステップ 6: クラウド・コンテナ

```bash
# 使用するクラウドに応じて
brew install awscli
brew install --cask google-cloud-sdk
brew install lazydocker
```

### エイリアス設定のまとめ（~/.zshrc に追記）

```bash
# DuckDB で CSV を SQL で分析
alias dq="duckdb -c"

# Jupyter の起動
alias jl="jupyter lab"

# Ruff の実行
alias lint="ruff check --fix . && ruff format ."
```

---

**関連ガイド:**

- [10 - DS 向け Mac アプリガイド](10-mac-apps-guide.md) — DS 向けの Mac アプリ
- [12 - DS 向け Web サイトガイド](12-web-resources-guide.md) — DS 向けの Web サイト・学習リソース
- [13 - DS 向け SNS・情報発信ガイド](13-sns-guide.md) — DS 向けの SNS・コミュニティ
