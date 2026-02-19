# DS プロジェクト構成ガイド

## 0. はじめに

このガイドは **データサイエンスプロジェクトのディレクトリ構成・環境管理・再現性確保のベストプラクティスをまとめた自分用リファレンス** です。

- **想定読者**: DS・ML のツールは揃ったが、プロジェクトをどう整理すればいいかわからない
- **ゴール**: 再現可能で保守しやすい DS プロジェクトを構築できるようになる
- **前提**: [10 - DS 向け Mac アプリガイド](10-mac-apps-guide.md)・[11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) のツールを理解していること
- **関連ガイド**: [15 - DS ワークフローガイド](15-workflow-guide.md)

> **10・11 との棲み分け**: [10](10-mac-apps-guide.md)・[11](11-terminal-tools-guide.md) は **個別のツール** を紹介した。
> このガイドでは **それらのツールを組み合わせてプロジェクトをどう構成するか** に焦点を当てる。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. 標準ディレクトリ構成](#1-標準ディレクトリ構成) | Cookiecutter Data Science ベースの構成 |
| [2. 環境管理ファイル](#2-環境管理ファイル) | environment.yml・requirements.txt・pyproject.toml |
| [3. ノートブックの管理](#3-ノートブックの管理) | 命名規則・src との分離・nbstripout |
| [4. データの管理](#4-データの管理) | raw / processed / external の分離・DVC・.gitignore |
| [5. 設定・パラメータ管理](#5-設定パラメータ管理) | config.yaml・Hydra・環境変数 |
| [6. コード品質の維持](#6-コード品質の維持) | Ruff・mypy・pre-commit hooks |
| [7. Git の運用](#7-git-の運用) | ブランチ戦略・コミットメッセージ・.gitignore |
| [8. ドキュメント](#8-ドキュメント) | README・CHANGELOG・docstring |
| [9. まとめ — プロジェクト開始チェックリスト](#9-まとめ--プロジェクト開始チェックリスト) | テンプレート・初期設定手順 |

---

## 1. 標準ディレクトリ構成

DS プロジェクトは「ノートブック 1 つにすべてを詰め込む」状態から始まりがち。
早い段階でディレクトリ構成を整理することで、再現性・保守性が大幅に向上する。

### 推奨ディレクトリ構成

```
my-ds-project/
├── README.md                 ← プロジェクトの概要・セットアップ手順
├── pyproject.toml            ← プロジェクト設定・依存関係
├── environment.yml           ← conda 環境定義（conda 利用時）
├── requirements.txt          ← pip 依存関係（pip 利用時）
├── .gitignore                ← Git 除外設定
├── .pre-commit-config.yaml   ← pre-commit hooks 設定
├── Makefile                  ← よく使うコマンドのショートカット
│
├── data/
│   ├── raw/                  ← 元データ（変更しない）
│   ├── processed/            ← 前処理済みデータ
│   ├── external/             ← 外部から取得したデータ
│   └── interim/              ← 中間データ
│
├── notebooks/
│   ├── 01_eda.ipynb          ← 探索的データ分析
│   ├── 02_feature_eng.ipynb  ← 特徴量エンジニアリング
│   └── 03_modeling.ipynb     ← モデリング
│
├── src/
│   ├── __init__.py
│   ├── data/                 ← データの読み込み・前処理
│   │   ├── __init__.py
│   │   └── preprocess.py
│   ├── features/             ← 特徴量エンジニアリング
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/               ← モデルの学習・予測
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── predict.py
│   └── visualization/        ← 可視化
│       ├── __init__.py
│       └── plots.py
│
├── models/                   ← 学習済みモデルの保存先
│   └── model_v1.pkl
│
├── reports/
│   ├── figures/              ← レポート用の図表
│   └── final_report.md
│
├── tests/                    ← テストコード
│   ├── test_preprocess.py
│   └── test_features.py
│
└── configs/                  ← 設定ファイル
    ├── config.yaml
    └── params.yaml
```

### 各ディレクトリの役割

| ディレクトリ | 役割 | Git 管理 |
|------------|------|---------|
| `data/raw/` | 元データ。絶対に変更しない | DVC で管理（Git には入れない） |
| `data/processed/` | 前処理済みデータ | DVC で管理 |
| `data/external/` | 外部 API・Web スクレイピングで取得したデータ | DVC で管理 |
| `notebooks/` | 探索・実験用のノートブック | Git 管理（nbstripout で出力除去） |
| `src/` | 再利用可能な Python コード | Git 管理 |
| `models/` | 学習済みモデル | DVC で管理 |
| `reports/` | レポート・図表 | Git 管理 |
| `tests/` | テストコード | Git 管理 |
| `configs/` | 設定・ハイパーパラメータ | Git 管理 |

### Cookiecutter Data Science — テンプレートの自動生成

```bash
# Cookiecutter のインストール
pipx install cookiecutter

# テンプレートからプロジェクトを生成
cookiecutter https://github.com/drivendata/cookiecutter-data-science

# 対話形式でプロジェクト名・著者名などを入力
# → 上記のような構成が自動生成される
```

> **Cookiecutter を使うかどうか**: テンプレートの構成が自分に合わない場合は、上記の構成を参考に手動で作っても良い。
> 重要なのはテンプレートそのものではなく、**data / notebooks / src / models を分離する原則**。

---

## 2. 環境管理ファイル

「自分の環境では動いたのに、他の人の環境では動かない」を防ぐ。

### 環境管理ファイルの選択肢

| ファイル | ツール | 用途 |
|---------|-------|------|
| `environment.yml` | conda | conda 環境の完全な定義 |
| `requirements.txt` | pip | pip パッケージの一覧 |
| `pyproject.toml` | uv / poetry | プロジェクト設定 + 依存関係の統合管理 |
| `Dockerfile` | Docker | コンテナレベルの環境定義 |

### environment.yml — conda 環境の定義

```yaml
name: my-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.12
  - numpy=1.26
  - pandas=2.2
  - scikit-learn=1.4
  - matplotlib=3.8
  - seaborn=0.13
  - jupyter=1.0
  - pip:
    - wandb==0.16
    - lightgbm==4.3
    - ruff==0.3
```

```bash
# 環境の作成
conda env create -f environment.yml

# 環境の更新（パッケージ追加後）
conda env update -f environment.yml --prune

# 現在の環境をエクスポート
conda env export --from-history > environment.yml
```

> **`--from-history` オプション**: 明示的にインストールしたパッケージだけをエクスポートする。
> これを使わないと依存の依存まで含まれ、OS が変わると再現できなくなる。

### requirements.txt — pip 環境の定義

```txt
numpy==1.26.4
pandas==2.2.1
scikit-learn==1.4.1
matplotlib==3.8.3
seaborn==0.13.2
jupyter==1.0.0
wandb==0.16.4
lightgbm==4.3.0
ruff==0.3.2
```

```bash
# インストール
pip install -r requirements.txt

# 現在の環境をエクスポート
pip freeze > requirements.txt
```

### pyproject.toml — モダンなプロジェクト定義

```toml
[project]
name = "my-ds-project"
version = "0.1.0"
description = "My data science project"
requires-python = ">=3.12"
dependencies = [
    "numpy>=1.26",
    "pandas>=2.2",
    "scikit-learn>=1.4",
    "matplotlib>=3.8",
    "seaborn>=0.13",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.3",
    "mypy>=1.8",
    "pytest>=8.0",
    "nbstripout>=0.7",
]
notebook = [
    "jupyter>=1.0",
    "jupyterlab>=4.0",
]
ml = [
    "wandb>=0.16",
    "mlflow>=2.10",
    "lightgbm>=4.3",
]

[tool.ruff]
line-length = 120
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B"]

[tool.mypy]
python_version = "3.12"
ignore_missing_imports = true
```

```bash
# uv でインストール
uv pip install -e ".[dev,notebook,ml]"

# pip でインストール
pip install -e ".[dev,notebook,ml]"
```

> **おすすめ**: conda 利用者は `environment.yml`。pip / uv 利用者は `pyproject.toml`。
> どちらの場合も `pyproject.toml` で Ruff・mypy の設定を管理するのが便利。

---

## 3. ノートブックの管理

ノートブックは探索には最適だが、管理が雑になりやすい。ルールを決めて運用する。

### ノートブックの命名規則

```
notebooks/
├── 01_eda.ipynb
├── 02_feature_engineering.ipynb
├── 03_baseline_model.ipynb
├── 04_hyperparameter_tuning.ipynb
├── 05_model_evaluation.ipynb
└── 06_final_analysis.ipynb
```

**命名ルール:**

| ルール | 説明 | 例 |
|-------|------|-----|
| 番号プレフィックス | 実行順序を明確に | `01_`、`02_`、... |
| スネークケース | ファイル名はスネークケース | `feature_engineering`（スペースや日本語は避ける） |
| 内容を表す名前 | 何をするノートブックか一目でわかる | `03_baseline_model`（`Untitled3` は禁止） |
| 日付は入れない | 日付は Git の履歴で追跡 | `01_eda`（`2024-01-15_eda` は不要） |

### ノートブックと src の分離

ノートブックは探索用、src は再利用可能なコード。この分離が最重要。

```python
# notebooks/03_baseline_model.ipynb
# ノートブックでは src のコードを呼び出す

import sys
sys.path.append("..")

from src.data.preprocess import load_and_clean
from src.features.build_features import create_features
from src.models.train import train_model

# データの読み込み・前処理
df = load_and_clean("data/raw/train.csv")

# 特徴量の作成
X, y = create_features(df)

# モデルの学習
model = train_model(X, y)
```

```python
# src/data/preprocess.py
# 再利用可能な関数として定義

import pandas as pd


def load_and_clean(filepath: str) -> pd.DataFrame:
    """データを読み込んでクリーニングする。"""
    df = pd.read_csv(filepath)
    df = df.dropna(subset=["target"])
    df["date"] = pd.to_datetime(df["date"])
    return df
```

**分離の判断基準:**

| 状況 | 置き場所 |
|------|---------|
| 1 回限りの探索・可視化 | ノートブック内に直接書く |
| 2 回以上使う処理 | `src/` に関数として切り出す |
| パイプラインで自動実行する処理 | `src/` に書き、CLI から実行可能にする |

### nbstripout — ノートブックの出力除去

```bash
# インストール・設定
pip install nbstripout
nbstripout --install    # Git フィルターとして登録

# 以降、git commit 時にノートブックの出力セルが自動除去される
```

> **なぜ必須か**: ノートブックの出力（グラフ・テーブル・ログ）はバイナリとして .ipynb に埋め込まれる。
> これが Git の差分を読めなくし、リポジトリサイズを肥大化させる。
> nbstripout を入れることで、Git にはコードだけがコミットされる。

---

## 4. データの管理

データは Git で管理しない。大きなファイルは DVC やクラウドストレージで管理する。

### data/ ディレクトリの原則

| 原則 | 説明 |
|------|------|
| **raw は不変** | `data/raw/` のファイルは絶対に変更しない。元データの真実のソース |
| **処理結果は processed に** | 前処理済みデータは `data/processed/` に保存。いつでも raw から再生成できるようにする |
| **Git にデータを入れない** | `.gitignore` でデータディレクトリを除外 |
| **DVC でバージョン管理** | データの変更履歴は DVC で追跡 |

### .gitignore — データファイルの除外

```gitignore
# データファイル
data/raw/
data/processed/
data/interim/
data/external/
*.csv
*.parquet
*.h5
*.pkl
*.joblib

# モデルファイル
models/*.pkl
models/*.h5
models/*.pt
models/*.onnx

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# 環境
.env

# OS
.DS_Store
```

### DVC によるデータバージョン管理

```bash
# DVC の初期化
dvc init

# データを DVC で管理
dvc add data/raw/train.csv
git add data/raw/train.csv.dvc data/raw/.gitignore

# リモートストレージの設定
dvc remote add -d storage s3://my-bucket/dvc-store

# データのプッシュ・プル
dvc push
dvc pull
```

**DVC を使うタイミング:**

| プロジェクト規模 | データ管理方法 |
|----------------|-------------|
| 個人・小規模（データ < 100MB） | `.gitignore` で除外 + README にデータの取得方法を記載 |
| 中規模（データ 100MB〜10GB） | DVC でバージョン管理 + S3/GCS にプッシュ |
| 大規模（データ > 10GB） | DVC + クラウドストレージ + データパイプライン |

---

## 5. 設定・パラメータ管理

ハイパーパラメータや設定値をコードにハードコードしない。

### config.yaml — 基本的な設定管理

```yaml
# configs/config.yaml
data:
  raw_path: data/raw/train.csv
  processed_path: data/processed/train_processed.csv
  test_size: 0.2
  random_state: 42

features:
  numerical: [age, income, score]
  categorical: [gender, region, category]
  target: label

model:
  type: lightgbm
  params:
    n_estimators: 1000
    learning_rate: 0.05
    max_depth: 7
    num_leaves: 31
    min_child_samples: 20

training:
  n_folds: 5
  early_stopping_rounds: 100
  seed: 42
```

```python
# src/utils/config.py
import yaml


def load_config(path: str = "configs/config.yaml") -> dict:
    """設定ファイルを読み込む。"""
    with open(path) as f:
        return yaml.safe_load(f)
```

```python
# src/models/train.py
from src.utils.config import load_config

config = load_config()
model_params = config["model"]["params"]
```

### 環境変数 — シークレットの管理

```bash
# .env（Git にコミットしない）
WANDB_API_KEY=xxxxxxxxxxxxx
AWS_ACCESS_KEY_ID=xxxxxxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxx
DATABASE_URL=postgresql://user:pass@host:5432/db
```

```python
# python-dotenv で読み込み
from dotenv import load_dotenv
import os

load_dotenv()
wandb_key = os.getenv("WANDB_API_KEY")
```

> **原則**: パスワード・API キーは `.env` に保存し、`.gitignore` に追加。
> ハイパーパラメータ・パスなどの設定は `configs/` に YAML で管理して Git にコミット。

---

## 6. コード品質の維持

DS のコードも品質を保つ。pre-commit hooks で自動チェック。

### pre-commit hooks の設定

```bash
# pre-commit のインストール
pip install pre-commit
```

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.2
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=500]

  - repo: https://github.com/kynan/nbstripout
    rev: 0.7.1
    hooks:
      - id: nbstripout
```

```bash
# hooks のインストール
pre-commit install

# 全ファイルに対して手動実行
pre-commit run --all-files
```

**hooks の効果:**

| hook | 効果 |
|------|------|
| `ruff` | Lint エラーの自動修正 |
| `ruff-format` | コードの自動フォーマット |
| `trailing-whitespace` | 行末の空白を除去 |
| `check-added-large-files` | 大きなファイルの誤コミットを防止 |
| `nbstripout` | ノートブックの出力を自動除去 |

---

## 7. Git の運用

### ブランチ戦略（DS プロジェクト向け）

DS プロジェクトは Web アプリほど複雑なブランチ戦略は不要。シンプルに運用する。

| ブランチ | 用途 |
|---------|------|
| `main` | 安定版のコード・ノートブック・レポート |
| `experiment/*` | 実験用ブランチ（`experiment/try-xgboost`） |
| `feature/*` | 新しい特徴量やパイプラインの追加 |

```bash
# 実験ブランチの作成
git checkout -b experiment/try-xgboost

# 作業・コミット
git add .
git commit -m "Add XGBoost baseline model"

# main にマージ
git checkout main
git merge experiment/try-xgboost
```

### コミットメッセージの規約

| プレフィックス | 用途 | 例 |
|-------------|------|-----|
| `data:` | データの追加・変更 | `data: Add raw training dataset` |
| `feat:` | 特徴量・モデルの追加 | `feat: Add time-based features` |
| `exp:` | 実験の追加・変更 | `exp: Try LightGBM with tuned params` |
| `fix:` | バグ修正 | `fix: Handle missing values in age column` |
| `refactor:` | コードの整理 | `refactor: Move preprocessing to src/` |
| `docs:` | ドキュメントの更新 | `docs: Update README with setup instructions` |

---

## 8. ドキュメント

### README.md のテンプレート

```markdown
# プロジェクト名

## 概要
（このプロジェクトが何を解決するか、1〜2 文で）

## データ
- データソース: （URL or 説明）
- 期間: YYYY-MM-DD 〜 YYYY-MM-DD
- レコード数: X 行 x Y 列

## セットアップ

### 環境構築
conda env create -f environment.yml
conda activate project-name

### データの取得
dvc pull

## ディレクトリ構成
（上記の構成を簡略化して記載）

## 実行方法

### EDA
jupyter lab notebooks/01_eda.ipynb

### モデルの学習
python src/models/train.py

### 予測
python src/models/predict.py

## 結果
| モデル | CV スコア | テストスコア |
|--------|----------|------------|
| Baseline (LogReg) | 0.82 | 0.80 |
| LightGBM | 0.89 | 0.87 |

## 参考
- （参考にした論文・記事のリンク）
```

### Makefile — コマンドのショートカット

```makefile
.PHONY: setup data train test lint clean

setup:
	conda env create -f environment.yml

data:
	dvc pull

train:
	python src/models/train.py

test:
	pytest tests/

lint:
	ruff check --fix . && ruff format .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
```

```bash
make setup    # 環境構築
make data     # データ取得
make train    # モデル学習
make lint     # コード品質チェック
```

---

## 9. まとめ — プロジェクト開始チェックリスト

新しい DS プロジェクトを始めるときのチェックリスト。

### 初期セットアップ手順

```bash
# 1. ディレクトリ作成
mkdir -p my-project/{data/{raw,processed,external,interim},notebooks,src/{data,features,models,visualization},models,reports/figures,tests,configs}

# 2. Git 初期化
cd my-project
git init

# 3. Python ファイルの作成
touch src/__init__.py src/data/__init__.py src/features/__init__.py src/models/__init__.py src/visualization/__init__.py

# 4. 環境構築
conda create -n my-project python=3.12
conda activate my-project
conda install numpy pandas scikit-learn matplotlib seaborn jupyter

# 5. 環境定義のエクスポート
conda env export --from-history > environment.yml

# 6. Git 設定
# .gitignore を作成（上記参照）
pip install nbstripout pre-commit
nbstripout --install
pre-commit install

# 7. DVC 初期化（データが大きい場合）
pip install dvc
dvc init

# 8. 初回コミット
git add .
git commit -m "Initial project structure"
```

### チェックリスト

- [ ] ディレクトリ構成が整理されている（data / notebooks / src / models が分離）
- [ ] 環境定義ファイルがある（environment.yml or pyproject.toml）
- [ ] .gitignore でデータ・モデル・キャッシュを除外
- [ ] nbstripout が設定されている
- [ ] pre-commit hooks が設定されている
- [ ] ノートブックに番号プレフィックスと意味のある名前がついている
- [ ] 再利用するコードは src/ に切り出されている
- [ ] 設定・パラメータは configs/ に YAML で管理
- [ ] シークレットは .env に保存（.gitignore に追加済み）
- [ ] README.md にセットアップ手順が記載されている

---

**関連ガイド:**

- [15 - DS ワークフローガイド](15-workflow-guide.md) — EDA からデプロイまでの実践フロー
- [10 - DS 向け Mac アプリガイド](10-mac-apps-guide.md) — DS 向けの Mac アプリ
- [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) — DS 向けの CLI ツール
