# データ分析入門ガイド

## 0. はじめに

### 想定読者

- プログラミング初心者（Python の基本文法を理解している方）
- データの集計・可視化を Python で行いたい方
- Mac 環境で開発を始めたばかりの方

### ゴール

このガイドを読むことで、以下のスキルを習得できます。

- データ分析の全体像と Python を使う利点を理解する
- pandas を使ったデータの読み込み・加工・集計ができる
- matplotlib でグラフを作成・保存できる
- Jupyter Notebook で対話的にデータ分析を行える
- CSV/Excel データを読み込んで分析・可視化する一連の流れを実践する
- Claude Code を活用してデータ分析を効率化する

### 関連ガイド

- [VS Code ガイド](00-vscode-guide.md) - エディタの基本操作
- [Claude Code 基本操作ガイド](10-claude-code-guide.md) - AI を活用した開発環境
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) - アプリケーション開発の実践
- [Python 環境構築ガイド](26-python-setup-guide.md) - Python のインストールと設定
- [学習ロードマップ](30-learning-roadmap-guide.md) - 学習の全体計画

---

## 1. データ分析とは

### データ分析の全体像

データ分析は、生のデータから有用な情報を引き出す作業です。一般的に以下の流れで進めます。

```
データ収集 → データ整理 → 集計・分析 → 可視化 → レポート作成
```

| ステップ | やること | 使うツール |
|----------|----------|------------|
| データ収集 | CSV・Excel・データベースからデータを取得 | pandas |
| データ整理 | 欠損値の処理、型変換、不要列の削除 | pandas |
| 集計・分析 | グループ集計、統計量の算出、傾向の把握 | pandas |
| 可視化 | グラフやチャートでデータを視覚的に表現 | matplotlib |
| レポート作成 | 分析結果をまとめて共有 | Jupyter Notebook |

### Python でデータ分析をする理由

Python を使うと、大量のデータを効率よく処理でき、分析コードをそのまま共有・再実行できます。Git でバージョン管理でき、豊富なライブラリで機能を拡張できるのも大きな利点です。

1. **pandas** - データの読み込み・加工・集計を簡潔に書ける
2. **matplotlib / seaborn** - 美しいグラフを柔軟に作成できる
3. **Jupyter Notebook** - コードと結果を一緒に記録できる
4. **豊富なエコシステム** - 機械学習（scikit-learn）、統計（scipy）など拡張が容易

---

## 2. pandas 入門

### インストール

ターミナルで以下を実行します。

```bash
pip install pandas openpyxl
```

> **補足**: `openpyxl` は Excel ファイル（.xlsx）を読み書きするために必要です。

### DataFrame の基本

pandas の中心的なデータ構造が **DataFrame**（表形式のデータ）です。

```python
import pandas as pd

# DataFrame を手動で作成
df = pd.DataFrame({
    "名前": ["田中", "鈴木", "佐藤", "高橋"],
    "部署": ["営業", "開発", "営業", "開発"],
    "売上": [150, 200, 180, 220],
})

print(df)
```

出力:

```
   名前  部署   売上
0  田中  営業   150
1  鈴木  開発   200
2  佐藤  営業   180
3  高橋  開発   220
```

### CSV / Excel ファイルの読み込み

```python
# CSV ファイルを読み込む
df = pd.read_csv("sales_data.csv")

# Excel ファイルを読み込む
df = pd.read_excel("sales_data.xlsx", sheet_name="Sheet1")

# 先頭 5 行を確認する
print(df.head())

# データの概要を確認する
print(df.info())
```

### 列の選択・フィルタリング

```python
# 1 列を選択
print(df["名前"])

# 複数列を選択
print(df[["名前", "売上"]])

# 条件でフィルタリング
high_sales = df[df["売上"] >= 200]
print(high_sales)

# 複数条件（AND）
result = df[(df["部署"] == "営業") & (df["売上"] >= 150)]
print(result)
```

### 基本的な集計

