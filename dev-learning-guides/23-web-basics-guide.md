# Web 開発基礎ガイド

---

## 0. はじめに

### 想定読者
- プログラミング初心者
- Web 開発に興味がある方
- HTML/CSS/JavaScript の基礎を学びたい方
- React や Next.js などのモダンな技術に触れたい方

### ゴール
このガイドでは、Web 開発の基礎から最新のフレームワークまでを体系的に学びます。

- HTML/CSS/JavaScript の基本を理解する
- ブラウザの開発者ツールを使いこなす
- React と Next.js の概要を把握する
- フロントエンド開発のツールチェーンを理解する
- Claude Code を活用した Web 開発の方法を学ぶ

### 関連ガイド
- [VS Code 基本操作ガイド](00-vscode-guide.md) - エディタの使い方
- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) - アプリ開発の実践
- [セキュリティ基礎ガイド](20-security-basics-guide.md) - Web セキュリティ
- [テスト入門ガイド](21-testing-intro-guide.md) - フロントエンドテスト
- [API 設計・連携ガイド](25-api-guide.md) - バックエンド連携

---

## 1. Web 開発の概要

### Web 開発とは

Web 開発は、インターネット上で動作するアプリケーションを作成する技術です。

**主な分野**

| 分野 | 説明 | 主な技術 |
|------|------|----------|
| フロントエンド | ユーザーが見る・操作する部分 | HTML, CSS, JavaScript, React |
| バックエンド | サーバー側の処理・データ管理 | Node.js, Python, Go, データベース |
| フルスタック | フロントエンドとバックエンド両方 | Next.js, MERN スタック |

### Web の仕組み

```
ユーザー (ブラウザ)
    ↓ HTTP リクエスト
サーバー
    ↓ HTML/CSS/JS を返す
ブラウザが表示・実行
    ↓ ユーザーが操作
JavaScript が動作
    ↓ API リクエスト
サーバーがデータを返す
    ↓ 画面を更新
```

> **ヒント**: Web 開発では、まず「何をユーザーに見せるか」(フロントエンド) から始めると理解しやすいです。

---

## 2. HTML の基礎

### HTML とは

HTML (HyperText Markup Language) は、Web ページの構造を定義するマークアップ言語です。

### 基本構造

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>私の Web ページ</title>
</head>
<body>
    <h1>ようこそ</h1>
    <p>これは段落です。</p>
</body>
</html>
```

### よく使うタグ

| タグ | 用途 | 例 |
|------|------|-----|
| `<h1>` ~ `<h6>` | 見出し | `<h1>大見出し</h1>` |
| `<p>` | 段落 | `<p>テキスト</p>` |
| `<a>` | リンク | `<a href="/">ホーム</a>` |
| `<img>` | 画像 | `<img src="logo.png" alt="ロゴ">` |
| `<div>` | 汎用コンテナ | `<div class="container">...</div>` |
| `<span>` | インライン要素 | `<span class="highlight">強調</span>` |
| `<ul>`, `<li>` | リスト | `<ul><li>項目1</li></ul>` |
| `<button>` | ボタン | `<button>クリック</button>` |
| `<input>` | 入力欄 | `<input type="text" placeholder="名前">` |
| `<form>` | フォーム | `<form action="/submit">...</form>` |

### セマンティック HTML

意味のある HTML タグを使うことで、SEO やアクセシビリティが向上します。

```html
<header>
    <nav>
        <ul>
            <li><a href="/">ホーム</a></li>
            <li><a href="/about">会社概要</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h1>記事タイトル</h1>
        <section>
            <h2>セクション1</h2>
            <p>内容...</p>
        </section>
    </article>

    <aside>
        <h3>関連情報</h3>
        <p>サイドバー</p>
    </aside>
</main>

<footer>
    <p>&copy; 2026 My Company</p>
