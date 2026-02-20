# Claude Code アプリケーション開発ガイド

## 0. はじめに

このガイドは **Claude Code を開発パートナーとして、実際に動くアプリケーションを作るための学習ガイド** です。

- **想定読者**: プログラミング初心者（[Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) を読み終え、Claude Code のカスタマイズや自動化ができる）
- **ゴール**: コマンドラインツール・Web アプリ・データベース連携を体験し、実際に動くアプリケーションを作れるようになる
- **関連ガイド**:
  - [Claude Code 実践ガイド](11-claude-code-practical-guide.md) — Git・開発フロー（レベル 2）
  - [Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) — カスタマイズ・自動化（レベル 3）
  - [Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md) — 公開・運用（次のステップ）
  - [セキュリティ基礎ガイド](20-security-basics-guide.md) — API キーの安全な管理
  - [テスト入門ガイド](21-testing-intro-guide.md) — テストの書き方
  - [Docker 入門ガイド](22-docker-intro-guide.md) — 環境構築の基礎
  - [Web 基礎ガイド](23-web-basics-guide.md) — Web アプリの仕組み
  - [データベース入門ガイド](24-database-intro-guide.md) — データベースの使い方
  - [API ガイド](25-api-guide.md) — API の使い方

> レベル 1〜3 は「Claude Code 自体の操作スキル」を高める内容でした。
> このガイドでは視点を切り替え、**「Claude Code を開発パートナーとして、実際に動くものを作る」** ことに焦点を当てます。
> プログラミングの基礎を学んだ段階から、実際に **実用的なツールやアプリケーションを開発する** 段階への移行です。

---

## 1. データ処理の基本を Python で学ぶ

プログラミング初心者にとって最も親しみやすい入口。「Excel でやっていたこと」は Python でもできます。

### Excel ファイルの読み書き

Excel の操作は、Python では `openpyxl` や `pandas` というライブラリで行います。

| Excel での操作 | Python（pandas） |
|-----|-----------------|
| セル A1 の値を読む | `df.iloc[0, 0]` |
| i 行目の 1 列目を読む | `df.iloc[i-1, 0]` |
| セル範囲 A1:C10 を選択 | `df.iloc[0:10, 0:3]` |
| 列全体の合計を計算 | `df["A"].sum()` |

### Claude Code への指示例

```
あなた: 「data/sales.xlsx を読み込んで、月ごとの売上合計を計算する Python スクリプトを作って」

Claude: pandas を使って実装します...
```

### CSV の読み込みと集計

```python
import pandas as pd

# CSV を読み込む
df = pd.read_csv("data/sales.csv")

# 月ごとの売上合計を計算
monthly = df.groupby("月")["売上"].sum()
print(monthly)
```

> コードを覚える必要はありません。Claude Code に「Excel でやっていた○○と同じ処理を Python で書いて」と伝えれば書いてくれます。

### ファイルの一括処理

複数のファイルを一括で処理する場合も、Claude Code に依頼できます。

```
あなた: 「data フォルダ内の全 CSV ファイルを読み込んで、1 つのファイルに統合して」

Claude: glob と pandas を使って実装します...
```

---

## 2. プロジェクトの設計を Claude Code と一緒に考える

### いきなりコードを書かない

プロジェクト開発では **先に設計を考える** と後で楽になります。

### Claude Code に壁打ちしてもらう

```
あなた: 「毎月の経費レポートを自動生成するツールを作りたい。
        入力: 経費データの CSV
        出力: 部門ごとの集計と Excel レポート
        どういう構成にすべき？」

Claude: 以下の構成を提案します。
        expense-report/
          src/
            main.py          # メインの処理フロー
            data_loader.py   # CSV 読み込み
            calculator.py    # 集計ロジック
            report_writer.py # Excel レポート出力
          tests/
            test_calculator.py
          data/              # 入力データ置き場
          output/            # 出力レポート置き場
          requirements.txt
          CLAUDE.md
```

### 単一スクリプト vs モジュール分割

| 規模 | 構成 | 目安 |
|------|------|------|
| 小さい（〜100 行） | `main.py` 1 ファイル | ちょっとした変換・集計 |
| 中くらい（100〜500 行） | 機能ごとに 3〜5 ファイル | ツールやユーティリティ |
| 大きい（500 行〜） | パッケージ構成 | Web アプリやサービス |

> コードが長くなってきたら、早めに機能ごとにファイルを分割することをおすすめします。1 つのファイルに全部書くと、後で「どこに何があるかわからなくなる」問題が起きやすくなります。

### プランモードで設計 → 承認 → 実装

```
あなた: /plan
あなた: 「上の構成で実装してほしい。まず計画を立てて」

Claude: 実装計画:
        ステップ 1: プロジェクト構成の作成
        ステップ 2: data_loader.py の実装
        ステップ 3: calculator.py の実装
        ...

あなた: （計画を確認して承認）
あなた: 「計画に沿って実装して」
```

---

## 3. コマンドラインツールを作る

### コマンドラインツールとは

ターミナルから実行して結果を得るプログラム。最もシンプルなアプリケーション形態です。

