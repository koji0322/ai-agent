# API 設計・連携ガイド

## 0. はじめに

### 想定読者
- プログラミング初心者
- Web 開発の基礎を学んだ方
- API の設計や利用方法を学びたい方
- Claude API を使ってアプリケーションを作りたい方

### ゴール
このガイドでは、API の基礎から実践的な設計・利用方法まで学びます。

- API の概念と HTTP の基礎を理解する
- REST API の設計原則を学ぶ
- FastAPI/Flask で簡単な API を作成する
- 外部 API（Claude API など）を利用する
- API の認証とセキュリティを理解する
- Claude Code を活用した API 開発を実践する

### 関連ガイド
- [Claude Code 基本操作ガイド](10-claude-code-guide.md)
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md)
- [Web 開発基礎ガイド](23-web-basics-guide.md)
- [データベース入門ガイド](24-database-intro-guide.md)
- [セキュリティ基礎ガイド](20-security-basics-guide.md)
- [テスト入門ガイド](21-testing-intro-guide.md)

---

## 1. API とは何か

### API の定義

**API（Application Programming Interface）** は、ソフトウェア同士が情報をやり取りするための「窓口」です。

### レストランの例え

API を理解するには、レストランに例えるとわかりやすいです。

```
レストランの仕組み           API の仕組み
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
お客さん（あなた）      →    クライアント（アプリ）
メニュー               →    API ドキュメント
ウェイター             →    API エンドポイント
注文                   →    リクエスト
キッチン               →    サーバー/データベース
料理                   →    レスポンス
```

お客さんはキッチンに直接入れません。ウェイターを通じて注文し、料理を受け取ります。同様に、アプリケーションは API を通じてサーバーとやり取りします。

### API の種類

| 種類 | 説明 | 例 |
|------|------|-----|
| **REST API** | HTTP を使った最も一般的な API | Twitter API, GitHub API |
| **GraphQL** | クエリ言語を使った柔軟な API | Facebook Graph API |
| **WebSocket** | リアルタイム双方向通信 | チャットアプリ |
| **gRPC** | 高速なバイナリプロトコル | Google 内部サービス |

このガイドでは、最も広く使われている **REST API** を中心に学びます。

> **ヒント**: Web API と聞いたら、ほとんどの場合 REST API を指します。

---

## 2. HTTP の基礎

### HTTP メソッド

API では、HTTP メソッドで「何をしたいか」を表現します。

| メソッド | 意味 | 例 |
|----------|------|-----|
| **GET** | データを取得 | ユーザー情報を取得 |
| **POST** | データを作成 | 新しいユーザーを登録 |
| **PUT** | データを更新（全体） | ユーザー情報を完全に上書き |
| **PATCH** | データを更新（一部） | ユーザーのメールアドレスだけ変更 |
| **DELETE** | データを削除 | ユーザーを削除 |

### HTTP ステータスコード

サーバーからの応答には、必ずステータスコードが含まれます。

| コード | 意味 | 説明 |
|--------|------|------|
| **200** | OK | 成功 |
| **201** | Created | リソースの作成成功 |
| **204** | No Content | 成功（レスポンスボディなし） |
| **400** | Bad Request | リクエストが不正 |
| **401** | Unauthorized | 認証が必要 |
| **403** | Forbidden | アクセス権限がない |
| **404** | Not Found | リソースが見つからない |
| **500** | Internal Server Error | サーバーエラー |

```python
# Python での HTTP リクエスト例
import requests

response = requests.get("https://api.example.com/users/123")

print(response.status_code)  # 200
print(response.json())        # レスポンスボディ
```

### HTTP ヘッダー

ヘッダーは、リクエストやレスポンスに関する追加情報を伝えます。

```http
# リクエストヘッダーの例
GET /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer abc123xyz
Accept: application/json
User-Agent: MyApp/1.0
```

主要なヘッダー:

| ヘッダー | 説明 |
|----------|------|
| **Content-Type** | データの形式（application/json など） |
| **Authorization** | 認証情報 |
| **Accept** | 受け入れ可能なレスポンス形式 |
| **User-Agent** | クライアント情報 |