</footer>
```

**セマンティックタグの例**

| タグ | 意味 |
|------|------|
| `<header>` | ヘッダー領域 |
| `<nav>` | ナビゲーション |
| `<main>` | メインコンテンツ |
| `<article>` | 独立したコンテンツ |
| `<section>` | セクション |
| `<aside>` | サイドバー・補足情報 |
| `<footer>` | フッター領域 |

> **ヒント**: `<div>` だけでなく、意味のあるタグを使うことで、コードの可読性と保守性が向上します。

---

## 3. CSS の基礎

### CSS とは

CSS (Cascading Style Sheets) は、HTML 要素のスタイル (色、サイズ、配置など) を定義する言語です。

### CSS の適用方法

```html
<!-- 1. インラインスタイル (非推奨) -->
<p style="color: red;">赤い文字</p>

<!-- 2. 内部スタイルシート -->
<head>
    <style>
        p { color: blue; }
    </style>
</head>

<!-- 3. 外部スタイルシート (推奨) -->
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

### セレクタの種類

```css
/* 要素セレクタ */
p {
    color: black;
}

/* クラスセレクタ */
.highlight {
    background-color: yellow;
}

/* ID セレクタ */
#header {
    font-size: 24px;
}

/* 子孫セレクタ */
div p {
    margin: 10px;
}

/* 直接の子セレクタ */
div > p {
    padding: 5px;
}

/* 擬似クラス */
a:hover {
    color: red;
}

button:disabled {
    opacity: 0.5;
}
```

### ボックスモデル

CSS では、すべての要素が「ボックス」として扱われます。

```
┌─────────────── margin ───────────────┐
│ ┌──────────── border ─────────────┐ │
│ │ ┌────────── padding ──────────┐ │ │
│ │ │                              │ │ │
│ │ │         content              │ │ │
│ │ │      (width × height)        │ │ │
│ │ │                              │ │ │
│ │ └──────────────────────────────┘ │ │
│ └──────────────────────────────────┘ │
└──────────────────────────────────────┘
```

```css
.box {
    width: 200px;
    height: 100px;
    padding: 20px;      /* 内側の余白 */
    border: 2px solid black;  /* 枠線 */
    margin: 10px;       /* 外側の余白 */
}
```

### Flexbox

要素を柔軟に配置するためのレイアウトシステムです。

```css
.container {
    display: flex;
    justify-content: space-between;  /* 横方向の配置 */
    align-items: center;             /* 縦方向の配置 */
    gap: 10px;                       /* 要素間の間隔 */
}

.item {
    flex: 1;  /* 均等に伸縮 */
}
```

```html
<div class="container">
    <div class="item">アイテム1</div>
    <div class="item">アイテム2</div>
    <div class="item">アイテム3</div>
</div>
```

**Flexbox の主なプロパティ**

| プロパティ | 説明 | 値の例 |
|-----------|------|--------|
| `justify-content` | 主軸方向の配置 | `flex-start`, `center`, `space-between` |
| `align-items` | 交差軸方向の配置 | `flex-start`, `center`, `stretch` |
| `flex-direction` | 配置の方向 | `row`, `column` |
| `gap` | 要素間の間隔 | `10px`, `1rem` |

### レスポンシブデザイン

画面サイズに応じてレイアウトを変更します。

```css
/* モバイルファースト */
.container {
    padding: 10px;
}

/* タブレット以上 */
@media (min-width: 768px) {
    .container {
        padding: 20px;
        max-width: 960px;
        margin: 0 auto;
    }
}

/* デスクトップ */
@media (min-width: 1024px) {
    .container {
        max-width: 1200px;
    }
}
```

> **ヒント**: Chrome DevTools でデバイスモードを使うと、様々な画面サイズでの表示を確認できます。

---

## 4. JavaScript の基礎

### JavaScript とは

JavaScript は、Web ページに動的な機能を追加するプログラミング言語です。

### 変数と定数

