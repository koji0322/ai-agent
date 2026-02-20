# Docker 入門ガイド

## 0. はじめに

### 想定読者
- プログラミング初心者
- ターミナル操作の基本を理解している方
- 環境構築でトラブルが多い方
- チーム開発で環境を統一したい方

### ゴール
このガイドを読むことで、以下ができるようになります。

- Docker の基本概念を理解する
- コンテナを使った開発環境の構築ができる
- Dockerfile を書いてカスタムイメージを作成できる
- docker-compose で複数コンテナを管理できる
- VS Code の Dev Containers を活用できる

### 関連ガイド
- [VS Code 基本操作ガイド](00-vscode-guide.md) - エディタの基本操作
- [ターミナル CLI ツールガイド](03-terminal-tools-guide.md) - ターミナル操作の基礎
- [Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) - 自動化との連携
- [テスト入門ガイド](21-testing-intro-guide.md) - テスト環境の構築
- [データベース入門ガイド](24-database-intro-guide.md) - DB コンテナの活用

---

## 1. Docker とは

### Docker の役割

Docker は、アプリケーションとその実行環境を「コンテナ」という単位でパッケージ化する技術です。

**従来の問題点**
- 「私のパソコンでは動くのに、あなたのパソコンでは動かない」
- Python のバージョンが違う
- 必要なライブラリがインストールされていない
- OS の違いで動作が異なる

**Docker で解決**
- 環境をまるごとパッケージ化
- どのパソコンでも同じ環境で実行
- 環境構築が簡単
- チーム全体で環境を統一

### コンテナが重要な理由

```plaintext
開発者 A のパソコン          開発者 B のパソコン
Python 3.9                Python 3.11
Node.js 14                Node.js 18
PostgreSQL 12             PostgreSQL 15

↓ Docker を使うと

開発者 A                   開発者 B
Docker コンテナ           Docker コンテナ
(Python 3.10,             (Python 3.10,
 Node.js 16,               Node.js 16,
 PostgreSQL 14)            PostgreSQL 14)

→ 完全に同じ環境で開発できる
```

> **Tip**: Docker を使えば、新しいメンバーがチームに参加してもすぐに開発を始められます。

---

## 2. コンテナの概念

### コンテナと仮想マシンの比較

| 項目 | コンテナ (Docker) | 仮想マシン (VM) |
|------|-------------------|-----------------|
| **起動速度** | 数秒 | 数分 |
| **リソース** | 軽量（数十 MB〜） | 重い（数 GB〜） |
| **OS** | ホスト OS を共有 | ゲスト OS が必要 |
| **分離レベル** | プロセスレベル | ハードウェアレベル |
| **用途** | アプリケーション実行 | OS 全体の仮想化 |

### イメージとコンテナの違い

```plaintext
[Docker イメージ]
設計図・テンプレート
読み取り専用
一度作成したら変更しない

        ↓ docker run

[Docker コンテナ]
実際に動いているアプリケーション
読み書き可能
削除しても元のイメージは残る
```

**例え**
- **イメージ**: ケーキのレシピ本
- **コンテナ**: レシピから実際に作ったケーキ

同じレシピから何個でもケーキを作れるように、同じイメージから何個でもコンテナを作れます。

---

## 3. Docker のインストール

### macOS への Docker Desktop インストール

1. **Docker Desktop のダウンロード**
   ```bash
   # ブラウザで以下にアクセス
   https://www.docker.com/products/docker-desktop
   ```

2. **インストール手順**
   - ダウンロードした `.dmg` ファイルを開く
   - Docker アイコンを Applications フォルダにドラッグ
   - Applications から Docker を起動
   - メニューバーに Docker アイコンが表示されるのを確認

3. **インストール確認**
   ```bash
   docker --version
   # 出力例: Docker version 24.0.7, build afdd53b

   docker compose version
   # 出力例: Docker Compose version v2.23.0
   ```

> **Tip**: Docker Desktop を起動していないとコマンドが使えません。メニューバーの Docker アイコンを確認しましょう。

---

## 4. 基本コマンド

### docker run - コンテナの実行

**最初の Docker コンテナを起動**
```bash
# Hello World を実行
docker run hello-world

# 出力:
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

**対話的に Ubuntu を起動**
```bash
# Ubuntu コンテナを起動してシェルに入る
docker run -it ubuntu bash

# コンテナ内で実行
root@abc123:/# ls
root@abc123:/# cat /etc/os-release
root@abc123:/# exit  # コンテナから抜ける
```

**Web サーバーを起動**
```bash
# Nginx を起動してポート 8080 で公開
docker run -d -p 8080:80 --name my-nginx nginx