> **ヒント**: API では、ほとんどの場合 JSON 形式（`Content-Type: application/json`）でデータをやり取りします。

---

## 3. REST API の設計原則

### REST とは

**REST（Representational State Transfer）** は、Web API を設計する際の標準的なアーキテクチャスタイルです。

### REST の主要原則

#### 1. リソースベースの URL

リソース（データの対象）を URL で表現します。

```
良い例（RESTful）:
GET    /users          # ユーザー一覧を取得
GET    /users/123      # ID=123 のユーザーを取得
POST   /users          # 新しいユーザーを作成
PUT    /users/123      # ID=123 のユーザーを更新
DELETE /users/123      # ID=123 のユーザーを削除

悪い例（非 RESTful）:
GET    /getUser?id=123
POST   /createUser
POST   /deleteUser
```

#### 2. ステートレス

各リクエストは独立しており、サーバーはセッション状態を保持しません。

```python
# 悪い例: サーバーがセッションに依存
GET /set-user/123    # ユーザーをセッションに保存
GET /get-orders      # セッションのユーザーの注文を取得

# 良い例: 各リクエストが完結
GET /users/123/orders  # ユーザー 123 の注文を取得
```

#### 3. CRUD とメソッドのマッピング

| CRUD 操作 | HTTP メソッド | URL 例 |
|-----------|---------------|---------|
| **Create** | POST | `POST /users` |
| **Read** | GET | `GET /users/123` |
| **Update** | PUT/PATCH | `PUT /users/123` |
| **Delete** | DELETE | `DELETE /users/123` |

### URL 設計のベストプラクティス

```
✓ 複数形を使う: /users ではなく /user
✓ 小文字を使う: /UserProfiles ではなく /user-profiles
✓ ハイフンで区切る: /user_profiles ではなく /user-profiles
✓ 階層構造を表現: /users/123/orders/456
✗ 動詞を使わない: /getUsers ではなく GET /users
✗ 拡張子を使わない: /users.json ではなく /users
```

> **ヒント**: REST API は「リソース」を中心に設計します。「動作」ではなく「もの」に焦点を当てましょう。

---

## 4. FastAPI 入門

### FastAPI とは

**FastAPI** は、Python で高速に API を開発できる現代的なフレームワークです。

**特徴:**
- 高速（非同期処理対応）
- 自動ドキュメント生成（Swagger UI）
- 型ヒントによる自動バリデーション
- 直感的な構文

### インストール

```bash
pip install fastapi
pip install "uvicorn[standard]"  # ASGI サーバー
```

### Hello World API

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
```

実行:

```bash
uvicorn main:app --reload
```

ブラウザで `http://localhost:8000` にアクセスすると、JSON が返ってきます。

### 自動ドキュメント

FastAPI は自動的に API ドキュメントを生成します。

```
http://localhost:8000/docs       # Swagger UI
http://localhost:8000/redoc      # ReDoc
```

### パスパラメータとクエリパラメータ

```python
from fastapi import FastAPI

app = FastAPI()

# パスパラメータ
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# クエリパラメータ
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# 両方の組み合わせ
@app.get("/users/{user_id}/items")
def get_user_items(user_id: int, skip: int = 0):
    return {"user_id": user_id, "skip": skip}
```

使用例:
```
GET /users/123                  # user_id=123
GET /items?skip=20&limit=5      # skip=20, limit=5
GET /users/123/items?skip=10    # user_id=123, skip=10
```

### リクエストボディ

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int | None = None

@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} created", "user": user}
```

リクエスト例:
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"name": "太郎", "email": "taro@example.com", "age": 25}'
```

### 完全な CRUD 例

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# データストア（本番では DB を使用）
users_db = {}
next_id = 1

class User(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# Create
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: User):
    global next_id
    user_id = next_id
    users_db[user_id] = user.model_dump()
    next_id += 1
    return {"id": user_id, **user.model_dump()}

# Read (一覧)
@app.get("/users")
def list_users():
    return [{"id": uid, **data} for uid, data in users_db.items()]

# Read (単一)
@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **users_db[user_id]}