```javascript
// const: 再代入できない (推奨)
const userName = "田中太郎";

// let: 再代入できる
let count = 0;
count = 1;  // OK

// var: 古い書き方 (使用非推奨)
var oldStyle = "avoid";
```

### データ型

```javascript
// 文字列
const message = "こんにちは";

// 数値
const age = 25;
const price = 1980.5;

// 真偽値
const isActive = true;

// 配列
const fruits = ["りんご", "バナナ", "オレンジ"];

// オブジェクト
const user = {
    name: "田中",
    age: 30,
    email: "tanaka@example.com"
};

// null と undefined
const emptyValue = null;
let notDefined;  // undefined
```

### 関数

```javascript
// 関数宣言
function greet(name) {
    return `こんにちは、${name}さん`;
}

// アロー関数 (モダンな書き方)
const add = (a, b) => {
    return a + b;
};

// 短縮形 (1行の場合)
const multiply = (a, b) => a * b;

// 使用例
console.log(greet("佐藤"));  // "こんにちは、佐藤さん"
console.log(add(5, 3));      // 8
console.log(multiply(4, 2)); // 8
```

### DOM 操作

DOM (Document Object Model) を使って、HTML を動的に変更できます。

```html
<!DOCTYPE html>
<html>
<body>
    <h1 id="title">タイトル</h1>
    <button id="changeButton">変更</button>
    <ul id="list"></ul>

    <script>
        // 要素の取得
        const title = document.getElementById("title");
        const button = document.getElementById("changeButton");
        const list = document.getElementById("list");

        // テキストの変更
        title.textContent = "新しいタイトル";

        // スタイルの変更
        title.style.color = "blue";

        // 要素の追加
        const newItem = document.createElement("li");
        newItem.textContent = "新しい項目";
        list.appendChild(newItem);

        // クラスの追加・削除
        title.classList.add("highlight");
        title.classList.remove("old-class");
    </script>
</body>
</html>
```

### イベント処理

ユーザーの操作に反応する処理を実装します。

```javascript
// クリックイベント
button.addEventListener("click", () => {
    alert("ボタンがクリックされました");
});

// フォーム送信
const form = document.getElementById("myForm");
form.addEventListener("submit", (event) => {
    event.preventDefault();  // デフォルトの送信を防ぐ

    const input = document.getElementById("nameInput");
    console.log("入力値:", input.value);
});

// キーボード入力
input.addEventListener("keyup", (event) => {
    console.log("入力中:", event.target.value);
});
```

### 配列操作

```javascript
const numbers = [1, 2, 3, 4, 5];

// map: 各要素を変換
const doubled = numbers.map(n => n * 2);
// [2, 4, 6, 8, 10]

// filter: 条件に合う要素を抽出
const evens = numbers.filter(n => n % 2 === 0);
// [2, 4]

// reduce: 集計
const sum = numbers.reduce((total, n) => total + n, 0);
// 15

// forEach: ループ処理
numbers.forEach(n => {
    console.log(n);
});
```

> **ヒント**: モダンな JavaScript では、`map`, `filter`, `reduce` などの配列メソッドを使うと、コードが簡潔で読みやすくなります。

---

## 5. ブラウザ DevTools

### DevTools とは

ブラウザに内蔵された開発者向けツールです。Chrome DevTools が最も一般的です。

**起動方法**
- Windows/Linux: `F12` または `Ctrl + Shift + I`
- Mac: `Cmd + Option + I`

### Elements タブ

HTML と CSS をリアルタイムで確認・編集できます。

**主な機能**
1. **要素の検査**: 要素をクリックして HTML 構造を確認
2. **スタイルの確認**: 適用されている CSS を確認
3. **スタイルの編集**: リアルタイムで CSS を変更してテスト
4. **ボックスモデルの確認**: margin, padding, border のサイズを視覚的に確認

```
使い方:
1. 左上の矢印アイコンをクリック
2. ページ上の要素をクリック
3. 右側の Styles パネルで CSS を確認・編集
```

