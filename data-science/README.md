# データサイエンティスト向けガイドシリーズ

## 概要

このディレクトリには **データサイエンティスト（DS）・ML エンジニア・データアナリスト向け** のガイドシリーズを収録している。

Mac 環境でのツール導入から、学習リソース、コミュニティ参加、実務スキルまで、DS に必要な情報を体系的にまとめた自分用リファレンス。

## 対象読者

- データサイエンティスト（DS）
- 機械学習（ML）エンジニア
- データアナリスト
- これから DS・ML を始めたい人

## ガイド一覧

### ツール・リソース編（10〜13）

| ガイド | ファイル | 内容 |
|--------|---------|------|
| **10 - DS 向け Mac アプリガイド** | [10-mac-apps-guide.md](10-mac-apps-guide.md) | Python 環境・IDE・実験管理・データベース・可視化ツール等の Mac アプリ |
| **11 - DS 向けターミナル CLI ツールガイド** | [11-terminal-tools-guide.md](11-terminal-tools-guide.md) | パッケージ管理・Jupyter CLI・データ処理・ML 実験管理・コード品質ツール |
| **12 - DS 向け Web サイトガイド** | [12-web-resources-guide.md](12-web-resources-guide.md) | 公式ドキュメント・学習プラットフォーム・論文・データセット・コンペ |
| **13 - DS 向け SNS・情報発信ガイド** | [13-sns-guide.md](13-sns-guide.md) | ML 研究者の SNS・YouTube チャンネル・Discord・ポッドキャスト |

### 実務・スキル編（14〜19）

| ガイド | ファイル | 内容 |
|--------|---------|------|
| **14 - DS プロジェクト構成ガイド** | [14-project-structure-guide.md](14-project-structure-guide.md) | ディレクトリ構成・環境管理・ノートブック管理・データ管理・Git 運用 |
| **15 - DS ワークフローガイド** | [15-workflow-guide.md](15-workflow-guide.md) | EDA → 前処理 → 特徴量 → モデリング → 評価 → デプロイの実践フロー |
| **16 - DS のための SQL ガイド** | [16-sql-guide.md](16-sql-guide.md) | 集約・JOIN・CTE・ウィンドウ関数・DS 実務パターン |
| **17 - DS のための数学・統計ガイド** | [17-math-stats-guide.md](17-math-stats-guide.md) | 線形代数・微積分・確率・統計検定・回帰分析・学習ロードマップ |
| **18 - LLM / 生成 AI 活用ガイド** | [18-llm-guide.md](18-llm-guide.md) | API 利用・プロンプト設計・RAG・埋め込み・ファインチューニング |
| **19 - Kaggle 攻略ガイド** | [19-kaggle-guide.md](19-kaggle-guide.md) | コンペの取り組み方・EDA テンプレート・特徴量戦略・アンサンブル |

### 学習ロードマップ編（20）

| ガイド | ファイル | 内容 |
|--------|---------|------|
| **20 - DS 学習ロードマップガイド** | [20-learning-roadmap-guide.md](20-learning-roadmap-guide.md) | 初心者→プロへの 5 フェーズ・学習リソース・キャリアパス・習慣づくり |

## 各ガイドの概要

### 10 - DS 向け Mac アプリガイド

Mac に導入すべき DS 向けアプリ。Python 環境構築から始まり、IDE・ノートブック・実験管理・データベースクライアント・可視化ツール・バージョン管理・クラウド CLI・論文管理ツールまで網羅。

**主なトピック:** Miniconda / JupyterLab / VS Code / PyCharm / W&B / MLflow / DBeaver / Tableau / DVC / Docker / Zotero

### 11 - DS 向けターミナル CLI ツールガイド

ターミナルで使う DS 向け CLI ツール。Python パッケージ管理・仮想環境・Jupyter の自動化・CSV/JSON のコマンドライン処理・ML 実験管理・クラウド CLI・コード品質ツールを紹介。

**主なトピック:** pip / conda / uv / papermill / nbstripout / csvkit / DuckDB CLI / MLflow / wandb / DVC / Ruff

### 12 - DS 向け Web サイトガイド

ブックマークしておくべき DS 向け Web サイト。公式ドキュメント・学習プラットフォーム・論文サイト・データセット・ML プラットフォーム・可視化ギャラリー・コンペティション・ニュースを整理。