```bash
# 実行例
python src/main.py data/sales.csv --month 2026-01
```

> コマンドラインツールでは、ユーザーからの入力を実行時の引数として渡します。GUI を作る必要がないので、最も手軽にツールを作成できます。

### 引数の受け取り

```python
import argparse

parser = argparse.ArgumentParser(description="CSV 集計ツール")
parser.add_argument("input_file", help="入力 CSV ファイルのパス")
parser.add_argument("--month", help="集計対象の月（例: 2026-01）")
args = parser.parse_args()

print(f"入力ファイル: {args.input_file}")
print(f"対象月: {args.month}")
```

### Claude Code と一緒に作る

```
あなた: 「CSV を読み込んで月ごとの売上合計を出力するコマンドラインツールを作って。
        引数で入力ファイルと対象月を指定できるようにして。
        --help でヘルプが表示されるようにして」

Claude: argparse と pandas を使って実装します...
```

### 実行と動作確認

```
あなた: 「作ったツールを data/sales.csv で実行して、動作確認して」

Claude: python src/main.py data/sales.csv --month 2026-01 を実行します。
        結果: ...
```

---

## 4. Web アプリの基本を知る

### Web アプリとは

**ブラウザで動くアプリケーション**。デスクトップアプリと違い、URL を共有すれば誰でも使えます。

| デスクトップアプリ | Web アプリ |
|-------------------|----------|
| 特定のソフト（Excel など）で動く | ブラウザで動く |
| 自分の PC でしか使えない | URL を共有すれば誰でも使える |
| インストールが必要 | ブラウザがあればすぐ使える |
| ボタンクリックでローカルのコードが動く | ボタンクリックでサーバー側のコードが動く |

### 最も手軽な方法: Streamlit

Streamlit は **Python だけで Web アプリが作れるフレームワーク**。HTML や CSS を書く必要がない。

```
あなた: 「Streamlit で CSV ファイルをアップロードして集計結果をグラフで表示する Web アプリを作って」

Claude: Streamlit で実装します...
```

作られるコードのイメージ:

```python
import streamlit as st
import pandas as pd

st.title("売上集計ダッシュボード")

# ファイルアップロード
uploaded_file = st.file_uploader("CSV ファイルを選択", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)  # テーブル表示

    # グラフ表示
    monthly = df.groupby("月")["売上"].sum()
    st.bar_chart(monthly)
```

実行:

```bash
streamlit run app.py
```

ブラウザが自動で開き、アプリが表示される。

> Web アプリの仕組みについて詳しくは [Web 基礎ガイド](23-web-basics-guide.md) を参照してください。

### Flask（もう少し本格的に作りたいとき）

Flask は Web アプリの定番フレームワーク。HTML を自分で書く必要があるが、自由度が高い。

```
あなた: 「Flask で経費入力フォームを作って。入力されたデータを SQLite に保存して」

Claude: Flask + SQLite で実装します...
```

> 最初は Streamlit で試して、物足りなくなったら Flask に移行するのがおすすめ。

---

## 5. データベースを使う

### データベースとは

**データを構造的に保存・検索するための専用システム**。

| Excel シート | データベース |
|-------------|------------|
| 行と列でデータを管理 | テーブル（表）でデータを管理（ここまでは同じ） |
| 数千行で重くなる | 数百万行でも高速 |
| `VLOOKUP` で検索 | `SELECT ... WHERE ...` で検索 |
| 複数シートをまたぐ処理が複雑 | テーブル間の結合（JOIN）が簡単 |
| ファイルを開いている人しか使えない | 複数のアプリから同時にアクセスできる |

### SQLite: 最も手軽なデータベース

SQLite は **ファイル 1 つで動く** 軽量データベース。インストール不要で、Python に標準搭載されている。

### 基本操作

```
あなた: 「SQLite で顧客管理データベースを作って。
        テーブル: customers（id, name, email, created_at）
        サンプルデータを 5 件入れて。
        名前で検索する関数も作って」

Claude: sqlite3 を使って実装します...
```

作られるコードのイメージ:

```python
import sqlite3

# データベースに接続（ファイルがなければ自動作成）
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# データ挿入
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("田中太郎", "tanaka@example.com"))

# 検索
cursor.execute("SELECT * FROM customers WHERE name LIKE ?", ("%田中%",))
results = cursor.fetchall()
```

### SQL を覚える必要はない

Claude Code に日本語で依頼すれば、SQL を書いてくれる。

```
あなた: 「customers テーブルから、今月登録された顧客の一覧を取得するクエリを書いて」
あなた: 「売上テーブルと顧客テーブルを結合して、顧客ごとの合計売上を計算して」
```

> データベースについて詳しくは [データベース入門ガイド](24-database-intro-guide.md) を参照してください。

---

## 6. API を使って外部サービスと連携する

### API とは

**他のサービスのデータや機能を、プログラムから利用するための窓口**。

> 例えば、天気予報サービスや為替レートサービスが提供している API を使うと、プログラムから最新の情報を取得できます。

