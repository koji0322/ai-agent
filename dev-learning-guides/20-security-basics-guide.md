# セキュリティ基礎ガイド

---

## 0. はじめに

### 想定読者
- プログラミングを学び始めた方
- セキュリティの基本を理解したい開発者
- Git や GitHub を使い始めた方
- Web アプリケーション開発に興味がある方

### ゴール
このガイドでは、プログラミング初心者が知っておくべきセキュリティの基礎知識を習得します。

**学習後にできるようになること:**
- パスワードと認証情報を安全に管理する
- API キーや秘密情報を適切に扱う
- Git リポジトリでの情報漏洩を防ぐ
- 一般的な脆弱性の種類と対策を理解する
- 依存パッケージのセキュリティリスクに対応する

### 関連ガイド
- [Claude Code 基本操作ガイド](10-claude-code-guide.md) - セキュアなコーディング支援
- [テスト入門ガイド](21-testing-intro-guide.md) - セキュリティテストの基礎
- [Docker 入門ガイド](22-docker-intro-guide.md) - コンテナのセキュリティ
- [Web 開発基礎ガイド](23-web-basics-guide.md) - Web セキュリティの実践
- [API 設計・連携ガイド](25-api-guide.md) - API のセキュリティ設計
- [開発学習ロードマップ](30-learning-roadmap-guide.md) - 体系的な学習計画

---

## 1. セキュリティの重要性

### なぜセキュリティを学ぶべきか

プログラミング初心者でも、最初からセキュリティを意識することが重要です。

**セキュリティインシデントの例:**
- GitHub に API キーを公開 → 数時間で悪用され高額請求
- SQL インジェクション → データベース全体が漏洩
- 弱いパスワード → アカウント乗っ取り
- 脆弱な依存パッケージ → マルウェア感染

> **重要:** セキュリティは「後から追加する」ものではなく、「最初から組み込む」ものです。

### セキュリティの3つの基本原則

| 原則 | 説明 | 具体例 |
|------|------|--------|
| **機密性 (Confidentiality)** | 許可された人だけが情報にアクセスできる | パスワード暗号化、アクセス制御 |
| **完全性 (Integrity)** | データが改ざんされない | チェックサム、デジタル署名 |
| **可用性 (Availability)** | 必要な時にシステムが利用できる | バックアップ、冗長化 |

---

## 2. パスワードとアカウント管理

### 強力なパスワードの作り方

**悪い例:**
```
password123
tanaka2024
qwerty
```

**良い例:**
```
Xk9#mL2$pQ7@vN4!
correct-horse-battery-staple (パスフレーズ)
```

**パスワード要件チェックリスト:**
- [ ] 12文字以上
- [ ] 大文字・小文字・数字・記号を含む
- [ ] 辞書に載っている単語を避ける
- [ ] サービスごとに異なるパスワードを使用
- [ ] 個人情報(誕生日、名前)を含めない

### パスワードマネージャーの活用

**推奨ツール:**
- **1Password** - 個人・チーム向け
- **Bitwarden** - オープンソース
- **LastPass** - 無料プラン有り

```bash
# macOS Keychain を使った管理例
# パスワードを保存
security add-generic-password -a "myuser" -s "myapp" -w "mypassword"

# パスワードを取得
security find-generic-password -a "myuser" -s "myapp" -w
```

### 二要素認証 (2FA/MFA)

**2FA の種類:**

| 種類 | 例 | セキュリティレベル |
|------|----|--------------------|
| SMS | 電話番号に送信されるコード | ★★☆☆☆ |
| 認証アプリ | Google Authenticator, Authy | ★★★★☆ |
| ハードウェアキー | YubiKey, Titan Security Key | ★★★★★ |

**GitHub で 2FA を有効化:**
```bash
# 1. GitHub Settings → Security → Two-factor authentication
# 2. 認証アプリで QR コードをスキャン
# 3. リカバリーコードを安全に保存
```

> **Tip:** リカバリーコードは紙に印刷して、パスワードマネージャーにも保存しましょう。

### SSH キーの管理