# ブラウザで http://localhost:8080 にアクセス
# → Nginx のウェルカムページが表示される
```

**オプション解説**
- `-it`: 対話的モード (interactive + tty)
- `-d`: バックグラウンド実行 (detached)
- `-p 8080:80`: ポートマッピング (ホスト:コンテナ)
- `--name`: コンテナに名前をつける
- `--rm`: 終了時に自動削除

### docker ps - コンテナ一覧

```bash
# 実行中のコンテナを表示
docker ps

# 出力例:
# CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
# abc123def456   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp   my-nginx

# 停止中も含めてすべて表示
docker ps -a
```

### docker stop / start / restart - コンテナの制御

```bash
# コンテナを停止
docker stop my-nginx

# コンテナを開始
docker start my-nginx

# コンテナを再起動
docker restart my-nginx
```

### docker rm - コンテナの削除

```bash
# コンテナを削除（停止中のみ）
docker rm my-nginx

# 強制削除（実行中でも削除）
docker rm -f my-nginx

# 停止中のコンテナを一括削除
docker container prune
```

### docker images - イメージ一覧

```bash
# ローカルのイメージを表示
docker images

# 出力例:
# REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
# nginx        latest    abc123def456   2 weeks ago    187MB
# ubuntu       latest    def456abc789   3 weeks ago    77.8MB
```

### docker pull - イメージの取得

```bash
# 最新の Python イメージを取得
docker pull python

# 特定バージョンを取得
docker pull python:3.10

# Alpine Linux ベースの軽量版を取得
docker pull python:3.10-alpine
```

### docker logs - ログの確認

```bash
# コンテナのログを表示
docker logs my-nginx

# リアルタイムでログを表示
docker logs -f my-nginx

# 最新 100 行を表示
docker logs --tail 100 my-nginx
```

---

## 5. Dockerfile の書き方

### Dockerfile とは

Dockerfile は、Docker イメージの設計図です。どんな環境を作りたいか、何をインストールするかを記述します。

### 基本的な命令

| 命令 | 説明 | 例 |
|------|------|-----|
| `FROM` | ベースイメージを指定 | `FROM python:3.10` |
| `WORKDIR` | 作業ディレクトリを設定 | `WORKDIR /app` |
| `COPY` | ファイルをコピー | `COPY . /app` |
| `RUN` | コマンドを実行 | `RUN pip install -r requirements.txt` |
| `ENV` | 環境変数を設定 | `ENV DEBUG=True` |
| `EXPOSE` | ポートを公開 | `EXPOSE 8000` |
| `CMD` | コンテナ起動時のコマンド | `CMD ["python", "app.py"]` |

### Python Web アプリケーションの例

**プロジェクト構成**
```plaintext
my-python-app/
├── Dockerfile
├── requirements.txt
└── app.py
```

**app.py**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

**requirements.txt**
```
flask==3.0.0
```

**Dockerfile**
```dockerfile
# ベースイメージを指定
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# ポート 8000 を公開
EXPOSE 8000

# アプリケーションを起動
CMD ["python", "app.py"]
```

**ビルドと実行**
```bash
# イメージをビルド
docker build -t my-python-app .

# コンテナを実行
docker run -d -p 8000:8000 --name my-app my-python-app

# ブラウザで http://localhost:8000 にアクセス
```

> **Tip**: `COPY requirements.txt .` と `COPY . .` を分けることで、コードを変更しても依存関係のインストールをスキップできます（ビルドキャッシュの活用）。

### マルチステージビルド

本番環境用に軽量なイメージを作成する場合:

```dockerfile
# ビルドステージ
FROM python:3.10 AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 実行ステージ
FROM python:3.10-slim

WORKDIR /app

# ビルドステージからインストール済みパッケージをコピー
COPY --from=builder /root/.local /root/.local
COPY . .

# PATH に追加
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000
CMD ["python", "app.py"]
```

---

## 6. docker-compose

### docker-compose とは

複数のコンテナを一度に管理するためのツールです。Web サーバー + データベース + キャッシュなど、複数のサービスを組み合わせたアプリケーションに便利です。

### docker-compose.yml の基本構造

```yaml
version: '3.8'

services:
  # サービス名（任意）
  web:
    # イメージまたは Dockerfile
    build: .
    # ポートマッピング
    ports:
      - "8000:8000"
    # 環境変数
    environment:
      - DEBUG=True
    # 依存関係
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
    # ボリューム
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

### Flask + PostgreSQL の例

**プロジェクト構成**
```plaintext
flask-postgres-app/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── app.py
```

**docker-compose.yml**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/myapp
    depends_on:
      - db
    volumes:
      - .:/app
    command: python app.py

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres-data:
```

**Dockerfile**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
```

**requirements.txt**
```
flask==3.0.0
psycopg2-binary==2.9.9
```

**app.py**
```python
import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # データベース接続テスト
    try:
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        conn.close()
        return 'Connected to database!'
    except Exception as e:
        return f'Database error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### docker-compose コマンド

```bash
# すべてのサービスを起動
docker compose up