### Console タブ

JavaScript の実行とデバッグができます。

```javascript
// ログ出力
console.log("通常のログ");
console.warn("警告メッセージ");
console.error("エラーメッセージ");

// オブジェクトの確認
const user = { name: "田中", age: 30 };
console.log(user);
console.table(user);  // テーブル形式で表示

// 計測
console.time("処理時間");
// 何か重い処理
console.timeEnd("処理時間");
```

### Network タブ

HTTP リクエストとレスポンスを確認できます。

**確認できる情報**
- リクエストした URL
- HTTP メソッド (GET, POST など)
- ステータスコード (200, 404, 500 など)
- レスポンスのサイズ
- 読み込み時間

```
使い方:
1. Network タブを開く
2. ページをリロード
3. リクエスト一覧が表示される
4. クリックして詳細を確認
```

### デバッグ方法

```javascript
// debugger: ブレークポイントを設定
function calculate(a, b) {
    debugger;  // ここで実行が一時停止
    const result = a + b;
    return result;
}

// Sources タブでブレークポイントを設定
// 1. Sources タブを開く
// 2. ファイルを選択
// 3. 行番号をクリックしてブレークポイントを設定
// 4. ページを操作すると、ブレークポイントで停止
```

> **ヒント**: `console.log` よりも DevTools のブレークポイントを使うと、変数の状態を詳しく確認できます。

---

## 6. React 概要

### React とは

React は、UI を構築するための JavaScript ライブラリです。Facebook (Meta) が開発しています。

**特徴**
- コンポーネントベース
- 宣言的な UI
- 仮想 DOM による高速なレンダリング

### コンポーネント

React では、UI を再利用可能なコンポーネントに分割します。

```jsx
// 関数コンポーネント (モダンな書き方)
function Greeting({ name }) {
    return <h1>こんにちは、{name}さん</h1>;
}

// 使用例
function App() {
    return (
        <div>
            <Greeting name="田中" />
            <Greeting name="佐藤" />
        </div>
    );
}
```

### JSX

JavaScript の中に HTML ライクな構文を書けます。

```jsx
function UserCard({ user }) {
    return (
        <div className="card">
            <h2>{user.name}</h2>
            <p>年齢: {user.age}</p>
            <p>メール: {user.email}</p>
        </div>
    );
}

// 使用例
const user = {
    name: "田中太郎",
    age: 30,
    email: "tanaka@example.com"
};

<UserCard user={user} />
```

> **注意**: JSX では `class` の代わりに `className` を使います。

### Props

親コンポーネントから子コンポーネントにデータを渡します。

```jsx
function Button({ text, onClick, disabled }) {
    return (
        <button onClick={onClick} disabled={disabled}>
            {text}
        </button>
    );
}

function App() {
    const handleClick = () => {
        alert("クリックされました");
    };

    return (
        <Button
            text="送信"
            onClick={handleClick}
            disabled={false}
        />
    );
}
```

### State

コンポーネント内で変化する値を管理します。

```jsx
import { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>カウント: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                増やす
            </button>
            <button onClick={() => setCount(count - 1)}>
                減らす
            </button>
            <button onClick={() => setCount(0)}>
                リセット
            </button>
        </div>
    );
}
```

### Hooks の基礎