# Update
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user.model_dump()
    return {"id": user_id, **user.model_dump()}

# Delete
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return None
```

> **ヒント**: FastAPI の Pydantic モデルは、自動的にバリデーションとドキュメント生成を行います。型ヒントを活用しましょう。

---

## 5. Flask 概要

### Flask とは

**Flask** は、Python の軽量な Web フレームワークです。FastAPI より歴史が長く、シンプルな API に適しています。

### FastAPI との比較

| 特徴 | FastAPI | Flask |
|------|---------|-------|
| **速度** | 高速（非同期対応） | 標準的 |
| **自動ドキュメント** | あり（Swagger） | なし（拡張が必要） |
| **型ヒント** | 必須・活用 | オプション |
| **学習曲線** | 緩やか | 非常に緩やか |
| **エコシステム** | 成長中 | 成熟 |

### Flask の基本例

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
next_id = 1

@app.route("/")
def home():
    return {"message": "Hello, Flask!"}

@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.get_json()
    user_id = next_id
    users[user_id] = data
    next_id += 1
    return jsonify({"id": user_id, **data}), 201

@app.route("/users/<int:user_id>")
def get_user(user_id):
    if user_id not in users:
        return {"error": "User not found"}, 404
    return jsonify({"id": user_id, **users[user_id]})

if __name__ == "__main__":
    app.run(debug=True)
```

実行:
```bash
pip install flask
python app.py
```

### どちらを選ぶべきか

- **FastAPI を選ぶ場合:**
  - 新規プロジェクト
  - 型安全性が重要
  - 自動ドキュメントが必要
  - 高速な API が必要

- **Flask を選ぶ場合:**
  - シンプルな API
  - 既存の Flask エコシステムを活用
  - 学習コストを最小限にしたい

> **ヒント**: 2026 年現在、新規プロジェクトでは FastAPI が推奨されることが多いです。

---

## 6. 外部 API の利用

### requests ライブラリ

Python で外部 API を呼び出すには、`requests` ライブラリを使います。

```bash
pip install requests
```

### 基本的な GET リクエスト

```python
import requests

# GET リクエスト
response = requests.get("https://api.github.com/users/github")

# ステータスコードを確認
print(response.status_code)  # 200

# JSON レスポンスを取得
data = response.json()
print(data["name"])  # "GitHub"
print(data["public_repos"])
```

### パラメータ付きリクエスト

```python
import requests

# クエリパラメータ
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc"
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

data = response.json()
print(f"Total: {data['total_count']}")
for repo in data["items"][:5]:
    print(f"- {repo['name']}: {repo['stargazers_count']} stars")
```

### POST リクエスト

```python
import requests

# JSON データを送信
user_data = {
    "name": "太郎",
    "email": "taro@example.com"
}

response = requests.post(
    "https://api.example.com/users",
    json=user_data,  # 自動的に JSON に変換し、Content-Type を設定
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

if response.status_code == 201:
    print("ユーザー作成成功:", response.json())
else:
    print("エラー:", response.status_code)
```

### エラーハンドリング

```python
import requests
from requests.exceptions import RequestException, Timeout, HTTPError

def fetch_user(user_id):
    try:
        response = requests.get(
            f"https://api.example.com/users/{user_id}",
            timeout=5  # タイムアウトを設定
        )

        # HTTP エラーをチェック（4xx, 5xx）
        response.raise_for_status()

        return response.json()

    except Timeout:
        print("タイムアウトしました")
    except HTTPError as e:
        print(f"HTTP エラー: {e.response.status_code}")
    except RequestException as e:
        print(f"リクエストエラー: {e}")

    return None

# 使用例
user = fetch_user(123)
if user:
    print(user)
```

### JSON の扱い

```python
import requests

response = requests.get("https://api.example.com/data")

# JSON を Python オブジェクトに変換
data = response.json()

# データへのアクセス
if isinstance(data, dict):
    print(data.get("name", "名前なし"))
elif isinstance(data, list):
    for item in data:
        print(item)

# ネストされたデータ
user = response.json()
print(user["profile"]["address"]["city"])
```

