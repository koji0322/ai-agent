# テスト入門ガイド

---

## 0. はじめに

### 想定読者

- プログラミングの基本文法を学んだ初心者
- テストコードを書いたことがない、またはテストの重要性を理解したい方
- Python や JavaScript で開発を始めた方
- Claude Code を使ってテスト駆動開発を実践したい方

### ゴール

このガイドを読むことで、以下ができるようになります：

- テストの種類と役割を理解する
- pytest を使った Python のテストコードを書ける
- テスト駆動開発（TDD）の基本サイクルを実践できる
- テストカバレッジを測定し、改善できる
- CI/CD パイプラインでテストを自動化できる
- Claude Code を活用してテストコードを効率的に書ける

### 関連ガイド

- [Claude Code 基本操作ガイド](10-claude-code-guide.md) - Claude Code の基本的な使い方
- [Claude Code 実践ガイド](11-claude-code-practical-guide.md) - 実践的な開発フロー
- [セキュリティ基礎ガイド](20-security-basics-guide.md) - セキュリティテストの考え方
- [Docker 入門ガイド](22-docker-intro-guide.md) - コンテナ環境でのテスト実行
- [Web 開発基礎ガイド](23-web-basics-guide.md) - Web アプリケーションのテスト
- [API 設計・連携ガイド](25-api-guide.md) - API テストの実践

---

## 1. なぜテストが重要なのか

### テストコードの価値

テストコードは、プログラムが正しく動作することを自動的に確認するためのコードです。

**テストコードがない場合の問題：**

- 変更のたびに手動で動作確認が必要（時間がかかる）
- バグに気づかずにリリースしてしまう
- リファクタリングが怖くてコードが改善できない
- 新しいメンバーがコードを理解しにくい

**テストコードがある場合の利点：**

- 自動でバグを検出できる
- 自信を持ってコードを変更できる
- ドキュメントとしての役割も果たす
- 開発速度が長期的に向上する

### 実例：テストがあると何が変わるか

```python
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # ゼロ除算のバグがある
```

テストコードを書くことで、バグを早期発見できます：

```python
# test_calculator.py
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

    # ゼロ除算のテスト → バグを発見！
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

> **💡 ヒント：** テストは「保険」のようなもの。最初は時間がかかりますが、長期的には開発効率を大幅に向上させます。

---

## 2. テストの種類

テストにはいくつかの種類があり、それぞれ異なる目的と粒度を持ちます。

### 主なテストの種類

| テストの種類 | 粒度 | 目的 | 実行速度 | 例 |
|------------|------|------|---------|-----|
| **ユニットテスト** | 小 | 関数やクラス単位の動作確認 | 高速 | 1つの関数が正しい値を返すか |
| **統合テスト** | 中 | 複数のモジュールの連携確認 | 中速 | DB とアプリケーションの連携 |
| **E2Eテスト** | 大 | システム全体の動作確認 | 低速 | ユーザーの操作フロー全体 |

### テストピラミッド

理想的なテスト構成は「ピラミッド型」と言われています：

```
        /\
       /E2E\      ← 少ない（遅いが、実際の使用に近い）
      /------\
     / 統合  \    ← 中程度
    /--------\
   / ユニット \   ← 多い（速くて安定している）
  /----------\
```

**推奨バランス：**
- ユニットテスト：70%
- 統合テスト：20%
- E2Eテスト：10%

### 各テストの具体例

**ユニットテスト：**

```python
# ユーザー名のバリデーション関数をテスト
def test_validate_username():
    assert validate_username("alice") == True
    assert validate_username("ab") == False  # 短すぎる
    assert validate_username("") == False    # 空文字
```

**統合テスト：**

```python
# データベースとの連携をテスト
def test_user_creation_in_db():
    user = create_user("alice", "alice@example.com")
    saved_user = get_user_by_id(user.id)
    assert saved_user.name == "alice"
```

**E2Eテスト（例：Playwright）：**

```python
# ログインから投稿までの一連の流れをテスト
def test_user_can_post_article(page):
    page.goto("http://localhost:3000/login")
    page.fill("#username", "alice")
    page.fill("#password", "password123")
    page.click("button[type='submit']")
    page.click("text=新規投稿")
    page.fill("#title", "テスト記事")
    page.click("text=投稿する")
    expect(page.locator("text=投稿しました")).to_be_visible()