```python
# 全体の統計量を確認
print(df.describe())

# 部署ごとの売上合計
print(df.groupby("部署")["売上"].sum())

# 部署ごとの人数カウント
print(df["部署"].value_counts())

# 売上の平均
print(df["売上"].mean())
```

---

## 3. matplotlib でグラフ作成

### インストール

```bash
pip install matplotlib
```

### 日本語フォント設定（Mac）

Mac でグラフに日本語を表示するには、フォント設定が必要です。

```python
import matplotlib.pyplot as plt
import matplotlib

# Mac のヒラギノフォントを指定
matplotlib.rcParams["font.family"] = "Hiragino Sans"
# マイナス記号の文字化け対策
matplotlib.rcParams["axes.unicode_minus"] = False
```

> **Tip**: この設定はスクリプトの先頭に一度書いておけば、以降のすべてのグラフに適用されます。

### 棒グラフ

```python
import matplotlib.pyplot as plt

categories = ["営業", "開発", "人事", "経理"]
values = [350, 420, 180, 210]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color="steelblue")
plt.title("部署別売上")
plt.xlabel("部署")
plt.ylabel("売上（万円）")
plt.tight_layout()
plt.show()
```

### 折れ線グラフ

```python
months = ["1月", "2月", "3月", "4月", "5月", "6月"]
sales = [120, 135, 150, 145, 170, 190]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", color="coral", linewidth=2)
plt.title("月別売上推移")
plt.xlabel("月")
plt.ylabel("売上（万円）")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
```

### 円グラフ

```python
labels = ["製品A", "製品B", "製品C", "製品D"]
sizes = [35, 25, 22, 18]
colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"]

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("製品別売上構成比")
plt.tight_layout()
plt.show()
```

### グラフの保存

```python
# PNG として保存（高解像度）
plt.savefig("sales_chart.png", dpi=150, bbox_inches="tight")

# PDF として保存
plt.savefig("sales_chart.pdf", bbox_inches="tight")
```

> **注意**: `plt.savefig()` は `plt.show()` より前に呼び出してください。`plt.show()` の後はグラフがリセットされます。

---

## 4. Jupyter Notebook

### Jupyter Notebook とは

Jupyter Notebook は、コードの実行結果をその場で確認しながら分析を進められる対話型の開発環境です。コード・テキスト・グラフを 1 つのファイル（`.ipynb`）にまとめられます。

### インストールと起動

```bash
# インストール
pip install jupyter

# 起動（ブラウザが自動で開く）
jupyter notebook
```

### セルの種類

| セルの種類 | 用途 | 内容 |
|------------|------|------|
| **Code セル** | Python コードを書いて実行する | `import pandas as pd` など |
| **Markdown セル** | 説明文や見出しを書く | `# 分析の目的` など |

### 基本操作

| 操作 | ショートカット |
|------|----------------|
| セルを実行 | `Shift + Enter` |
| 上にセルを追加 | `A`（コマンドモード） |
| 下にセルを追加 | `B`（コマンドモード） |
| セルを削除 | `D D`（コマンドモード） |
| コードセルに変更 | `Y`（コマンドモード） |
| マークダウンセルに変更 | `M`（コマンドモード） |
| コマンドモードに切り替え | `Esc` |
| 編集モードに切り替え | `Enter` |

### VS Code での利用

VS Code でも Jupyter Notebook を使うことができます。

1. VS Code で拡張機能「**Jupyter**」をインストール
2. `.ipynb` ファイルを開く、または `Cmd + Shift + P` → `Jupyter: Create New Notebook`
3. セルにコードを入力して `Shift + Enter` で実行

> **Tip**: VS Code で使う場合はブラウザを開く必要がなく、他のファイルとの行き来もスムーズです。

---

## 5. 実践: CSV/Excel データの分析

ここでは、売上データを題材に、データ分析の一連の流れを実践します。

### 5.1 サンプルデータの準備

以下の Python コードでサンプル CSV を作成します。

