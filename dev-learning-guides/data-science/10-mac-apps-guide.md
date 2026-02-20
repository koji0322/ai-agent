# DS 向け Mac おすすめアプリガイド

## 0. はじめに

このガイドは **データサイエンティスト（DS）が Mac に導入すべきおすすめアプリをまとめた自分用リファレンス** です。

- **想定読者**: データサイエンス・機械学習に取り組む人。Python 環境や分析ツールを整えたい
- **ゴール**: DS に必要なアプリを知り、Homebrew で効率的にセットアップできるようになる
- **前提**: Mac の基本操作・Homebrew の使い方を理解していること
- **関連ガイド**: [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md)、[12 - DS 向け Web サイトガイド](12-web-resources-guide.md)

> **元ガイドとの棲み分け**: [02 - Mac おすすめアプリガイド](../02-mac-apps-guide.md) は **Web 開発者向け** の汎用アプリを紹介している。
> このガイドでは **データサイエンス・機械学習に特化したアプリ** に絞って紹介する。
> ウィンドウ管理（Rectangle）やランチャー（Raycast）など汎用ツールは元ガイドを参照。

> **無料アプリを優先** して紹介する。有料の場合は明記する。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. Python 環境](#1-python-環境) | Anaconda・Miniconda・Python 公式 |
| [2. IDE・エディタ](#2-ideエディタ) | JupyterLab・VS Code・PyCharm・RStudio |
| [3. ノートブック・実験管理](#3-ノートブック実験管理) | Jupyter Notebook・nbviewer・Weights & Biases |
| [4. データベース・SQL クライアント](#4-データベースsql-クライアント) | DBeaver・TablePlus・pgAdmin |
| [5. データ可視化](#5-データ可視化) | Tableau Public・Power BI Desktop |
| [6. Git・バージョン管理](#6-gitバージョン管理) | GitHub Desktop・GitKraken・DVC |
| [7. クラウド・コンテナ](#7-クラウドコンテナ) | Docker Desktop・AWS CLI・GCP CLI |
| [8. 生産性ツール](#8-生産性ツール) | Notion・Obsidian・Zotero |
| [9. まとめ — おすすめセットアップ](#9-まとめ--おすすめセットアップ) | インストール順序・Brewfile |

---

## 1. Python 環境

DS の作業は Python が中心。まず Python 環境を正しく構築することが最優先。

### Python 環境の選択肢

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Miniconda** | https://docs.conda.io/en/latest/miniconda.html | 最小構成の conda 環境。必要なパッケージだけ追加 | 無料 |
| **Anaconda** | https://www.anaconda.com | conda + 科学計算パッケージを一括同梱 | 無料（個人） |
| **Python 公式** | https://www.python.org | Python.org からの公式インストーラ | 無料 |
| **pyenv** | https://github.com/pyenv/pyenv | 複数バージョンの Python を管理 | 無料 |

### Miniconda — 推奨の Python 環境構築

| 項目 | 内容 |
|------|------|
| **用途** | 軽量な conda 環境。DS に必要なパッケージ（numpy・pandas・scikit-learn）を conda で管理 |
| **料金** | 無料 |
| **インストール** | `brew install --cask miniconda` |
| **Anaconda との違い** | Anaconda は 3GB 以上の容量を消費する。Miniconda は最小構成で、必要なものだけ追加する方式 |

```bash
# Miniconda インストール後の初期設定
conda init zsh
# シェルを再起動

# 基本パッケージのインストール
conda install numpy pandas scikit-learn matplotlib jupyter
```

### Anaconda — オールインワンの科学計算環境

| 項目 | 内容 |
|------|------|
| **用途** | Python + 250 以上の科学計算パッケージ + Jupyter + conda を一括インストール |
| **料金** | 個人利用は無料（商用利用は有料プランあり） |
| **インストール** | `brew install --cask anaconda` |
| **適したユーザー** | 環境構築に時間をかけたくない人。パッケージ選びに迷いたくない人 |

**Anaconda に同梱される主なパッケージ:**

| パッケージ | 用途 |
|-----------|------|
| NumPy | 数値計算 |
| pandas | データ操作・分析 |
| scikit-learn | 機械学習 |
| Matplotlib | グラフ描画 |
| Seaborn | 統計的可視化 |
| JupyterLab | ノートブック環境 |
| SciPy | 科学計算 |
| Statsmodels | 統計モデリング |

### Python 公式 + pyenv — 柔軟なバージョン管理

| 項目 | 内容 |
|------|------|
| **用途** | pyenv でプロジェクトごとに異なる Python バージョンを管理 |
| **料金** | 無料 |
| **インストール** | `brew install pyenv` |
| **適したユーザー** | conda を使わず pip + venv で管理したい人。複数バージョンを切り替えたい人 |

```bash
# pyenv のセットアップ
brew install pyenv
eval "$(pyenv init -)"  # ~/.zshrc に追記

# Python 3.12 をインストールして使用
pyenv install 3.12
pyenv global 3.12
```

> **おすすめ**: DS 初心者は **Miniconda** から始めるのがベスト。
> conda 環境に慣れたら、プロジェクトごとに `conda create` で仮想環境を分ける運用に移行する。
> conda を使わない派は pyenv + venv + pip の構成を選ぶ。

---

## 2. IDE・エディタ

DS ではノートブック環境とコードエディタの両方が必要。用途に応じて使い分ける。

### IDE・エディタ一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **JupyterLab** | https://jupyter.org | ノートブック + ファイルブラウザ + ターミナルの統合環境 | 無料 |
| **VS Code** | https://code.visualstudio.com | 汎用コードエディタ。Python・Jupyter 拡張が強力 | 無料 |
| **PyCharm** | https://www.jetbrains.com/pycharm/ | Python 特化の IDE。デバッグ・リファクタリングが強力 | Community: 無料 / Pro: $24.90/月 |
| **RStudio** | https://posit.co/products/open-source/rstudio/ | R 言語の統合開発環境。R で統計分析する場合に | 無料 |
| **Cursor** | https://cursor.com | AI 特化エディタ。VS Code ベースで AI 補完が強力 | 無料プランあり / Pro: $20/月 |

### JupyterLab — DS の標準ノートブック環境

| 項目 | 内容 |
|------|------|
| **用途** | データ探索・可視化・モデル構築を対話的に行う。コード・出力・Markdown を 1 つのドキュメントに |
| **料金** | 無料 |
| **インストール** | `conda install jupyterlab` または `pip install jupyterlab` |
| **起動** | `jupyter lab` でブラウザが開く |

**JupyterLab の主な機能:**

| 機能 | 説明 |
|------|------|
| ノートブック | セル単位でコードを実行し、出力を即座に確認 |
| ファイルブラウザ | プロジェクト内のファイルをサイドバーで管理 |
| ターミナル | ブラウザ内でターミナルを使用 |
| マルチタブ | ノートブック・テキストファイル・ターミナルを並べて表示 |
| 拡張機能 | 目次表示・Git 連携・変数インスペクタなどを追加可能 |

**おすすめ拡張機能:**

| 拡張機能 | 用途 |
|---------|------|
| `jupyterlab-git` | JupyterLab 内で Git 操作 |
| `jupyterlab-lsp` | コード補完・定義ジャンプ |
| `jupyterlab_code_formatter` | black / isort によるコード整形 |

### VS Code — Python 拡張で DS にも対応

| 項目 | 内容 |
|------|------|
| **用途** | Jupyter ノートブックの編集・Python スクリプト開発・デバッグを 1 つのエディタで |
| **料金** | 無料 |
| **インストール** | `brew install --cask visual-studio-code` |

**DS 向けおすすめ拡張機能:**

| 拡張機能 | 用途 |
|---------|------|
| Python（Microsoft） | Python の IntelliSense・デバッグ・Linting |
| Jupyter（Microsoft） | VS Code 内で Jupyter ノートブックを編集・実行 |
| Pylance | 高速な型チェック・補完 |
| Data Wrangler | データフレームをビジュアルに探索・変換 |
| Rainbow CSV | CSV ファイルを列ごとに色分け表示 |

> **JupyterLab vs VS Code**: データ探索・可視化中心なら **JupyterLab**。
> スクリプト開発・デバッグ・Git 連携を重視するなら **VS Code**。
> 両方を併用するのが実践的。

### PyCharm — Python 専用 IDE

| 項目 | 内容 |
|------|------|
| **用途** | 大規模な Python プロジェクトの開発。デバッグ・リファクタリング・テストが強力 |
| **料金** | Community Edition: 無料 / Professional: $24.90/月 |
| **インストール** | `brew install --cask pycharm-ce`（Community）または `brew install --cask pycharm`（Professional） |

**Community vs Professional:**

| 機能 | Community（無料） | Professional（有料） |
|------|------------------|---------------------|
| Python 開発 | 対応 | 対応 |
| デバッグ | 対応 | 対応 |
| Jupyter ノートブック | 非対応 | 対応 |
| データベースツール | 非対応 | 対応 |
| リモートインタプリタ | 非対応 | 対応 |
| Web フレームワーク | 非対応 | 対応 |

### RStudio — R 言語の統合環境

| 項目 | 内容 |
|------|------|
| **用途** | R 言語での統計分析・可視化。R Markdown でレポート作成 |
| **料金** | 無料（オープンソース） |
| **インストール** | `brew install --cask rstudio` |
| **適したユーザー** | R を使って統計分析・バイオインフォマティクスを行う人 |

---

## 3. ノートブック・実験管理

DS ではモデルの実験を繰り返す。実験のパラメータ・結果を記録し、比較するためのツール。

### ノートブック・実験管理ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Jupyter Notebook** | https://jupyter.org | 対話的なノートブック環境（JupyterLab の軽量版） | 無料 |
| **Google Colab** | https://colab.research.google.com | クラウド上の Jupyter 環境。GPU/TPU を無料で使える | 無料 / Pro: $11.79/月 |
| **Weights & Biases** | https://wandb.ai | 実験管理・ハイパーパラメータ追跡・可視化 | 無料（個人） |
| **MLflow** | https://mlflow.org | 実験管理・モデルレジストリ・デプロイ（OSS） | 無料 |
| **nbviewer** | https://nbviewer.org | Jupyter ノートブックの静的レンダリング・共有 | 無料 |

### Weights & Biases — 実験管理の定番

| 項目 | 内容 |
|------|------|
| **用途** | ML 実験のメトリクス・ハイパーパラメータ・モデルの成果物を自動記録・可視化・比較 |
| **料金** | 個人利用は無料 / Team: $50/月〜 |
| **インストール** | `pip install wandb` |
| **特徴** | コード 2〜3 行の追加で実験追跡を開始。ダッシュボードで実験を比較 |

```python
# 基本的な使い方
import wandb

wandb.init(project="my-project")
wandb.config.learning_rate = 0.001
wandb.config.epochs = 10

for epoch in range(10):
    loss = train()
    wandb.log({"loss": loss, "epoch": epoch})
```

**主な機能:**

| 機能 | 説明 |
|------|------|
| Experiments | 実験のメトリクスをリアルタイムで記録・可視化 |
| Sweeps | ハイパーパラメータの自動チューニング |
| Artifacts | データセット・モデルのバージョン管理 |
| Reports | 実験結果をインタラクティブなレポートにまとめる |
| Tables | 予測結果をテーブル形式で比較・フィルタ |

### MLflow — オープンソースの実験管理

| 項目 | 内容 |
|------|------|
| **用途** | 実験追跡・モデルのパッケージング・デプロイを一元管理 |
| **料金** | 無料（オープンソース） |
| **インストール** | `pip install mlflow` |
| **特徴** | セルフホスト可能。クラウドロックインを避けたい場合に |

```bash
# MLflow UI を起動
mlflow ui
# ブラウザで http://localhost:5000 にアクセス
```

> **W&B vs MLflow**: 手軽さ・ダッシュボードの美しさでは **W&B**。
> セルフホスト・OSS にこだわるなら **MLflow**。
> 両方試して合う方を選ぶのがおすすめ。

---

## 4. データベース・SQL クライアント

DS はデータベースからデータを抽出する場面が多い。SQL クライアントを用意しておく。

### SQL クライアント一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **DBeaver** | https://dbeaver.io | 多数の DB に対応するオープンソース SQL クライアント | Community: 無料 |
| **TablePlus** | https://tableplus.com | 軽量でモダンな SQL クライアント | 無料プランあり / ライセンス: $89 |
| **pgAdmin** | https://www.pgadmin.org | PostgreSQL 専用の管理ツール | 無料 |
| **DataGrip** | https://www.jetbrains.com/datagrip/ | JetBrains 製の高機能 DB IDE | $24.90/月 |

### DBeaver — オープンソースの万能 SQL クライアント

| 項目 | 内容 |
|------|------|
| **用途** | PostgreSQL・MySQL・SQLite・BigQuery・Redshift など 80 以上の DB に対応 |
| **料金** | Community Edition: 無料 |
| **インストール** | `brew install --cask dbeaver-community` |
| **特徴** | ER 図の自動生成・データエクスポート（CSV・JSON）・SQL 補完 |

**DS に便利な機能:**

| 機能 | 説明 |
|------|------|
| SQL エディタ | 補完・フォーマット・実行計画の表示 |
| データエクスポート | クエリ結果を CSV・JSON・Excel に出力 |
| ER 図 | テーブル間のリレーションを自動で図示 |
| データ転送 | 異なる DB 間でデータを移動 |

### TablePlus — 軽量でモダンな UI

| 項目 | 内容 |
|------|------|
| **用途** | シンプルなUIで高速に DB を操作。データの閲覧・編集・クエリ実行 |
| **料金** | 無料プラン（タブ数制限）/ ライセンス: $89 買い切り |
| **インストール** | `brew install --cask tableplus` |

> **DBeaver vs TablePlus**: 多機能で無料を重視するなら **DBeaver**。
> 軽量さと UI を重視するなら **TablePlus**。

---

## 5. データ可視化

コードを書かずにデータを可視化・ダッシュボードを作成するツール。

### データ可視化ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Tableau Public** | https://public.tableau.com | ドラッグ&ドロップでインタラクティブな可視化を作成 | 無料（公開のみ） |
| **Power BI Desktop** | https://powerbi.microsoft.com | Microsoft 製の BI ツール。Excel との連携が強力 | 無料（Desktop 版） |
| **Metabase** | https://www.metabase.com | セルフホスト可能な BI ツール。SQL 不要で分析 | OSS 版: 無料 |
| **Apache Superset** | https://superset.apache.org | OSS の BI ダッシュボードツール | 無料 |

### Tableau Public — ノーコードの可視化ツール

| 項目 | 内容 |
|------|------|
| **用途** | CSV・Excel・DB のデータをドラッグ&ドロップで可視化。インタラクティブなダッシュボードを作成 |
| **料金** | 無料（作成したビジュアライゼーションは公開される） |
| **インストール** | 公式サイトからダウンロード |
| **特徴** | DS のポートフォリオ作成に最適。Tableau Gallery で他の人の作品も参考にできる |

**主なチャートタイプ:**

| チャート | 用途 |
|---------|------|
| 棒グラフ・折れ線グラフ | 時系列データ・比較 |
| 散布図 | 相関関係の探索 |
| ヒートマップ | 密度・分布の可視化 |
| 地図 | 地理空間データの可視化 |
| ダッシュボード | 複数チャートの統合表示 |

### Power BI Desktop — Microsoft の BI ツール

| 項目 | 内容 |
|------|------|
| **用途** | Excel・CSV・DB からデータを取り込み、ダッシュボードを作成 |
| **料金** | Desktop 版は無料 / Pro: $10/月 |
| **インストール** | 公式サイトからダウンロード（Mac 版は Web 版を利用） |
| **注意** | Mac ネイティブアプリは提供されていない。Web 版（app.powerbi.com）を使う |

> **Tableau vs Power BI**: Mac ユーザーには **Tableau Public** がおすすめ（ネイティブアプリあり）。
> Microsoft 365 環境が充実している場合は **Power BI** が便利。
> コードで可視化する場合は Matplotlib・Seaborn・Plotly を使う（[11](11-terminal-tools-guide.md) 参照）。

---

## 6. Git・バージョン管理

DS ではコードだけでなく、データ・モデル・実験結果のバージョン管理も重要。

### バージョン管理ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **GitHub Desktop** | https://desktop.github.com | Git 操作を GUI で行える | 無料 |
| **GitKraken** | https://www.gitkraken.com | Git のブランチツリーをビジュアルに管理 | 無料プランあり |
| **DVC** | https://dvc.org | データ・モデルのバージョン管理（Git for Data） | 無料（OSS） |
| **Git LFS** | https://git-lfs.github.com | 大きなファイルを Git で管理 | 無料（GitHub: 1GB まで） |

### DVC — データ・モデルのバージョン管理

| 項目 | 内容 |
|------|------|
| **用途** | 大容量のデータセット・モデルファイルを Git と連携してバージョン管理 |
| **料金** | 無料（オープンソース） |
| **インストール** | `pip install dvc` または `brew install dvc` |
| **特徴** | Git のコマンド体系に似ており、学習コストが低い |

```bash
# DVC の初期化
dvc init

# データファイルを DVC で管理
dvc add data/dataset.csv

# リモートストレージの設定（S3 の例）
dvc remote add -d myremote s3://my-bucket/dvc-store

# データのプッシュ・プル
dvc push
dvc pull
```

**DVC が解決する問題:**

| 問題 | DVC の解決策 |
|------|------------|
| データファイルが大きすぎて Git に入らない | DVC がリモートストレージに保存し、Git にはメタデータだけ記録 |
| データのバージョンを戻したい | `dvc checkout` で過去のバージョンのデータを復元 |
| チームでデータを共有したい | `dvc push` / `dvc pull` で S3 / GCS を介して共有 |
| パイプラインの再現性を確保したい | `dvc.yaml` でデータ処理パイプラインを定義・再実行 |

### Git LFS — 大きなファイルの Git 管理

| 項目 | 内容 |
|------|------|
| **用途** | モデルファイル・画像データなど大きなファイルを Git リポジトリで管理 |
| **料金** | 無料（GitHub: ストレージ 1GB・帯域 1GB/月まで） |
| **インストール** | `brew install git-lfs && git lfs install` |

```bash
# 特定の拡張子を LFS で管理
git lfs track "*.pkl"
git lfs track "*.h5"
git lfs track "*.parquet"
git add .gitattributes
```

> **DVC vs Git LFS**: パイプラインの再現性・S3/GCS との連携を重視するなら **DVC**。
> シンプルに大きなファイルを Git で管理するだけなら **Git LFS**。

---

## 7. クラウド・コンテナ

DS の実行環境をクラウドやコンテナで管理するツール。

### クラウド・コンテナツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Docker Desktop** | https://www.docker.com/products/docker-desktop/ | コンテナ環境の構築・管理 | 個人利用: 無料 |
| **AWS CLI** | https://aws.amazon.com/cli/ | AWS の操作をコマンドラインから | 無料（AWS の利用料は別途） |
| **Google Cloud CLI** | https://cloud.google.com/sdk | GCP の操作をコマンドラインから | 無料（GCP の利用料は別途） |
| **Azure CLI** | https://learn.microsoft.com/cli/azure/ | Azure の操作をコマンドラインから | 無料（Azure の利用料は別途） |

### Docker Desktop — 再現可能な分析環境

| 項目 | 内容 |
|------|------|
| **用途** | Python 環境・依存パッケージをコンテナにパッケージ化。「自分の環境では動く」問題を解消 |
| **料金** | 個人利用・小規模企業は無料 |
| **インストール** | `brew install --cask docker` |

**DS での Docker 活用例:**

| 用途 | 説明 |
|------|------|
| 分析環境の共有 | Dockerfile で Python + パッケージの環境を定義し、チームで共有 |
| GPU 環境 | NVIDIA Container Toolkit で GPU を利用した学習環境を構築 |
| モデルのサービング | 学習済みモデルを API として提供するコンテナを作成 |
| パイプラインの実行 | データ処理パイプラインをコンテナで実行し、再現性を確保 |

```dockerfile
# DS 向け Dockerfile の例
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
```

### クラウド CLI — リモート環境の操作

| 項目 | AWS CLI | Google Cloud CLI | Azure CLI |
|------|---------|-------------------|-----------|
| **インストール** | `brew install awscli` | `brew install --cask google-cloud-sdk` | `brew install azure-cli` |
| **初回認証** | `aws configure` | `gcloud auth login` | `az login` |
| **DS での用途** | S3 のデータ操作・SageMaker | GCS のデータ操作・Vertex AI | Blob Storage・Azure ML |

```bash
# AWS S3 の操作例
aws s3 ls s3://my-bucket/
aws s3 cp data.csv s3://my-bucket/data/
aws s3 sync ./data s3://my-bucket/data/

# GCS の操作例
gsutil ls gs://my-bucket/
gsutil cp data.csv gs://my-bucket/data/
```

---

## 8. 生産性ツール

研究・学習の効率を上げるためのツール。

### 生産性ツール一覧

| 名前 | URL | 用途 | 料金 |
|------|-----|------|------|
| **Notion** | https://www.notion.so | メモ・ドキュメント・タスク管理 | 無料プランあり |
| **Obsidian** | https://obsidian.md | ローカルファーストの Markdown ナレッジベース | 個人利用: 無料 |
| **Zotero** | https://www.zotero.org | 論文・参考文献の管理 | 無料（ストレージ 300MB） |
| **Skim** | https://skim-app.sourceforge.io | 軽量な PDF リーダー。注釈機能付き | 無料 |

### Zotero — 論文管理の定番

| 項目 | 内容 |
|------|------|
| **用途** | 論文の収集・整理・引用管理。ブラウザ拡張でワンクリックで論文を保存 |
| **料金** | 無料（ストレージ 300MB。追加: $20/年で 2GB） |
| **インストール** | `brew install --cask zotero` |
| **特徴** | BibTeX エクスポート対応。ブラウザ拡張（Zotero Connector）で arXiv・Google Scholar から直接保存 |

**主な機能:**

| 機能 | 説明 |
|------|------|
| ブラウザ拡張 | arXiv・Google Scholar・PubMed からワンクリックで論文を保存 |
| タグ・コレクション | 論文をプロジェクト別・テーマ別に整理 |
| PDF 注釈 | PDF に直接ハイライト・メモを追加 |
| 引用生成 | BibTeX・APA・IEEE など各種引用形式に対応 |
| 同期 | 複数デバイス間で同期 |

### Obsidian — DS のナレッジベース

| 項目 | 内容 |
|------|------|
| **用途** | 論文メモ・実験ログ・学習ノートをリンクでつなげるナレッジベース |
| **料金** | 個人利用: 無料 |
| **インストール** | `brew install --cask obsidian` |
| **DS での活用** | 論文の要約 → 関連論文へのリンク → 実装メモ → 実験結果を相互リンクで管理 |

**DS 向けおすすめプラグイン:**

| プラグイン | 用途 |
|-----------|------|
| Dataview | ノート内のメタデータをクエリしてテーブル表示 |
| Excalidraw | 手書き風の図をノート内に作成 |
| Citations | Zotero と連携して論文の引用を管理 |
| Templater | 実験ログ・論文メモのテンプレートを自動展開 |

---

## 9. まとめ — おすすめセットアップ

新しい Mac で DS 環境を構築する手順。

### ステップ 1: Python 環境

```bash
# Miniconda のインストール
brew install --cask miniconda
conda init zsh
# シェルを再起動

# 基本パッケージ
conda install numpy pandas scikit-learn matplotlib seaborn jupyter
```

### ステップ 2: IDE・ノートブック

```bash
brew install --cask visual-studio-code
# JupyterLab は conda で既にインストール済み
jupyter lab  # 動作確認
```

### ステップ 3: データベース・可視化

```bash
brew install --cask dbeaver-community
# Tableau Public は公式サイトからダウンロード
```

### ステップ 4: バージョン管理

```bash
brew install --cask github
brew install git-lfs && git lfs install
pip install dvc
```

### ステップ 5: クラウド・コンテナ

```bash
brew install --cask docker
brew install awscli        # AWS を使う場合
brew install --cask google-cloud-sdk  # GCP を使う場合
```

### ステップ 6: 生産性ツール

```bash
brew install --cask zotero
brew install --cask obsidian
```

### 一括インストール（Brewfile）

```ruby
# DS 向け Brewfile

# Python 環境
cask "miniconda"

# IDE・エディタ
cask "visual-studio-code"

# データベース
cask "dbeaver-community"

# バージョン管理
cask "github"
brew "git-lfs"
brew "dvc"

# クラウド・コンテナ
cask "docker"
brew "awscli"

# 生産性ツール
cask "zotero"
cask "obsidian"
```

```bash
# Brewfile から一括インストール
brew bundle
```

> **ポイント**: すべてを一度に入れる必要はない。
> まずステップ 1〜2 で Python + Jupyter 環境を整え、プロジェクトの必要に応じて追加していく。

---

**関連ガイド:**

- [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) — DS 向けの CLI ツール
- [12 - DS 向け Web サイトガイド](12-web-resources-guide.md) — DS 向けの Web サイト・学習リソース
- [13 - DS 向け SNS・情報発信ガイド](13-sns-guide.md) — DS 向けの SNS・コミュニティ