**SSH キーの生成:**
```bash
# ED25519 アルゴリズムで生成(推奨)
ssh-keygen -t ed25519 -C "your_email@example.com"

# パスフレーズを必ず設定する
Enter passphrase (empty for no passphrase): ********
```

**SSH 設定ファイル例:**
```bash
# ~/.ssh/config
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

**公開鍵を GitHub に登録:**
```bash
# 公開鍵をクリップボードにコピー
pbcopy < ~/.ssh/id_ed25519.pub

# GitHub Settings → SSH and GPG keys → New SSH key
# タイトルを入力してペースト
```

---

## 3. API キー管理

### 環境変数と .env ファイル

**絶対にやってはいけないこと:**
```python
# ❌ 悪い例: コードに直接書く
api_key = "sk-1234567890abcdefghijklmnop"
database_url = "postgresql://user:password@localhost/db"
```

**正しい方法:**
```python
# ✅ 良い例: 環境変数から読み込む
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
```

**.env ファイル例:**
```bash
# .env
API_KEY=sk-1234567890abcdefghijklmnop
DATABASE_URL=postgresql://user:password@localhost/db
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### .gitignore の設定

```gitignore
# .gitignore

# 環境変数ファイル
.env
.env.local
.env.*.local

# API キー・認証情報
secrets.yaml
credentials.json
*.key
*.pem

# OS 固有ファイル
.DS_Store
Thumbs.db

# IDE 設定
.vscode/
.idea/

# 依存関係
node_modules/
venv/
```

> **重要:** .gitignore は最初のコミット前に設定しましょう。

### 環境変数の設定方法

**ローカル開発環境:**
```bash
# .zshrc または .bashrc に追加
export API_KEY="sk-1234567890abcdefghijklmnop"
export DATABASE_URL="postgresql://user:password@localhost/db"

# 反映
source ~/.zshrc
```

**Node.js での読み込み:**
```javascript
// dotenv を使用
require('dotenv').config();

const apiKey = process.env.API_KEY;
const dbUrl = process.env.DATABASE_URL;

console.log('API Key:', apiKey.substring(0, 5) + '...'); // 一部のみ表示
```

**Python での読み込み:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY が設定されていません")
```

### シークレット管理ツール

| ツール | 用途 | 特徴 |
|--------|------|------|
| **AWS Secrets Manager** | クラウド環境 | AWS サービスとの統合 |
| **HashiCorp Vault** | エンタープライズ | 高度な暗号化機能 |
| **GitHub Secrets** | CI/CD | GitHub Actions との連携 |
| **Azure Key Vault** | クラウド環境 | Azure サービスとの統合 |

---

## 4. Git とセキュリティ

### 誤ってコミットした秘密情報の削除

**問題のコミット例:**
```bash
# 誤って .env をコミットしてしまった
git add .
git commit -m "Add configuration"
git push
```

**対処方法 1: 最新コミットから削除**
```bash
# まだプッシュしていない場合
git reset HEAD~1
git add .gitignore
git add .env.example  # サンプルファイルのみ追加
git commit -m "Add configuration (without secrets)"
```

**対処方法 2: 履歴から完全削除**
```bash
# BFG Repo-Cleaner を使用(推奨)
brew install bfg

# .env を履歴から削除
bfg --delete-files .env

# 変更を反映
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 強制プッシュ(注意!)
git push --force
```

> **警告:** 履歴から削除しても、既に公開された秘密情報は漏洩したものとして扱い、必ず再発行してください。

### git-secrets の導入

**インストール:**
```bash
# macOS
brew install git-secrets

# git-secrets を有効化
git secrets --install
git secrets --register-aws  # AWS キーを検出
```

**カスタムパターンの追加:**
```bash
# API キーパターンを追加
git secrets --add 'sk-[a-zA-Z0-9]{32,}'
git secrets --add 'password\s*=\s*["\'][^"\']+["\']'

