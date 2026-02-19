# DS のための SQL ガイド

## 0. はじめに

このガイドは **データサイエンティストが実務で使う SQL パターンをまとめた自分用リファレンス** です。

- **想定読者**: Python は使えるが、SQL でのデータ抽出に慣れていない DS
- **ゴール**: 実務で必要な SQL パターンを理解し、DB やファイルからデータを効率的に抽出できるようになる
- **前提**: SQL の基本（SELECT・FROM・WHERE）を知っていること
- **関連ガイド**: [15 - DS ワークフローガイド](15-workflow-guide.md)、[11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md)

> **15 との棲み分け**: [15](15-workflow-guide.md) は Python 中心のワークフローを紹介した。
> このガイドでは **SQL でのデータ操作** に焦点を当てる。DS の実務ではデータの大部分を SQL で抽出する。

> サンプルクエリは **DuckDB / PostgreSQL / BigQuery** で動作する標準的な SQL を使用する。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. SQL 実行環境](#1-sql-実行環境) | DuckDB・PostgreSQL・BigQuery の使い分け |
| [2. 基本クエリ](#2-基本クエリ) | SELECT・WHERE・ORDER BY・LIMIT |
| [3. 集約・グループ化](#3-集約グループ化) | GROUP BY・HAVING・集約関数 |
| [4. 結合（JOIN）](#4-結合join) | INNER・LEFT・CROSS JOIN |
| [5. サブクエリ・CTE](#5-サブクエリcte) | WITH 句・相関サブクエリ |
| [6. ウィンドウ関数](#6-ウィンドウ関数) | ROW_NUMBER・RANK・LAG・移動平均 |
| [7. 日付・時系列](#7-日付時系列) | DATE 関数・時系列集約 |
| [8. DS 実務パターン](#8-ds-実務パターン) | サンプリング・ピボット・欠損分析・分位数 |
| [9. まとめ — SQL チートシート](#9-まとめ--sql-チートシート) | よく使うパターンの一覧 |

---

## 1. SQL 実行環境

DS が使う主な SQL 実行環境。

### 環境の比較

| 環境 | 用途 | 料金 | セットアップ |
|------|------|------|------------|
| **DuckDB** | ローカルの CSV・Parquet ファイルに SQL | 無料 | `brew install duckdb` |
| **PostgreSQL** | ローカル / リモートの RDB | 無料 | `brew install postgresql` |
| **BigQuery** | Google Cloud の大規模データウェアハウス | 無料枠あり | GCP アカウント |
| **Redshift** | AWS の大規模データウェアハウス | 有料 | AWS アカウント |

### DuckDB — ファイルに直接 SQL

DS にとって最も手軽な SQL 環境。CSV や Parquet に直接クエリを投げられる。

```bash
# CLI で起動
duckdb

# ファイルに直接クエリ
duckdb -c "SELECT * FROM 'data.csv' LIMIT 10"
```

```python
# Python から使用
import duckdb

# CSV に SQL を実行
df = duckdb.sql("SELECT * FROM 'data/raw/train.csv' WHERE age > 30").df()

# pandas DataFrame に SQL を実行
import pandas as pd
df = pd.read_csv("data/raw/train.csv")
result = duckdb.sql("SELECT category, AVG(price) as avg_price FROM df GROUP BY category").df()
```

### Python から PostgreSQL に接続

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/mydb")

# SQL で読み込み
df = pd.read_sql("SELECT * FROM users WHERE created_at > '2024-01-01'", engine)

# DataFrame を書き込み
df.to_sql("results", engine, if_exists="replace", index=False)
```

---

## 2. 基本クエリ

### SELECT — 列の選択

```sql
-- 全列を取得
SELECT * FROM users LIMIT 10;

-- 特定の列を取得
SELECT name, age, city FROM users;

-- 列にエイリアスを付ける
SELECT
    name AS user_name,
    age,
    price * quantity AS total_amount
FROM orders;

-- 重複を除去
SELECT DISTINCT city FROM users;

-- 重複除去してカウント
SELECT COUNT(DISTINCT city) AS unique_cities FROM users;
```

### WHERE — 行のフィルタ

```sql
-- 条件でフィルタ
SELECT * FROM users WHERE age >= 30;
SELECT * FROM users WHERE city = 'Tokyo';
SELECT * FROM users WHERE age BETWEEN 20 AND 40;
SELECT * FROM users WHERE city IN ('Tokyo', 'Osaka', 'Nagoya');
SELECT * FROM users WHERE name LIKE '%田%';       -- 部分一致
SELECT * FROM users WHERE email IS NULL;           -- NULL チェック
SELECT * FROM users WHERE email IS NOT NULL;

-- 複数条件
SELECT * FROM users WHERE age >= 30 AND city = 'Tokyo';
SELECT * FROM users WHERE age >= 30 OR city = 'Tokyo';
SELECT * FROM users WHERE NOT (age < 20);
```

### ORDER BY・LIMIT

```sql
-- ソート
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users ORDER BY city ASC, age DESC;

-- 上位 N 件
SELECT * FROM users ORDER BY score DESC LIMIT 10;

-- オフセット（ページネーション）
SELECT * FROM users ORDER BY id LIMIT 10 OFFSET 20;
```

---

## 3. 集約・グループ化

### 集約関数

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT user_id) AS unique_users,
    AVG(price) AS avg_price,
    SUM(price) AS total_revenue,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    STDDEV(price) AS std_price,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS median_price
FROM orders;
```

### GROUP BY — グループ別集約

```sql
-- カテゴリ別の集約
SELECT
    category,
    COUNT(*) AS count,
    AVG(price) AS avg_price,
    SUM(price) AS total_revenue
FROM products
GROUP BY category
ORDER BY total_revenue DESC;

-- 複数キーでグループ化
SELECT
    category,
    region,
    COUNT(*) AS count,
    AVG(price) AS avg_price
FROM products
GROUP BY category, region;
```

### HAVING — 集約結果のフィルタ

```sql
-- 100 件以上あるカテゴリのみ
SELECT
    category,
    COUNT(*) AS count,
    AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING COUNT(*) >= 100
ORDER BY avg_price DESC;
```

> **WHERE vs HAVING**: WHERE は集約前の行をフィルタ。HAVING は集約後の結果をフィルタ。

---

## 4. 結合（JOIN）

### JOIN の種類

| 種類 | 説明 | 結果 |
|------|------|------|
| `INNER JOIN` | 両方のテーブルにマッチする行のみ | マッチしない行は除外 |
| `LEFT JOIN` | 左テーブルの全行 + 右のマッチ行 | 右にマッチしない場合は NULL |
| `RIGHT JOIN` | 右テーブルの全行 + 左のマッチ行 | 左にマッチしない場合は NULL |
| `FULL OUTER JOIN` | 両方の全行 | マッチしない側は NULL |
| `CROSS JOIN` | すべての組み合わせ（直積） | 行数 = 左の行数 x 右の行数 |

### JOIN の実例

```sql
-- INNER JOIN: 注文とユーザー情報を結合
SELECT
    o.order_id,
    o.product_name,
    o.price,
    u.name,
    u.city
FROM orders o
INNER JOIN users u ON o.user_id = u.id;

-- LEFT JOIN: 全ユーザー + 注文情報（注文がないユーザーも含む）
SELECT
    u.name,
    COUNT(o.order_id) AS order_count,
    COALESCE(SUM(o.price), 0) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name;

-- 複数テーブルの結合
SELECT
    o.order_id,
    u.name AS user_name,
    p.product_name,
    p.category,
    o.quantity,
    o.quantity * p.price AS total_price
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN products p ON o.product_id = p.id;
```

---

## 5. サブクエリ・CTE

### CTE（Common Table Expression）— WITH 句

CTE を使うとクエリを段階的に構築でき、可読性が大幅に向上する。

```sql
-- カテゴリ別の統計を計算し、平均以上のカテゴリを抽出
WITH category_stats AS (
    SELECT
        category,
        COUNT(*) AS count,
        AVG(price) AS avg_price,
        SUM(price) AS total_revenue
    FROM products
    GROUP BY category
),
overall_avg AS (
    SELECT AVG(avg_price) AS overall_avg_price
    FROM category_stats
)
SELECT
    cs.category,
    cs.count,
    cs.avg_price,
    cs.total_revenue
FROM category_stats cs
CROSS JOIN overall_avg oa
WHERE cs.avg_price > oa.overall_avg_price
ORDER BY cs.total_revenue DESC;
```

### サブクエリ

```sql
-- WHERE 句でのサブクエリ
SELECT * FROM users
WHERE id IN (
    SELECT user_id FROM orders
    WHERE price > 10000
);

-- 平均より高い商品
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- FROM 句でのサブクエリ（インラインビュー）
SELECT category, avg_price
FROM (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
) sub
WHERE avg_price > 5000;
```

> **CTE vs サブクエリ**: 基本的に **CTE（WITH 句）を優先** する。可読性が高く、同じ結果を複数回参照できる。

---

## 6. ウィンドウ関数

DS で最も強力な SQL 機能。行ごとに集計値を付与でき、ランキング・移動平均・前後比較が簡単に書ける。

### 基本構文

```sql
関数名() OVER (
    PARTITION BY グループ列
    ORDER BY ソート列
    ROWS BETWEEN 範囲
)
```

### ROW_NUMBER / RANK / DENSE_RANK — ランキング

```sql
-- ユーザー別に注文を日付順に番号付け
SELECT
    user_id,
    order_date,
    price,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date) AS order_seq
FROM orders;

-- カテゴリ別の売上ランキング
SELECT
    category,
    product_name,
    price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) AS price_rank
FROM products;

-- 各カテゴリの上位 3 商品
WITH ranked AS (
    SELECT
        category,
        product_name,
        price,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 3;
```

**RANK 系関数の違い:**

| 関数 | 同順位の扱い | 例（値: 100, 100, 90） |
|------|------------|----------------------|
| `ROW_NUMBER` | 同順位でも異なる番号 | 1, 2, 3 |
| `RANK` | 同順位に同じ番号。次は飛ぶ | 1, 1, 3 |
| `DENSE_RANK` | 同順位に同じ番号。次は飛ばない | 1, 1, 2 |

### LAG / LEAD — 前後の行の値

```sql
-- 前月との売上比較
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month_revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS mom_change,
    ROUND(
        (revenue - LAG(revenue, 1) OVER (ORDER BY month))
        / LAG(revenue, 1) OVER (ORDER BY month) * 100, 1
    ) AS mom_change_pct
FROM monthly_revenue;

-- ユーザーの次回購入までの日数
SELECT
    user_id,
    order_date,
    LEAD(order_date, 1) OVER (PARTITION BY user_id ORDER BY order_date) AS next_order_date,
    LEAD(order_date, 1) OVER (PARTITION BY user_id ORDER BY order_date) - order_date AS days_to_next
FROM orders;
```

### 累積・移動集計

```sql
-- 累積合計
SELECT
    order_date,
    price,
    SUM(price) OVER (ORDER BY order_date) AS cumulative_revenue
FROM orders;

-- 7 日間の移動平均
SELECT
    date,
    daily_revenue,
    AVG(daily_revenue) OVER (
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM daily_sales;

-- カテゴリ別の構成比
SELECT
    category,
    revenue,
    ROUND(revenue * 100.0 / SUM(revenue) OVER (), 1) AS pct_of_total,
    ROUND(revenue * 100.0 / SUM(revenue) OVER (PARTITION BY region), 1) AS pct_of_region
FROM category_revenue;
```

---

## 7. 日付・時系列

DS は時系列データを頻繁に扱う。日付関数の理解は必須。

### 日付の操作

```sql
-- 現在日時
SELECT CURRENT_DATE, CURRENT_TIMESTAMP;

-- 日付の抽出
SELECT
    order_date,
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    EXTRACT(DOW FROM order_date) AS day_of_week,    -- 0=日曜
    EXTRACT(WEEK FROM order_date) AS week_number
FROM orders;

-- 日付の切り捨て
SELECT
    DATE_TRUNC('month', order_date) AS month,
    DATE_TRUNC('week', order_date) AS week,
    DATE_TRUNC('quarter', order_date) AS quarter
FROM orders;

-- 日付の加減
SELECT
    order_date,
    order_date + INTERVAL '7 days' AS plus_7_days,
    order_date - INTERVAL '1 month' AS minus_1_month,
    CURRENT_DATE - order_date AS days_since_order
FROM orders;
```

### 時系列の集約

```sql
-- 月別の売上推移
SELECT
    DATE_TRUNC('month', order_date) AS month,
    COUNT(*) AS order_count,
    SUM(price) AS revenue,
    COUNT(DISTINCT user_id) AS unique_users
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- 曜日別の平均売上
SELECT
    EXTRACT(DOW FROM order_date) AS day_of_week,
    AVG(price) AS avg_price,
    COUNT(*) AS order_count
FROM orders
GROUP BY EXTRACT(DOW FROM order_date)
ORDER BY day_of_week;

-- 前年同月比
WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(price) AS revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
)
SELECT
    month,
    revenue,
    LAG(revenue, 12) OVER (ORDER BY month) AS revenue_last_year,
    ROUND(
        (revenue - LAG(revenue, 12) OVER (ORDER BY month))
        / LAG(revenue, 12) OVER (ORDER BY month) * 100, 1
    ) AS yoy_change_pct
FROM monthly;
```

---

## 8. DS 実務パターン

DS の日常業務で頻出する SQL パターン。

### サンプリング

```sql
-- ランダムサンプリング（1%）
SELECT * FROM large_table
WHERE RANDOM() < 0.01;

-- 層化サンプリング（カテゴリ別に 100 件ずつ）
WITH ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY RANDOM()) AS rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 100;
```

### 欠損値の分析

```sql
-- 列ごとの欠損率
SELECT
    COUNT(*) AS total_rows,
    ROUND(SUM(CASE WHEN age IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS age_null_pct,
    ROUND(SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS city_null_pct,
    ROUND(SUM(CASE WHEN email IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS email_null_pct
FROM users;
```

### ピボット（縦持ち → 横持ち）

```sql
-- CASE 式でピボット
SELECT
    user_id,
    SUM(CASE WHEN category = 'A' THEN amount ELSE 0 END) AS category_a,
    SUM(CASE WHEN category = 'B' THEN amount ELSE 0 END) AS category_b,
    SUM(CASE WHEN category = 'C' THEN amount ELSE 0 END) AS category_c
FROM transactions
GROUP BY user_id;

-- DuckDB の PIVOT 構文
PIVOT transactions ON category USING SUM(amount) GROUP BY user_id;
```

### 分位数・パーセンタイル

```sql
-- 四分位数
SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY price) AS q1,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY price) AS median,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY price) AS q3
FROM products;

-- ユーザーを購入金額でデシル分類
SELECT
    user_id,
    total_spent,
    NTILE(10) OVER (ORDER BY total_spent DESC) AS decile
FROM (
    SELECT user_id, SUM(price) AS total_spent
    FROM orders
    GROUP BY user_id
) sub;
```

### コホート分析

```sql
-- ユーザーの初回購入月をコホートとし、月ごとのリテンションを計算
WITH first_purchase AS (
    SELECT
        user_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY user_id
),
monthly_activity AS (
    SELECT
        user_id,
        DATE_TRUNC('month', order_date) AS activity_month
    FROM orders
    GROUP BY user_id, DATE_TRUNC('month', order_date)
)
SELECT
    fp.cohort_month,
    EXTRACT(MONTH FROM AGE(ma.activity_month, fp.cohort_month)) AS months_since_first,
    COUNT(DISTINCT ma.user_id) AS active_users
FROM first_purchase fp
INNER JOIN monthly_activity ma ON fp.user_id = ma.user_id
GROUP BY fp.cohort_month, months_since_first
ORDER BY fp.cohort_month, months_since_first;
```

### RFM 分析

```sql
-- Recency・Frequency・Monetary の計算
WITH rfm AS (
    SELECT
        user_id,
        CURRENT_DATE - MAX(order_date) AS recency_days,
        COUNT(*) AS frequency,
        SUM(price) AS monetary
    FROM orders
    GROUP BY user_id
)
SELECT
    user_id,
    recency_days,
    frequency,
    monetary,
    NTILE(5) OVER (ORDER BY recency_days ASC) AS r_score,
    NTILE(5) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC) AS m_score
FROM rfm;
```

---

## 9. まとめ — SQL チートシート

### よく使うパターン一覧

| パターン | SQL |
|---------|-----|
| 上位 N 件 | `ORDER BY col DESC LIMIT N` |
| 重複除去 | `SELECT DISTINCT col` |
| 欠損チェック | `WHERE col IS NULL` |
| 条件分岐 | `CASE WHEN ... THEN ... ELSE ... END` |
| グループ別集約 | `GROUP BY col` |
| 集約後フィルタ | `HAVING COUNT(*) > N` |
| 結合 | `LEFT JOIN t2 ON t1.id = t2.id` |
| CTE | `WITH name AS (SELECT ...) SELECT ...` |
| ランキング | `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` |
| 前後比較 | `LAG(col, 1) OVER (ORDER BY ...)` |
| 移動平均 | `AVG(col) OVER (ORDER BY ... ROWS BETWEEN N PRECEDING AND CURRENT ROW)` |
| 累積合計 | `SUM(col) OVER (ORDER BY ...)` |
| 構成比 | `col * 100.0 / SUM(col) OVER ()` |
| 月別集約 | `GROUP BY DATE_TRUNC('month', date_col)` |
| ランダムサンプル | `WHERE RANDOM() < 0.01` |
| 分位数 | `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY col)` |
| デシル分類 | `NTILE(10) OVER (ORDER BY col)` |

### DS が SQL を書くときの原則

| 原則 | 説明 |
|------|------|
| **CTE を使う** | サブクエリよりも CTE（WITH 句）で段階的に書く |
| **SELECT * を避ける** | 必要な列だけ明示的に指定する |
| **早めにフィルタ** | WHERE で早い段階で行数を減らす（パフォーマンス向上） |
| **コメントを書く** | 複雑なロジックにはコメントを付ける |
| **LIMIT で試す** | 大きなテーブルはまず `LIMIT 100` で結果を確認 |
| **集計結果を確認** | GROUP BY 後の行数が想定通りか `COUNT(*)` で確認 |

---

**関連ガイド:**

- [15 - DS ワークフローガイド](15-workflow-guide.md) — EDA からデプロイまでの実践フロー
- [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) — DuckDB CLI・csvkit 等のツール
- [14 - DS プロジェクト構成ガイド](14-project-structure-guide.md) — プロジェクトの構成・環境管理