```python
import pandas as pd

data = {
    "日付": ["2025-01-05", "2025-01-12", "2025-01-20", "2025-02-03",
             "2025-02-14", "2025-02-28", "2025-03-10", "2025-03-22",
             "2025-03-30", "2025-04-05"],
    "商品名": ["商品A", "商品B", "商品A", "商品C", "商品B",
              "商品A", "商品C", "商品B", "商品A", "商品C"],
    "カテゴリ": ["食品", "飲料", "食品", "日用品", "飲料",
                "食品", "日用品", "飲料", "食品", "日用品"],
    "数量": [10, 5, 8, None, 12, 6, 3, 9, 15, 7],
    "単価": [500, 300, 500, 800, 300, 500, 800, 300, 500, 800],
}

df = pd.DataFrame(data)
df.to_csv("sample_sales.csv", index=False)
print("サンプルデータを作成しました")
```

### 5.2 データの読み込みと概要把握

```python
df = pd.read_csv("sample_sales.csv")

# データの先頭を確認
print(df.head())

# データの形状（行数・列数）
print(f"行数: {df.shape[0]}, 列数: {df.shape[1]}")

# 各列のデータ型と欠損値の有無
print(df.info())

# 基本統計量
print(df.describe())
```

### 5.3 データクリーニング

```python
# 欠損値の確認
print(df.isnull().sum())

# 欠損値を中央値で埋める
df["数量"] = df["数量"].fillna(df["数量"].median())

# 日付列を日付型に変換
df["日付"] = pd.to_datetime(df["日付"])

# 売上列を追加
df["売上"] = df["数量"] * df["単価"]

print(df.head())
```

### 5.4 集計・グラフ作成

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "Hiragino Sans"

# カテゴリ別売上集計
category_sales = df.groupby("カテゴリ")["売上"].sum().sort_values(ascending=False)
print(category_sales)

# 棒グラフで可視化
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="steelblue")
plt.title("カテゴリ別売上合計")
plt.ylabel("売上（円）")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("category_sales.png", dpi=150)
plt.show()
```

### 5.5 結果の保存

```python
# 集計結果を CSV に保存
summary = df.groupby("カテゴリ").agg(
    売上合計=("売上", "sum"),
    平均売上=("売上", "mean"),
    件数=("売上", "count"),
).reset_index()

summary.to_csv("sales_summary.csv", index=False)
print("集計結果を保存しました")

# Excel に保存
summary.to_excel("sales_summary.xlsx", index=False)
print("Excel ファイルとしても保存しました")
```

---

## 6. Claude Code でデータ分析

Claude Code を使うと、自然言語の指示だけでデータ分析のコードを生成・実行できます。

### データ分析を依頼する指示例

以下のようなプロンプトで Claude Code にデータ分析を依頼できます。

| 目的 | プロンプト例 |
|------|-------------|
| データの概要把握 | `sample_sales.csv を読み込んで、データの概要を教えて` |
| 集計 | `カテゴリ別に売上の合計と平均を集計して` |
| グラフ作成 | `月別の売上推移を折れ線グラフにして` |
| データクリーニング | `欠損値を確認して適切に処理して` |
| レポート作成 | `分析結果を Jupyter Notebook にまとめて` |

### pandas コードの生成と実行

Claude Code にデータファイルのパスを伝えるだけで、分析コードを生成してくれます。

```
あなた: sample_sales.csv を読み込んで、商品別の売上合計を集計してください

Claude Code: CSV を読み込み、商品別の売上を集計します。
（pandas コードを生成・実行し、結果を表示）
```

> **Tip**: Claude Code はプロジェクトフォルダ内のファイルを直接読み込めるため、ファイルパスだけ指示すれば自動的にコードを書いて実行してくれます。

### グラフのカスタマイズ依頼

生成されたグラフに対して、追加の指示で細かいカスタマイズが可能です。

```
あなた: このグラフの色を緑系に変えて、タイトルのフォントサイズを大きくして