# スキャン実行
git secrets --scan
```

### GitHub Secret Scanning

GitHub では、プッシュされたコードから自動的に秘密情報を検出します。

**検出される情報:**
- AWS アクセスキー
- Azure トークン
- Google API キー
- Stripe API キー
- その他 200+ のパターン

**アラートを受け取ったら:**
1. 該当の秘密情報を直ちに無効化
2. 新しい秘密情報を発行
3. コミット履歴から削除
4. 環境変数の設定を確認

---

## 5. OWASP Top 10 概要

### OWASP Top 10 とは

OWASP (Open Web Application Security Project) が定期的に発表する、最も重要な Web アプリケーションセキュリティリスクのリストです。

### 主な脆弱性と対策

#### 1. インジェクション攻撃

**SQL インジェクションの例:**
```python
# ❌ 悪い例: SQL インジェクションの危険性
user_input = "admin' OR '1'='1"
query = f"SELECT * FROM users WHERE username = '{user_input}'"
# 結果: SELECT * FROM users WHERE username = 'admin' OR '1'='1'
# → 全ユーザーが取得されてしまう
```

**対策:**
```python
# ✅ 良い例: プリペアドステートメント使用
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

user_input = "admin' OR '1'='1"
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
# → user_input はエスケープされ、リテラル文字列として扱われる
```

#### 2. クロスサイトスクリプティング (XSS)

**XSS 攻撃の例:**
```javascript
// ❌ 悪い例: ユーザー入力を直接 HTML に挿入
const username = "<script>alert('XSS!')</script>";
document.getElementById('output').innerHTML = username;
// → スクリプトが実行されてしまう
```

**対策:**
```javascript
// ✅ 良い例: エスケープして表示
const username = "<script>alert('XSS!')</script>";
document.getElementById('output').textContent = username;
// → &lt;script&gt;... として表示される

// または DOMPurify などのライブラリを使用
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(username);
```

#### 3. クロスサイトリクエストフォージェリ (CSRF)

**CSRF トークンの実装:**
```python
# Flask での CSRF 対策
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)

# フォームに CSRF トークンを含める
@app.route('/transfer', methods=['POST'])
def transfer():
    # CSRF トークンが自動的に検証される
    amount = request.form.get('amount')
    # 処理...
```

```html
<!-- HTML フォーム -->
<form method="POST" action="/transfer">
  {{ csrf_token() }}
  <input type="text" name="amount">
  <button type="submit">送金</button>
</form>
```

#### 4. 認証の不備

**安全なパスワードハッシュ化:**
```python
# ✅ bcrypt を使用した安全な実装
import bcrypt

# パスワードのハッシュ化
password = "user_password"
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# パスワードの検証
if bcrypt.checkpw(password.encode('utf-8'), hashed):
    print("認証成功")
```

```javascript
// Node.js での実装
const bcrypt = require('bcrypt');
const saltRounds = 10;

// ハッシュ化
const hash = await bcrypt.hash('user_password', saltRounds);

// 検証
const match = await bcrypt.compare('user_password', hash);
```

### OWASP Top 10 一覧表

| 順位 | 脆弱性 | 対策 |
|------|--------|------|
| 1 | Broken Access Control | 権限チェック、最小権限の原則 |
| 2 | Cryptographic Failures | 適切な暗号化、HTTPS 使用 |
| 3 | Injection | プリペアドステートメント、入力検証 |
| 4 | Insecure Design | セキュアな設計パターン |
| 5 | Security Misconfiguration | デフォルト設定の変更、最小構成 |
| 6 | Vulnerable Components | 依存関係の定期更新 |
| 7 | Authentication Failures | MFA、強力なパスワードポリシー |
| 8 | Software and Data Integrity | コード署名、サプライチェーン検証 |
| 9 | Logging Failures | 適切なログ記録とモニタリング |
| 10 | Server-Side Request Forgery | URL 検証、ホワイトリスト |

---

## 6. HTTPS と通信の基礎

### なぜ HTTPS が重要か

**HTTP vs HTTPS:**

| プロトコル | 暗号化 | リスク | 用途 |
|------------|--------|--------|------|
| HTTP | なし | 盗聴、改ざん可能 | ローカル開発のみ |
| HTTPS | あり | 安全な通信 | 本番環境必須 |

### SSL/TLS の仕組み

```
クライアント                         サーバー
    |                                   |
    |------ 1. ClientHello ----------->|
    |                                   |
    |<----- 2. ServerHello ------------|
    |<----- 3. 証明書 ----------------|
    |                                   |
    |------ 4. 鍵交換 --------------->|
    |                                   |
    |====== 5. 暗号化通信開始 =========|
