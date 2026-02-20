# データベース入門ガイド

---

## 0. はじめに

### 想定読者

- プログラミング初心者（Python の基本文法を理解している方）
- データ管理の基礎を学びたい方
- Web アプリケーション開発に興味がある方
- スプレッドシートからステップアップしたい方

### このガイドのゴール

このガイドを読むことで、以下のスキルを習得できます。

- データベースの基本概念と種類の理解
- SQL の基本文法と操作方法
- Python からデータベースを操作する方法
- テーブル設計の基礎知識
- ORM とマイグレーションツールの活用

### 関連ガイド

- [Claude Code 基本操作ガイド](10-claude-code-guide.md) - AI を活用した開発環境
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) - アプリケーション開発の実践
- [Docker 入門ガイド](22-docker-intro-guide.md) - コンテナでデータベース環境を構築
- [API 設計・連携ガイド](25-api-guide.md) - API とデータベースの連携
- [セキュリティ基礎ガイド](20-security-basics-guide.md) - データベースセキュリティ

---

## 1. データベースの必要性

### なぜデータベースが必要なのか

データを管理する方法はいくつかありますが、それぞれに適した用途があります。

**スプレッドシート vs データベース比較表**

| 観点 | スプレッドシート | データベース |
|------|-----------------|--------------|
| データ量 | 数千〜数万行まで | 数百万〜数億行も可能 |
| 同時アクセス | 限定的（数人程度） | 多数のユーザーが同時アクセス可能 |
| データ整合性 | 手動で管理が必要 | 制約で自動的に保証 |
| 検索速度 | データ量が増えると遅い | インデックスで高速検索 |
| プログラムとの連携 | API 経由で限定的 | 直接的に連携可能 |
| バックアップ | 手動コピーが基本 | 自動バックアップ・復元機能 |
| セキュリティ | 限定的 | 細かいアクセス制御が可能 |

### データベースが活躍する場面

- Web アプリケーションのユーザー情報管理
- EC サイトの商品・注文データ管理
- SNS の投稿・コメントデータ保存
- IoT デバイスからのセンサーデータ収集
- 業務システムの顧客・取引データ管理

> **Tip**: 100 行程度のデータならスプレッドシートで十分ですが、複数のテーブルを関連付けたり、プログラムから頻繁にアクセスする場合はデータベースが適しています。

---

## 2. データベースの種類

### RDB vs NoSQL

データベースには大きく分けて 2 つのタイプがあります。

| 項目 | RDB（リレーショナルデータベース） | NoSQL |
|------|-----------------------------------|-------|
| データ構造 | テーブル（行・列） | ドキュメント、Key-Value など |
| スキーマ | 事前定義が必要（固定） | 柔軟に変更可能 |
| データ整合性 | ACID 特性で厳密に保証 | 緩やかな整合性 |
| クエリ言語 | SQL（標準化されている） | データベースごとに異なる |
| 得意分野 | 複雑な関連データ、トランザクション | 大量データ、高速読み書き |
| スケーラビリティ | 垂直スケーリング（サーバー強化） | 水平スケーリング（サーバー追加） |

### 主要なデータベース製品

**RDB（リレーショナルデータベース）**

- **SQLite**: ファイルベース、セットアップ不要、組み込み用途に最適
- **PostgreSQL**: オープンソース、高機能、本番環境で人気
- **MySQL/MariaDB**: オープンソース、Web アプリで広く使用
- **Oracle/SQL Server**: 商用、エンタープライズ向け

**NoSQL**

- **MongoDB**: ドキュメント型、JSON ライクなデータ構造
- **Redis**: Key-Value 型、高速キャッシュに最適
- **Cassandra**: 列指向、大規模分散システム向け

> **初心者へのおすすめ**: まずは SQLite で SQL の基本を学び、次に PostgreSQL で本格的な開発を体験するのがおすすめです。

---

## 3. SQLite 入門

### SQLite とは

SQLite は以下の特徴を持つ軽量なデータベースです。

- ファイルベース（1 つの `.db` ファイルにすべてのデータを保存）
- サーバー不要（セットアップが簡単）
- Python に標準で組み込まれている
- 学習用・小規模アプリに最適

### インストール確認

Python には SQLite が標準で含まれています。