# バックグラウンドで起動
docker compose up -d

# ビルドしてから起動
docker compose up --build

# ログを表示
docker compose logs
docker compose logs -f web  # 特定サービスのログ

# サービスを停止
docker compose stop

# サービスを停止して削除
docker compose down

# ボリュームも含めて削除
docker compose down -v

# 特定サービスでコマンド実行
docker compose exec web bash
docker compose exec db psql -U postgres
```

---

## 7. ボリュームとネットワーク

### ボリューム - データの永続化

コンテナを削除するとデータも消えてしまいます。データを保存し続けるにはボリュームを使います。

**ボリュームの種類**

| 種類 | 説明 | 用途 |
|------|------|------|
| **名前付きボリューム** | Docker が管理 | データベースデータ |
| **バインドマウント** | ホストのディレクトリをマウント | 開発中のコード |
| **tmpfs** | メモリ上に一時保存 | 一時ファイル |

**名前付きボリュームの例**
```bash
# ボリュームを作成
docker volume create my-data

# ボリュームを使ってコンテナを起動
docker run -v my-data:/data ubuntu

# ボリューム一覧
docker volume ls

# ボリュームの詳細
docker volume inspect my-data
```

**バインドマウントの例**
```bash
# カレントディレクトリをコンテナにマウント
docker run -v $(pwd):/app -w /app python:3.10 python app.py

# Windows の場合
docker run -v ${PWD}:/app -w /app python:3.10 python app.py
```

**docker-compose でのボリューム**
```yaml
services:
  db:
    image: postgres:15
    volumes:
      # 名前付きボリューム
      - db-data:/var/lib/postgresql/data
      # バインドマウント
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  db-data:
```

### ネットワーク - コンテナ間通信

docker-compose を使うと、自動的にネットワークが作成され、サービス名で通信できます。

```yaml
services:
  web:
    # ...
    environment:
      # サービス名 "db" で接続できる
      - DATABASE_URL=postgresql://postgres:secret@db:5432/myapp

  db:
    # ...
```

**手動でネットワークを作成**
```bash
# ネットワークを作成
docker network create my-network

# ネットワークに接続してコンテナを起動
docker run -d --network my-network --name web nginx
docker run -d --network my-network --name db postgres

# web コンテナから db コンテナに接続可能
docker exec web ping db
```

---

## 8. Dev Containers（VS Code）

### Dev Containers とは

VS Code の拡張機能で、コンテナの中で開発できます。

**メリット**
- ローカル環境を汚さない
- プロジェクトごとに異なる環境を簡単に切り替え
- チーム全体で同じ開発環境を共有

### セットアップ

1. **VS Code 拡張機能のインストール**
   - `Dev Containers` をインストール

2. **プロジェクト構成**
   ```plaintext
   my-project/
   ├── .devcontainer/
   │   ├── devcontainer.json
   │   └── Dockerfile
   └── src/
       └── app.py
   ```

3. **devcontainer.json の作成**
   ```json
   {
     "name": "Python 3.10 Development",
     "build": {
       "dockerfile": "Dockerfile"
     },
     "customizations": {
       "vscode": {
         "extensions": [
           "ms-python.python",
           "ms-python.vscode-pylance",
           "ms-toolsai.jupyter"
         ],
         "settings": {
           "python.defaultInterpreterPath": "/usr/local/bin/python"
         }
       }
     },
     "forwardPorts": [8000],
     "postCreateCommand": "pip install -r requirements.txt",
     "remoteUser": "vscode"
   }
   ```

4. **Dockerfile**
   ```dockerfile
   FROM python:3.10

   # 非 root ユーザーを作成
   ARG USERNAME=vscode
   ARG USER_UID=1000
   ARG USER_GID=$USER_UID

   RUN groupadd --gid $USER_GID $USERNAME \
       && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
       && apt-get update \
       && apt-get install -y git \
       && apt-get clean

   USER $USERNAME
   ```

### Dev Container の使い方

```bash
# VS Code でプロジェクトを開く
code my-project

# コマンドパレット (Cmd+Shift+P) を開いて
# "Dev Containers: Reopen in Container" を選択

# コンテナ内で開発開始
# ターミナルもコンテナ内で実行される
```

**docker-compose との連携**
```json
{
  "name": "Flask + PostgreSQL",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "web",
  "workspaceFolder": "/app",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python"
      ]
    }
  }
}
```

---

## 9. Docker と Claude Code

### Claude Code でのプロジェクト例

Claude Code を使って Docker 化されたプロジェクトを管理する方法。

**プロンプト例**
```
Claude、このプロジェクトを Docker 化してください。
Python 3.10、Flask、PostgreSQL を使います。
docker-compose.yml も作成してください。
```

**Claude の応答（例）**
```
Dockerfile と docker-compose.yml を作成しました。

