# Claude Code アプリケーション開発ガイド

## 0. はじめに

このガイドは **Claude Code を開発パートナーとして、実際に動くアプリケーションを作るための自分用リファレンス** です。

- **想定読者**: [Claude Code 応用・自動化ガイド](03-claude-code-advanced-guide.md) を読み終え、Claude Code のカスタマイズや自動化ができる
- **ゴール**: VBA で行っていた作業を現代的な技術で再現し、コマンドラインツール・Web アプリ・データベース連携を体験する
- **関連ガイド**:
  - [Claude Code 実践ガイド](02-claude-code-practical-guide.md) — Git・開発フロー（レベル 2）
  - [Claude Code 応用・自動化ガイド](03-claude-code-advanced-guide.md) — カスタマイズ・自動化（レベル 3）
  - [Claude Code 公開・運用ガイド](05-claude-code-deploy-guide.md) — 公開・運用（次のステップ）

> レベル 1〜3 は「Claude Code 自体の操作スキル」を高める内容だった。
> このガイドでは視点を切り替え、**「Claude Code を開発パートナーとして、実際に動くものを作る」** ことに焦点を当てる。
> VBA で例えると、VBE の使い方を覚えた段階から、実際に **Excel アドインや独立したツールを開発する** 段階への移行。

---

## 1. VBA の「あの作業」を Python で再現する

VBA ユーザーにとって最も親しみやすい入口。「Excel マクロでやっていたこと」は Python でもできる。

### Excel ファイルの読み書き

VBA で `Range("A1").Value` と書いていた操作は、Python では `openpyxl` や `pandas` というライブラリで行う。

| VBA | Python（pandas） |
|-----|-----------------|
| `Range("A1").Value` | `df.iloc[0, 0]` |
| `Cells(i, 1).Value` | `df.iloc[i-1, 0]` |
| `Range("A1:C10")` | `df.iloc[0:10, 0:3]` |
| `WorksheetFunction.Sum(Range("A:A"))` | `df["A"].sum()` |

### Claude Code への指示例

```
あなた: 「data/sales.xlsx を読み込んで、月ごとの売上合計を計算する Python スクリプトを作って。
        VBA の WorksheetFunction.Sum に相当する処理を pandas で書いて」

Claude: pandas を使って実装します...
```

### CSV の読み込みと集計

```python
import pandas as pd

# CSV を読み込む（VBA の QueryTable.Add に相当）
df = pd.read_csv("data/sales.csv")

# 月ごとの売上合計（VBA の SUMIF に相当）
monthly = df.groupby("月")["売上"].sum()
print(monthly)
```

> VBA では何十行も書いていた集計処理が、Python + pandas では数行で書ける。
> コードを覚える必要はない。Claude Code に「VBA でやっていた○○と同じ処理を Python で書いて」と伝えれば書いてくれる。

### ファイルの一括処理

VBA では `Dir` 関数でファイルをループしていた処理:

```
あなた: 「data フォルダ内の全 CSV ファイルを読み込んで、1 つのファイルに統合して」

Claude: glob と pandas を使って実装します...
```

---

## 2. プロジェクトの設計を Claude Code と一緒に考える

### いきなりコードを書かない

VBA では「とりあえず標準モジュールに書き始める」ことが多かったが、プロジェクト開発では **先に設計を考える** と後で楽になる。

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

> VBA で「標準モジュール 1 つに 1000 行書いて、どこに何があるかわからなくなった」経験があるなら、早めの分割がおすすめ。

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

ターミナルから実行して結果を得るプログラム。最もシンプルなアプリケーション形態。

```bash
# 実行例
python src/main.py data/sales.csv --month 2026-01
```

> VBA では `InputBox` でユーザーからの入力を受けていた。コマンドラインツールでは、実行時に引数として渡す。

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

**ブラウザで動くアプリケーション**。VBA のユーザーフォームに相当するものを、ブラウザの中で動かすイメージ。

| VBA ユーザーフォーム | Web アプリ |
|-------------------|----------|
| Excel の中で動く | ブラウザで動く |
| 自分の PC でしか使えない | URL を共有すれば誰でも使える |
| TextBox, ComboBox などの部品 | HTML の input, select などの部品 |
| ボタンクリックで VBA コードが動く | ボタンクリックで Python（サーバー側）が動く |

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

# ファイルアップロード（VBA の Application.GetOpenFilename に相当）
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

# テーブル作成（VBA の Worksheets.Add に相当）
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# データ挿入（VBA の Range("A1").Value = "..." に相当）
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ("田中太郎", "tanaka@example.com"))

# 検索（VBA の VLOOKUP / Find に相当）
cursor.execute("SELECT * FROM customers WHERE name LIKE ?", ("%田中%",))
results = cursor.fetchall()
```

### SQL を覚える必要はない

Claude Code に日本語で依頼すれば、SQL を書いてくれる。

```
あなた: 「customers テーブルから、今月登録された顧客の一覧を取得するクエリを書いて」
あなた: 「売上テーブルと顧客テーブルを結合して、顧客ごとの合計売上を計算して」
```

---

## 6. API を使って外部サービスと連携する

### API とは

**他のサービスのデータや機能を、プログラムから利用するための窓口**。

> VBA の対比: `CreateObject("MSXML2.XMLHTTP")` で Web サイトからデータを取得していたのと同じこと。Python ではもっと簡単に書ける。

### requests ライブラリ

```python
import requests

# API からデータを取得（VBA の XMLHTTP.Send に相当）
response = requests.get("https://api.example.com/data")
data = response.json()
print(data)
```

### Claude Code への指示例

```
あなた: 「天気予報 API を使って、東京の今日の天気を取得して表示するスクリプトを作って」

あなた: 「為替レート API を使って、USD/JPY のレートを取得して CSV に保存するスクリプトを作って」
```

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

---

## 7. テストを書く

### テストとは

**コードが正しく動くことを自動で確認する仕組み**。

> VBA の対比: イミディエイトウィンドウで `? MyFunction(10)` と入力して結果を手動確認していた。テストコードはそれを自動化する。手動だと「確認し忘れ」が起きるが、テストコードなら毎回同じチェックを確実に実行できる。

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