Hooks は、関数コンポーネントで状態管理などを行うための機能です。

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    // データの取得
    useEffect(() => {
        fetch(`/api/users/${userId}`)
            .then(res => res.json())
            .then(data => {
                setUser(data);
                setLoading(false);
            });
    }, [userId]);  // userId が変わったら再実行

    if (loading) return <p>読み込み中...</p>;

    return (
        <div>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
        </div>
    );
}
```

**主な Hooks**

| Hook | 用途 |
|------|------|
| `useState` | 状態管理 |
| `useEffect` | 副作用の処理 (データ取得など) |
| `useContext` | コンテキストの使用 |
| `useRef` | DOM 要素への参照 |
| `useMemo` | 計算結果のメモ化 |
| `useCallback` | 関数のメモ化 |

---

## 7. Next.js 概要

### Next.js とは

Next.js は、React ベースのフルスタックフレームワークです。Vercel が開発しています。

> **Next.js 15 / React 19 の主な変更点（2026 年 2 月時点の最新安定版）**
> - Dynamic Route の `params` が非同期（Promise 型）になった。`await params` で取得する
> - React 19 で Server Actions が安定版に、`use()` フック追加など

**主な特徴**
- ファイルベースのルーティング
- サーバーサイドレンダリング (SSR)
- 静的サイト生成 (SSG)
- API ルート
- 画像最適化
- TypeScript サポート

### ページとルーティング

```
app/
├── page.tsx           # / (トップページ)
├── about/
│   └── page.tsx       # /about
├── blog/
│   ├── page.tsx       # /blog
│   └── [id]/
│       └── page.tsx   # /blog/123
└── api/
    └── users/
        └── route.ts   # /api/users
```

```tsx
// app/page.tsx
export default function Home() {
    return (
        <main>
            <h1>ホームページ</h1>
        </main>
    );
}

// app/about/page.tsx
export default function About() {
    return <h1>会社概要</h1>;
}

// app/blog/[id]/page.tsx
// Next.js 15 以降: params は Promise 型
export default async function BlogPost({ params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    return <h1>ブログ記事 #{id}</h1>;
}
```

### SSR vs CSR vs SSG

| レンダリング方式 | 説明 | メリット | 使用例 |
|-----------------|------|----------|--------|
| CSR (Client-Side Rendering) | ブラウザで React を実行 | インタラクティブ | ダッシュボード |
| SSR (Server-Side Rendering) | サーバーで HTML を生成 | SEO、初回表示が速い | 商品ページ |
| SSG (Static Site Generation) | ビルド時に HTML を生成 | 超高速、CDN 配信可能 | ブログ、ドキュメント |

```tsx
// SSR: サーバーで毎回データ取得
// Next.js 15 以降: params は Promise 型
export default async function UserPage({ params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    const user = await fetch(`https://api.example.com/users/${id}`, {
        cache: 'no-store'  // キャッシュしない
    }).then(res => res.json());

    return <div>{user.name}</div>;
}

// SSG: ビルド時にデータ取得
// Next.js 15 以降: params は Promise 型
export default async function BlogPost({ params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    const post = await fetch(`https://api.example.com/posts/${id}`).then(res => res.json());

    return <article>{post.content}</article>;
}
```

### API ルート

Next.js で簡単にバックエンド API を作成できます。

```typescript
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
    const users = [
        { id: 1, name: "田中" },
        { id: 2, name: "佐藤" }
    ];

    return NextResponse.json(users);
}

export async function POST(request: Request) {
    const body = await request.json();

    // データベースに保存する処理など
    console.log("受信データ:", body);

    return NextResponse.json({ success: true });
}
```

### レイアウト

共通レイアウトを定義できます。

```tsx
// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="ja">
            <body>
                <header>
                    <nav>
                        <a href="/">ホーム</a>
                        <a href="/about">会社概要</a>
                    </nav>
                </header>
                <main>{children}</main>
                <footer>
                    <p>&copy; 2026 My Company</p>
                </footer>
            </body>
        </html>
    );
}
```

---

## 8. パッケージマネージャ

### npm とは

npm (Node Package Manager) は、JavaScript のパッケージ管理ツールです。

### package.json

プロジェクトの設定ファイルです。

```json
{
  "name": "my-web-app",
  "version": "1.0.0",
  "description": "私の Web アプリ",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint ."
  },
  "dependencies": {
    "react": "^19.0.0",
    "next": "^15.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "eslint": "^8.0.0"
  }
}
```

**主なフィールド**

| フィールド | 説明 |
|-----------|------|
| `name` | パッケージ名 |
| `version` | バージョン |
| `scripts` | npm コマンド |
| `dependencies` | 本番環境で必要なパッケージ |
| `devDependencies` | 開発時のみ必要なパッケージ |

### npm コマンド

```bash
# パッケージのインストール
npm install              # package.json から全パッケージをインストール
npm install react        # react をインストール
npm install -D eslint    # devDependencies としてインストール