```bash
# Python のバージョン確認
python3 --version

# SQLite のバージョン確認
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```

### 最初のデータベース作成

```python
import sqlite3

# データベースに接続（ファイルがなければ自動作成）
conn = sqlite3.connect('mydata.db')

# カーソルオブジェクトを作成
cursor = conn.cursor()

# テーブルを作成
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# 変更を保存
conn.commit()

# 接続を閉じる
conn.close()

print("データベースとテーブルを作成しました！")
```

### 基本操作

```python
import sqlite3

conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

# データ挿入
cursor.execute('''
    INSERT INTO users (name, email, age)
    VALUES ('山田太郎', 'yamada@example.com', 30)
''')

# 複数データ挿入
users_data = [
    ('佐藤花子', 'sato@example.com', 25),
    ('鈴木一郎', 'suzuki@example.com', 35),
    ('田中美咲', 'tanaka@example.com', 28)
]
cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', users_data)

# データ取得
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
```

**出力例:**
```
(1, '山田太郎', 'yamada@example.com', 30, '2026-02-19 10:30:00')
(2, '佐藤花子', 'sato@example.com', 25, '2026-02-19 10:30:01')
(3, '鈴木一郎', 'suzuki@example.com', 35, '2026-02-19 10:30:01')
(4, '田中美咲', 'tanaka@example.com', 28, '2026-02-19 10:30:01')
```

---

## 4. SQL 基本文法

### SELECT - データ取得

```sql
-- すべてのカラムを取得
SELECT * FROM users;

-- 特定のカラムのみ取得
SELECT name, email FROM users;

-- 条件を指定して取得
SELECT * FROM users WHERE age >= 30;

-- 並び替え
SELECT * FROM users ORDER BY age DESC;

-- 件数制限
SELECT * FROM users LIMIT 3;

-- 件数カウント
SELECT COUNT(*) FROM users;

-- 平均値
SELECT AVG(age) FROM users;
```

### WHERE - 条件指定

```sql
-- 比較演算子
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age <= 30;
SELECT * FROM users WHERE name = '山田太郎';

-- 範囲指定
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

-- リストから選択
SELECT * FROM users WHERE name IN ('山田太郎', '佐藤花子');

-- パターンマッチング
SELECT * FROM users WHERE email LIKE '%@example.com';

-- AND / OR / NOT
SELECT * FROM users WHERE age >= 30 AND name LIKE '山%';
SELECT * FROM users WHERE age < 25 OR age > 35;
SELECT * FROM users WHERE NOT age = 30;
```

### INSERT - データ挿入

```sql
-- 1 件挿入
INSERT INTO users (name, email, age)
VALUES ('高橋健太', 'takahashi@example.com', 32);

-- カラム名を省略（すべてのカラムを順番通りに指定）
INSERT INTO users VALUES (NULL, '小林真理', 'kobayashi@example.com', 29, CURRENT_TIMESTAMP);

-- 複数件挿入
INSERT INTO users (name, email, age) VALUES
    ('渡辺優子', 'watanabe@example.com', 27),
    ('伊藤大輔', 'ito@example.com', 31);
```

### UPDATE - データ更新

```sql
-- 特定のレコードを更新
UPDATE users SET age = 31 WHERE name = '山田太郎';

-- 複数カラムを更新
UPDATE users
SET age = 26, email = 'sato-new@example.com'
WHERE name = '佐藤花子';

-- すべてのレコードを更新（注意！）
UPDATE users SET age = age + 1;
```

> **Warning**: WHERE 句を忘れると全レコードが更新されます。必ず条件を確認してから実行しましょう。

### DELETE - データ削除

```sql
-- 特定のレコードを削除
DELETE FROM users WHERE id = 1;

-- 条件に一致するレコードを削除
DELETE FROM users WHERE age < 25;

-- すべてのレコードを削除（注意！）
DELETE FROM users;
```

### JOIN - テーブル結合

```sql
-- テーブル準備例
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    amount INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO orders (user_id, product, amount) VALUES
    (1, 'ノートPC', 120000),
    (1, 'マウス', 3000),
    (2, 'キーボード', 8000),
    (3, 'モニター', 35000);

-- INNER JOIN（両方に存在するデータのみ）
SELECT users.name, orders.product, orders.amount
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN（左テーブルのすべてのデータ + 右テーブルの一致データ）
SELECT users.name, orders.product, orders.amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- 集計と組み合わせ
SELECT users.name, COUNT(orders.id) as order_count, SUM(orders.amount) as total_amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name;
```