> **ヒント**: API を呼び出す際は、必ずタイムアウトとエラーハンドリングを設定しましょう。

---

## 7. Claude API（Anthropic API）

### Claude API とは

**Claude API** は、Anthropic が提供する AI モデルを利用するための API です。高度な会話、文章生成、分析などが可能です。

### SDK のインストール

```bash
pip install anthropic
```

### 基本的なメッセージ API

```python
import anthropic
import os

# API キーを設定
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# メッセージを送信
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Python で API を作る方法を教えてください。"}
    ]
)

print(message.content[0].text)
```

### システムプロンプトの使用

```python
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    system="あなたは親切なプログラミング講師です。初心者にもわかりやすく説明してください。",
    messages=[
        {"role": "user", "content": "REST API とは何ですか？"}
    ]
)

print(message.content[0].text)
```

### ストリーミング

リアルタイムでレスポンスを受け取ることができます。

```python
with client.messages.stream(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "簡単な物語を作ってください。"}
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### ツール使用（Tool Use）の概要

Claude はツール（関数）を呼び出すことができます。

```python
tools = [
    {
        "name": "get_weather",
        "description": "指定された都市の天気を取得します。",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "都市名（例: 東京）"
                }
            },
            "required": ["city"]
        }
    }
]

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "東京の天気を教えて"}
    ]
)

# Claude がツールの使用を提案
for block in message.content:
    if block.type == "tool_use":
        print(f"ツール: {block.name}")
        print(f"入力: {block.input}")
```

### FastAPI と Claude API の統合例

```python
from fastapi import FastAPI
from pydantic import BaseModel
import anthropic
import os

app = FastAPI()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": request.message}
        ]
    )

    return {
        "response": message.content[0].text,
        "model": message.model,
        "usage": {
            "input_tokens": message.usage.input_tokens,
            "output_tokens": message.usage.output_tokens
        }
    }
```

使用例:
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "こんにちは！"}'
```

> **ヒント**: API キーは環境変数に保存し、コードに直接書かないようにしましょう。詳しくは [セキュリティ基礎ガイド](20-security-basics-guide.md) を参照してください。

---

## 8. API 認証

### API キー認証

最もシンプルな認証方法です。

**リクエスト例:**
```python
import requests

headers = {
    "X-API-Key": "your-api-key-here"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

**FastAPI での実装:**
```python
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "secret-api-key"

@app.get("/protected")
def protected_route(x_api_key: str = Header()):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"message": "認証成功"}
```

### Bearer トークン

JWT（JSON Web Token）などでよく使われます。

```python
import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

response = requests.get(
    "https://api.example.com/user",
    headers=headers
)
```

**FastAPI での実装:**
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return credentials.credentials

@app.get("/user")
def get_user(token: str = Depends(verify_token)):
    return {"message": "認証成功", "token": token}
```

### OAuth 2.0 の基礎

OAuth は、第三者アプリケーションにアクセス権を付与する標準プロトコルです。

**フロー:**
```
1. ユーザーが「GitHub でログイン」をクリック
2. GitHub の認証ページにリダイレクト
3. ユーザーが許可
4. アプリケーションに認可コードが返される
5. 認可コードをアクセストークンに交換
6. アクセストークンで API を呼び出し
```

**使用例（GitHub OAuth）:**
```python
import requests

# ステップ 1: ユーザーを認証ページに送る
auth_url = (
    "https://github.com/login/oauth/authorize"
    "?client_id=YOUR_CLIENT_ID"
    "&scope=user"
)

# ステップ 2: 認可コードを受け取る（リダイレクトで）
# code = "受け取った認可コード"

# ステップ 3: アクセストークンを取得
token_response = requests.post(
    "https://github.com/login/oauth/access_token",
    data={
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "code": code
    },
    headers={"Accept": "application/json"}
)

access_token = token_response.json()["access_token"]

# ステップ 4: API を呼び出す
user_response = requests.get(
    "https://api.github.com/user",
    headers={"Authorization": f"Bearer {access_token}"}
)

print(user_response.json())
```

### 認証方式の比較