**主なトピック:** scikit-learn / Kaggle / Coursera / fast.ai / arXiv / Papers With Code / Hugging Face / SIGNATE

### 13 - DS 向け SNS・情報発信ガイド

フォロー・購読すべき DS 向けの SNS アカウント・コミュニティ。ML 研究者の X アカウント・YouTube チャンネル・Discord サーバー・Reddit・ポッドキャストを紹介。

**主なトピック:** ML 研究者アカウント / 3Blue1Brown / StatQuest / Hugging Face Discord / r/MachineLearning / Latent Space

### 14 - DS プロジェクト構成ガイド

DS プロジェクトのディレクトリ構成・環境管理・再現性確保のベストプラクティス。Cookiecutter Data Science ベースの構成、environment.yml・pyproject.toml の使い分け、nbstripout・pre-commit hooks の設定を紹介。

**主なトピック:** ディレクトリ構成 / environment.yml / pyproject.toml / nbstripout / DVC / pre-commit / Makefile

### 15 - DS ワークフローガイド

データ取得からデプロイまでの一連のワークフローを具体的なコード例とともに解説。EDA・前処理・特徴量エンジニアリング・モデリング・評価の各ステップを実践的にまとめている。

**主なトピック:** EDA テンプレート / 欠損値処理 / 特徴量作成 / LightGBM / Optuna / 交差検証 / Streamlit / FastAPI

### 16 - DS のための SQL ガイド

DS が実務で使う SQL パターンを網羅。基本クエリから集約・JOIN・CTE・ウィンドウ関数・日付操作まで、DuckDB / PostgreSQL / BigQuery で動作するサンプルコード付き。

**主なトピック:** ウィンドウ関数 / CTE / LAG・LEAD / 移動平均 / サンプリング / コホート分析 / RFM 分析

### 17 - DS のための数学・統計ガイド

DS に必要な数学・統計の要点と学習ロードマップ。線形代数・微積分・確率・統計検定・回帰分析を DS の用途に絞って解説し、推奨リソースを紹介。

**主なトピック:** 線形代数 / 勾配降下法 / 確率分布 / ベイズの定理 / 仮説検定 / A/B テスト / 正則化

### 18 - LLM / 生成 AI 活用ガイド

DS が LLM を業務に活用するための実践ガイド。API の使い方・プロンプト設計・RAG・埋め込み・ファインチューニングを具体的なコード例とともに解説。

**主なトピック:** Claude API / OpenAI API / プロンプトエンジニアリング / RAG / Embeddings / LoRA / LangChain / Ollama

### 19 - Kaggle 攻略ガイド

Kaggle コンペティションに取り組むための実践的な攻略ガイド。コンペの選び方・EDA テンプレート・特徴量戦略・LightGBM テンプレート・アンサンブル・バリデーション戦略を紹介。

**主なトピック:** Kaggle API / EDA テンプレート / Target Encoding / LightGBM CV テンプレート / アンサンブル / スタッキング

### 20 - DS 学習ロードマップガイド

完全な初心者からプロフェッショナルな DS になるまでの学習ロードマップ。5 つのフェーズ（基礎固め → DS 基本スキル → 機械学習 → 実践・応用 → プロフェッショナル）に分けて、何を・どの順で・どのくらい学ぶかを体系的に示している。

**主なトピック:** 5 フェーズのロードマップ / フェーズ別の学習項目・確認ポイント / 推奨リソースマップ / キャリアパス / 転職戦略 / 学習の習慣づくり

## 目的別ショートカット