---

## 5. テーブル設計の基礎

### 主キー（Primary Key）

各レコードを一意に識別するためのカラムです。

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 自動採番される主キー
    code TEXT UNIQUE NOT NULL,             -- 商品コード（一意制約）
    name TEXT NOT NULL,
    price INTEGER
);
```

**主キーの特徴:**
- NULL 値を許可しない
- 重複した値を許可しない
- 各テーブルに 1 つだけ定義できる
- 通常は `id` という名前で自動採番

### 外部キー（Foreign Key）

他のテーブルとの関連を定義するカラムです。

```sql
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

**外部キー制約の効果:**
- 存在しない ID を参照できない（データ整合性の保証）
- 参照されているデータは削除できない（オプションで設定可能）

### 正規化の基礎

正規化とは、データの重複を排除し、整合性を保つためのテーブル設計手法です。

**悪い例（正規化されていない）:**

| order_id | customer_name | customer_email | product_name | price | quantity |
|----------|--------------|----------------|--------------|-------|----------|
| 1 | 山田太郎 | yamada@example.com | ノートPC | 120000 | 1 |
| 2 | 山田太郎 | yamada@example.com | マウス | 3000 | 2 |
| 3 | 佐藤花子 | sato@example.com | キーボード | 8000 | 1 |

問題点:
- 顧客情報が重複している
- 顧客のメールアドレスを変更する場合、複数行を更新する必要がある

**良い例（正規化されている）:**

```sql
-- 顧客テーブル
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- 商品テーブル
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
);

-- 注文テーブル
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- 注文明細テーブル
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### ER 図（Entity Relationship Diagram）

テーブル間の関係を視覚化した図です。

```
[customers]          [orders]            [order_items]        [products]
-----------          --------            -------------        ----------
id (PK)             id (PK)             id (PK)              id (PK)
name                customer_id (FK) ←  order_id (FK)        name
email               order_date          product_id (FK) →    price
                                        quantity
```

**関係の種類:**
- **1 対 多**: 1 人の顧客が複数の注文を持つ
- **多 対 多**: 1 つの注文が複数の商品を含み、1 つの商品が複数の注文に含まれる（中間テーブルで実現）

> **Tip**: テーブル設計では、まず ER 図を描いてから SQL を書くと、整理された設計ができます。

---

## 6. PostgreSQL 概要

### PostgreSQL とは

PostgreSQL は高機能なオープンソースのリレーショナルデータベースです。

**SQLite との比較:**

| 項目 | SQLite | PostgreSQL |
|------|--------|------------|
| アーキテクチャ | ファイルベース | クライアント・サーバー型 |
| 同時書き込み | 1 プロセスのみ | 多数のクライアント可能 |
| データ型 | 5 種類のみ | 豊富（JSON、配列など） |
| トランザクション | 基本的なサポート | 高度な ACID 対応 |
| 用途 | 開発・テスト・組み込み | 本番環境・大規模システム |

### いつ PostgreSQL を使うべきか

- Web アプリケーションを本番環境にデプロイする
- 複数のユーザーが同時にデータを書き込む
- 高度な SQL 機能（JSON 型、全文検索など）が必要
- データの整合性とトランザクション管理が重要

### Homebrew でのインストール（macOS）

```bash
# PostgreSQL のインストール
brew install postgresql@17

# サービス起動
brew services start postgresql@17

# バージョン確認
psql --version
```

### 基本セットアップ

```bash
# データベース作成
createdb myapp_db

# データベースに接続
psql myapp_db

# psql コマンド例
\l          # データベース一覧
\c dbname   # データベース切り替え
\dt         # テーブル一覧
\d table    # テーブル構造表示
\q          # 終了
```

### Python から PostgreSQL に接続

```bash
# psycopg2 のインストール
pip install psycopg2-binary
```

```python
import psycopg2

# 接続
conn = psycopg2.connect(
    host="localhost",
    database="myapp_db",
    user="your_username",
    password="your_password"
)

cursor = conn.cursor()

# テーブル作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# データ挿入
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ('山田太郎', 'yamada@example.com')
)