```

### Let's Encrypt で無料 SSL 証明書取得

```bash
# Certbot のインストール(Ubuntu)
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# Nginx 用の証明書取得
sudo certbot --nginx -d example.com -d www.example.com

# 自動更新の設定
sudo certbot renew --dry-run
```

### 開発環境での HTTPS

**mkcert を使用:**
```bash
# インストール
brew install mkcert
mkcert -install

# ローカル証明書の作成
mkcert localhost 127.0.0.1 ::1

# Node.js で使用
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('localhost-key.pem'),
  cert: fs.readFileSync('localhost.pem')
};

https.createServer(options, app).listen(3000);
```

---

## 7. 依存パッケージのセキュリティ

### 脆弱性のスキャン

**Node.js (npm):**
```bash
# 脆弱性をチェック
npm audit

# 自動修正(破壊的変更なし)
npm audit fix

# 強制的に修正(メジャーバージョンアップ含む)
npm audit fix --force

# 詳細レポート
npm audit --json
```

**Python (pip):**
```bash
# safety のインストール
pip install safety

# 脆弱性チェック
safety check

# requirements.txt をチェック
safety check -r requirements.txt

# pip-audit を使用(推奨)
pip install pip-audit
pip-audit
```

### Dependabot の活用

**GitHub で Dependabot を有効化:**
```yaml
# .github/dependabot.yml
version: 2
updates:
  # npm パッケージの監視
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10

  # Python パッケージの監視
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"

  # GitHub Actions の監視
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### バージョン固定の重要性

**package.json での設定:**
```json
{
  "dependencies": {
    "express": "4.18.2",        // ✅ 固定バージョン
    "lodash": "^4.17.21",       // ⚠️ マイナーバージョンまで許可
    "react": "~18.2.0"          // ⚠️ パッチバージョンのみ許可
  }
}
```

**package-lock.json の役割:**
- 完全なバージョン固定
- 再現可能なビルド
- セキュリティ監査

> **Tip:** package-lock.json や poetry.lock は必ず Git にコミットしましょう。

---

## 8. Claude Code でのセキュリティ

### セキュリティ問題の検出

Claude Code は以下のようなセキュリティ問題を検出できます:

**例 1: ハードコードされた秘密情報**
```python
# Claude Code が警告するコード
api_key = "sk-1234567890abcdefghijklmnop"  # ⚠️ Warning
```

Claude Code の提案:
```python
# 環境変数を使用するように修正
import os
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY が設定されていません")
```

**例 2: SQL インジェクションのリスク**
```python
# Claude Code が警告するコード
query = f"SELECT * FROM users WHERE id = {user_id}"  # ⚠️ Warning
```

Claude Code の提案:
```python
# プリペアドステートメントを使用
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### セキュアなコード生成

**プロンプト例:**
```
「ユーザー認証機能を実装してください。
- bcrypt でパスワードをハッシュ化
- JWT トークンで認証
- CSRF 対策を含める
- 入力バリデーションを実装」
```

Claude Code は自動的にセキュリティベストプラクティスに従ったコードを生成します。

### コードレビュー機能の活用

```bash
# Claude Code にセキュリティレビューを依頼
"このコードのセキュリティ上の問題点をチェックしてください"
```

Claude Code が確認する項目:
- 入力検証の有無
- 認証・認可の実装
- エラーハンドリング
- ログ出力における機密情報の漏洩
- 依存パッケージの脆弱性

詳細は [Claude Code 基本操作ガイド](10-claude-code-guide.md) を参照してください。

---

## 9. セキュリティチェックリスト

### 日常的なチェック項目

#### コーディング時

- [ ] パスワードや API キーをコードに直接書かない
- [ ] 環境変数ファイル(.env)を .gitignore に追加済み
- [ ] ユーザー入力を必ずバリデーション・サニタイズする
- [ ] SQL クエリにプリペアドステートメントを使用
- [ ] エラーメッセージに機密情報を含めない
- [ ] ログに個人情報やパスワードを出力しない

#### Git 操作時

- [ ] コミット前に `git status` で確認
- [ ] .env や秘密鍵ファイルが含まれていないか確認
- [ ] git-secrets でスキャン済み
- [ ] コミットメッセージに機密情報を書かない
- [ ] 公開リポジトリに Push する前に再確認

#### デプロイ時

- [ ] 本番環境の環境変数を正しく設定
- [ ] HTTPS を有効化
- [ ] セキュリティヘッダーを設定
- [ ] 不要なエンドポイントを無効化
- [ ] デバッグモードを無効化
- [ ] ファイアウォール・セキュリティグループを設定

### プロジェクト開始時のセキュリティ設定

```bash
# 1. .gitignore の作成
cat > .gitignore << EOF
.env
.env.local
*.key
*.pem
secrets.yaml
credentials.json
node_modules/
venv/
EOF