```

---

## 3. pytest 入門

Python のテストフレームワークとして最も人気のある pytest を学びましょう。

### インストール

```bash
# pytest のインストール
pip install pytest

# バージョン確認
pytest --version
```

### 最初のテスト

**プロジェクト構成：**

```
my_project/
├── src/
│   └── calculator.py
└── tests/
    └── test_calculator.py
```

**calculator.py:**

```python
def add(a, b):
    """2つの数値を足す"""
    return a + b

def subtract(a, b):
    """2つの数値を引く"""
    return a - b

def multiply(a, b):
    """2つの数値を掛ける"""
    return a * b
```

**test_calculator.py:**

```python
from src.calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
```

**テストの実行：**

```bash
# すべてのテストを実行
pytest

# 詳細表示
pytest -v

# 特定のファイルだけ実行
pytest tests/test_calculator.py

# 特定のテスト関数だけ実行
pytest tests/test_calculator.py::test_add
```

### アサーション（assert）の使い方

pytest では、Python の標準的な `assert` 文を使います。

```python
def test_assertions():
    # 等価性
    assert 1 + 1 == 2

    # 不等価性
    assert 1 + 1 != 3

    # 比較
    assert 5 > 3
    assert 2 <= 2

    # 真偽値
    assert True
    assert not False

    # コンテナ
    assert "apple" in ["apple", "banana"]
    assert len([1, 2, 3]) == 3

    # 文字列
    assert "hello".startswith("he")

    # None チェック
    assert None is None
    assert [] is not None
```

### 例外のテスト

エラーが正しく発生することを確認するテスト：

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("ゼロで除算できません")
    return a / b

def test_divide_by_zero():
    # ValueError が発生することを確認
    with pytest.raises(ValueError):
        divide(10, 0)

    # エラーメッセージも確認
    with pytest.raises(ValueError, match="ゼロで除算できません"):
        divide(10, 0)
```

### フィクスチャ（Fixture）

テストで共通して使うデータやセットアップを定義できます。

```python
import pytest

@pytest.fixture
def sample_user():
    """テスト用のユーザーデータ"""
    return {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    }

@pytest.fixture
def database_connection():
    """データベース接続のセットアップとクリーンアップ"""
    # セットアップ
    db = create_test_database()

    yield db  # テストに渡す

    # クリーンアップ（テスト後に実行される）
    db.close()
    delete_test_database()

def test_user_creation(sample_user):
    # sample_user が自動的に渡される
    assert sample_user["name"] == "Alice"
    assert sample_user["age"] == 25

def test_database_insert(database_connection):
    # データベースを使ったテスト
    database_connection.insert("users", {"name": "Bob"})
    result = database_connection.query("SELECT * FROM users")
    assert len(result) == 1
```

### パラメータ化テスト

同じテストを異なるデータで複数回実行できます。

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("email", [
    "invalid",           # @ がない
    "@example.com",      # ローカル部がない
    "user@",             # ドメインがない
    "user @example.com", # スペースがある
])
def test_invalid_emails(email):
    assert not is_valid_email(email)
```

---

## 4. テスト駆動開発（TDD）

TDD（Test-Driven Development）は、テストを先に書いてから実装するプログラミング手法です。

### Red-Green-Refactor サイクル

TDD の基本サイクル：

1. **Red（失敗するテストを書く）**：まだ実装していない機能のテストを書く
2. **Green（最小限の実装で通す）**：テストが通る最小限のコードを書く
3. **Refactor（リファクタリング）**：コードを改善する（テストは通ったまま）

```
Red → Green → Refactor → Red → Green → Refactor → ...
```

### 実践例：Todo アプリの開発

**ステップ1：Red（失敗するテストを書く）**

```python
# test_todo.py
from todo import TodoList

def test_create_empty_todo_list():
    todo_list = TodoList()
    assert len(todo_list) == 0

def test_add_todo_item():
    todo_list = TodoList()
    todo_list.add("買い物に行く")
    assert len(todo_list) == 1
    assert todo_list.get(0) == "買い物に行く"
