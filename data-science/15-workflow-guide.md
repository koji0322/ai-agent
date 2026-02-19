# DS ワークフローガイド

## 0. はじめに

このガイドは **データサイエンスの一連のワークフロー（EDA → 特徴量 → モデリング → 評価 → デプロイ）を実践的にまとめた自分用リファレンス** です。

- **想定読者**: DS のツールは揃い、プロジェクト構成も理解した。実際の分析フローを体系的に知りたい
- **ゴール**: データ取得からモデルのデプロイまでの一連のワークフローを、具体的なコード例とともに理解できるようになる
- **前提**: [14 - DS プロジェクト構成ガイド](14-project-structure-guide.md) のディレクトリ構成を理解していること
- **関連ガイド**: [14 - DS プロジェクト構成ガイド](14-project-structure-guide.md)、[16 - DS のための SQL ガイド](16-sql-guide.md)

> **14 との棲み分け**: [14](14-project-structure-guide.md) は **プロジェクトの構成・環境** を扱った。
> このガイドでは **実際の分析作業フロー** に焦点を当てる。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. ワークフロー全体像](#1-ワークフロー全体像) | DS プロジェクトの 7 ステップ |
| [2. データ取得・理解](#2-データ取得理解) | データの読み込み・基本統計量・型確認 |
| [3. 探索的データ分析（EDA）](#3-探索的データ分析eda) | 分布・相関・欠損値・外れ値の確認 |
| [4. データ前処理](#4-データ前処理) | 欠損値処理・エンコーディング・スケーリング |
| [5. 特徴量エンジニアリング](#5-特徴量エンジニアリング) | 特徴量の作成・選択・重要度分析 |
| [6. モデリング](#6-モデリング) | ベースライン → 複数モデル比較 → ハイパーパラメータチューニング |
| [7. 評価・検証](#7-評価検証) | 交差検証・評価指標・過学習の検出 |
| [8. デプロイ・共有](#8-デプロイ共有) | Streamlit・API 化・レポート作成 |
| [9. まとめ — ワークフローチェックリスト](#9-まとめ--ワークフローチェックリスト) | 各段階のチェック項目 |

---

## 1. ワークフロー全体像

DS プロジェクトは以下の 7 ステップで進む。必ずしも直線的ではなく、EDA と特徴量の間を行き来することが多い。

### 7 ステップの流れ

| ステップ | 内容 | 主なツール |
|---------|------|-----------|
| 1. データ取得・理解 | データの読み込み・基本情報の把握 | pandas・SQL・DuckDB |
| 2. EDA（探索的データ分析） | データの分布・関係性・問題点を可視化で把握 | pandas・Matplotlib・Seaborn |
| 3. データ前処理 | 欠損値・外れ値・型変換・エンコーディング | pandas・scikit-learn |
| 4. 特徴量エンジニアリング | 予測に有効な特徴量の作成・選択 | pandas・Feature-engine |
| 5. モデリング | モデルの選択・学習・ハイパーパラメータ調整 | scikit-learn・LightGBM・XGBoost |
| 6. 評価・検証 | モデルの性能評価・過学習の検出・比較 | scikit-learn・W&B |
| 7. デプロイ・共有 | 予測 API・ダッシュボード・レポートの作成 | Streamlit・FastAPI・MLflow |

```
[データ取得] → [EDA] ⇄ [前処理] ⇄ [特徴量] → [モデリング] ⇄ [評価] → [デプロイ]
                ↑_________________________↓
                    （反復・改善）
```

---

## 2. データ取得・理解

まず「どんなデータなのか」を把握する。コードを書く前にデータの全体像を掴む。

### データの読み込み

```python
import pandas as pd

# CSV
df = pd.read_csv("data/raw/train.csv")

# Excel
df = pd.read_excel("data/raw/data.xlsx", sheet_name="Sheet1")

# Parquet（高速・推奨）
df = pd.read_parquet("data/raw/data.parquet")

# SQL（DuckDB 経由）
import duckdb
df = duckdb.sql("SELECT * FROM 'data/raw/train.csv'").df()
```

### 基本情報の確認

```python
# データの概要
df.shape                    # 行数・列数
df.head()                   # 最初の 5 行
df.tail()                   # 最後の 5 行
df.info()                   # 列名・型・非 null 数
df.dtypes                   # 各列のデータ型
df.describe()               # 数値列の基本統計量
df.describe(include="object")  # カテゴリ列の統計量

# 欠損値の確認
df.isnull().sum()           # 列ごとの欠損数
df.isnull().mean()          # 列ごとの欠損率

# ユニーク値の確認
df.nunique()                # 列ごとのユニーク値数
df["category"].value_counts()  # カテゴリの出現頻度
```

**確認すべき項目チェックリスト:**

| 確認項目 | 確認方法 | 注目ポイント |
|---------|---------|-------------|
| データサイズ | `df.shape` | 行数・列数は想定通りか |
| データ型 | `df.dtypes` | 数値が object になっていないか |
| 欠損値 | `df.isnull().mean()` | 欠損率が高い列はあるか |
| 重複行 | `df.duplicated().sum()` | 重複データがないか |
| ターゲット変数 | `df["target"].value_counts()` | クラス不均衡がないか |
| ID 列 | `df["id"].nunique() == len(df)` | ユニークキーが正しいか |

---

## 3. 探索的データ分析（EDA）

データの傾向・パターン・問題点を可視化で発見する。

### 数値変数の分布

```python
import matplotlib.pyplot as plt
import seaborn as sns

# ヒストグラム
df.hist(figsize=(16, 12), bins=30)
plt.tight_layout()
plt.savefig("reports/figures/histograms.png")

# 特定の列の分布
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(df["price"], kde=True, ax=ax[0])
sns.boxplot(x=df["price"], ax=ax[1])
plt.tight_layout()
```

### 相関分析

```python
# 相関行列
corr = df.select_dtypes(include="number").corr()

# ヒートマップ
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("reports/figures/correlation.png")

# ターゲットとの相関（上位 10 列）
corr["target"].abs().sort_values(ascending=False).head(10)
```

### カテゴリ変数の分析

```python
# カテゴリ別のターゲット平均
df.groupby("category")["target"].mean().sort_values(ascending=False)

# カテゴリ別の分布
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for i, col in enumerate(["category", "region", "type"]):
    sns.countplot(data=df, x=col, ax=axes[i])
    axes[i].tick_params(axis="x", rotation=45)
plt.tight_layout()
```

### 欠損値の可視化

```python
# 欠損値パターンの可視化
import missingno as msno

msno.matrix(df)
msno.heatmap(df)      # 欠損値の相関
msno.bar(df)           # 列ごとの非欠損率
```

### EDA のテンプレート

| 分析 | やること | 発見したい問題 |
|------|---------|-------------|
| 分布 | 全列のヒストグラム・箱ひげ図 | 偏り・外れ値・異常値 |
| 相関 | 相関行列・散布図 | 多重共線性・予測に有効な変数 |
| カテゴリ | 出現頻度・ターゲットとのクロス集計 | レアカテゴリ・リーケージ |
| 時系列 | 時間軸での推移・周期性 | トレンド・季節性・データ漏洩 |
| 欠損 | 欠損パターン・欠損の相関 | MCAR / MAR / MNAR の判断 |

---

## 4. データ前処理

EDA で発見した問題を修正し、モデルに入力できる形に変換する。

### 欠損値の処理

```python
from sklearn.impute import SimpleImputer

# 数値列: 中央値で補完
num_imputer = SimpleImputer(strategy="median")
df[num_cols] = num_imputer.fit_transform(df[num_cols])

# カテゴリ列: 最頻値で補完
cat_imputer = SimpleImputer(strategy="most_frequent")
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

# 欠損率が高すぎる列は削除
high_missing = df.columns[df.isnull().mean() > 0.8]
df = df.drop(columns=high_missing)
```

**欠損値処理の方針:**

| 欠損率 | 対応 |
|--------|------|
| 0〜5% | 中央値・最頻値で補完 |
| 5〜30% | モデルベースの補完（KNN・反復補完）or 欠損フラグを追加 |
| 30〜80% | 欠損フラグを追加 + 補完。列の有用性を検討 |
| 80%〜 | 列の削除を検討 |

### カテゴリ変数のエンコーディング

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding（順序がある場合・木系モデル向き）
le = LabelEncoder()
df["category_encoded"] = le.fit_transform(df["category"])

# One-Hot Encoding（順序がない場合・線形モデル向き）
df = pd.get_dummies(df, columns=["category"], drop_first=True)

# Target Encoding（カテゴリ数が多い場合）
target_mean = df.groupby("category")["target"].mean()
df["category_target_enc"] = df["category"].map(target_mean)
```

### スケーリング

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 標準化（平均 0・分散 1）— 線形モデル・SVM 向き
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Min-Max スケーリング（0〜1 に変換）— ニューラルネットワーク向き
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
```

> **木系モデル（LightGBM・XGBoost）はスケーリング不要**。
> 線形モデル・SVM・ニューラルネットワークはスケーリングが必要。

---

## 5. 特徴量エンジニアリング

モデルの精度を最も大きく左右するステップ。ドメイン知識とデータの理解が重要。

### 基本的な特徴量作成

```python
# 数値の組み合わせ
df["price_per_area"] = df["price"] / df["area"]
df["total_rooms"] = df["bedrooms"] + df["bathrooms"]
df["age"] = 2024 - df["year_built"]

# 日時からの特徴量
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)

# テキストからの特徴量
df["text_length"] = df["description"].str.len()
df["word_count"] = df["description"].str.split().str.len()

# 集約特徴量
group_stats = df.groupby("category")["price"].agg(["mean", "std", "min", "max"])
group_stats.columns = ["cat_price_mean", "cat_price_std", "cat_price_min", "cat_price_max"]
df = df.merge(group_stats, on="category", how="left")

# ビニング（連続値をカテゴリ化）
df["age_bin"] = pd.cut(df["age"], bins=[0, 20, 40, 60, 100], labels=["young", "adult", "middle", "senior"])
```

### 特徴量選択

```python
from sklearn.feature_selection import mutual_info_classif

# 相互情報量による特徴量の重要度
mi_scores = mutual_info_classif(X, y, random_state=42)
mi_df = pd.DataFrame({"feature": X.columns, "mi_score": mi_scores})
mi_df = mi_df.sort_values("mi_score", ascending=False)

# LightGBM の特徴量重要度
import lightgbm as lgb

model = lgb.LGBMClassifier(n_estimators=100)
model.fit(X, y)
importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)
```

### 特徴量エンジニアリングのチェックリスト

| カテゴリ | 作成する特徴量 |
|---------|-------------|
| 数値の組み合わせ | 比率・差分・積 |
| 日時 | 年・月・曜日・祝日フラグ・経過日数 |
| カテゴリの集約 | グループ別の平均・標準偏差・カウント |
| テキスト | 文字数・単語数・TF-IDF |
| ラグ特徴量 | 過去 N 期間の値・移動平均（時系列） |
| 交互作用 | カテゴリ x 数値の組み合わせ |

---

## 6. モデリング

ベースラインから始めて、段階的にモデルを改善する。

### ステップ 1: ベースラインモデル

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# データ分割
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# シンプルなベースライン
baseline = LogisticRegression(max_iter=1000)
baseline.fit(X_train, y_train)
y_pred = baseline.predict(X_val)
print(f"Baseline Accuracy: {accuracy_score(y_val, y_pred):.4f}")
print(classification_report(y_val, y_pred))
```

### ステップ 2: 複数モデルの比較

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
import lightgbm as lgb

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "LightGBM": lgb.LGBMClassifier(n_estimators=100, random_state=42),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    score = accuracy_score(y_val, y_pred)
    results[name] = score
    print(f"{name}: {score:.4f}")
```

### ステップ 3: ハイパーパラメータチューニング

```python
import optuna

def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 1000),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "max_depth": trial.suggest_int("max_depth", 3, 10),
        "num_leaves": trial.suggest_int("num_leaves", 20, 100),
        "min_child_samples": trial.suggest_int("min_child_samples", 5, 100),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
        "reg_alpha": trial.suggest_float("reg_alpha", 1e-8, 10.0, log=True),
        "reg_lambda": trial.suggest_float("reg_lambda", 1e-8, 10.0, log=True),
    }

    model = lgb.LGBMClassifier(**params, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    return accuracy_score(y_val, y_pred)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

print(f"Best Score: {study.best_value:.4f}")
print(f"Best Params: {study.best_params}")
```

---

## 7. 評価・検証

モデルの性能を正しく評価し、過学習を検出する。

### 交差検証（Cross-Validation）

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
print(f"CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

### 評価指標の選択

| タスク | 主な指標 | 使い分け |
|--------|---------|---------|
| 二値分類 | Accuracy / F1 / AUC-ROC / Log Loss | 不均衡データでは F1 or AUC-ROC |
| 多クラス分類 | Macro F1 / Weighted F1 / Accuracy | クラス数が多い場合は Weighted F1 |
| 回帰 | RMSE / MAE / R2 / MAPE | 外れ値に敏感か否かで MAE vs RMSE |
| ランキング | MAP / NDCG | 推薦システム・検索 |

### 過学習の検出

```python
# 学習曲線
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, train_sizes=[0.2, 0.4, 0.6, 0.8, 1.0]
)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), label="Train")
plt.plot(train_sizes, val_scores.mean(axis=1), label="Validation")
plt.xlabel("Training Size")
plt.ylabel("Score")
plt.title("Learning Curve")
plt.legend()
plt.savefig("reports/figures/learning_curve.png")
```

**過学習の判断:**

| 状態 | Train スコア | Val スコア | 対策 |
|------|------------|-----------|------|
| 正常 | 高い | 高い（Train に近い） | そのまま |
| 過学習 | 非常に高い | 低い（大きなギャップ） | 正則化・データ増加・モデル簡素化 |
| 未学習 | 低い | 低い | モデル複雑化・特徴量追加 |

---

## 8. デプロイ・共有

分析結果を他の人が使える形にする。

### Streamlit — DS のための Web アプリ

```python
# app.py
import streamlit as st
import pandas as pd
import joblib

st.title("Price Prediction App")

# モデルの読み込み
model = joblib.load("models/model.pkl")

# 入力フォーム
area = st.number_input("Area (sqft)", min_value=100, max_value=10000, value=1000)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
age = st.slider("Building Age", 0, 100, 10)

# 予測
if st.button("Predict"):
    input_data = pd.DataFrame({"area": [area], "bedrooms": [bedrooms], "age": [age]})
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Price: ${prediction:,.0f}")
```

```bash
# 起動
streamlit run app.py

# Streamlit Cloud にデプロイ（GitHub 連携）
# https://streamlit.io/cloud
```

### FastAPI — 予測 API の作成

```python
# api.py
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/model.pkl")

@app.post("/predict")
def predict(area: float, bedrooms: int, age: int):
    input_data = pd.DataFrame({"area": [area], "bedrooms": [bedrooms], "age": [age]})
    prediction = model.predict(input_data)[0]
    return {"predicted_price": float(prediction)}
```

```bash
# 起動
uvicorn api:app --reload
# http://localhost:8000/docs で Swagger UI が開く
```

### モデルの保存

```python
import joblib

# 保存
joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# 読み込み
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
```

---

## 9. まとめ — ワークフローチェックリスト

### 各段階のチェック項目

| 段階 | チェック項目 |
|------|------------|
| データ理解 | データサイズ・型・欠損率・重複を確認したか |
| EDA | 分布・相関・欠損パターン・外れ値を可視化したか |
| 前処理 | 欠損値・カテゴリ変数・スケーリングを適切に処理したか |
| 特徴量 | ドメイン知識を活かした特徴量を作成したか |
| モデリング | ベースラインから始めて段階的に改善したか |
| 評価 | 交差検証を行い、過学習を検出したか |
| デプロイ | 他の人が使える形（アプリ or API or レポート）にしたか |

### よくある失敗と対策

| 失敗 | 原因 | 対策 |
|------|------|------|
| バリデーションスコアが異常に高い | データ漏洩（リーケージ） | 時系列は時間で分割。未来の情報を特徴量に含めていないか確認 |
| 本番でスコアが大幅に低下 | 訓練データと本番データの分布が異なる | EDA で分布の比較を行う。定期的にモデルを再学習 |
| モデルの結果が再現できない | 乱数シードの固定漏れ | `random_state=42` を全箇所で設定。環境を `environment.yml` で固定 |
| ノートブックが巨大で読めない | 1 つのノートブックにすべてを詰め込んだ | 段階別にノートブックを分割。再利用するコードは `src/` に切り出す |

---

**関連ガイド:**

- [14 - DS プロジェクト構成ガイド](14-project-structure-guide.md) — プロジェクトの構成・環境管理
- [16 - DS のための SQL ガイド](16-sql-guide.md) — データ取得のための SQL
- [10 - DS 向け Mac アプリガイド](10-mac-apps-guide.md) — DS 向けの Mac アプリ
- [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) — DS 向けの CLI ツール