conn.commit()
cursor.close()
conn.close()
```

---

## 7. Python から DB 操作

### sqlite3 モジュールの基本

```python
import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """データベースに接続"""
        self.conn = sqlite3.connect(self.db_path)
        # Row オブジェクトとして取得（カラム名でアクセス可能）
        self.conn.row_factory = sqlite3.Row
        return self.conn

    def close(self):
        """接続を閉じる"""
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None):
        """クエリを実行"""
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor

# 使用例
db = DatabaseManager('app.db')
db.connect()

# テーブル作成
db.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

db.close()
```

### パラメータ化クエリ（SQL インジェクション対策）

```python
# 悪い例（SQL インジェクションの危険性）
user_input = "'; DROP TABLE users; --"
query = f"SELECT * FROM users WHERE name = '{user_input}'"  # 危険！

# 良い例（パラメータ化クエリ）
cursor.execute(
    "SELECT * FROM users WHERE name = ?",
    (user_input,)  # タプルで渡す
)

# 複数パラメータ
cursor.execute(
    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
    ('山田太郎', 'yamada@example.com', 30)
)

# 名前付きパラメータ
cursor.execute(
    "INSERT INTO users (name, email, age) VALUES (:name, :email, :age)",
    {'name': '山田太郎', 'email': 'yamada@example.com', 'age': 30}
)
```

> **重要**: ユーザー入力を含む SQL は必ずパラメータ化クエリを使用してください。文字列結合は SQL インジェクションの原因になります。

### コンテキストマネージャーの活用

```python
import sqlite3

