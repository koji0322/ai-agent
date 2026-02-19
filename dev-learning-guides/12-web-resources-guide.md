# おすすめ Web サイトガイド

## 0. はじめに

このガイドは **開発者がブックマークしておくべき Web サイト・オンラインサービスをまとめた自分用リファレンス** です。

- **想定読者**: 開発を始めたが、どのサイトを参照すればいいかわからない。定番サイトを一通り把握したい
- **ゴール**: 学習・開発・デザイン・情報収集に役立つ定番サイトを知り、効率的にブックマーク整理できるようになる
- **前提**: ブラウザの基本操作ができること
- **関連ガイド**: [10 - Mac おすすめアプリガイド](10-mac-apps-guide.md)、[11 - ターミナル CLI ツールガイド](11-terminal-tools-guide.md)

> **10・11 との棲み分け**: [10](10-mac-apps-guide.md) は **Mac にインストールする GUI アプリ**、[11](11-terminal-tools-guide.md) は **ターミナルで使う CLI ツール** を紹介した。
> このガイドでは **ブラウザでアクセスする Web サイト・オンラインサービス** に特化する。

> **無料サイトを優先** して紹介する。有料の場合は料金欄に明記する。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. 公式ドキュメント・リファレンス](#1-公式ドキュメントリファレンス) | MDN・Python Docs・DevDocs・Can I Use |
| [2. 学習プラットフォーム](#2-学習プラットフォーム) | freeCodeCamp・The Odin Project・Codecademy・Udemy |
| [3. 技術コミュニティ・Q&A](#3-技術コミュニティqa) | Stack Overflow・GitHub Discussions・Qiita・Zenn・Dev.to |
| [4. AI サービス・ツール](#4-ai-サービスツール) | Claude・ChatGPT・GitHub Copilot・Perplexity・v0 |
| [5. ホスティング・デプロイ](#5-ホスティングデプロイ) | Vercel・Netlify・Render・Cloudflare Pages・GitHub Pages |
| [6. デザイン・UI リソース](#6-デザインui-リソース) | Figma・Tailwind CSS・shadcn/ui・Heroicons・Google Fonts |
| [7. API・データ](#7-apiデータ) | Public APIs リスト・JSONPlaceholder・Postman API Network |
| [8. 開発支援ツール（Web）](#8-開発支援ツールweb) | regex101・Excalidraw・CodePen・StackBlitz・readme.so |
| [9. ニュース・トレンド](#9-ニューストレンド) | Hacker News・daily.dev・JavaScript Weekly・GitHub Trending |

---

## 1. 公式ドキュメント・リファレンス

何か調べるときの最初の一手。公式ドキュメントを読む習慣をつけることが上達の近道。

### 公式ドキュメント一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **MDN Web Docs** | https://developer.mozilla.org | HTML・CSS・JavaScript の公式リファレンス | 無料 |
| **Python 公式ドキュメント** | https://docs.python.org/ja/ | Python の公式リファレンス（日本語あり） | 無料 |
| **Node.js Docs** | https://nodejs.org/docs/latest/api/ | Node.js API リファレンス | 無料 |
| **TypeScript Handbook** | https://www.typescriptlang.org/docs/ | TypeScript の公式ガイド・リファレンス | 無料 |
| **React** | https://react.dev | React 公式ドキュメント（チュートリアル付き） | 無料 |
| **Next.js** | https://nextjs.org/docs | Next.js 公式ドキュメント | 無料 |

### 横断検索・互換性チェック

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **DevDocs** | https://devdocs.io | 複数言語・フレームワークのドキュメントを横断検索 | 無料 |
| **Can I Use** | https://caniuse.com | ブラウザの機能対応状況をチェック | 無料 |

### DevDocs — 統合ドキュメントビューア

| 項目 | 内容 |
|------|------|
| **URL** | https://devdocs.io |
| **用途** | HTML・CSS・JavaScript・Python・React など 600 以上のドキュメントをオフラインでも検索・閲覧 |
| **料金** | 無料 |
| **特徴** | オフライン対応・キーボード操作に最適化・高速検索 |

**おすすめの使い方:**

- 左上の「Enable」で使う言語のドキュメントを有効化
- `/` キーで検索を開始 → 候補をキーボードで選択
- オフラインモード（設定 → Offline）を有効にしておくと、回線がなくても使える

### Can I Use — ブラウザ互換性チェック

| 項目 | 内容 |
|------|------|
| **URL** | https://caniuse.com |
| **用途** | CSS プロパティや JavaScript API がどのブラウザで使えるかを一目で確認 |
| **料金** | 無料 |
| **特徴** | バージョン別の対応状況を色で表示。使用率の統計も確認可能 |

**使用例:**

- `css grid` で検索 → 各ブラウザの対応状況を確認
- `fetch api` で検索 → IE 非対応だが他は全対応、のように判断できる

---

## 2. 学習プラットフォーム

手を動かして学べるサイトを中心に紹介。すべて英語だが、ブラウザの翻訳機能で十分対応できる。

### 学習プラットフォーム一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **freeCodeCamp** | https://www.freecodecamp.org | HTML/CSS/JS を体系的に学べるカリキュラム | 無料 |
| **The Odin Project** | https://www.theodinproject.com | フルスタック開発を実践形式で学ぶ | 無料 |
| **Codecademy** | https://www.codecademy.com | インタラクティブなコーディング学習 | 無料 / Pro $19.99/月 |
| **Udemy** | https://www.udemy.com | 動画ベースの講座マーケットプレイス | 有料（セール時 ¥1,500〜） |
| **Scrimba** | https://scrimba.com | 動画+コードエディタが一体化した学習 | 無料 / Pro $18/月 |

### freeCodeCamp — 無料のフルスタック学習

| 項目 | 内容 |
|------|------|
| **URL** | https://www.freecodecamp.org |
| **用途** | Web 開発（HTML/CSS/JS）→ フロントエンド → バックエンド → データベースまで体系的に学習 |
| **料金** | 完全無料（非営利団体が運営） |
| **特徴** | ブラウザ上でコードを書いて即フィードバック。修了証明書も発行される |

**カリキュラム構成:**

| コース | 学習内容 | 時間の目安 |
|--------|---------|-----------|
| Responsive Web Design | HTML・CSS・Flexbox・Grid | 300 時間 |
| JavaScript Algorithms | JavaScript の基礎・アルゴリズム | 300 時間 |
| Front End Libraries | React・Redux・Bootstrap | 300 時間 |
| Back End & APIs | Node.js・Express・MongoDB | 300 時間 |

### The Odin Project — 実践重視のフルスタック学習

| 項目 | 内容 |
|------|------|
| **URL** | https://www.theodinproject.com |
| **用途** | 実際のツール（VS Code・Git・ターミナル）を使いながらフルスタック開発を学ぶ |
| **料金** | 完全無料（オープンソース） |
| **特徴** | 「ブラウザ内エディタ」ではなく、ローカル環境でのコーディングを推奨。より実践的 |

---

## 3. 技術コミュニティ・Q&A

エラーに詰まったとき、新しい技術を知りたいとき、アウトプットしたいとき。

### コミュニティ一覧

| サイト | URL | 用途 | 料金 | 言語 |
|--------|-----|------|------|------|
| **Stack Overflow** | https://stackoverflow.com | プログラミングの Q&A（世界最大） | 無料 | 英語 |
| **GitHub Discussions** | https://github.com（各リポジトリ） | OSS プロジェクトごとの Q&A・議論 | 無料 | 英語 |
| **Qiita** | https://qiita.com | 日本語の技術記事投稿・共有 | 無料 | 日本語 |
| **Zenn** | https://zenn.dev | 日本語の技術記事・本の投稿（マネタイズ可能） | 無料 | 日本語 |
| **Dev.to** | https://dev.to | 英語の技術ブログプラットフォーム | 無料 | 英語 |
| **Hacker News** | https://news.ycombinator.com | テック系ニュース・議論（Y Combinator 運営） | 無料 | 英語 |

### Stack Overflow — プログラミング Q&A の定番

| 項目 | 内容 |
|------|------|
| **URL** | https://stackoverflow.com |
| **用途** | エラーメッセージで検索すると、同じ問題に遭遇した人の質問と回答が見つかる |
| **料金** | 無料 |
| **特徴** | 投票制で質の高い回答が上位に表示。20 年以上の蓄積 |

**効率的な使い方:**

- Google で `エラーメッセージ site:stackoverflow.com` と検索するのが最速
- 回答のコードは **そのままコピペせず、理解してから使う**（バージョンが古い場合がある）
- 質問投稿時は [Minimal Reproducible Example](https://stackoverflow.com/help/minimal-reproducible-example) を意識する

### Qiita / Zenn — 日本語の技術コミュニティ

| 比較項目 | Qiita | Zenn |
|---------|-------|------|
| **URL** | https://qiita.com | https://zenn.dev |
| **運営** | Increments（エイチーム） | classmethod |
| **特徴** | 記事投稿に特化。タグベースの分類 | 記事+本（Book）+スクラップ。マネタイズ可能 |
| **向いている用途** | 技術メモ・Tips の共有 | 体系的な解説・チュートリアル |
| **おすすめ** | まずは読む側から。慣れたらアウトプットに使う | 長めの記事や連載を書きたいときに |

---

## 4. AI サービス・ツール

開発を加速させる AI サービス。使い分けが重要。

### AI サービス一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **Claude** | https://claude.ai | コード生成・レビュー・文章作成・分析（Anthropic） | 無料 / Pro $20/月 |
| **ChatGPT** | https://chatgpt.com | 汎用 AI アシスタント（OpenAI） | 無料 / Plus $20/月 |
| **GitHub Copilot** | https://github.com/features/copilot | エディタ内でのコード補完・生成 | 無料枠あり / $10/月 |
| **Perplexity** | https://www.perplexity.ai | AI 検索エンジン（ソース付き回答） | 無料 / Pro $20/月 |
| **v0** | https://v0.dev | プロンプトから UI コンポーネントを生成（Vercel） | 無料枠あり |

### Claude — コード生成・分析に強い AI

| 項目 | 内容 |
|------|------|
| **URL** | https://claude.ai |
| **用途** | コード生成・デバッグ・コードレビュー・文章作成・データ分析 |
| **料金** | 無料（制限あり）/ Pro $20/月 / Max $100/月 |
| **特徴** | 長い文脈の理解に優れる。Claude Code（CLI）との連携が強力 |

**開発での活用パターン:**

| パターン | 使い方 |
|---------|-------|
| コード生成 | 「Python で CSV を読み込んでグラフを作成するコードを書いて」 |
| デバッグ | エラーメッセージとコードを貼って「このエラーの原因と修正方法を教えて」 |
| コードレビュー | コードを貼って「パフォーマンスやセキュリティの問題点を指摘して」 |
| 学習 | 「async/await の仕組みを初心者向けに説明して」 |

### GitHub Copilot — エディタ内 AI コード補完

| 項目 | 内容 |
|------|------|
| **URL** | https://github.com/features/copilot |
| **用途** | VS Code などのエディタ内でリアルタイムにコード補完・生成 |
| **料金** | 無料枠あり / Individual $10/月 / Business $19/月 |
| **特徴** | コードを書いている最中に次の行を予測して提案。チャット機能も搭載 |

### Perplexity — ソース付き AI 検索

| 項目 | 内容 |
|------|------|
| **URL** | https://www.perplexity.ai |
| **用途** | 質問するとソース付きで回答。技術的な調査の入口として便利 |
| **料金** | 無料（制限あり）/ Pro $20/月 |
| **特徴** | 回答の根拠となる URL を明示。最新情報にも対応 |

---

## 5. ホスティング・デプロイ

作ったアプリを公開するためのサービス。無料枠が充実しているものを中心に紹介。

### ホスティングサービス一覧

| サイト | URL | 用途 | 無料枠 | 料金 |
|--------|-----|------|--------|------|
| **Vercel** | https://vercel.com | Next.js / React アプリのデプロイ | 個人利用は無料 | Pro $20/月 |
| **Netlify** | https://www.netlify.com | 静的サイト・JAMstack のデプロイ | 月 100GB 帯域 | Pro $19/月 |
| **Render** | https://render.com | Web サービス・DB・バックグラウンドジョブ | 静的サイト無料 | 有料プランあり |
| **Cloudflare Pages** | https://pages.cloudflare.com | 静的サイト・フルスタックアプリ | 無制限リクエスト | 無料 |
| **GitHub Pages** | https://pages.github.com | 静的サイトのホスティング（GitHub 連携） | 無料 | 無料 |
| **Streamlit Cloud** | https://streamlit.io/cloud | Streamlit アプリの公開 | パブリックアプリ無料 | 有料プランあり |

### 用途別の選び方

| やりたいこと | おすすめサービス | 理由 |
|------------|----------------|------|
| Next.js アプリを公開 | **Vercel** | Next.js 開発元。最も相性が良い |
| 静的サイト（HTML/CSS/JS）を公開 | **Cloudflare Pages** または **GitHub Pages** | 完全無料で十分 |
| Python（Streamlit）アプリを公開 | **Streamlit Cloud** | Streamlit 公式。GitHub 連携で簡単 |
| バックエンド（API サーバー）を公開 | **Render** | PostgreSQL も無料枠あり |
| ポートフォリオサイトを公開 | **Netlify** または **Vercel** | CI/CD が簡単。プレビューデプロイが便利 |

### Vercel — フロントエンド特化のデプロイ

| 項目 | 内容 |
|------|------|
| **URL** | https://vercel.com |
| **用途** | Git push するだけで自動デプロイ。プレビュー URL も自動生成 |
| **料金** | Hobby（個人）は無料 / Pro $20/月 |
| **特徴** | Next.js の開発元。サーバーレスファンクション・Edge Functions 対応 |

**デプロイの流れ:**

1. GitHub にリポジトリを push
2. Vercel にサインアップ（GitHub アカウントで）
3. リポジトリをインポート → 自動でビルド・デプロイ
4. 以後、`git push` するたびに自動デプロイ

### GitHub Pages — 最もシンプルな静的サイトホスティング

| 項目 | 内容 |
|------|------|
| **URL** | https://pages.github.com |
| **用途** | GitHub リポジトリから静的サイトを公開。ドキュメントやポートフォリオに最適 |
| **料金** | 完全無料 |
| **特徴** | `username.github.io` ドメインが無料で使える。Jekyll でブログも作れる |

---

## 6. デザイン・UI リソース

見た目を整えるためのツールと素材。デザイナーでなくても使えるものを厳選。

### デザイン・UI ツール一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **Figma** | https://www.figma.com | UI デザイン・プロトタイプ作成 | 無料枠あり / Pro $15/月 |
| **Tailwind CSS** | https://tailwindcss.com | ユーティリティファーストの CSS フレームワーク | 無料（OSS） |
| **shadcn/ui** | https://ui.shadcn.com | コピペで使える React UI コンポーネント集 | 無料（OSS） |
| **Heroicons** | https://heroicons.com | Tailwind CSS チーム製の SVG アイコン集 | 無料（OSS） |
| **Lucide** | https://lucide.dev | 軽量でカスタマイズ可能なアイコン集 | 無料（OSS） |
| **Google Fonts** | https://fonts.google.com | Web フォントの配信サービス | 無料 |
| **Realtime Colors** | https://www.realtimecolors.com | 配色をリアルタイムでプレビュー | 無料 |

### Figma — UI デザインの標準ツール

| 項目 | 内容 |
|------|------|
| **URL** | https://www.figma.com |
| **用途** | Web・モバイルアプリの UI デザイン・プロトタイプ作成 |
| **料金** | Starter（個人・3 プロジェクト）無料 / Professional $15/月 |
| **特徴** | ブラウザで動作。リアルタイム共同編集。プラグインが豊富 |

**開発者が Figma を使う場面:**

- デザインカンプからサイズ・色・フォントの値を取得（Inspect 機能）
- ワイヤーフレームを作って、AI に UI を生成させる入力にする
- 簡単なアイコンやロゴの作成

### Tailwind CSS — ユーティリティファースト CSS

| 項目 | 内容 |
|------|------|
| **URL** | https://tailwindcss.com |
| **用途** | HTML にクラス名を書くだけでスタイリング。CSS ファイルをほぼ書かない開発スタイル |
| **料金** | 無料（OSS） |
| **特徴** | Claude Code との相性が非常に良い（クラス名で指示しやすい） |

### shadcn/ui — コピペで使える UI コンポーネント

| 項目 | 内容 |
|------|------|
| **URL** | https://ui.shadcn.com |
| **用途** | Button・Dialog・Table など、よく使う UI コンポーネントをプロジェクトにコピーして使う |
| **料金** | 無料（OSS） |
| **特徴** | npm パッケージではなくソースコードをコピーする方式。自由にカスタマイズ可能 |

---

## 7. API・データ

API の学習・テスト・探索に使えるサービス。

### API・データサービス一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **Public APIs** | https://github.com/public-apis/public-apis | 無料 API のカテゴリ別リスト（GitHub） | 無料 |
| **JSONPlaceholder** | https://jsonplaceholder.typicode.com | テスト用のフェイク REST API | 無料 |
| **httpbin** | https://httpbin.org | HTTP リクエスト・レスポンスのテスト用 API | 無料 |
| **Postman API Network** | https://www.postman.com/explore | 公開 API のコレクションを検索・テスト | 無料 |
| **RapidAPI** | https://rapidapi.com | API のマーケットプレイス（数千の API を統一インターフェースで） | 無料枠あり |

### JSONPlaceholder — テスト用フェイク API

| 項目 | 内容 |
|------|------|
| **URL** | https://jsonplaceholder.typicode.com |
| **用途** | API 連携のコードをテストするときに使うダミーデータ API |
| **料金** | 無料 |
| **特徴** | ユーザー・投稿・コメント・アルバムなどの REST API をすぐに使える |

**使用例:**

```bash
# ユーザー一覧を取得
curl https://jsonplaceholder.typicode.com/users

# 投稿の作成（POST リクエストのテスト）
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "テスト", "body": "本文", "userId": 1}'
```

### Public APIs — 無料 API ディレクトリ

| 項目 | 内容 |
|------|------|
| **URL** | https://github.com/public-apis/public-apis |
| **用途** | カテゴリ別に整理された無料 API のリスト。個人開発のアイデア探しにも |
| **料金** | 無料 |
| **特徴** | 天気・ニュース・音楽・ゲーム・金融など 50 以上のカテゴリ |

**カテゴリ例:**

| カテゴリ | API の例 |
|---------|---------|
| Weather | OpenWeatherMap・WeatherAPI |
| News | NewsAPI・The Guardian |
| Music | Spotify Web API・Last.fm |
| Finance | Alpha Vantage・CoinGecko |
| Games | RAWG・PokéAPI |

---

## 8. 開発支援ツール（Web）

インストール不要。ブラウザだけで使える開発支援ツール。

### 開発支援ツール一覧

| サイト | URL | 用途 | 料金 |
|--------|-----|------|------|
| **regex101** | https://regex101.com | 正規表現のテスト・デバッグ・解説 | 無料 |
| **Excalidraw** | https://excalidraw.com | 手書き風のホワイトボード・図解ツール | 無料 |
| **CodePen** | https://codepen.io | HTML/CSS/JS のオンラインエディタ・共有 | 無料 / Pro $8/月 |
| **StackBlitz** | https://stackblitz.com | ブラウザで動くフルスタック開発環境 | 無料 |
| **readme.so** | https://readme.so | README.md をビジュアルに作成 | 無料 |
| **transform.tools** | https://transform.tools | JSON↔YAML・CSS↔Tailwind など各種変換 | 無料 |
| **Squoosh** | https://squoosh.app | 画像の圧縮・リサイズ（Google 製） | 無料 |

### regex101 — 正規表現のテスト・学習

| 項目 | 内容 |
|------|------|
| **URL** | https://regex101.com |
| **用途** | 正規表現をリアルタイムでテスト。各パーツの意味も解説してくれる |
| **料金** | 無料 |
| **特徴** | Python・JavaScript・Go・PHP など複数の正規表現エンジンに対応 |

**使い方:**

1. 左上でフレーバー（Python / JavaScript 等）を選択
2. 上段に正規表現パターンを入力
3. 下段にテスト文字列を入力
4. マッチ箇所がリアルタイムでハイライトされる
5. 右側に各パーツの解説が表示される

### Excalidraw — 手書き風の図解ツール

| 項目 | 内容 |
|------|------|
| **URL** | https://excalidraw.com |
| **用途** | アーキテクチャ図・フローチャート・ワイヤーフレームを手軽に描く |
| **料金** | 無料（OSS） |
| **特徴** | 手書き風のスタイルが特徴。リアルタイム共同編集。エクスポート（PNG / SVG）対応 |

### StackBlitz — ブラウザ内開発環境

| 項目 | 内容 |
|------|------|
| **URL** | https://stackblitz.com |
| **用途** | ブラウザ上で Node.js を実行。React・Next.js・Vue などのプロジェクトを即座に作成 |
| **料金** | 無料 |
| **特徴** | WebContainers 技術でブラウザ内に Node.js が動作。インストール不要で開発環境が完成 |

---

## 9. ニュース・トレンド

技術トレンドを追うための情報源。全部を毎日見る必要はない。1〜2 つに絞って定期的にチェックするのがおすすめ。

### ニュース・トレンドサイト一覧

| サイト | URL | 用途 | 料金 | 頻度 |
|--------|-----|------|------|------|
| **Hacker News** | https://news.ycombinator.com | テック全般のニュース・議論 | 無料 | リアルタイム |
| **daily.dev** | https://daily.dev | 開発者向けニュースアグリゲーター | 無料 | 毎日 |
| **JavaScript Weekly** | https://javascriptweekly.com | JavaScript の週刊ニュースレター | 無料 | 毎週金曜 |
| **bytes.dev** | https://bytes.dev | JavaScript・React の週刊ニュースレター（カジュアルな文体） | 無料 | 毎週月曜 |
| **GitHub Trending** | https://github.com/trending | GitHub で今注目されているリポジトリ | 無料 | リアルタイム |
| **TLDR Newsletter** | https://tldr.tech | テック全般の日刊ニュースレター（5 分で読める） | 無料 | 毎日 |

### daily.dev — パーソナライズされた開発者ニュース

| 項目 | 内容 |
|------|------|
| **URL** | https://daily.dev |
| **用途** | 複数の技術ブログ・ニュースサイトの記事を一箇所に集約。ブラウザの新しいタブに表示 |
| **料金** | 無料 |
| **特徴** | Chrome 拡張で新しいタブをニュースフィードに。興味のあるタグでパーソナライズ |

### GitHub Trending — 今注目のリポジトリ

| 項目 | 内容 |
|------|------|
| **URL** | https://github.com/trending |
| **用途** | 今日 / 今週 / 今月の人気リポジトリ・開発者を確認 |
| **料金** | 無料 |
| **特徴** | 言語でフィルタ可能。新しいツールやライブラリの発見に最適 |

**おすすめの使い方:**

- 週 1 回、自分の使う言語（Python・JavaScript 等）でフィルタして確認
- 気になるリポジトリは Star を付けて後で試す
- README を読んで、どんな問題を解決するツールなのかを把握する

---

## まとめ — ブックマーク推奨サイト

まずはこれだけブックマークしておけば十分、というサイトを厳選。

### 最初にブックマークすべき 10 サイト

| 優先度 | サイト | 用途 |
|--------|--------|------|
| 1 | **MDN Web Docs** | Web 技術のリファレンス |
| 2 | **Claude** | AI によるコード生成・質問 |
| 3 | **Stack Overflow** | エラー解決・Q&A |
| 4 | **GitHub Trending** | 新しいツール・ライブラリの発見 |
| 5 | **DevDocs** | ドキュメント横断検索 |
| 6 | **Vercel** | アプリのデプロイ |
| 7 | **regex101** | 正規表現のテスト |
| 8 | **Excalidraw** | 図解・設計メモ |
| 9 | **Zenn** | 日本語の技術記事 |
| 10 | **daily.dev** | テックニュースの収集 |

---

**関連ガイド:**

- [10 - Mac おすすめアプリガイド](10-mac-apps-guide.md) — Mac にインストールするアプリ
- [11 - ターミナル CLI ツールガイド](11-terminal-tools-guide.md) — ターミナルで使うコマンド
- [04 - アプリケーション開発ガイド](04-claude-code-app-dev-guide.md) — API 連携の実践
- [05 - 公開・運用ガイド](05-claude-code-deploy-guide.md) — デプロイの詳細手順