| やりたいこと | 参照先 |
|------------|--------|
| Python 環境を構築したい | [10](10-mac-apps-guide.md) セクション 1 |
| Jupyter 環境を整えたい | [10](10-mac-apps-guide.md) セクション 2・3 |
| パッケージ管理を理解したい | [11](11-terminal-tools-guide.md) セクション 1・2 |
| CSV / JSON をコマンドラインで処理したい | [11](11-terminal-tools-guide.md) セクション 4 |
| ML を基礎から学びたい | [12](12-web-resources-guide.md) セクション 2 |
| 最新の ML 論文を追いたい | [12](12-web-resources-guide.md) セクション 3 |
| データセットを探したい | [12](12-web-resources-guide.md) セクション 4 |
| ML 研究者をフォローしたい | [13](13-sns-guide.md) セクション 1 |
| ML を動画で学びたい | [13](13-sns-guide.md) セクション 2 |
| ML コミュニティに参加したい | [13](13-sns-guide.md) セクション 3 |
| プロジェクトのディレクトリ構成を整えたい | [14](14-project-structure-guide.md) セクション 1 |
| 環境管理ファイルの書き方を知りたい | [14](14-project-structure-guide.md) セクション 2 |
| EDA からモデリングの流れを知りたい | [15](15-workflow-guide.md) セクション 1〜7 |
| Streamlit でアプリを作りたい | [15](15-workflow-guide.md) セクション 8 |
| SQL でデータを抽出したい | [16](16-sql-guide.md) セクション 2〜5 |
| ウィンドウ関数を使いたい | [16](16-sql-guide.md) セクション 6 |
| ML に必要な数学を学びたい | [17](17-math-stats-guide.md) セクション 1 |
| A/B テストの方法を知りたい | [17](17-math-stats-guide.md) セクション 6 |
| LLM API を使いたい | [18](18-llm-guide.md) セクション 2 |
| RAG を構築したい | [18](18-llm-guide.md) セクション 4 |
| Kaggle コンペに参加したい | [19](19-kaggle-guide.md) セクション 1〜3 |
| LightGBM のテンプレートが欲しい | [19](19-kaggle-guide.md) セクション 6 |
| DS の学習ロードマップを知りたい | [20](20-learning-roadmap-guide.md) セクション 1 |
| DS のキャリアパスを知りたい | [20](20-learning-roadmap-guide.md) セクション 8 |
| 学習リソースをフェーズ別に探したい | [20](20-learning-roadmap-guide.md) セクション 7 |

## 推奨する学習順序

> **初心者の方へ**: まず [20 - DS 学習ロードマップガイド](20-learning-roadmap-guide.md) を読み、全体像を把握してから各ガイドに進むことをおすすめする。

```
[20: ロードマップ（全体像の把握）]
        ↓
[10: ツール導入] → [14: プロジェクト構成] → [15: ワークフロー]
                                                    ↓
[11: CLI ツール] → [16: SQL] → [17: 数学・統計] → [19: Kaggle 実践]
                                                    ↓
[12: Web リソース] → [13: SNS] → [18: LLM 活用]
```

1. **20** で学習の全体像とロードマップを把握する
2. **10・11** でツールを整える
3. **14** でプロジェクトの構成を理解する
4. **15** で実際のワークフローを学ぶ
5. **16・17** でSQL と数学・統計の基礎を固める
6. **19** で Kaggle で実践力を磨く
7. **18** で LLM を業務に活用する
8. **12・13** で継続的に情報収集する

## 元ガイドシリーズとの関係

10〜13 は、既存の **Web 開発者向けガイド（10〜13）** に対応する DS 専用版として作成した。
14〜19 は DS 固有の実務・スキルガイドとして新規に追加した。

| 番号 | Web 開発者向け（元ガイド） | DS 向け（本シリーズ） |
|------|------------------------|---------------------|
| 10 | [Mac おすすめアプリガイド](../10-mac-apps-guide.md) | [DS 向け Mac アプリガイド](10-mac-apps-guide.md) |
| 11 | [ターミナル CLI ツールガイド](../11-terminal-tools-guide.md) | [DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) |
| 12 | [おすすめ Web サイトガイド](../12-web-resources-guide.md) | [DS 向け Web サイトガイド](12-web-resources-guide.md) |
| 13 | [開発者向け SNS・情報発信ガイド](../13-sns-guide.md) | [DS 向け SNS・情報発信ガイド](13-sns-guide.md) |
| 14 | — | [DS プロジェクト構成ガイド](14-project-structure-guide.md) |
| 15 | — | [DS ワークフローガイド](15-workflow-guide.md) |
| 16 | — | [DS のための SQL ガイド](16-sql-guide.md) |
| 17 | — | [DS のための数学・統計ガイド](17-math-stats-guide.md) |
| 18 | — | [LLM / 生成 AI 活用ガイド](18-llm-guide.md) |
| 19 | — | [Kaggle 攻略ガイド](19-kaggle-guide.md) |
| 20 | — | [DS 学習ロードマップガイド](20-learning-roadmap-guide.md) |

ウィンドウ管理・ランチャー・汎用 CLI ツール（eza・bat・fzf 等）など、DS にも共通で役立つ内容は元ガイドを参照のこと。