### requests ライブラリ

```python
import requests

# API からデータを取得
response = requests.get("https://api.example.com/data")
data = response.json()
print(data)
```

### Claude Code への指示例

```
あなた: 「天気予報 API を使って、東京の今日の天気を取得して表示するスクリプトを作って」

あなた: 「為替レート API を使って、USD/JPY のレートを取得して CSV に保存するスクリプトを作って」
```

> API の使い方について詳しくは [API ガイド](25-api-guide.md) を参照してください。

### API キーの管理

多くの API は **API キー**（パスワードのようなもの）が必要。これをコードに直書きしてはいけない。

```
× コードに直書き（絶対にやらない）
api_key = "sk-abc123..."

○ .env ファイルに書いて読み込む
```

`.env` ファイル:

```
API_KEY=sk-abc123...
```

Python コード:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
```

**重要**: `.env` ファイルは必ず `.gitignore` に追加する。GitHub に API キーが公開されると悪用される。

```
あなた: 「.env ファイルに API キーを管理する仕組みを作って。.gitignore にも追加して」
```

> API キーの安全な管理について詳しくは [セキュリティ基礎ガイド](20-security-basics-guide.md) を参照してください。

---

## 7. テストを書く

### テストとは

**コードが正しく動くことを自動で確認する仕組み**。

> プログラムを修正するたびに、手動で動作確認するのは大変です。テストコードを書いておけば、自動で確認できるので「確認し忘れ」を防げます。

### pytest の基本

```python
# tests/test_calculator.py

from src.calculator import calculate_total

def test_calculate_total_basic():
    """基本的な合計計算"""
    assert calculate_total([100, 200, 300]) == 600

def test_calculate_total_empty():
    """空リストの場合は 0"""
    assert calculate_total([]) == 0

def test_calculate_total_with_tax():
    """税込み計算"""
    assert calculate_total([100], tax_rate=0.1) == 110
```

実行:

```bash
pytest tests/ -v
```

### Claude Code にテストを書いてもらう

```
あなた: 「calculator.py の calculate_total 関数のテストを作って。
        正常系、空リスト、税率指定のケースをカバーして」

Claude: pytest を使ってテストを作成します...
```

> テストの書き方について詳しくは [テスト入門ガイド](21-testing-intro-guide.md) を参照してください。

### テストがあると安心してリファクタリングできる

テストがあれば、Claude Code に大胆な変更を依頼しても安全。

```
あなた: 「calculator.py をリファクタリングして。テストが通ることを確認して」

Claude: リファクタリング後にテストを実行します...
        全テスト合格を確認しました。
```

---

## 8. 困ったときは

### よくある問題と対処法

| 症状 | 対処法 |
|------|--------|
| `ModuleNotFoundError: No module named 'pandas'` | `pip install pandas` でインストール。`requirements.txt` に追記 |
| パッケージのバージョン競合 | 仮想環境（`python -m venv .venv`）を作ってやり直す |
| ライブラリの使い方がわからない | Claude Code に「pandas の groupby の使い方を教えて」と聞く |
| Streamlit のアプリが表示されない | ブラウザで `http://localhost:8501` にアクセスしているか確認 |
| SQLite のデータが消えた | `app.db` ファイルが残っているか確認。Git に含めていれば復元可能 |
| API が 401 エラーを返す | API キーが正しいか確認。`.env` から正しく読み込めているか確認 |

### 仮想環境の基本

プロジェクトごとにパッケージを隔離する仕組み。パッケージの競合を防げる。

```bash
# 仮想環境を作成
python -m venv .venv

# 仮想環境を有効化
source .venv/bin/activate

# パッケージをインストール
pip install pandas openpyxl flask

# インストール済みパッケージを記録
pip freeze > requirements.txt
```

> これも Claude Code に「仮想環境をセットアップして」と頼める。

> 環境構築について詳しくは [Docker 入門ガイド](22-docker-intro-guide.md) も参照してください。より再現性の高い環境を構築できます。

---

## 9. 次のステップ

このガイドで基本的なアプリケーション開発を体験しました。次は以下のガイドで学習を深めることをおすすめします。

- [Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md) — アプリを公開・運用する方法
- [Claude Code Skills ガイド](15-claude-code-skills-guide.md) — よく使う機能を Skills として登録
- [Claude Code マルチエージェントガイド](16-claude-code-multi-agent-guide.md) — 複数の Claude エージェントを連携させる
- [開発学習ロードマップ](30-learning-roadmap-guide.md) — さらなる学習の進め方

各技術の詳細は、以下の専門ガイドを参照してください。

- [セキュリティ基礎ガイド](20-security-basics-guide.md) — セキュリティの基本
- [テスト入門ガイド](21-testing-intro-guide.md) — テスト駆動開発
- [Docker 入門ガイド](22-docker-intro-guide.md) — コンテナ技術
- [Web 基礎ガイド](23-web-basics-guide.md) — Web 技術の基礎
- [データベース入門ガイド](24-database-intro-guide.md) — データベース設計
- [API ガイド](25-api-guide.md) — API 設計と実装
