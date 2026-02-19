# Kaggle 攻略ガイド

## 0. はじめに

このガイドは **Kaggle コンペティションに取り組むための実践的な攻略ガイドをまとめた自分用リファレンス** です。

- **想定読者**: DS の基礎は学んだ。Kaggle コンペに参加して実力を伸ばしたい
- **ゴール**: Kaggle のコンペに効率的に取り組み、メダルを獲得できるようになる
- **前提**: [15 - DS ワークフローガイド](15-workflow-guide.md) の EDA・モデリングの流れを理解していること
- **関連ガイド**: [15 - DS ワークフローガイド](15-workflow-guide.md)、[12 - DS 向け Web サイトガイド](12-web-resources-guide.md)

> **12 との棲み分け**: [12](12-web-resources-guide.md) では Kaggle をプラットフォームとして紹介した。
> このガイドでは **Kaggle コンペにどう取り組むか** の実践的な戦略に焦点を当てる。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. Kaggle の始め方](#1-kaggle-の始め方) | アカウント作成・環境設定・Kaggle API |
| [2. コンペの種類と選び方](#2-コンペの種類と選び方) | Getting Started・Featured・Research |
| [3. コンペの取り組み方](#3-コンペの取り組み方) | 初日〜最終日のスケジュール |
| [4. EDA テンプレート](#4-eda-テンプレート) | コンペ開始時の定型 EDA |
| [5. 特徴量エンジニアリング戦略](#5-特徴量エンジニアリング戦略) | コンペで使える特徴量パターン |
| [6. モデリング戦略](#6-モデリング戦略) | ベースライン → チューニング → アンサンブル |
| [7. バリデーション戦略](#7-バリデーション戦略) | 信頼できる CV の構築 |
| [8. Discussion・Notebooks の活用](#8-discussionnotebooks-の活用) | コミュニティから学ぶ |
| [9. まとめ — メダル獲得ロードマップ](#9-まとめ--メダル獲得ロードマップ) | レベル別の目標設定 |

---

## 1. Kaggle の始め方

### アカウント作成と初期設定

1. https://www.kaggle.com でアカウントを作成
2. プロフィールを完成させる（Contributor ランクの条件）
3. Kaggle API をセットアップ

### Kaggle API のセットアップ

```bash
# インストール
pip install kaggle

# API キーの設定
# 1. https://www.kaggle.com/settings → API → Create New Token
# 2. ダウンロードした kaggle.json を配置
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

```bash
# コンペのデータをダウンロード
kaggle competitions download -c titanic

# データセットのダウンロード
kaggle datasets download -d dataset-owner/dataset-name

# ノートブックの提出
kaggle kernels push -p ./my-notebook/
```

### Kaggle Notebook の環境

| 項目 | 内容 |
|------|------|
| **GPU** | NVIDIA T4 x 1（週 30 時間まで） |
| **TPU** | TPU v3-8（週 20 時間まで） |
| **メモリ** | 16GB RAM |
| **ディスク** | 73GB |
| **実行時間** | 最大 12 時間（GPU）/ 9 時間（CPU） |
| **インターネット** | 提出用ノートブックではオフライン |

> **ローカル vs Kaggle Notebook**: EDA・実験はローカルで行い、最終提出は Kaggle Notebook で行うのが一般的。
> GPU が必要な DL コンペでは Kaggle Notebook をメインで使う。

---

## 2. コンペの種類と選び方

### コンペの種類

| 種類 | 説明 | おすすめレベル |
|------|------|-------------|
| **Getting Started** | 初心者向けチュートリアルコンペ（Titanic・House Prices） | 初心者 |
| **Playground** | 気軽に参加できる練習コンペ。メダルは付かないことが多い | 初心者〜中級 |
| **Featured** | 企業スポンサー付きの本格コンペ。賞金あり | 中級〜上級 |
| **Research** | 研究テーマのコンペ。論文の再現など | 上級 |
| **Community** | コミュニティが運営するコンペ | 全レベル |

### 初心者が最初に取り組むべきコンペ

| コンペ | タスク | 学べること |
|--------|--------|-----------|
| **Titanic** | 二値分類（生存予測） | 基本的な ML パイプライン |
| **House Prices** | 回帰（住宅価格予測） | 特徴量エンジニアリング・回帰モデル |
| **Digit Recognizer** | 画像分類（手書き数字） | DL の基礎・CNN |
| **Spaceship Titanic** | 二値分類 | Titanic の次のステップ |
| **Playground Series** | 月替わり | 幅広いタスクに触れられる |

---

## 3. コンペの取り組み方

### コンペのスケジュール（2 ヶ月のコンペの場合）

| 期間 | やること |
|------|---------|
| **1 週目** | データ理解・EDA・Discussion を読む |
| **2 週目** | ベースラインモデルの構築・初回提出 |
| **3〜4 週目** | 特徴量エンジニアリング・モデル改善 |
| **5〜6 週目** | 複数モデルの試行・ハイパーパラメータ調整 |
| **7 週目** | アンサンブル・後処理 |
| **最終週** | 最終提出の選択・提出ノートブックの整理 |

### 初日にやること

```
1. コンペの Overview を読む（評価指標・ルール・データの説明）
2. Discussion の人気スレッドを読む（EDA・ベースライン・FAQ）
3. データをダウンロードして基本情報を確認
4. 公開ノートブックの上位を確認（EDA・ベースライン）
5. シンプルなベースラインを作成して提出
```

### 提出の管理

```
submissions/
├── sub_001_baseline_lgbm_cv0.82.csv
├── sub_002_add_features_cv0.84.csv
├── sub_003_tuned_params_cv0.85.csv
├── sub_004_ensemble_cv0.86.csv
└── submission_log.md     ← 各提出の内容・CV・LB スコアを記録
```

**submission_log.md の例:**

```markdown
| # | 日付 | 説明 | CV | Public LB |
|---|------|------|-----|-----------|
| 001 | 01/15 | LightGBM baseline | 0.820 | 0.815 |
| 002 | 01/18 | +target encoding | 0.840 | 0.835 |
| 003 | 01/22 | +tuned params (Optuna) | 0.850 | 0.843 |
| 004 | 01/28 | ensemble (LGBM+XGB+CatBoost) | 0.860 | 0.852 |
```

---

## 4. EDA テンプレート

コンペ開始時に毎回行う定型の EDA。

### EDA テンプレートコード

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# データの読み込み
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

print(f"Train shape: {train.shape}")
print(f"Test shape: {test.shape}")

# --- 基本情報 ---
print("\n--- Train Info ---")
print(train.info())
print("\n--- Train Describe ---")
print(train.describe())
print(train.describe(include="object"))

# --- ターゲット変数 ---
print(f"\nTarget distribution:\n{train['target'].value_counts()}")
print(f"Target ratio:\n{train['target'].value_counts(normalize=True)}")
train["target"].hist(bins=50)
plt.title("Target Distribution")
plt.savefig("reports/figures/target_dist.png")

# --- 欠損値 ---
missing = pd.DataFrame({
    "train_null_pct": train.isnull().mean() * 100,
    "test_null_pct": test.isnull().mean() * 100,
}).sort_values("train_null_pct", ascending=False)
print(f"\nMissing values:\n{missing[missing['train_null_pct'] > 0]}")

# --- データ型 ---
print(f"\nData types:\n{train.dtypes.value_counts()}")

# --- 数値変数の分布 ---
num_cols = train.select_dtypes(include="number").columns.tolist()
if "target" in num_cols:
    num_cols.remove("target")

fig, axes = plt.subplots(len(num_cols) // 3 + 1, 3, figsize=(18, 4 * (len(num_cols) // 3 + 1)))
for i, col in enumerate(num_cols):
    ax = axes.flatten()[i]
    train[col].hist(bins=30, ax=ax, alpha=0.7, label="train")
    test[col].hist(bins=30, ax=ax, alpha=0.7, label="test")
    ax.set_title(col)
    ax.legend()
plt.tight_layout()
plt.savefig("reports/figures/num_distributions.png")

# --- train と test の分布比較 ---
# train / test の分布が異なる列はリーケージや分布シフトの可能性

# --- 相関行列 ---
corr = train[num_cols + ["target"]].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("reports/figures/correlation.png")
```

### EDA で確認すべきポイント

| 確認項目 | 発見すべき問題 |
|---------|-------------|
| ターゲットの分布 | クラス不均衡 → サンプリング・重み付けを検討 |
| train と test の分布差 | 分布シフト → 特定の期間や属性が偏っていないか |
| 欠損パターン | 欠損が特定の行に集中 → 欠損フラグが特徴量になる可能性 |
| カーディナリティ | カテゴリ数が多すぎる列 → Target Encoding を検討 |
| 外れ値 | 異常な値 → クリッピングまたは除外を検討 |
| リーケージ | ターゲットと相関が異常に高い特徴量 → 本番では使えないデータが混入 |

---

## 5. 特徴量エンジニアリング戦略

### テーブルコンペの定番特徴量

| カテゴリ | 特徴量 | 例 |
|---------|--------|-----|
| **基本統計** | グループ別の平均・標準偏差・中央値 | カテゴリ別の price_mean |
| **比率** | 数値列同士の比率 | price / area |
| **差分** | 数値列同士の差 | max_price - min_price |
| **カウント** | グループ別のレコード数 | ユーザーの購入回数 |
| **ランク** | グループ内での順位 | カテゴリ内の価格ランク |
| **Target Encoding** | カテゴリ別のターゲット平均 | カテゴリの平均コンバージョン率 |
| **日時特徴量** | 年・月・曜日・時間・祝日 | purchase_dayofweek |
| **ラグ特徴量** | 過去の値 | 前月の売上 |
| **移動平均** | N 期間の移動平均 | 過去 7 日の平均売上 |
| **Null 特徴量** | 欠損の有無をフラグ化 | is_null_age |
| **頻度エンコーディング** | カテゴリの出現頻度 | city_count |
| **組み合わせ** | カテゴリの組み合わせ | city + gender の組み合わせ |

### Target Encoding（リーケージを防ぐ）

```python
from sklearn.model_selection import KFold

def target_encode(train, test, col, target, n_folds=5):
    """交差検証ベースの Target Encoding（リーケージ防止）。"""
    train[f"{col}_te"] = 0
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)

    for train_idx, val_idx in kf.split(train):
        mean = train.iloc[train_idx].groupby(col)[target].mean()
        train.loc[train.index[val_idx], f"{col}_te"] = train.iloc[val_idx][col].map(mean)

    # test は train 全体の平均を使う
    global_mean = train.groupby(col)[target].mean()
    test[f"{col}_te"] = test[col].map(global_mean)

    # 欠損は全体平均で補完
    overall_mean = train[target].mean()
    train[f"{col}_te"] = train[f"{col}_te"].fillna(overall_mean)
    test[f"{col}_te"] = test[f"{col}_te"].fillna(overall_mean)

    return train, test
```

### 特徴量の重要度分析

```python
import lightgbm as lgb

model = lgb.LGBMClassifier(n_estimators=500, random_state=42)
model.fit(X_train, y_train)

importance = pd.DataFrame({
    "feature": X_train.columns,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

# 上位 20 特徴量を表示
plt.figure(figsize=(10, 8))
plt.barh(importance["feature"].head(20), importance["importance"].head(20))
plt.xlabel("Importance")
plt.title("Top 20 Feature Importances")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("reports/figures/feature_importance.png")
```

---

## 6. モデリング戦略

### テーブルコンペの定番モデル

| モデル | 特徴 | 用途 |
|--------|------|------|
| **LightGBM** | 高速・高精度・メモリ効率が良い | ほぼすべてのテーブルコンペ |
| **XGBoost** | 安定した性能 | LightGBM と並ぶ定番 |
| **CatBoost** | カテゴリ変数の自動処理 | カテゴリ変数が多いデータ |
| **Random Forest** | シンプルで頑健 | ベースラインとして |
| **Neural Network** | 複雑なパターンを学習 | 大規模データ・Embedding |
| **Linear Model** | 解釈性が高い | アンサンブルの多様性 |

### LightGBM のテンプレート

```python
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
import numpy as np

def train_lgbm(X, y, X_test, params=None, n_folds=5):
    """LightGBM の交差検証学習テンプレート。"""
    if params is None:
        params = {
            "objective": "binary",
            "metric": "auc",
            "learning_rate": 0.05,
            "num_leaves": 31,
            "max_depth": -1,
            "min_child_samples": 20,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "reg_alpha": 0.1,
            "reg_lambda": 0.1,
            "random_state": 42,
            "verbose": -1,
        }

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
    oof_preds = np.zeros(len(X))
    test_preds = np.zeros(len(X_test))
    models = []

    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        train_data = lgb.Dataset(X_train, y_train)
        val_data = lgb.Dataset(X_val, y_val)

        model = lgb.train(
            params,
            train_data,
            num_boost_round=10000,
            valid_sets=[val_data],
            callbacks=[
                lgb.early_stopping(100),
                lgb.log_evaluation(200),
            ],
        )

        oof_preds[val_idx] = model.predict(X_val)
        test_preds += model.predict(X_test) / n_folds
        models.append(model)

        print(f"Fold {fold}: AUC = {roc_auc_score(y_val, oof_preds[val_idx]):.4f}")

    print(f"\nOverall CV AUC: {roc_auc_score(y, oof_preds):.4f}")
    return oof_preds, test_preds, models
```

### アンサンブル

```python
# 加重平均アンサンブル
final_pred = 0.4 * lgbm_pred + 0.3 * xgb_pred + 0.3 * catboost_pred

# スタッキング
from sklearn.linear_model import LogisticRegression

stack_X = np.column_stack([lgbm_oof, xgb_oof, catboost_oof])
stack_model = LogisticRegression()
stack_model.fit(stack_X, y)

stack_test = np.column_stack([lgbm_test, xgb_test, catboost_test])
final_pred = stack_model.predict_proba(stack_test)[:, 1]
```

**アンサンブルの原則:**

| 原則 | 説明 |
|------|------|
| 多様性が重要 | 異なるアルゴリズム・異なる特徴量セットで学習したモデルを組み合わせる |
| CV スコアで重み決定 | CV スコアが高いモデルに大きな重みを与える |
| 単純な平均から始める | まずは等重み平均。それからスタッキングに進む |

---

## 7. バリデーション戦略

コンペで最も重要な要素。信頼できる CV（交差検証）がなければ、改善の判断ができない。

### CV 戦略の選択

| データの性質 | 推奨 CV 戦略 |
|------------|------------|
| 通常のテーブルデータ | StratifiedKFold（分類）/ KFold（回帰） |
| 時系列データ | TimeSeriesSplit / 時間でカットオフ |
| グループがあるデータ | GroupKFold（同一ユーザーが train/val に分かれないように） |
| 不均衡データ | StratifiedKFold |

### CV スコアと LB スコアの関係

| 状況 | 原因 | 対策 |
|------|------|------|
| CV 上がる + LB 上がる | 正常。改善が汎化している | そのまま継続 |
| CV 上がる + LB 下がる | CV がオーバーフィットしている | CV 戦略を見直す |
| CV 下がる + LB 上がる | 偶然。LB のオーバーフィット | CV を信頼する |
| CV 変わらない + LB 変わらない | 改善が効いていない | 別のアプローチを試す |

> **原則: CV を信頼する**。Public LB は全テストデータの一部（通常 30%）でしか計算されない。
> CV スコアが安定して改善している限り、LB の一時的な低下は気にしない。

### CV のコード

```python
from sklearn.model_selection import StratifiedKFold, TimeSeriesSplit, GroupKFold

# 分類タスク
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 時系列タスク
cv = TimeSeriesSplit(n_splits=5)

# グループがあるタスク
cv = GroupKFold(n_splits=5)
# split 時に groups を渡す
for train_idx, val_idx in cv.split(X, y, groups=df["user_id"]):
    pass
```

---

## 8. Discussion・Notebooks の活用

Kaggle コミュニティから学ぶことが上達の最短ルート。

### Discussion の読み方

| スレッドタイプ | 内容 | 活用法 |
|-------------|------|--------|
| **EDA** | データの分析結果・発見 | 自分の EDA で見落とした点を補完 |
| **Baseline** | ベースラインモデルの共有 | 出発点として活用 |
| **Feature Engineering** | 特徴量のアイデア | 自分の特徴量に追加 |
| **Validation** | CV 戦略の議論 | 信頼できる CV の構築 |
| **Post-Competition** | コンペ後の上位解法 | 最も学びが多い。必ず読む |

### 公開ノートブックの活用

```
1. 人気のノートブック（Vote 数が多い）を確認
2. EDA ノートブックでデータの全体像を把握
3. ベースラインノートブックを fork して改善
4. 上位のノートブックのコードを読んで技術を吸収
```

> **注意**: 公開ノートブックをそのまま提出してもメダルは取れない（多くの人が同じスコアになる）。
> 公開ノートブックを出発点として、**自分の改善を加える** ことが重要。

### コンペ後の振り返り

| やること | 説明 |
|---------|------|
| 上位解法を読む | Discussion に投稿される上位者の解法を 3〜5 本読む |
| 手法をまとめる | 使われた特徴量・モデル・アンサンブル手法をメモ |
| 自分の改善点を特定 | 上位者との差を分析。次回のコンペに活かす |
| コードを再現 | 上位者のコードを動かして理解を深める |

---

## 9. まとめ — メダル獲得ロードマップ

### レベル別の目標設定

| レベル | 目標 | やること |
|--------|------|---------|
| 初心者 | Contributor ランク達成 | Titanic で初提出。Getting Started コンペを 2〜3 つ完了 |
| 初級 | Playground でスコア改善 | 特徴量エンジニアリング・LightGBM のチューニングを学ぶ |
| 中級 | Featured コンペでブロンズメダル | EDA → 特徴量 → 複数モデル → アンサンブルのフルパイプライン |
| 上級 | シルバー・ゴールドメダル | 独自の特徴量設計・高度なアンサンブル・後処理 |
| Expert+ | Expert / Master ランク | 複数コンペでメダル獲得。コミュニティへの貢献 |

### メダルの条件（Featured コンペの場合）

| メダル | 条件（参加チーム数による） |
|--------|----------------------|
| ブロンズ | 上位 40% |
| シルバー | 上位 5% |
| ゴールド | 上位 10 チーム以内 or 上位 0.2% |

### 最初にやることチェックリスト

- [ ] Kaggle アカウントを作成し、プロフィールを完成
- [ ] Kaggle API をセットアップ
- [ ] Titanic コンペで初提出（スコアは気にしない）
- [ ] Titanic の上位ノートブックを 3 つ読む
- [ ] House Prices コンペでベースラインを作成
- [ ] Discussion の読み方を習慣化
- [ ] Playground Series コンペに 1 つ参加
- [ ] LightGBM の交差検証テンプレートを自分のものにする
- [ ] 提出ログを管理する仕組みを作る

---

**関連ガイド:**

- [15 - DS ワークフローガイド](15-workflow-guide.md) — EDA からデプロイまでの実践フロー
- [12 - DS 向け Web サイトガイド](12-web-resources-guide.md) — Kaggle・学習プラットフォーム
- [14 - DS プロジェクト構成ガイド](14-project-structure-guide.md) — プロジェクトの構成・環境管理
- [17 - DS のための数学・統計ガイド](17-math-stats-guide.md) — ML の数学的基礎