```

この時点で `pytest` を実行すると失敗します（todo.py がないため）。

**ステップ2：Green（最小限の実装）**

```python
# todo.py
class TodoList:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def get(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)
```

`pytest` を実行するとテストが通ります。

**ステップ3：Refactor（改善）**

次に、Todo 項目の完了機能を追加します。

```python
# test_todo.py（テストを追加）
def test_complete_todo_item():
    todo_list = TodoList()
    todo_list.add("買い物に行く")
    todo_list.complete(0)
    assert todo_list.is_completed(0) == True
```

実装：

```python
# todo.py
class TodoList:
    def __init__(self):
        self._items = []
        self._completed = set()

    def add(self, item):
        self._items.append(item)

    def get(self, index):
        return self._items[index]

    def complete(self, index):
        self._completed.add(index)

    def is_completed(self, index):
        return index in self._completed

    def __len__(self):
        return len(self._items)
```

### TDD のメリット

- **設計の改善：** テストを先に書くことで、使いやすい API を設計できる
- **バグの早期発見：** 実装と同時にバグを見つけられる
- **ドキュメント：** テストコードが仕様書になる
- **リファクタリングの安心感：** テストがあるので自信を持って改善できる

> **💡 ヒント：** 最初は完璧な TDD を目指す必要はありません。「テストを書く → 実装する」のサイクルに慣れることが大切です。

---

## 5. カバレッジ（テストの網羅性）

カバレッジは、テストコードが実際のコードをどれだけカバーしているかを示す指標です。

### pytest-cov のインストール

```bash
pip install pytest-cov
```

### カバレッジの測定

```bash
# カバレッジを測定して実行
pytest --cov=src tests/

# HTML レポートを生成
pytest --cov=src --cov-report=html tests/

# ターミナルで詳細表示
pytest --cov=src --cov-report=term-missing tests/
```

### カバレッジレポートの読み方

```
---------- coverage: platform darwin, python 3.13.2 -----------
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src/calculator.py       10      2    80%   15-16
src/validator.py        20      5    75%   8, 12-15
--------------------------------------------------
TOTAL                   30      7    77%
```

**各列の意味：**

- **Stmts（Statements）：** コードの総行数
- **Miss：** テストされていない行数
- **Cover：** カバレッジ率（%）
- **Missing：** テストされていない行番号

### カバレッジの目標値

| カバレッジ率 | 評価 | 説明 |
|------------|------|------|
| 90%以上 | 優秀 | 本番環境に適したレベル |
| 80-90% | 良好 | 多くのプロジェクトで推奨 |
| 70-80% | 普通 | 最低限のライン |
| 70%未満 | 改善必要 | テストが不足している |

> **⚠️ 注意：** カバレッジが高ければ良いわけではありません。100% を目指すよりも、重要な部分を確実にテストすることが大切です。

### カバレッジを改善する例

**カバレッジ 60% の状態：**

```python
# validator.py
def validate_age(age):
    if age < 0:
        raise ValueError("年齢は0以上である必要があります")
    if age > 150:
        raise ValueError("年齢が不正です")
    return True

# test_validator.py
def test_validate_age():
    assert validate_age(25) == True  # 正常系のみテスト
```

**カバレッジ 100% に改善：**

```python
# test_validator.py
import pytest

def test_validate_age_valid():
    assert validate_age(25) == True
    assert validate_age(0) == True
    assert validate_age(150) == True

def test_validate_age_negative():
    with pytest.raises(ValueError, match="年齢は0以上"):
        validate_age(-1)

def test_validate_age_too_large():
    with pytest.raises(ValueError, match="年齢が不正"):
        validate_age(151)
```

---

## 6. JavaScript のテスト

Python 以外の言語でもテストは重要です。JavaScript の代表的なテストフレームワークを紹介します。

### Jest（従来の標準）

```javascript
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;

// sum.test.js
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('adds negative numbers', () => {
  expect(sum(-1, -2)).toBe(-3);
});
```

**インストールと実行：**

```bash
npm install --save-dev jest

# package.json に追加
{
  "scripts": {
    "test": "jest"
  }
}

# 実行
npm test
```

### Vitest（モダンな選択肢）

Vite ベースの高速テストフレームワーク。

```javascript
// calculator.js
export function add(a, b) {
  return a + b;
}

// calculator.test.js
import { describe, it, expect } from 'vitest';
import { add } from './calculator';