# 2. .env.example の作成
cat > .env.example << EOF
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost/db
DEBUG=False
EOF

# 3. git-secrets のセットアップ
git secrets --install
git secrets --register-aws

# 4. pre-commit フックの設定(オプション)
pip install pre-commit
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-added-large-files
      - id: check-yaml
      - id: detect-private-key
EOF
pre-commit install
```

### 定期的なメンテナンス

**週次タスク:**
```bash
# 依存パッケージの更新確認
npm audit
pip-audit

# Dependabot の PR を確認
gh pr list --label dependencies
```

**月次タスク:**
```bash
# パスワードローテーション(必要に応じて)
# API キーの棚卸し
# アクセスログの確認
# セキュリティパッチの適用
```

### インシデント対応フロー

```
1. 検出
   ↓
2. 影響範囲の特定
   ↓
3. 秘密情報の無効化・再発行
   ↓
4. コード・履歴からの削除
   ↓
5. 原因分析と再発防止策
   ↓
6. ドキュメント化
```

**インシデント対応テンプレート:**
```markdown
## セキュリティインシデント報告

- **発生日時:** 2026-02-19 14:30
- **発見者:** 田中太郎
- **種類:** API キーの誤コミット
- **影響範囲:** GitHub 公開リポジトリ
- **対応状況:**
  - [x] API キーを無効化
  - [x] 新しい API キーを発行
  - [x] 履歴から削除
  - [ ] 不正利用の確認
- **再発防止策:**
  - git-secrets の導入
  - pre-commit フックの設定
```

---

## まとめ

### セキュリティの基本原則

1. **最小権限の原則** - 必要最小限のアクセス権のみ付与
2. **多層防御** - 複数のセキュリティ対策を組み合わせる
3. **フェイルセーフ** - 障害時は安全な状態になるように設計
4. **セキュリティバイデザイン** - 設計段階からセキュリティを考慮

### 初心者が今すぐできること

- [ ] パスワードマネージャーを導入する
- [ ] GitHub で 2FA を有効化する
- [ ] .gitignore を正しく設定する
- [ ] 環境変数で秘密情報を管理する
- [ ] 依存パッケージの脆弱性をチェックする
- [ ] HTTPS を使用する
- [ ] Claude Code でセキュリティレビューを受ける

### 次のステップ

- [テスト入門ガイド](21-testing-intro-guide.md) でセキュリティテストを学ぶ
- [Web 開発基礎ガイド](23-web-basics-guide.md) で Web セキュリティを深める
- [API 設計・連携ガイド](25-api-guide.md) で API セキュリティを実践
- [開発学習ロードマップ](30-learning-roadmap-guide.md) で体系的に学習

### 参考リソース

**公式ドキュメント:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE (Common Weakness Enumeration)](https://cwe.mitre.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

**学習リソース:**
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) - 無料のハンズオン教材
- [HackTheBox](https://www.hackthebox.eu/) - セキュリティ実践環境
- [PicoCTF](https://picoctf.org/) - 初心者向け CTF

> **最後に:** セキュリティは「完璧」を目指すのではなく、「継続的に改善」することが重要です。小さなことから始めて、徐々にセキュリティ意識を高めていきましょう。

---

**作成日:** 2026-02-19
**対象バージョン:** 汎用(プログラミング初心者向け)
**ライセンス:** MIT