あなた: 棒グラフの上に数値を表示して

あなた: このグラフを PDF で保存して
```

### Claude Code 活用のコツ

1. **具体的な指示を出す** - 「いい感じに分析して」ではなく「カテゴリ別の売上合計を棒グラフにして」
2. **ファイルパスを明示する** - 分析対象のファイル名を正確に伝える
3. **段階的に依頼する** - まずデータの概要を確認してから、集計やグラフ作成に進む
4. **修正を繰り返す** - 結果を見ながら「もう少し見やすくして」と改善を依頼する

---

## よく使う pandas メソッド一覧

| メソッド | 説明 | 使用例 |
|----------|------|--------|
| `read_csv()` | CSV ファイルを読み込む | `pd.read_csv("data.csv")` |
| `read_excel()` | Excel ファイルを読み込む | `pd.read_excel("data.xlsx")` |
| `head()` | 先頭 n 行を表示（デフォルト 5） | `df.head(10)` |
| `tail()` | 末尾 n 行を表示 | `df.tail(10)` |
| `info()` | データ型と欠損値を確認 | `df.info()` |
| `describe()` | 基本統計量を表示 | `df.describe()` |
| `shape` | 行数・列数を取得 | `df.shape` |
| `columns` | 列名の一覧を取得 | `df.columns` |
| `dtypes` | 各列のデータ型を確認 | `df.dtypes` |
| `isnull().sum()` | 欠損値の数を確認 | `df.isnull().sum()` |
| `fillna()` | 欠損値を埋める | `df["col"].fillna(0)` |
| `dropna()` | 欠損値のある行を削除 | `df.dropna()` |
| `groupby()` | グループ化して集計 | `df.groupby("col").sum()` |
| `value_counts()` | 値の出現回数を集計 | `df["col"].value_counts()` |
| `sort_values()` | 値でソート | `df.sort_values("col", ascending=False)` |
| `merge()` | 2 つの DataFrame を結合 | `pd.merge(df1, df2, on="key")` |
| `to_csv()` | CSV ファイルに保存 | `df.to_csv("out.csv", index=False)` |
| `to_excel()` | Excel ファイルに保存 | `df.to_excel("out.xlsx", index=False)` |

---

## 困ったときは

| 症状 | 原因 | 対処法 |
|------|------|--------|
| `ModuleNotFoundError: No module named 'pandas'` | pandas がインストールされていない | `pip install pandas` を実行 |
| `ModuleNotFoundError: No module named 'openpyxl'` | openpyxl がインストールされていない | `pip install openpyxl` を実行 |
| グラフの日本語が文字化け（豆腐になる） | フォント設定がされていない | `matplotlib.rcParams["font.family"] = "Hiragino Sans"` を追加 |
| `FileNotFoundError` | ファイルパスが間違っている | `ls` コマンドでファイルの場所を確認 |
| `UnicodeDecodeError` | CSV の文字コードが合っていない | `pd.read_csv("data.csv", encoding="cp932")` を試す |
| `ParserError` | CSV の区切り文字が違う | `pd.read_csv("data.csv", sep="\t")` でタブ区切りを指定 |
| `KeyError: '列名'` | 列名が存在しない | `df.columns` で列名を確認 |
| Jupyter Notebook が起動しない | ポートが使用中の場合がある | `jupyter notebook --port=8889` で別ポートを指定 |
| `plt.show()` でグラフが表示されない | バックエンドの問題 | Jupyter Notebook で `%matplotlib inline` を先頭に追加 |

---

## 関連ガイド

- [VS Code ガイド](00-vscode-guide.md) - エディタの基本操作
- [Claude Code 基本操作ガイド](10-claude-code-guide.md) - Claude Code の基本的な使い方
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) - アプリケーション開発の実践
- [Python 環境構築ガイド](26-python-setup-guide.md) - Python のインストールと設定
- [学習ロードマップ](30-learning-roadmap-guide.md) - 次に何を学ぶべきかの全体計画