describe('Calculator', () => {
  it('should add two numbers', () => {
    expect(add(2, 3)).toBe(5);
  });

  it('should handle negative numbers', () => {
    expect(add(-1, 1)).toBe(0);
  });
});
```

**インストールと実行：**

```bash
npm install --save-dev vitest

# package.json
{
  "scripts": {
    "test": "vitest"
  }
}

# 実行（watch モード）
npm test
```

### フレームワークの比較

| フレームワーク | 特徴 | 速度 | エコシステム |
|-------------|------|------|------------|
| **Jest** | 歴史が長く安定 | 中速 | 非常に豊富 |
| **Vitest** | モダンで高速 | 高速 | 成長中 |

---

## 7. CI 連携：GitHub Actions でテストを自動化

コードをプッシュするたびに自動でテストを実行する仕組みを作りましょう。

### GitHub Actions の基本設定

**`.github/workflows/test.yml`:**

```yaml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.13'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: Run tests
      run: |
        pytest --cov=src --cov-report=xml --cov-report=term

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v4
      with:
        file: ./coverage.xml
```

### 複数 Python バージョンでのテスト

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12', '3.13']

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest

    - name: Run tests
      run: pytest
```

### JavaScript プロジェクトの CI 設定

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'

    - name: Install dependencies
      run: npm ci

    - name: Run tests
      run: npm test

    - name: Run linter
      run: npm run lint
```

### テスト失敗時の通知

GitHub Actions が失敗すると、自動的にメール通知が届きます。また、PR のステータスチェックにも反映されます。

> **💡 ヒント：** CI でテストを自動化することで、バグを含むコードが main ブランチにマージされるのを防げます。

---

## 8. Claude Code でのテスト活用

Claude Code を使うと、テストコードの作成と実行が効率的になります。

### テストコードの生成

**プロンプト例：**

```
この関数のテストコードを pytest で書いてください：

def calculate_discount(price, discount_rate):
    if price < 0 or discount_rate < 0 or discount_rate > 100:
        raise ValueError("Invalid input")
    return price * (1 - discount_rate / 100)
```

Claude Code が生成する例：

```python
import pytest
from myapp import calculate_discount

class TestCalculateDiscount:
    def test_normal_discount(self):
        assert calculate_discount(1000, 10) == 900
        assert calculate_discount(500, 50) == 250

    def test_no_discount(self):
        assert calculate_discount(1000, 0) == 1000

    def test_full_discount(self):
        assert calculate_discount(1000, 100) == 0

    def test_negative_price(self):
        with pytest.raises(ValueError):
            calculate_discount(-100, 10)

    def test_negative_discount_rate(self):
        with pytest.raises(ValueError):
            calculate_discount(1000, -10)

    def test_discount_rate_over_100(self):
        with pytest.raises(ValueError):
            calculate_discount(1000, 110)
```

### TDD ワークフロー

**ステップ 1：要件を説明**

```
Todo リストアプリを TDD で作りたいです。
以下の機能をテストファーストで実装してください：

1. Todo アイテムの追加
2. Todo アイテムの完了
3. 未完了の Todo のみを取得
```

**ステップ 2：Claude Code がテストを先に書く**

```python
# test_todo.py
import pytest
from todo import TodoList

def test_add_todo():
    todo_list = TodoList()
    todo_list.add("買い物")
    assert len(todo_list.items) == 1

def test_complete_todo():
    todo_list = TodoList()
    todo_list.add("買い物")
    todo_list.complete(0)
    assert todo_list.items[0].is_completed == True

def test_get_pending_todos():
    todo_list = TodoList()
    todo_list.add("買い物")
    todo_list.add("掃除")
    todo_list.complete(0)
    pending = todo_list.get_pending()
    assert len(pending) == 1
    assert pending[0].title == "掃除"
```

**ステップ 3：実装**

Claude Code がテストを通すための実装を提案します。

### テストのデバッグ

```
このテストが失敗します。原因を調査して修正してください：

FAILED test_user.py::test_user_creation - AssertionError: assert 'alice' == 'Alice'
```

Claude Code が：
1. テストコードを読む
2. 実装コードを確認
3. 問題を特定
4. 修正案を提示

### カバレッジの改善依頼

```
現在のカバレッジは 65% です。80% 以上に改善するテストを追加してください。