# スクリプトの実行
npm run dev              # 開発サーバー起動
npm run build            # ビルド
npm start                # 本番サーバー起動

# パッケージの削除
npm uninstall react

# パッケージの更新
npm update

# キャッシュのクリア
npm cache clean --force
```

### node_modules

インストールしたパッケージが保存されるディレクトリです。

```
プロジェクト/
├── node_modules/     # パッケージが入る (Git には含めない)
├── package.json      # パッケージ一覧
├── package-lock.json # バージョンをロック
└── .gitignore        # node_modules/ を除外
```

**.gitignore の例**

```
node_modules/
.next/
.env.local
```

> **ヒント**: `node_modules/` は Git にコミットせず、`package.json` だけをコミットします。他の人は `npm install` で復元できます。

---

## 9. フロントエンドのビルドツール

### ビルドツールとは

モダンな JavaScript を古いブラウザでも動作するコードに変換したり、複数のファイルを1つにまとめたりするツールです。

### Vite

高速な開発サーバーとビルドツールです。

**特徴**
- 超高速な起動
- HMR (Hot Module Replacement) による即座の反映
- モダンなブラウザ向けに最適化

```bash
# プロジェクトの作成
npm create vite@latest my-app -- --template react

cd my-app
npm install
npm run dev  # 開発サーバー起動
```

### バンドリングの概念

複数の JavaScript ファイルを1つにまとめることです。

```
ビルド前:
src/
├── main.js       (10 KB)
├── utils.js      (5 KB)
└── components/
    ├── Header.js (3 KB)
    └── Footer.js (2 KB)

↓ ビルド

ビルド後:
dist/
└── bundle.js     (20 KB, 圧縮済み: 5 KB)
```

**メリット**
- HTTP リクエスト数の削減
- ファイルサイズの圧縮
- 未使用コードの削除 (Tree Shaking)

### トランスパイル

最新の JavaScript を古いブラウザでも動作するコードに変換します。

```javascript
// 最新の JavaScript (ES6+)
const greet = (name) => `Hello, ${name}`;
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);

// ↓ トランスパイル (ES5)

var greet = function(name) {
    return "Hello, " + name;
};
var numbers = [1, 2, 3];
var doubled = numbers.map(function(n) {
    return n * 2;
});
```

### 主なツール

| ツール | 用途 | 特徴 |
|--------|------|------|
| Vite | 開発サーバー・ビルド | 高速、モダン |
| webpack | バンドラー | 柔軟、豊富なプラグイン |
| Babel | トランスパイラー | 最新 JS → 古い JS |
| ESLint | 静的解析 | コード品質チェック |
| Prettier | フォーマッター | コード整形 |

---

## 10. Claude Code で Web 開発

### Claude Code とは

Claude Code は、AI がコード生成やデバッグを支援するツールです。

### Web プロジェクトの作成

```bash
# Next.js プロジェクトの作成を依頼
claude-code "Next.js で TypeScript を使った新しいプロジェクトを作成してください"

# 具体的な指示
claude-code "ブログアプリを作りたいです。
- Next.js App Router を使用
- TypeScript で型安全に
- トップページに記事一覧を表示
- 各記事の詳細ページを作成"
```

### コンポーネントの生成

```bash
# コンポーネントの作成依頼
"ユーザーカードコンポーネントを作成してください。
- props: name, email, avatarUrl
- Tailwind CSS でスタイリング
- クリックでメールを送れるボタンを追加"
```

生成例:

```tsx
interface UserCardProps {
    name: string;
    email: string;
    avatarUrl: string;
}