以下のコマンドで起動できます:
docker compose up -d

データベースのマイグレーションは:
docker compose exec web python migrate.py
```

### Docker コンテナ内でテストを実行

```bash
# テストを実行
docker compose exec web pytest

# カバレッジ付きでテスト
docker compose exec web pytest --cov=app

# 特定のテストファイルを実行
docker compose exec web pytest tests/test_api.py
```

### Claude Code との統合例

**.claude/tasks/docker-test.sh**
```bash
#!/bin/bash
# Docker コンテナ内でテストを実行するタスク

echo "Starting Docker services..."
docker compose up -d

echo "Running tests..."
docker compose exec -T web pytest --cov=app --cov-report=term

echo "Stopping Docker services..."
docker compose down
```

**使い方**
```bash
# Claude に依頼
# "Docker 環境でテストを実行してください"

# または直接実行
bash .claude/tasks/docker-test.sh
```

---

## 10. よく使うパターン集

### Python アプリケーション

**シンプルな Python アプリ**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

**Jupyter Notebook 環境**
```dockerfile
FROM python:3.10

WORKDIR /workspace

RUN pip install jupyter numpy pandas matplotlib

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

```bash
# 実行
docker run -p 8888:8888 -v $(pwd):/workspace my-jupyter
```

### Node.js アプリケーション

**Express サーバー**
```dockerfile
FROM node:18-alpine

WORKDIR /app

# package.json と package-lock.json をコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm ci --only=production

# アプリケーションコードをコピー
COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

**開発環境用（ホットリロード対応）**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules  # node_modules は除外
    command: npm run dev
    environment:
      - NODE_ENV=development
```

### データベースコンテナ

**PostgreSQL with 初期データ**
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"

volumes:
  postgres-data:
```

**init-scripts/01-create-tables.sql**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');
```

### Redis キャッシュサーバー

```yaml
version: '3.8'

services:
  web:
    build: .
    depends_on:
      - redis
    environment:
      - REDIS_URL=redis://redis:6379

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

### フルスタックアプリケーション

**React + FastAPI + PostgreSQL**
```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - REACT_APP_API_URL=http://localhost:8000

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=postgresql://postgres:secret@db:5432/myapp
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

### 便利な Docker コマンドスニペット

```bash
# すべてのコンテナを停止
docker stop $(docker ps -q)

# すべてのコンテナを削除
docker rm $(docker ps -aq)

# 未使用のイメージを削除
docker image prune

# すべての未使用リソースを削除（注意！）
docker system prune -a

# ディスク使用量を確認
docker system df

# コンテナ内でシェルを起動
docker exec -it <container-name> bash

# コンテナのファイルをホストにコピー
docker cp <container-name>:/path/to/file ./local-path

# ホストのファイルをコンテナにコピー
docker cp ./local-file <container-name>:/path/to/destination

# コンテナのリソース使用状況を確認
docker stats

# 特定コンテナの詳細情報
docker inspect <container-name>
```

---

## まとめ

### 学んだこと

- Docker の基本概念（イメージとコンテナ）
- 基本的な Docker コマンド
- Dockerfile の書き方とベストプラクティス
- docker-compose による複数コンテナの管理
- ボリュームとネットワークの活用
- VS Code Dev Containers での開発
- Claude Code との連携
- 実践的な Dockerfile パターン

### 次のステップ

1. **実際にプロジェクトを Docker 化してみる**
   - 既存のプロジェクトを選んで Dockerfile を作成
   - docker-compose で複数サービスを連携

2. **Dev Containers で開発環境を構築**
   - VS Code で Dev Containers を試す
   - チームメンバーと環境を共有

3. **本番環境を想定した最適化**
   - マルチステージビルドで軽量化
   - セキュリティベストプラクティスを学ぶ

4. **CI/CD パイプラインとの統合**
   - GitHub Actions で Docker イメージを自動ビルド
   - テストを自動化

### 参考リソース

- [Docker 公式ドキュメント](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) - 公式イメージの検索
- [Dev Containers 公式ドキュメント](https://code.visualstudio.com/docs/devcontainers/containers)
- [Dockerfile ベストプラクティス](https://docs.docker.com/develop/dev-best-practices/)

> **Tip**: Docker は最初は難しく感じるかもしれませんが、実際に手を動かして試すことで理解が深まります。小さなプロジェクトから始めて、徐々に複雑な構成に挑戦していきましょう。

---

**関連ガイド**
- [VS Code 基本操作ガイド](00-vscode-guide.md)
- [ターミナル CLI ツールガイド](03-terminal-tools-guide.md)
- [Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md)
- [テスト入門ガイド](21-testing-intro-guide.md)
- [データベース入門ガイド](24-database-intro-guide.md)