def get_user_by_email(email):
    """メールアドレスでユーザーを検索"""
    with sqlite3.connect('app.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()

def add_user(name, email, age):
    """ユーザーを追加"""
    with sqlite3.connect('app.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
        conn.commit()
        return cursor.lastrowid  # 挿入された ID を返す

# 使用例
user_id = add_user('山田太郎', 'yamada@example.com', 30)
print(f"新しいユーザー ID: {user_id}")

user = get_user_by_email('yamada@example.com')
if user:
    print(f"名前: {user['name']}, 年齢: {user['age']}")
```

---

## 8. ORM 入門

### ORM とは

ORM（Object-Relational Mapping）は、データベースのテーブルを Python のクラスとして扱える仕組みです。

**メリット:**
- SQL を書かずにデータベース操作ができる
- データベースの種類を切り替えやすい（SQLite → PostgreSQL など）
- Python のコードとして型安全に扱える

**デメリット:**
- 学習コストがかかる
- 複雑なクエリは SQL の方が書きやすい場合がある

### SQLAlchemy のインストール

```bash
pip install sqlalchemy
```

### モデル定義

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# ベースクラス
Base = declarative_base()

# ユーザーモデル
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    # リレーション
    posts = relationship('Post', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# 投稿モデル
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)

    # リレーション
    user = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"

# データベースエンジン作成
engine = create_engine('sqlite:///blog.db', echo=True)

# テーブル作成
Base.metadata.create_all(engine)

# セッション作成
Session = sessionmaker(bind=engine)
session = Session()
```

### CRUD 操作

```python
# Create - データ挿入
user1 = User(name='山田太郎', email='yamada@example.com', age=30)
user2 = User(name='佐藤花子', email='sato@example.com', age=25)

session.add(user1)
session.add(user2)
session.commit()

print(f"ユーザー ID: {user1.id}")  # 自動採番された ID

# 投稿を追加
post1 = Post(title='最初の投稿', content='SQLAlchemy を使ってみました', user_id=user1.id)
post2 = Post(title='Python の魅力', content='Python は素晴らしい言語です', user_id=user1.id)

session.add_all([post1, post2])
session.commit()

# Read - データ取得
# すべてのユーザーを取得
users = session.query(User).all()
for user in users:
    print(user)

# 条件で絞り込み
young_users = session.query(User).filter(User.age < 30).all()
print(young_users)

# 1 件取得
user = session.query(User).filter_by(email='yamada@example.com').first()
print(user)

# リレーションをたどる
user = session.query(User).filter_by(email='yamada@example.com').first()
for post in user.posts:
    print(f"{user.name} の投稿: {post.title}")

# JOIN を使った取得
results = session.query(User, Post).join(Post).all()
for user, post in results:
    print(f"{user.name}: {post.title}")

# Update - データ更新
user = session.query(User).filter_by(email='yamada@example.com').first()
user.age = 31
session.commit()

# 一括更新
session.query(User).filter(User.age < 30).update({'age': User.age + 1})
session.commit()

# Delete - データ削除
user = session.query(User).filter_by(email='sato@example.com').first()
session.delete(user)
session.commit()

# 一括削除
session.query(Post).filter(Post.title.like('%テスト%')).delete()
session.commit()

# セッションを閉じる
session.close()
```

---

## 9. マイグレーション

### マイグレーションとは

マイグレーションは、データベーススキーマ（テーブル構造）の変更履歴を管理する仕組みです。

**メリット:**
- スキーマ変更をバージョン管理できる
- チーム開発で DB 構造を同期できる
- 本番環境への適用が安全にできる
- ロールバック（元に戻す）が可能

### Alembic のインストール

```bash
pip install alembic
```

### Alembic の初期化

```bash
# プロジェクトディレクトリで実行
alembic init alembic
```

生成されるファイル構成:
```
project/
├── alembic/
│   ├── versions/          # マイグレーションファイル
│   ├── env.py             # 環境設定
│   └── script.py.mako     # テンプレート
├── alembic.ini            # 設定ファイル
└── models.py              # SQLAlchemy モデル
```

### 設定ファイルの編集

`alembic.ini` を編集:
```ini
# データベース接続 URL を設定
sqlalchemy.url = sqlite:///./app.db
```

`alembic/env.py` を編集:
```python
from models import Base  # 自分のモデルをインポート
target_metadata = Base.metadata  # モデルのメタデータを設定
```

### マイグレーションファイルの作成

```bash
# 自動生成（モデルとの差分を検出）
alembic revision --autogenerate -m "create users table"

# 手動生成
alembic revision -m "add column to users"
```

生成されたマイグレーションファイル例（`versions/xxxx_create_users_table.py`）:
```python
"""create users table

Revision ID: abc123
Revises:
Create Date: 2026-02-19 10:00:00
"""
from alembic import op
import sqlalchemy as sa

# リビジョン情報
revision = 'abc123'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    """データベースを更新"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('age', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

def downgrade():
    """ロールバック"""
    op.drop_table('users')
```

### マイグレーションの適用

```bash
# 最新バージョンまで適用
alembic upgrade head

# 特定のリビジョンまで適用
alembic upgrade abc123

# 1 つ前に戻す
alembic downgrade -1

# 現在のバージョン確認
alembic current

# マイグレーション履歴表示
alembic history
```

### 実践例：カラム追加

```bash
# 新しいマイグレーションを作成
alembic revision -m "add bio column to users"
```

生成されたファイルを編集:
```python
def upgrade():
    op.add_column('users', sa.Column('bio', sa.String(length=500), nullable=True))

def downgrade():
    op.drop_column('users', 'bio')
```

適用:
```bash
alembic upgrade head
```

> **Tip**: マイグレーションファイルは Git で管理し、チーム全体で共有しましょう。

---

## 10. Claude Code で DB 開発

### Claude Code の活用場面

Claude Code を使うと、データベース開発が効率的になります。

1. **テーブル設計の相談**
2. **SQL クエリの生成と最適化**
3. **ORM モデルの自動生成**
4. **マイグレーションファイルの作成**
5. **データベースのデバッグ**

### テーブル設計を依頼

```
ブログアプリのデータベース設計をお願いします。
以下の機能が必要です：
- ユーザー管理（名前、メール、パスワード）
- 記事投稿（タイトル、本文、公開/非公開）
- コメント機能
- タグ機能（1 つの記事に複数のタグ）

ER 図と SQLAlchemy モデルを作成してください。
```

### SQL クエリの生成

```
users テーブルと orders テーブルがあります。
各ユーザーの注文件数と総額を集計する SQL を書いてください。
注文がないユーザーも含めて表示したいです。
```

Claude が以下のような SQL を生成:
```sql
SELECT
    users.id,
    users.name,
    COALESCE(COUNT(orders.id), 0) as order_count,
    COALESCE(SUM(orders.amount), 0) as total_amount
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_amount DESC;
```

### マイグレーションの作成

```
users テーブルに以下のカラムを追加する Alembic マイグレーションを作成してください：
- profile_image: 画像 URL（255 文字まで、NULL 許可）
- last_login_at: 最終ログイン日時（NULL 許可）
```

### データベースのデバッグ

```
以下のエラーが出ました。原因と解決方法を教えてください：

sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError)
UNIQUE constraint failed: users.email
```

Claude が原因（メールアドレスの重複）と解決策（既存データの確認、エラーハンドリング）を提案してくれます。

### 実践的な開発フロー

1. **設計相談**: Claude に ER 図とモデル定義を依頼
2. **モデル作成**: 提案されたコードを `models.py` に保存
3. **マイグレーション**: Claude に Alembic コマンドを確認
4. **CRUD 実装**: Claude に基本的な操作コードを生成してもらう
5. **クエリ最適化**: 複雑な検索機能を Claude と一緒に実装

### Claude Code との対話例

**あなた:**
```
SQLite で商品管理アプリを作りたいです。
以下のテーブルが必要です：
- 商品（名前、価格、在庫数、カテゴリ）
- カテゴリ（名前、説明）

SQLAlchemy モデルと、基本的な CRUD 操作を実装してください。
```

**Claude Code:**
```python
# models.py を生成し、以下の機能を実装
# - Category と Product モデル
# - リレーション設定
# - CRUD 操作関数
# - サンプルデータ投入スクリプト
```

**あなた:**
```
在庫が 10 個以下の商品を検索する関数を追加してください。
```

**Claude Code:**
```python
def get_low_stock_products(session, threshold=10):
    """在庫が少ない商品を取得"""
    return session.query(Product).filter(Product.stock <= threshold).all()
```

---

## まとめ

このガイドでは、データベースの基礎から実践的な開発方法まで学びました。

### 習得したスキル

- データベースの種類と用途の理解
- SQL の基本文法（SELECT, INSERT, UPDATE, DELETE, JOIN）
- テーブル設計の基礎（主キー、外部キー、正規化）
- Python からデータベースを操作する方法
- ORM（SQLAlchemy）の基本的な使い方
- マイグレーション（Alembic）によるスキーマ管理
- Claude Code を活用した効率的な開発

### 次のステップ

1. **小さなアプリを作る**: ToDo アプリや家計簿アプリで練習
2. **Web フレームワークと連携**: Flask や FastAPI でデータベースを使う
3. **セキュリティ学習**: [セキュリティ基礎ガイド](20-security-basics-guide.md) で SQL インジェクション対策を深掘り
4. **API 設計**: [API 設計・連携ガイド](25-api-guide.md) でデータベースを API として公開
5. **本番環境構築**: [Docker 入門ガイド](22-docker-intro-guide.md) でデータベースコンテナを構築

### おすすめの学習リソース

- [SQLite Tutorial](https://www.sqlitetutorial.net/) - SQLite の公式チュートリアル
- [PostgreSQL 日本語ドキュメント](https://www.postgresql.jp/document/) - PostgreSQL の詳細な解説
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) - SQLAlchemy の公式ドキュメント
- [SQL Zoo](https://sqlzoo.net/) - インタラクティブな SQL 学習サイト

### トラブルシューティング

**よくある問題と解決策:**

| 問題 | 原因 | 解決方法 |
|------|------|---------|
| `database is locked` | 同時アクセス制限 | SQLite は 1 つの書き込みのみ。PostgreSQL に移行を検討 |
| `UNIQUE constraint failed` | 一意制約違反 | 重複データを確認し、既存データを削除または更新 |
| `no such table` | テーブル未作成 | マイグレーション実行またはテーブル作成クエリを実行 |
| `IntegrityError` | 外部キー制約違反 | 参照先のデータが存在するか確認 |

> **最後に**: データベースはすべての Web アプリケーションの基盤です。最初は難しく感じるかもしれませんが、実際に手を動かして試すことで理解が深まります。Claude Code と一緒に楽しく学んでいきましょう！

---

関連ガイド:
- [Claude Code 基本操作ガイド](10-claude-code-guide.md)
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md)
- [Docker 入門ガイド](22-docker-intro-guide.md)
- [API 設計・連携ガイド](25-api-guide.md)
- [セキュリティ基礎ガイド](20-security-basics-guide.md)