export default function UserCard({ name, email, avatarUrl }: UserCardProps) {
    const handleEmailClick = () => {
        window.location.href = `mailto:${email}`;
    };

    return (
        <div className="border rounded-lg p-4 shadow-md">
            <img
                src={avatarUrl}
                alt={name}
                className="w-16 h-16 rounded-full mb-2"
            />
            <h3 className="text-xl font-bold">{name}</h3>
            <p className="text-gray-600">{email}</p>
            <button
                onClick={handleEmailClick}
                className="mt-2 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
                メールを送る
            </button>
        </div>
    );
}
```

### デバッグの支援

```bash
# エラーの解決を依頼
"以下のエラーが出ています。解決方法を教えてください。

Error: Hydration failed because the initial UI does not match what was rendered on the server.
"

# Claude Code が原因と解決策を提示
# - サーバーとクライアントで異なる出力をしている
# - useEffect を使ってクライアント専用の処理を分離する
```

### レスポンシブ対応

```bash
"このコンポーネントをレスポンシブ対応にしてください。
- モバイル: 1カラム
- タブレット: 2カラム
- デスクトップ: 3カラム"
```

### API 連携

```bash
"/api/posts エンドポイントから記事一覧を取得して表示するコンポーネントを作成してください。
- ローディング状態を表示
- エラーハンドリング
- TypeScript で型定義"
```

### テストコードの生成

```bash
"このコンポーネントのテストコードを Jest と React Testing Library で書いてください"
```

### ベストプラクティス

**効果的な指示の出し方**

| 良い例 | 悪い例 |
|--------|--------|
| "Next.js の App Router で `/blog/[id]` の動的ルートを作成" | "ブログページを作って" |
| "Tailwind CSS で青いボタンを作成。hover 時に濃くなる" | "ボタンを作って" |
| "TypeScript で User 型を定義。name, email, age を含む" | "型を作って" |

**具体的に指示すること**
- 使用する技術スタック
- 期待する動作
- スタイルの詳細
- 型定義

> **ヒント**: Claude Code に「なぜこのコードを書いたのか」を質問すると、学習効果が高まります。

### 学習の進め方

1. **小さく始める**: まず静的な HTML/CSS から
2. **JavaScript を追加**: ボタンのクリックイベントなど
3. **React で書き直す**: コンポーネント化
4. **Next.js でプロジェクト化**: ルーティングや API
5. **Claude Code で拡張**: 新機能の追加や最適化

---

## まとめ

### 学んだこと

1. **HTML/CSS/JavaScript**: Web 開発の基礎三要素
2. **ブラウザ DevTools**: デバッグとパフォーマンス確認
3. **React**: コンポーネントベースの UI 構築
4. **Next.js**: フルスタックフレームワーク
5. **ビルドツール**: モダンな開発環境

### 次のステップ

- [Claude Code アプリ開発ガイド](13-claude-code-app-dev-guide.md) で実際にアプリを作成
- [API 設計・連携ガイド](25-api-guide.md) でバックエンドと連携
- [テスト入門ガイド](21-testing-intro-guide.md) でテストを学習
- [セキュリティ基礎ガイド](20-security-basics-guide.md) で安全な Web アプリ開発

### 参考リソース

**公式ドキュメント**
- MDN Web Docs: https://developer.mozilla.org/ja/
- React ドキュメント: https://ja.react.dev/
- Next.js ドキュメント: https://nextjs.org/docs

**学習サイト**
- freeCodeCamp: https://www.freecodecamp.org/
- JavaScript.info: https://ja.javascript.info/

> **最後に**: Web 開発は実践が重要です。小さなプロジェクトから始めて、徐々に複雑なものに挑戦しましょう。Claude Code が学習をサポートします。

---

**作成日**: 2026-02-19
**対象レベル**: 初心者
**想定学習時間**: 8-10 時間