特にカバーされていない行：
- validator.py の 15-20 行目（エラーハンドリング）
- user.py の 45 行目（エッジケース）
```

---

## 9. テスト戦略チェックリスト

実際のプロジェクトでテストを導入する際のチェックリストです。

### 基本事項

- [ ] **テストフレームワークを選択した**
  - Python: pytest
  - JavaScript: Jest / Vitest
  - その他の言語に対応したフレームワーク

- [ ] **プロジェクト構成を整理した**
  ```
  project/
  ├── src/
  │   └── (実装コード)
  └── tests/
      └── (テストコード)
  ```

- [ ] **依存関係を requirements.txt / package.json に記載した**

### テストコードの品質

- [ ] **テスト名が明確で分かりやすい**
  - 良い例：`test_user_cannot_login_with_wrong_password`
  - 悪い例：`test1`, `test_login`

- [ ] **Arrange-Act-Assert (AAA) パターンを使っている**
  ```python
  def test_example():
      # Arrange（準備）
      user = User("alice")

      # Act（実行）
      result = user.get_name()

      # Assert（検証）
      assert result == "alice"
  ```

- [ ] **1つのテストで1つのことだけを検証している**

- [ ] **テストは独立している（実行順序に依存しない）**

### カバレッジ

- [ ] **カバレッジツールを導入した**
  - Python: pytest-cov
  - JavaScript: Jest の組み込み機能

- [ ] **目標カバレッジを設定した（推奨: 80%以上）**

- [ ] **重要な部分は必ずテストしている**
  - ビジネスロジック
  - エラーハンドリング
  - バリデーション

### CI/CD 連携

- [ ] **GitHub Actions などで CI を設定した**

- [ ] **PR ごとに自動テストが実行される**

- [ ] **テスト失敗時に main へのマージがブロックされる**

- [ ] **カバレッジレポートが自動生成される**

### テスト種類のバランス

- [ ] **ユニットテストが充実している（全体の 70%）**

- [ ] **重要な統合部分はテストしている（全体の 20%）**

- [ ] **主要なユーザーフローは E2E テストでカバーしている（全体の 10%）**

### チーム運用

- [ ] **テストコードのレビューも行っている**

- [ ] **新機能追加時は必ずテストも書くルールにしている**

- [ ] **テストが壊れたら即座に修正する文化がある**

---

## まとめ

### このガイドで学んだこと

1. **テストの重要性**：バグの早期発見、安心なリファクタリング、開発速度の向上
2. **テストの種類**：ユニット、統合、E2E テストの違いと使い分け
3. **pytest の使い方**：基本的なテストの書き方、フィクスチャ、パラメータ化
4. **TDD の実践**：Red-Green-Refactor サイクルでの開発
5. **カバレッジ測定**：テストの網羅性を数値化して改善
6. **CI 連携**：GitHub Actions でテストを自動化
7. **Claude Code 活用**：AI を使った効率的なテスト作成

### 次のステップ

1. **小さく始める**：既存のプロジェクトの1つの関数からテストを書いてみる
2. **TDD を試す**：新しい機能を追加するときにテストファーストで開発する
3. **CI を導入する**：GitHub Actions で自動テストを設定する
4. **カバレッジを改善する**：目標 80% を目指してテストを追加する

### さらに学ぶためのリソース

- **公式ドキュメント**
  - [pytest 公式ドキュメント](https://docs.pytest.org/)
  - [Jest 公式ドキュメント](https://jestjs.io/)
  - [Vitest 公式ドキュメント](https://vitest.dev/)

- **関連ガイド**
  - [Claude Code 実践ガイド](11-claude-code-practical-guide.md) - テスト駆動開発の実践例
  - [Docker 入門ガイド](22-docker-intro-guide.md) - コンテナ環境でのテスト実行
  - [Web 開発基礎ガイド](23-web-basics-guide.md) - フロントエンドのテスト
  - [API 設計・連携ガイド](25-api-guide.md) - API テストの実践

> **最後に：** テストは最初は面倒に感じるかもしれませんが、長期的には確実に開発効率を向上させます。小さく始めて、徐々に習慣化していきましょう。

---

**作成日：** 2026-02-19
**対象レベル：** プログラミング初心者〜中級者
**推奨前提知識：** Python または JavaScript の基本文法