| 方式 | セキュリティ | 複雑さ | 用途 |
|------|--------------|--------|------|
| **API キー** | 低 | 簡単 | 内部 API、開発環境 |
| **Bearer トークン** | 中 | 中程度 | 一般的な API |
| **OAuth 2.0** | 高 | 複雑 | 第三者アプリ連携 |

> **ヒント**: API キーやトークンは絶対にコードにハードコードせず、環境変数や秘密管理サービスを使いましょう。

---

## 9. API テストとドキュメント

### Swagger / OpenAPI

**OpenAPI** は、API を記述する標準仕様です。FastAPI は自動的に OpenAPI ドキュメントを生成します。

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="これは素晴らしい API です",
    version="1.0.0"
)

@app.get("/items/{item_id}", tags=["items"])
def get_item(item_id: int):
    """
    アイテムを ID で取得します。

    - **item_id**: アイテムの ID
    """
    return {"item_id": item_id}
```

`/docs` にアクセスすると、美しいドキュメントが表示されます。

### httpx でのテスト

`httpx` は、`requests` の後継で、非同期にも対応しています。

```bash
pip install httpx pytest
```

**テストコード:**
```python
# test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_user():
    response = client.post(
        "/users",
        json={"name": "太郎", "email": "taro@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "太郎"
    assert "id" in data

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
```

実行:
```bash
pytest test_api.py -v
```

### Postman

**Postman** は、API をテストするための GUI ツールです。

**使い方:**
1. Postman をダウンロード（https://www.postman.com/）
2. 新しいリクエストを作成
3. メソッド、URL、ヘッダー、ボディを設定
4. Send をクリック

**便利な機能:**
- コレクション（複数のリクエストをグループ化）
- 環境変数（開発/本番の切り替え）
- テストスクリプト（自動テスト）
- モック サーバー

### API テストのベストプラクティス

```python
# test_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestUserAPI:
    def test_create_user_success(self):
        """正常系: ユーザー作成"""
        response = client.post("/users", json={
            "name": "太郎",
            "email": "taro@example.com"
        })
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "太郎"

    def test_create_user_invalid_email(self):
        """異常系: 不正なメールアドレス"""
        response = client.post("/users", json={
            "name": "太郎",
            "email": "invalid-email"
        })
        assert response.status_code == 422  # Validation error

    def test_get_user_success(self):
        """正常系: ユーザー取得"""
        # まずユーザーを作成
        create_response = client.post("/users", json={
            "name": "次郎",
            "email": "jiro@example.com"
        })
        user_id = create_response.json()["id"]

        # 作成したユーザーを取得
        get_response = client.get(f"/users/{user_id}")
        assert get_response.status_code == 200
        assert get_response.json()["name"] == "次郎"

    def test_get_user_not_found(self):
        """異常系: 存在しないユーザー"""
        response = client.get("/users/99999")
        assert response.status_code == 404
```

> **ヒント**: API テストは、正常系だけでなく異常系（エラーケース）も必ずテストしましょう。詳しくは [テスト入門ガイド](21-testing-intro-guide.md) を参照してください。

---

## 10. Claude Code で API 開発

### Claude Code を使った API 開発の流れ

Claude Code は、API の設計、実装、テストを効率化します。

**基本的な使い方:**

1. **API の設計を依頼:**
```
ユーザー管理 API を FastAPI で作成してください。
以下の機能が必要です:
- ユーザーの作成、取得、更新、削除
- メールアドレスのバリデーション
- ユーザー一覧の取得（ページネーション付き）
```

2. **Claude Code が生成:**
   - FastAPI アプリケーションコード
   - Pydantic モデル
   - バリデーションロジック
   - エラーハンドリング

3. **テストを依頼:**
```
上記の API のテストコードを pytest で作成してください。
```

4. **ドキュメントを依頼:**
```
API の README.md を作成してください。
エンドポイント一覧と使い方を含めてください。
```

### 実践例: ブログ API を作る

```
Claude Code に依頼:

ブログ記事を管理する REST API を FastAPI で作成してください。

要件:
- 記事の作成、取得、更新、削除
- 記事には title, content, author, created_at を含む
- SQLite データベースを使用
- 自動テストを含める
```

Claude Code は以下を生成します:

**1. main.py（API 本体）**
```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime

# データベース設定
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# モデル定義
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Pydantic スキーマ
class ArticleCreate(BaseModel):
    title: str
    content: str
    author: str

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime

    class Config:
        from_attributes = True

# FastAPI アプリ
app = FastAPI(title="Blog API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/articles", response_model=ArticleResponse, status_code=201)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/articles", response_model=list[ArticleResponse])
def list_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = db.query(Article).offset(skip).limit(limit).all()
    return articles

@app.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
```

**2. test_main.py（テスト）**
**3. README.md（ドキュメント）**

### Claude Code の活用テクニック

**データベース連携を追加:**
```
PostgreSQL を使うように変更してください。
また、マイグレーション用に Alembic を設定してください。
```

**認証を追加:**
```
JWT 認証を追加してください。
記事の作成、更新、削除には認証が必要です。
```

**エラーハンドリングを改善:**
```
より詳細なエラーメッセージとロギングを追加してください。
```

**デプロイ準備:**
```
Docker で動かせるように Dockerfile と docker-compose.yml を作成してください。
```

### Claude Code でできること

| タスク | 例 |
|--------|-----|
| **API 設計** | RESTful な URL 設計、レスポンス形式の提案 |
| **コード生成** | FastAPI/Flask アプリケーションの実装 |
| **テスト作成** | pytest によるテストコード生成 |
| **ドキュメント作成** | README、API 仕様書の作成 |
| **リファクタリング** | コードの改善、パフォーマンス最適化 |
| **デバッグ** | エラーの原因特定と修正 |
| **デプロイ支援** | Docker、CI/CD の設定 |

> **ヒント**: Claude Code は、要件を明確に伝えるほど良い結果が得られます。「何を作りたいか」だけでなく、「どう使われるか」も伝えましょう。

---

## まとめ

このガイドでは、API の基礎から実践的な開発方法まで学びました。

### 学んだこと

1. **API の概念**: レストランの例えで理解する API の仕組み
2. **HTTP の基礎**: メソッド、ステータスコード、ヘッダー
3. **REST 設計**: リソースベース、ステートレス、CRUD マッピング
4. **FastAPI**: 高速な API フレームワークの使い方
5. **外部 API 利用**: requests で API を呼び出す方法
6. **Claude API**: Anthropic API の基本的な使い方
7. **認証**: API キー、Bearer トークン、OAuth
8. **テスト**: pytest、Postman での API テスト
9. **Claude Code 活用**: AI を使った効率的な API 開発

### 次のステップ

1. **実践プロジェクト**: 簡単な API を作ってみる（Todo リスト、メモアプリなど）
2. **データベース統合**: [データベース入門ガイド](24-database-intro-guide.md) で学んだことを API に統合
3. **フロントエンド連携**: [Web 開発基礎ガイド](23-web-basics-guide.md) で学んだ HTML/JavaScript から API を呼び出す
4. **セキュリティ強化**: [セキュリティ基礎ガイド](20-security-basics-guide.md) で認証・認可を深く学ぶ
5. **テスト拡充**: [テスト入門ガイド](21-testing-intro-guide.md) で包括的なテスト戦略を学ぶ
6. **Claude API 活用**: AI を組み込んだアプリケーションを作る

### リソース

**公式ドキュメント:**
- [FastAPI 公式](https://fastapi.tiangolo.com/)
- [Flask 公式](https://flask.palletsprojects.com/)
- [Anthropic API ドキュメント](https://docs.anthropic.com/)
- [Python requests](https://requests.readthedocs.io/)

**学習リソース:**
- [REST API チュートリアル](https://restfulapi.net/)
- [HTTP ステータスコード一覧](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)
- [OpenAPI 仕様](https://swagger.io/specification/)

API 開発は、現代のソフトウェア開発において必須のスキルです。このガイドで学んだ基礎を土台に、実践的なプロジェクトに挑戦してみましょう。

Claude Code を活用すれば、複雑な API も効率的に開発できます。[Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) も参考にしてください。
