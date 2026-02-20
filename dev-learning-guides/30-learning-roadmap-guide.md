# Claude Code 開発学習ロードマップ — 初心者からプロフェッショナルへ

## 0. はじめに

このガイドは **プログラミング未経験の初心者が、Claude Code エコシステムを活用して開発のプロフェッショナルになるまでの学習ロードマップをまとめた自分用リファレンス** です。

- **想定読者**: プログラミング初心者。プログラミング未経験〜初心者。AI を活用した開発スキルを身につけ、キャリアとして成長したい人
- **ゴール**: 学習の全体像を把握し、各段階で何を・どの順で・どのくらい学ぶかを理解できるようになる
- **前提**: 特になし（完全な初心者を想定。Mac を使用）
- **関連ガイド**: 本シリーズのすべてのガイド（[00](00-vscode-guide.md)〜[05](05-sns-guide.md)、10〜16、20〜27）

> これまでのガイド（00〜05、10〜16、20〜27）は各テーマのリファレンスとして作成した。
> このガイドでは **「何を」「どの順で」「どのくらい」学ぶか** のロードマップに焦点を当てる。
> すべてのフェーズで **Claude Code を学習パートナーとして活用** し、従来の独学よりも効率的に成長する。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. ロードマップ全体像](#1-ロードマップ全体像) | 7 つのフェーズと到達レベル |
| [2. Phase 1 — Mac と開発環境の基礎（0〜2 週間）](#2-phase-1--mac-と開発環境の基礎02-週間) | Mac 操作・VS Code・ターミナルの基礎 |
| [3. Phase 2 — Claude Code で開発を始める（2 週間〜1 ヶ月）](#3-phase-2--claude-code-で開発を始める2-週間1-ヶ月) | Claude Code の基本操作・対話の流れ |
| [4. Phase 3 — Git とチーム開発の基礎（1〜2 ヶ月）](#4-phase-3--git-とチーム開発の基礎12-ヶ月) | Git・GitHub・開発フロー |
| [5. Phase 4 — プログラミングとアプリ開発（2〜5 ヶ月）](#5-phase-4--プログラミングとアプリ開発25-ヶ月) | Python・Web 基礎・DB・API |
| [6. Phase 5 — Claude Code の応用と自動化（5〜7 ヶ月）](#6-phase-5--claude-code-の応用と自動化57-ヶ月) | 設定・カスタムコマンド・フック・MCP |
| [7. Phase 6 — 公開・運用と実践力（7〜12 ヶ月）](#7-phase-6--公開運用と実践力712-ヶ月) | デプロイ・CI/CD・ポートフォリオ |
| [8. Phase 7 — プロフェッショナル（12 ヶ月〜）](#8-phase-7--プロフェッショナル12-ヶ月) | スキル・マルチエージェント・チーム開発 |
| [9. 学習リソースマップ](#9-学習リソースマップ) | フェーズ別の推奨リソース |
| [10. キャリアパス](#10-キャリアパス) | AI 時代の開発者キャリア・転職戦略 |
| [11. 学習を継続するための習慣](#11-学習を継続するための習慣) | 挫折しない仕組みづくり |
| [12. まとめ — レベル別チェックリスト](#12-まとめ--レベル別チェックリスト) | 各フェーズの到達確認 |

---

## 1. ロードマップ全体像

### 7 つのフェーズ

```
Phase 1         Phase 2         Phase 3         Phase 4
Mac・環境  →    Claude Code → Git・GitHub →  アプリ開発
(0-2 週間)      (2 週間-1 ヶ月)   (1-2 ヶ月)      (2-5 ヶ月)

                    Phase 5         Phase 6         Phase 7
                →  応用・自動化  →  公開・運用  →  プロフェッショナル
                    (5-7 ヶ月)      (7-12 ヶ月)     (12 ヶ月〜)
```

### フェーズと対応ガイド

| フェーズ | 対応ガイド | 到達レベル |
|---------|-----------|-----------|
| Phase 1 | [00](00-vscode-guide.md)・[01](01-mac-basics-guide.md) | Mac と開発ツールの基本操作ができる |
| Phase 2 | [10](10-claude-code-guide.md) | Claude Code で対話しながらファイルを作れる |
| Phase 3 | [11](11-claude-code-practical-guide.md)・[20](20-security-basics-guide.md)・[21](21-testing-intro-guide.md) | Git で管理しながら開発フローで作業できる |
| Phase 4 | [26](26-python-setup-guide.md)・[13](13-claude-code-app-dev-guide.md)・[23](23-web-basics-guide.md)・[24](24-database-intro-guide.md)・[25](25-api-guide.md)・[27](27-data-analysis-guide.md) | Python・Web アプリ・DB を使ったアプリを作れる |
| Phase 5 | [12](12-claude-code-advanced-guide.md)・[22](22-docker-intro-guide.md) | Claude Code をカスタマイズし作業を自動化できる |
| Phase 6 | [14](14-claude-code-deploy-guide.md) | アプリを公開し CI/CD で運用できる |
| Phase 7 | [15](15-claude-code-skills-guide.md)・[16](16-claude-code-multi-agent-guide.md) | スキル・マルチエージェントを使いこなせる |

> **補足**: [02](02-mac-apps-guide.md)・[03](03-terminal-tools-guide.md)・[04](04-web-resources-guide.md)・[05](05-sns-guide.md) はどのフェーズからでも参照できるリファレンスガイド。学習の進度に合わせて随時参照する。

### フェーズ別の到達レベル

| フェーズ | 期間の目安 | できるようになること |
|---------|-----------|------------------|
| Phase 1 | 0〜2 週間 | Mac 操作・VS Code・ターミナルの基本ができる |
| Phase 2 | 2 週間〜1 ヶ月 | Claude Code で指示を出しファイルを作成・編集できる |
| Phase 3 | 1〜2 ヶ月 | Git で管理しながら計画的に開発を進められる |
| Phase 4 | 2〜5 ヶ月 | Python・Web アプリ・DB で実用的なアプリを作れる |
| Phase 5 | 5〜7 ヶ月 | カスタムコマンド・フック・MCP で環境を最適化できる |
| Phase 6 | 7〜12 ヶ月 | GitHub で公開し CI/CD で自動テスト・運用できる |
| Phase 7 | 12 ヶ月〜 | 複数 AI を協調させ大規模プロジェクトをリードできる |

### 学習時間の目安

| 学習ペース | 1 日の学習時間 | Phase 7 到達までの目安 |
|-----------|-------------|---------------------|
| フルタイム学習 | 6〜8 時間 | 約 6〜8 ヶ月 |
| 働きながら（集中） | 2〜3 時間 | 約 12〜18 ヶ月 |
| 働きながら（ゆっくり） | 1〜2 時間 | 約 18〜24 ヶ月 |

> **重要**: Claude Code を活用することで、従来の独学に比べて学習効率は大幅に向上する。
> ただし「Claude Code が書いてくれるからコードを理解しなくて良い」わけではない。
> **Claude Code に書いてもらったコードを必ず読み、理解する** 習慣をつけること。

### AI 時代の学習の考え方

従来の学習とAI 時代の学習はアプローチが異なる。

| 項目 | 従来の学習 | AI 時代の学習（本ロードマップ） |
|------|-----------|--------------------------|
| コードの書き方 | 文法を暗記してから書く | Claude Code に生成させ、読んで理解する |
| エラー対処 | エラーメッセージを検索する | Claude Code に原因調査と修正を依頼する |
| 設計 | 設計パターンを学んでから実装 | Claude Code と対話しながら設計を進める |
| 学習の順序 | 基礎 → 応用 → 実践 | 実践 → 必要な基礎に戻る（実践ファースト） |
| 重要なスキル | 暗記力・タイピング速度 | 問題の言語化力・指示の明確さ・コードの読解力 |

---

## 2. Phase 1 — Mac と開発環境の基礎（0〜2 週間）

このフェーズのゴール: **Mac の基本操作と開発ツール（VS Code・ターミナル）を使えるようになる**。

### Phase 1 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| Mac の基本操作 | メニューバー・Dock・キーボード・トラックパッド | [01](01-mac-basics-guide.md) セクション 1〜5 | 2〜3 日 |
| Finder の使い方 | ファイル管理・フォルダ操作・パスの概念 | [01](01-mac-basics-guide.md) セクション内 | 1〜2 日 |
| VS Code の導入 | インストール・画面構成・基本操作 | [00](00-vscode-guide.md) セクション 1〜4 | 2〜3 日 |
| ターミナルの基礎 | 開き方・基本コマンド・パスの概念 | [10](10-claude-code-guide.md) セクション 1 | 2〜3 日 |
| Homebrew の導入 | Mac のパッケージマネージャーのインストール | [02](02-mac-apps-guide.md) セクション 2 | 1 日 |

### 2-1. Mac の基本操作

Windows から移行する場合、キーボードの修飾キーの違いが最初のハードル。

**最低限覚えるショートカット:**

| 操作 | Windows | Mac |
|------|---------|-----|
| コピー | `Ctrl + C` | `Cmd + C` |
| ペースト | `Ctrl + V` | `Cmd + V` |
| 切り取り | `Ctrl + X` | `Cmd + X` |
| 元に戻す | `Ctrl + Z` | `Cmd + Z` |
| 保存 | `Ctrl + S` | `Cmd + S` |
| 全選択 | `Ctrl + A` | `Cmd + A` |
| アプリ切り替え | `Alt + Tab` | `Cmd + Tab` |
| Spotlight（検索） | — | `Cmd + Space` |

> **ポイント**: Windows の `Ctrl` が Mac では `Cmd` になると覚えればほとんどのショートカットに対応できる。
> 詳細は [01 - Mac 基礎操作ガイド](01-mac-basics-guide.md) を参照。

### 2-2. ターミナルの基礎

ターミナルは **文字入力でパソコンを操作する画面**。Claude Code はターミナル上で動く。

**最低限覚えるコマンド:**

| コマンド | 意味 | 使用例 |
|---------|------|--------|
| `pwd` | 今いる場所を表示 | `pwd` → `/Users/matsubarakouji` |
| `ls` | フォルダの中身を一覧表示 | `ls` → ファイルの一覧 |
| `cd フォルダ名` | フォルダに移動 | `cd Documents` |
| `cd ..` | 一つ上のフォルダに戻る | `cd ..` |
| `mkdir フォルダ名` | 新しいフォルダを作る | `mkdir my-project` |

**パスの概念:**

```
/Users/matsubarakouji/Documents/my-project
↑ ルート   ↑ ユーザー    ↑ フォルダ    ↑ プロジェクト
```

Finder で「ホーム → Documents → my-project」と辿るのと同じ。ターミナルでは文字で表現する。

### 2-3. VS Code の導入

VS Code は Claude Code と連携できるコードエディタ。メモ帳の高機能版と考えればよい。

**最初にやること:**

1. VS Code をインストール（[00](00-vscode-guide.md) セクション 1）
2. 日本語化拡張をインストール（Japanese Language Pack）
3. フォルダを開く（`Cmd + O`）
4. 内蔵ターミナルを開く（`` Ctrl + ` ``）

> VS Code の内蔵ターミナルで Claude Code を実行すると、エディタとターミナルを行き来する手間がなくなる。
> この組み合わせが最も効率的な開発環境。

### 2-4. 開発に必要なアプリの導入

Phase 1 で入れるのは最小限。学習が進んだら [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md) を参照して追加する。

**Phase 1 の最小セットアップ:**

詳細は [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md) を参照。

```bash
# 1. Homebrew のインストール
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Node.js のインストール（Claude Code に必要）
brew install node

# 3. VS Code のインストール
brew install --cask visual-studio-code

# 4. Git のインストール（Phase 3 で使う。先に入れておく）
brew install git
```

### Phase 1 の確認ポイント

- [ ] Mac のキーボードショートカット（Cmd+C/V/Z/S/Tab）が使える
- [ ] Finder でファイルの作成・移動・コピーができる
- [ ] VS Code でフォルダを開き、ファイルを編集・保存できる
- [ ] ターミナルで `pwd`・`ls`・`cd`・`mkdir` が使える
- [ ] パスの概念（`/Users/ユーザー名/Documents/...`）を理解している
- [ ] Homebrew で Node.js をインストールした

---

## 3. Phase 2 — Claude Code で開発を始める（2 週間〜1 ヶ月）

このフェーズのゴール: **Claude Code と対話しながら、ファイルの作成・編集・コードの生成ができるようになる**。

### Phase 2 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| Claude Code のインストール | npm でインストール・初回ログイン | [10](10-claude-code-guide.md) セクション 2 | 30 分 |
| 起動と終了 | プロジェクトフォルダでの起動・`Ctrl+D` で終了 | [10](10-claude-code-guide.md) セクション 3 | 30 分 |
| 基本的な対話 | 指示 → 提案 → 承認の流れ | [10](10-claude-code-guide.md) セクション 4 | 1〜2 日 |
| スラッシュコマンド | `/help`・`/clear`・`/plan` | [10](10-claude-code-guide.md) セクション 5 | 1 日 |
| パーミッションモード | デフォルト・自動承認・プランモードの使い分け | [10](10-claude-code-guide.md) セクション 7 | 1 日 |
| CLAUDE.md | プロジェクト固有の設定ファイル | [10](10-claude-code-guide.md) セクション 8 | 1 日 |
| 効果的な指示の出し方 | 具体的な指示・段階的な進め方 | [10](10-claude-code-guide.md) セクション 9 | 継続的 |
| 実践演習 | 小さなプロジェクトを 3 つ以上作る | — | 1〜2 週間 |

### 3-1. Claude Code のインストールと起動

```bash
# インストール
npm install -g @anthropic-ai/claude-code

# プロジェクトフォルダを作成して移動
mkdir ~/Documents/my-first-project
cd ~/Documents/my-first-project

# Claude Code を起動
claude
```

> ターミナルでプロジェクトフォルダに移動して `claude` と入力するだけで起動できる。

### 3-2. 対話の基本フロー

Claude Code は **チャット形式** で操作する。日本語でやりたいことを入力する。

```
[指示を入力] → [Claude が提案] → [承認(y) or 拒否(n)] → [結果を確認]
```

**最初の会話例:**

```
あなた: 「index.html を作って。Hello World と表示するシンプルなページにして」

Claude: index.html を作成します。
        （ファイル内容が表示される）
        → 承認しますか？ [y/n]

あなた: y

Claude: index.html を作成しました。
```

### 3-3. 効果的な指示の出し方

Claude Code の活用力は **「指示の質」** で決まる。これは AI 時代の最重要スキル。

**悪い指示 → 良い指示:**

| 悪い指示 | 良い指示 | 理由 |
|---------|---------|------|
| 「Web サイト作って」 | 「自己紹介の Web ページを作って。名前・趣味・スキルの 3 セクションで、背景は薄いグレー」 | 具体的な要件がある |
| 「バグ直して」 | 「app.js を実行すると 12 行目で TypeError が出る。原因を調べて修正して」 | エラー情報が含まれている |
| 「全部やって」 | 「まずプロジェクトの構成を説明して。次にログイン機能のファイルを探して」 | ステップに分かれている |

**指示のテンプレート:**

```
1. 何をしたいか（目的）
2. どのファイルに対して（対象）
3. どのような条件で（制約・仕様）
4. 完了条件（何ができれば OK か）
```

### 3-4. CLAUDE.md の活用

プロジェクトフォルダに `CLAUDE.md` を置くと、Claude Code が起動時に自動で読み込む。

```
あなた: 「/init」
Claude: プロジェクトの内容を読み取って CLAUDE.md を生成しました。
```

**手動で書く場合の例:**

```markdown
# プロジェクト概要
初心者の学習用プロジェクト。HTML + CSS + JavaScript で自己紹介ページを作成する。

# 注意事項
- 初心者向けにシンプルなコードを書くこと
- コードには日本語のコメントを付けること
- 外部ライブラリは使わない
```

### 3-5. Phase 2 の実践演習

理論だけでなく、実際にプロジェクトを作ることが重要。以下の順で取り組む。

**演習 1: 自己紹介ページ（HTML + CSS）**

```
指示例: 「自己紹介の Web ページを作って。
       名前・趣味・スキルの 3 セクションを含めて。
       CSS でシンプルなデザインにして。色は青系統で」
```

**演習 2: 計算機アプリ（HTML + CSS + JavaScript）**

```
指示例: 「ブラウザで動く電卓アプリを作って。
       四則演算ができるようにして。
       ボタンのデザインは見やすくして」
```

**演習 3: ToDo リスト（HTML + CSS + JavaScript）**

```
指示例: 「ブラウザで動く ToDo リストアプリを作って。
       タスクの追加・完了チェック・削除ができるようにして。
       データはブラウザの localStorage に保存して」
```

> **重要**: Claude Code が生成したコードを **必ず読む**。
> 「何をしているか」を Claude Code に聞いて説明してもらい、理解してから次へ進む。
> 例: 「この JavaScript のコードを 1 行ずつ説明して」

### Phase 2 の確認ポイント

- [ ] Claude Code をインストールし、起動・終了ができる
- [ ] 日本語で指示を出し、ファイルを作成・編集できる
- [ ] スラッシュコマンド（`/help`・`/clear`・`/plan`）を使える
- [ ] パーミッションモードの違いを理解している
- [ ] CLAUDE.md を作成し、プロジェクト情報を記述できる
- [ ] 3 つ以上の小さなプロジェクトを Claude Code で作成した
- [ ] Claude Code が生成したコードを読んで大まかな意味が理解できる

---

## 4. Phase 3 — Git とチーム開発の基礎（1〜2 ヶ月）

このフェーズのゴール: **Git でバージョン管理しながら、計画的に開発を進められるようになる**。

### Phase 3 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| Git の基本概念 | バージョン管理とは何か・なぜ必要か | [11](11-claude-code-practical-guide.md) セクション 1 | 1〜2 日 |
| Git の基本コマンド | `init`・`add`・`commit`・`log`・`diff` | [11](11-claude-code-practical-guide.md) セクション 1 | 3〜4 日 |
| GitHub の使い方 | アカウント作成・SSH 設定・`push`・`pull` | [11](11-claude-code-practical-guide.md) セクション 2 | 2〜3 日 |
| 開発フロー | 調査 → 計画 → 実装 → 確認 → 記録 | [11](11-claude-code-practical-guide.md) セクション 4 | 1〜2 週間 |
| プロジェクトの始め方 | フォルダ構成・`.gitignore`・CLAUDE.md 整備 | [11](11-claude-code-practical-guide.md) セクション 3 | 1〜2 日 |
| 拡張思考モード | `Alt+T` で有効化・複雑な問題での活用 | [11](11-claude-code-practical-guide.md) セクション 5 | 1 日 |
| デバッグ | エラー貼り付け・スクリーンショット活用 | [11](11-claude-code-practical-guide.md) セクション 6 | 継続的 |
| セキュリティ基礎 | パスワード管理・API キーの安全な扱い | [20](20-security-basics-guide.md) セクション 1〜3 | 1〜2 日 |
| テストの考え方 | テストの種類・pytest の基本・TDD 入門 | [21](21-testing-intro-guide.md) セクション 1〜3 | 2〜3 日 |

### 4-1. Git の基本

Git はファイルの変更履歴を管理するツール。「セーブポイントを作る」感覚。

**Git の 3 ステップ:**

```
[ファイルを編集] → git add（ステージ）→ git commit（記録）
```

| 操作 | コマンド | 日常での例え |
|------|---------|------------|
| 変更をステージする | `git add ファイル名` | 「送りたい荷物を箱に入れる」 |
| 変更を記録する | `git commit -m "説明"` | 「箱に伝票を貼って発送する」 |
| 履歴を見る | `git log --oneline` | 「発送履歴を確認する」 |
| 差分を見る | `git diff` | 「前回からの変更点を確認する」 |
| 前に戻す | `git checkout -- ファイル名` | 「前の状態に巻き戻す」 |

> Claude Code に `git` コマンドを実行してもらうこともできる。
> 例: 「今の変更を Git にコミットして。メッセージは『自己紹介ページのデザインを改善』にして」

### 4-2. GitHub

GitHub は Git のリポジトリをクラウドに保存するサービス。バックアップ + 公開の機能を持つ。

**初期設定の手順:**

1. https://github.com でアカウント作成
2. SSH キーの設定（Claude Code に依頼可能）
3. リポジトリを作成して push

```
あなた: 「GitHub の SSH キーを設定するための手順を教えて。
       SSH キーの生成から GitHub への登録まで」

Claude: 以下の手順で設定します...
```

### 4-3. 開発フロー

「いきなり作り始める」のではなく、計画的に進めることで品質と効率が上がる。

**5 フェーズの開発フロー:**

```
[1. 調査] → [2. 計画] → [3. 実装] → [4. 確認] → [5. 記録]
    ↑________________________________↓
                （反復）
```

| フェーズ | やること | Claude Code への指示例 |
|---------|---------|---------------------|
| 1. 調査 | 既存コードの理解 | 「このプロジェクトの構成を説明して」 |
| 2. 計画 | 実装方針を立てる | `/plan ログイン機能を追加するための計画を立てて` |
| 3. 実装 | コードを書く | 「計画に沿ってログインフォームを作って」 |
| 4. 確認 | テスト・動作確認 | 「この機能をテストして。エッジケースも確認して」 |
| 5. 記録 | Git にコミット | 「変更を Git にコミットして」 |

### 4-4. デバッグの基本

エラーが出たときの対処法を身につける。

**エラー対処の手順:**

1. **エラーメッセージをコピーして Claude Code に貼り付ける**
2. 「このエラーの原因を調べて」と依頼
3. Claude Code の説明を読んで原因を理解する
4. 修正案を確認してから承認する

```
あなた: 「app.js を実行したら以下のエラーが出た:
       TypeError: Cannot read properties of undefined (reading 'map')
       原因を調べて修正して」

Claude: エラーの原因を調査します...
        変数 data が undefined のまま .map() を呼んでいます。
        データの読み込みを待つ処理が必要です。
        修正案: ...
```

> **重要**: エラーを恐れない。エラーは「何が問題か」を教えてくれる情報源。
> Claude Code はエラーの解読が得意なので、遠慮なく質問する。

### 4-5. セキュリティとテストの基礎

Phase 3 から、セキュリティとテストの基本的な考え方を身につけておく。

**セキュリティ**: API キーやパスワードをコードに直接書かない。`.env` と `.gitignore` でシークレットを管理する習慣を最初からつける。詳細は [20 - セキュリティ基礎ガイド](20-security-basics-guide.md) を参照。

**テスト**: 「動いているように見える」と「正しく動いている」は違う。小さなテストを書く習慣をつける。詳細は [21 - テスト入門ガイド](21-testing-intro-guide.md) を参照。

### Phase 3 の確認ポイント

- [ ] Git の `add`・`commit`・`log`・`diff` が使える
- [ ] GitHub にリポジトリを作成し、`push` できる
- [ ] 「調査 → 計画 → 実装 → 確認 → 記録」のフローで開発できる
- [ ] `/plan` モードで実装計画を立てられる
- [ ] エラーメッセージを Claude Code に貼り付けてデバッグできる
- [ ] `.gitignore` の役割を理解している
- [ ] API キーをコードに直接書いてはいけないことを理解している

---

## 5. Phase 4 — プログラミングとアプリ開発（2〜5 ヶ月）

このフェーズのゴール: **Python・Web 技術・DB・API を使って実用的なアプリケーションを作れるようになる**。

### Phase 4 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| Python 環境構築 | pyenv・venv・pip・VS Code 設定 | [26](26-python-setup-guide.md) | 2〜3 日 |
| Python 基礎 | 変数・リスト・辞書・関数・ファイル操作 | [13](13-claude-code-app-dev-guide.md) セクション 1 | 2〜3 週間 |
| Python 応用 | クラス・例外処理・外部ライブラリ | — | 1〜2 週間 |
| HTML / CSS / JavaScript | Web ページの構造・見た目・動き | [23](23-web-basics-guide.md) セクション 1〜3 | 2〜3 週間 |
| コマンドラインツール | `argparse` で引数を受け取るスクリプト | [13](13-claude-code-app-dev-guide.md) セクション 3 | 1 週間 |
| Web アプリ | Streamlit（手軽）・Flask（本格的） | [13](13-claude-code-app-dev-guide.md) セクション 4 | 2〜3 週間 |
| データベース | SQLite・SQL・テーブル設計 | [24](24-database-intro-guide.md)・[13](13-claude-code-app-dev-guide.md) セクション 5 | 1〜2 週間 |
| API 連携 | REST API・`requests`・FastAPI | [25](25-api-guide.md)・[13](13-claude-code-app-dev-guide.md) セクション 6 | 1〜2 週間 |
| テスト | `pytest` の基本 | [13](13-claude-code-app-dev-guide.md) セクション 7 | 1 週間 |
| データ分析（応用） | pandas・matplotlib・Jupyter Notebook | [27](27-data-analysis-guide.md) | 1〜2 週間 |

### 5-1. Python 環境の構築

Python で開発を始める前に、まず環境を整える。詳細は [26 - Python 環境構築ガイド](26-python-setup-guide.md) を参照。

**最低限やること:**

1. **pyenv で Python をインストール** — バージョンを自分で管理できるようにする
2. **venv で仮想環境を作る** — プロジェクトごとにライブラリを分離する
3. **VS Code の Python 拡張を入れる** — コード補完・デバッグが使えるようになる

```bash
# pyenv で Python 3.13 をインストール
pyenv install 3.13
pyenv global 3.13

# プロジェクトフォルダで仮想環境を作成・有効化
python -m venv .venv
source .venv/bin/activate
```

> 環境構築でつまずいたら Claude Code に「Python の環境構築でエラーが出た」と貼り付けて相談する。

### 5-2. Python の学習（Claude Code と一緒に）

Python は AI 時代の最重要言語。Claude Code と組み合わせることで効率的に学べる。

**AI 時代の Python 学習法:**

```
1. Claude Code に「○○するスクリプトを書いて」と依頼
2. 生成されたコードを読む
3. わからない部分を「この部分を説明して」と質問
4. 自分でコードを少し変更して動作を確認する
5. 理解したら次の課題に進む
```

**Python で最初に学ぶこと（優先度順）:**

| 優先度 | トピック | Claude Code への指示例 |
|--------|---------|---------------------|
| 1（必須） | 変数・型・演算 | 「変数の基本を教えて。実行可能なサンプルコードも書いて」 |
| 1（必須） | リスト・辞書 | 「リストと辞書の使い方を、実際のデータ処理の例で示して」 |
| 1（必須） | for ループ・条件分岐 | 「1〜100 の数字で FizzBuzz を書いて。コメント付きで」 |
| 1（必須） | 関数定義 | 「消費税を計算する関数を作って。テストコードも書いて」 |
| 2（重要） | ファイル操作 | 「CSV ファイルを読み込んで集計するスクリプトを書いて」 |
| 2（重要） | 外部ライブラリ | 「pandas でデータを読み込んでグラフを作るコードを書いて」 |
| 3（後回し可） | クラス・例外処理 | 「ToDoリストをクラスで実装して。エラー処理も入れて」 |

### 5-3. Web 技術の基礎

Web アプリを作るための 3 つの言語を理解する。

| 言語 | 役割 | 例え |
|------|------|------|
| HTML | ページの構造 | 家の骨組み |
| CSS | 見た目のデザイン | 壁紙・家具の配置 |
| JavaScript | 動き・インタラクション | 電気・水道（動く部分） |

**学習のアプローチ:**

```
あなた: 「HTML・CSS・JavaScript の基本を使った天気予報アプリのページを作って。
       各技術がどの部分を担当しているか、コメントで説明も入れて」

Claude: 3 つのファイルを作成します...
        - index.html: ページの構造（見出し・入力欄・表示エリア）
        - style.css: デザイン（色・レイアウト・フォント）
        - script.js: 動作（ボタンクリック・データ表示）
```

> Web 技術の詳細は [23 - Web 開発基礎ガイド](23-web-basics-guide.md) を参照。React や Next.js などのフレームワークも紹介している。

### 5-4. Web アプリ（Streamlit）

Streamlit は Python だけで Web アプリを作れるフレームワーク。フロントエンドの知識がなくても動くアプリが作れる。

**Streamlit アプリの作成例:**

```
あなた: 「CSV ファイルをアップロードすると、データの概要とグラフを表示する
       Streamlit アプリを作って」

Claude: streamlit_app.py を作成します...
```

```python
# Claude Code が生成するコードの例
import streamlit as st
import pandas as pd

st.title("CSV データビューア")

uploaded_file = st.file_uploader("CSV ファイルを選択", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("データの概要")
    st.dataframe(df.describe())
    st.subheader("グラフ")
    st.bar_chart(df.select_dtypes(include="number").iloc[:, :3])
```

```bash
# 実行
pip install streamlit pandas
streamlit run streamlit_app.py
```

### 5-5. データベース（SQLite）

データの永続化に SQLite を使う。Python に標準で入っているため追加インストール不要。詳細は [24 - データベース入門ガイド](24-database-intro-guide.md) を参照。

```
あなた: 「SQLite を使った簡単な読書記録アプリを作って。
       書籍の追加・一覧表示・検索ができるようにして。
       コマンドラインで操作できるようにして」

Claude: book_manager.py を作成します...
```

### 5-6. テスト

「動いているように見える」と「正しく動いている」は違う。テストを書く習慣をつける。

```
あなた: 「book_manager.py のテストを pytest で書いて。
       正常系と異常系の両方をカバーして」

Claude: test_book_manager.py を作成します...
```

```bash
# テストの実行
pip install pytest
pytest test_book_manager.py -v
```

### 5-7. データ分析（応用パス）

Python の基礎を学んだら、データ分析にも挑戦してみよう。CSV や Excel のデータを読み込んで集計・可視化する力は、どの職種でも役に立つ。

```
あなた: 「売上データの CSV を読み込んで、月別の集計と棒グラフを作って。
       pandas と matplotlib を使って」

Claude: analyze_sales.py を作成します...
```

> データ分析の詳細は [27 - データ分析入門ガイド](27-data-analysis-guide.md) を参照。pandas・matplotlib・Jupyter Notebook の使い方をまとめている。

### 5-8. Phase 4 の実践プロジェクト

以下のようなプロジェクトを Claude Code と一緒に作り、GitHub に公開する。

| プロジェクト | 使う技術 | 学べること |
|------------|---------|-----------|
| 家計簿 CLI ツール | Python・SQLite・argparse | DB・コマンドライン |
| CSV 集計ツール | Python・pandas | データ処理・ライブラリ活用 |
| Markdown ブログ生成ツール | Python・HTML・CSS | ファイル操作・テンプレート |
| 天気予報 Web アプリ | Streamlit・API | Web アプリ・API 連携 |
| 読書記録アプリ | Flask・SQLite・HTML | フルスタック開発の基本 |
| 売上データ分析ツール | pandas・matplotlib・Jupyter | データ分析・可視化 |

### Phase 4 の確認ポイント

- [ ] pyenv と venv で Python 環境を構築できる
- [ ] Python の基本文法（変数・リスト・辞書・関数・ループ）を理解している
- [ ] Claude Code に Python スクリプトを書いてもらい、動作を理解できる
- [ ] HTML・CSS・JavaScript の役割の違いを説明できる
- [ ] Streamlit で簡単な Web アプリを作れる
- [ ] SQLite を使ったデータの保存・検索ができる
- [ ] API からデータを取得するスクリプトを作れる
- [ ] pytest でテストを書いて実行できる
- [ ] GitHub にプロジェクトを 3 つ以上公開した

---

## 6. Phase 5 — Claude Code の応用と自動化（5〜7 ヶ月）

このフェーズのゴール: **Claude Code をカスタマイズし、繰り返し作業を自動化できるようになる**。

### Phase 5 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| 設定ファイル | ユーザー / プロジェクト共有 / ローカルの 3 スコープ | [12](12-claude-code-advanced-guide.md) セクション 1 | 2〜3 日 |
| CLAUDE.md 高度な活用 | 読み込み階層・禁止事項の明記 | [12](12-claude-code-advanced-guide.md) セクション 2 | 1〜2 日 |
| カスタムコマンド | `.claude/commands/` にテンプレートを配置 | [12](12-claude-code-advanced-guide.md) セクション 3 | 3〜4 日 |
| フック | `PreToolUse`・`PostToolUse`・`Notification` | [12](12-claude-code-advanced-guide.md) セクション 4 | 3〜4 日 |
| MCP | 外部ツール連携・`.mcp.json` | [12](12-claude-code-advanced-guide.md) セクション 5 | 3〜4 日 |
| ヘッドレスモード | `claude -p` でワンショット実行 | [12](12-claude-code-advanced-guide.md) セクション 6 | 1〜2 日 |
| ブランチ戦略 | 分岐・マージ・プルリクエスト | [12](12-claude-code-advanced-guide.md) セクション 7 | 3〜4 日 |
| Docker 入門 | コンテナ・Dockerfile・docker-compose | [22](22-docker-intro-guide.md) | 1〜2 週間 |

### 6-1. 設定ファイルの 3 スコープ

Claude Code の挙動は設定ファイルで制御できる。

| スコープ | ファイルの場所 | 適用範囲 |
|---------|-------------|---------|
| ユーザー設定 | `~/.claude/settings.json` | 全プロジェクト共通 |
| プロジェクト共有設定 | `.claude/settings.json` | チームで共有 |
| プロジェクトローカル設定 | `.claude/settings.local.json` | 個人のみ |

**よく使う設定:**

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test)",
      "Bash(python *)",
      "Bash(git status)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  }
}
```

### 6-2. カスタムコマンド

繰り返し使う指示をテンプレート化する。`.claude/commands/` フォルダに Markdown ファイルとして保存する。

**例: コードレビューコマンド**

`.claude/commands/review.md`:

```markdown
変更されたファイルをレビューして。以下の観点でチェック:

1. バグやエラーの可能性
2. セキュリティの問題
3. パフォーマンスの改善点
4. コードの可読性

問題があれば修正案も提示して。
```

```
# 使い方
/project:review
```

### 6-3. フック

特定のイベントが発生したときに自動でスクリプトを実行する仕組み。

**例: コミット前の自動テスト**

`.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(git commit*)",
        "hooks": [
          {
            "type": "command",
            "command": "npm test"
          }
        ]
      }
    ]
  }
}
```

> 「保存する前に自動で書類をチェックする仕組み」をイメージすると分かりやすい。

### 6-4. MCP（Model Context Protocol）

外部ツールと Claude Code を連携させる仕組み。データベース・API・ファイルシステムなどを直接操作できるようになる。

**MCP の設定例（ファイルシステム）:**

`.mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropic-ai/mcp-server-filesystem",
        "/Users/matsubarakouji/Documents"
      ]
    }
  }
}
```

### 6-5. ヘッドレスモード

対話なしでワンショット実行する。シェルスクリプトとの連携やバッチ処理に使う。

```bash
# 1 つのファイルを整形する
claude -p "src/app.py をリファクタリングして。変数名を明確にして" --allowedTools Edit

# 複数ファイルを一括処理する
for f in src/*.py; do
  claude -p "$f のドキュメントコメントを追加して" --allowedTools Edit
done
```

### 6-6. ブランチ戦略

複数の機能を並行開発するためのブランチの使い方を学ぶ。

```
main（本番）
 ├── feature/login（ログイン機能）
 ├── feature/search（検索機能）
 └── fix/bug-123（バグ修正）
```

```bash
# ブランチの作成と切り替え
git checkout -b feature/login

# 作業完了後、main にマージ
git checkout main
git merge feature/login
```

> Claude Code にブランチ操作を依頼することもできる。
> 例: 「feature/login ブランチを作成して切り替えて」

### Phase 5 の確認ポイント

- [ ] 設定ファイルの 3 スコープを理解し、使い分けられる
- [ ] カスタムコマンドを 3 つ以上作成している
- [ ] フックで自動テストやリントを設定できる
- [ ] MCP で外部ツールと連携できる
- [ ] ヘッドレスモードでバッチ処理を実行できる
- [ ] ブランチを切って並行開発し、マージできる
- [ ] プルリクエストを作成・レビュー・マージできる
- [ ] Docker でアプリをコンテナ化して実行できる

---

## 7. Phase 6 — 公開・運用と実践力（7〜12 ヶ月）

このフェーズのゴール: **アプリを公開し、CI/CD で運用しながら、実践的なポートフォリオを構築する**。

### Phase 6 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| README と文書整備 | プロジェクトの「顔」を整える | [14](14-claude-code-deploy-guide.md) セクション 1 | 1〜2 日 |
| 依存関係管理 | `requirements.txt`・`venv` | [14](14-claude-code-deploy-guide.md) セクション 2 | 1〜2 日 |
| GitHub 公開 | ライセンス・Issue 管理 | [14](14-claude-code-deploy-guide.md) セクション 3 | 1〜2 日 |
| 秘密情報管理 | `.env`・`.env.example`・`.gitignore` | [14](14-claude-code-deploy-guide.md) セクション 4 | 1 日 |
| デプロイ | Streamlit Cloud・GitHub Pages・Render | [14](14-claude-code-deploy-guide.md) セクション 5 | 1〜2 週間 |
| CI/CD | GitHub Actions でテスト自動実行 | [14](14-claude-code-deploy-guide.md) セクション 6 | 1〜2 週間 |
| 保守サイクル | Issue 駆動の開発・バージョニング | [14](14-claude-code-deploy-guide.md) セクション 7 | 継続的 |
| ポートフォリオ構築 | 成果物の整理・GitHub プロフィール | — | 継続的 |
| CLI ツールの活用 | モダンな開発支援ツールの導入 | [03](03-terminal-tools-guide.md) | 1〜2 週間 |

### 7-1. デプロイ（公開）

ローカルで動くアプリを、インターネット上で誰でも使える状態にする。

**デプロイ先の選択:**

| サービス | 適したアプリ | 料金 | 難易度 |
|---------|------------|------|--------|
| GitHub Pages | 静的 Web サイト（HTML/CSS/JS） | 無料 | 低 |
| Streamlit Cloud | Streamlit アプリ | 無料（制限あり） | 低 |
| Vercel | Next.js・React アプリ | 無料（制限あり） | 中 |
| Render | Flask・FastAPI・Node.js | 無料（制限あり） | 中 |
| Cloudflare Pages | 静的サイト・フルスタック | 無料（制限あり） | 中 |

**GitHub Pages での公開手順:**

```
あなた: 「このプロジェクトを GitHub Pages で公開するための手順を教えて。
       必要な設定ファイルも作って」

Claude: GitHub Pages で公開するには...
        1. リポジトリの Settings → Pages
        2. Source を main ブランチに設定
        ...
```

### 7-2. CI/CD（GitHub Actions）

コードを push するたびに自動でテスト・ビルド・デプロイを実行する仕組み。

**基本的な GitHub Actions の設定:**

```
あなた: 「GitHub Actions で pytest を自動実行する設定ファイルを作って。
       push と pull request のたびに実行されるようにして」

Claude: .github/workflows/test.yml を作成します...
```

```yaml
# Claude Code が生成するファイルの例
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
      - run: pip install -r requirements.txt
      - run: pytest -v
```

### 7-3. ポートフォリオの構築

学習の成果を **目に見える形** で示す。転職・就職で最も重視される。

**良いポートフォリオの構成:**

| 要素 | 内容 | 悪い例 → 良い例 |
|------|------|----------------|
| プロジェクト数 | 3〜5 個 | チュートリアルの写経 → 自分で考えた課題を解決 |
| README | 各プロジェクトの説明 | コードだけ → 目的・技術選定理由・スクリーンショット付き |
| 多様性 | 異なる技術を使う | 全部同じ構成 → CLI ツール・Web アプリ・API など多様 |
| コード品質 | 読みやすいコード | 1 ファイルに全部 → 適切なモジュール分割・テスト付き |
| 活動履歴 | コミットの頻度 | まとめてドン → 定期的にコミット |

**おすすめプロジェクト案:**

| プロジェクト | 技術 | アピールできること |
|------------|------|-----------------|
| 個人ブログ（静的サイト） | HTML・CSS・JavaScript・GitHub Pages | Web 基礎・デプロイ |
| タスク管理アプリ | Flask・SQLite・Bootstrap | フルスタック・DB |
| データ可視化ダッシュボード | Streamlit・pandas・Plotly | データ分析・可視化 |
| CLI 自動化ツール | Python・argparse・API 連携 | 自動化・実用性 |
| OSS へのコントリビュート | Git・GitHub | チーム開発・コミュニティ |

### 7-4. モダンな CLI ツールの導入

開発効率を上げるために、[03 - ターミナル CLI ツールガイド](03-terminal-tools-guide.md) からツールを導入する。

**Phase 6 で導入するツール:**

詳細は [03 - ターミナル CLI ツールガイド](03-terminal-tools-guide.md) を参照。

| ツール | 用途 | 標準コマンドとの比較 |
|--------|------|------------------|
| eza | ファイル一覧 | `ls` より見やすい・Git 情報表示 |
| bat | ファイル表示 | `cat` + シンタックスハイライト |
| ripgrep（rg） | テキスト検索 | `grep` より高速 |
| fzf | あいまい検索 | ファイル・履歴の検索が劇的に楽に |
| lazygit | Git 操作 | Git の全操作を TUI で実行 |
| delta | Git 差分表示 | diff がシンタックスハイライト付きに |

### Phase 6 の確認ポイント

- [ ] README を整備し、他の人がプロジェクトを理解・実行できる
- [ ] `.env` で秘密情報を管理し、`.gitignore` で除外できる
- [ ] 1 つ以上のアプリをインターネットに公開した
- [ ] GitHub Actions で自動テストを設定した
- [ ] Issue を作成し、Issue 駆動で開発を進められる
- [ ] GitHub にポートフォリオプロジェクトが 3 つ以上ある
- [ ] モダンな CLI ツールを 5 つ以上導入している

---

## 8. Phase 7 — プロフェッショナル（12 ヶ月〜）

このフェーズのゴール: **スキル・マルチエージェントを使いこなし、大規模プロジェクトをリードできるプロフェッショナルになる**。

### Phase 7 の学習項目

| 項目 | 内容 | 対応ガイド | 学習時間の目安 |
|------|------|-----------|-------------|
| スキル（Skills） | Claude Code の能力を拡張する知識パッケージ | [15](15-claude-code-skills-guide.md) セクション 1〜4 | 2〜3 週間 |
| プラグイン | 配布可能なスキルのパッケージ化 | [15](15-claude-code-skills-guide.md) セクション 6 | 1〜2 週間 |
| Agent Teams | 複数 AI の協調作業 | [16](16-claude-code-multi-agent-guide.md) セクション 1〜4 | 2〜3 週間 |
| Agent SDK | Python / TypeScript からの AI 制御 | [16](16-claude-code-multi-agent-guide.md) セクション 5〜6 | 2〜3 週間 |
| フルスタック開発 | フロントエンド + バックエンド + インフラ | — | 継続的 |
| チーム開発 | コードレビュー・設計・コミュニケーション | — | 実務で習得 |
| アーキテクチャ設計 | 技術選定・スケーラビリティ・保守性 | — | 継続的 |
| 最新技術のキャッチアップ | AI ツール・フレームワーク・ベストプラクティス | [04](04-web-resources-guide.md)・[05](05-sns-guide.md) | 継続的 |

### 8-1. スキル（Skills）

Claude Code に **専門知識** を持たせる仕組み。カスタムコマンドの上位互換。

**スキルの 3 層アーキテクチャ:**

```
第 1 層: メタデータ（YAML フロントマター）
  → いつ・どんな条件で発動するか

第 2 層: 本文（Markdown 本体）
  → 具体的な指示・手順・テンプレート

第 3 層: 補足資料（外部ファイル参照）
  → サンプルコード・設定ファイル・テスト
```

**スキルの作成例:**

`.claude/skills/api-design/SKILL.md`:

```markdown
---
name: API 設計スキル
description: RESTful API の設計ガイドラインに従って API を設計する
triggers:
  - "API を設計"
  - "エンドポイントを追加"
---

# API 設計ガイドライン

## 命名規則
- リソース名は複数形: `/users`、`/articles`
- ケバブケース: `/user-profiles`
- バージョニング: `/api/v1/`

## レスポンス形式
- 成功: `{ "data": {...}, "meta": {...} }`
- エラー: `{ "error": { "code": "...", "message": "..." } }`
```

### 8-2. Agent Teams（マルチエージェント）

複数の Claude Code エージェントが並列で作業する仕組み。大規模タスクを分割して処理する。

**Agent Teams の活用パターン:**

| パターン | 説明 | 使いどころ |
|---------|------|-----------|
| 並行開発 | フロント / バック / テストを同時に進める | 新機能の開発 |
| マルチ観点レビュー | セキュリティ / パフォーマンス / 可読性を同時にチェック | コードレビュー |
| 仮説検証 | 複数のアプローチを同時に試す | 技術選定・最適化 |
| 分割統治 | 大きなリファクタリングを分割 | レガシーコードの改善 |

**Agent Teams の使い方:**

```
あなた: 「このプロジェクトに検索機能を追加して。
       フロントエンド・バックエンド・テストを並行で進めて」

Claude: Agent Teams を起動します。
        - チームメイト 1: フロントエンド（検索 UI）
        - チームメイト 2: バックエンド（検索 API）
        - チームメイト 3: テスト（E2E テスト）
```

### 8-3. Agent SDK

プログラムから Claude Code を制御する。CI/CD パイプラインや自動化ワークフローに組み込める。

**Python での Agent SDK 使用例:**

```python
from claude_code_sdk import query

# 自動コードレビュー
result = query(
    prompt="このプルリクエストの変更をレビューして。"
           "セキュリティ・パフォーマンス・可読性の観点でチェックして。",
    options={
        "allowedTools": ["Read", "Glob", "Grep"],
    }
)
print(result)
```

### 8-4. フルスタック開発

フロントエンドからバックエンド、インフラまで一人でカバーできるスキルを身につける。

**フルスタックの技術マップ:**

```
フロントエンド           バックエンド            インフラ
────────────          ────────────          ────────────
HTML / CSS / JS       Python / Node.js      Docker
React / Next.js       FastAPI / Express      GitHub Actions
TypeScript            PostgreSQL / Redis     Vercel / Render
Tailwind CSS          REST API / GraphQL     AWS / GCP（基礎）
```

**学習の優先順序:**

| 優先度 | 技術 | 理由 |
|--------|------|------|
| 1（必須） | React（または Next.js） | フロントエンドの標準 |
| 1（必須） | FastAPI（または Express） | バックエンドの標準 |
| 2（重要） | TypeScript | 型安全性で品質向上 |
| 2（重要） | Docker | 環境の再現性 |
| 3（応用） | PostgreSQL | 本格的なデータベース |
| 3（応用） | AWS / GCP の基礎 | クラウドインフラ |

### 8-5. プロに求められるスキル

技術力だけではプロフェッショナルになれない。以下のスキルも重要。

| スキル | 内容 | 身につけ方 |
|--------|------|-----------|
| 問題分解力 | 大きな問題を小さなタスクに分割する | 開発フローの実践 |
| 技術選定力 | 要件に最適な技術を選ぶ | 複数のプロジェクト経験 |
| コードレビュー力 | 他者のコードを読んで改善点を指摘する | OSS・チーム開発 |
| コミュニケーション力 | 技術的な内容を非技術者にも伝える | ドキュメント・プレゼン |
| 見積もり力 | 実装の工数を概算する | プロジェクトの振り返り |
| セキュリティ意識 | 脆弱性を意識したコーディング | OWASP Top 10 の学習 |
| 継続的学習力 | 新技術をキャッチアップし続ける | 情報収集ルーティン |

### 8-6. 継続的な情報収集

[04 - おすすめ Web サイトガイド](04-web-resources-guide.md) と [05 - SNS・情報発信ガイド](05-sns-guide.md) を参照し、以下のルーティンを構築する。

**週間の情報収集ルーティン:**

| 頻度 | やること | ソース | 時間 |
|------|---------|--------|------|
| 毎日 | テックニュースをチェック | Hacker News・daily.dev | 15 分 |
| 毎日 | X で開発者のツイートを読む | [05](05-sns-guide.md) セクション 1 | 10 分 |
| 週 1 | 技術ブログを 2〜3 本読む | Zenn・dev.to | 30 分 |
| 週 1 | YouTube で技術動画を 1 本見る | [05](05-sns-guide.md) セクション 2 | 30 分 |
| 月 1 | 新しいツール / フレームワークを試す | GitHub Trending | 2〜3 時間 |
| 月 1 | Discord / Reddit のスレッドを巡回 | [05](05-sns-guide.md) セクション 3・4 | 1 時間 |

### Phase 7 の確認ポイント

- [ ] スキル（Skills）を 3 つ以上作成・運用している
- [ ] Agent Teams で並行開発を実行できる
- [ ] Agent SDK でプログラムから Claude Code を制御できる
- [ ] フロントエンド + バックエンドのアプリを一人で作れる
- [ ] Docker でアプリをコンテナ化できる
- [ ] コードレビューを実施し、改善点を指摘できる
- [ ] 最新の技術トレンドを定期的にキャッチアップしている

---

## 9. 学習リソースマップ

### フェーズ別の推奨リソース

詳細は [04 - おすすめ Web サイトガイド](04-web-resources-guide.md) を参照。

#### Phase 1〜2（環境構築・Claude Code 入門）

| リソース | 種類 | 内容 | 言語 |
|---------|------|------|------|
| 本シリーズ [00](00-vscode-guide.md)・[10](10-claude-code-guide.md) | ガイド | VS Code・Claude Code の基礎 | 日本語 |
| 本シリーズ [01](01-mac-basics-guide.md) | ガイド | Mac の基本操作 | 日本語 |
| Anthropic 公式ドキュメント | Web | Claude Code の公式リファレンス | 英語 |
| Progate | Web | プログラミングの基礎を学ぶ | 日本語 |

#### Phase 3（Git・開発フロー・セキュリティ・テスト）

| リソース | 種類 | 内容 | 言語 |
|---------|------|------|------|
| 本シリーズ [11](11-claude-code-practical-guide.md) | ガイド | Git・GitHub・開発フロー | 日本語 |
| 本シリーズ [20](20-security-basics-guide.md)・[21](21-testing-intro-guide.md) | ガイド | セキュリティ基礎・テスト入門 | 日本語 |
| GitHub Skills | Web | GitHub の公式学習コース | 英語 |
| Learn Git Branching | Web | Git のビジュアル学習ツール | 日本語あり |
| サル先生の Git 入門 | Web | Git の基礎を図解で学ぶ | 日本語 |

#### Phase 4（プログラミング・アプリ開発）

| リソース | 種類 | 内容 | 言語 |
|---------|------|------|------|
| 本シリーズ [26](26-python-setup-guide.md) | ガイド | Python 環境構築 | 日本語 |
| 本シリーズ [13](13-claude-code-app-dev-guide.md) | ガイド | Python・Web・DB・API 開発 | 日本語 |
| 本シリーズ [23](23-web-basics-guide.md)・[24](24-database-intro-guide.md)・[25](25-api-guide.md) | ガイド | Web 開発・DB・API の詳細 | 日本語 |
| 本シリーズ [27](27-data-analysis-guide.md) | ガイド | データ分析入門 | 日本語 |
| Python 公式チュートリアル | Web | Python の公式入門 | 日本語あり |
| freeCodeCamp | Web | Web 開発を実践的に学ぶ | 英語 |
| The Odin Project | Web | フルスタック開発の体系的カリキュラム | 英語 |
| MDN Web Docs | Web | HTML・CSS・JavaScript の公式リファレンス | 日本語あり |

#### Phase 5〜6（応用・公開・運用）

| リソース | 種類 | 内容 | 言語 |
|---------|------|------|------|
| 本シリーズ [12](12-claude-code-advanced-guide.md)・[14](14-claude-code-deploy-guide.md) | ガイド | Claude Code 応用・デプロイ | 日本語 |
| 本シリーズ [22](22-docker-intro-guide.md) | ガイド | Docker 入門 | 日本語 |
| GitHub Actions 公式ドキュメント | Web | CI/CD の設定方法 | 英語 |
| Vercel / Render 公式ドキュメント | Web | デプロイの手順 | 英語 |
| 本シリーズ [03](03-terminal-tools-guide.md) | ガイド | モダン CLI ツール | 日本語 |

#### Phase 7（プロフェッショナル）

| リソース | 種類 | 内容 | 言語 |
|---------|------|------|------|
| 本シリーズ [15](15-claude-code-skills-guide.md)・[16](16-claude-code-multi-agent-guide.md) | ガイド | スキル・マルチエージェント | 日本語 |
| React 公式チュートリアル | Web | React の基礎 | 日本語あり |
| FastAPI 公式チュートリアル | Web | Python Web API の構築 | 英語 |
| Docker 公式 Getting Started | Web | コンテナの基礎 | 英語 |
| 本シリーズ [04](04-web-resources-guide.md)・[05](05-sns-guide.md) | ガイド | Web リソース・SNS 情報収集 | 日本語 |

---

## 10. キャリアパス

### AI 時代の開発者キャリア

AI ツールの進化により、開発者に求められるスキルが変化している。

**従来型 vs AI 時代の開発者:**

| 項目 | 従来型の開発者 | AI 時代の開発者 |
|------|-------------|--------------|
| コードの書き方 | すべて手書き | AI 生成 + レビュー + カスタマイズ |
| 価値の源泉 | コードを書く速度 | 問題を定義し解決策を設計する能力 |
| デバッグ | 経験と勘 | AI による解析 + 人間の判断 |
| 学習速度 | 数年かけて一人前 | AI と協働して短期間で実践力を獲得 |
| 生産性 | 1 人 = 1 人分 | 1 人 + AI = 数人分の生産性 |

### 開発者の職種マップ

| 職種 | 主な業務 | 重点スキル |
|------|---------|-----------|
| フロントエンドエンジニア | Web の UI・UX 実装 | React・TypeScript・CSS |
| バックエンドエンジニア | API・サーバー・DB | Python / Node.js・SQL・設計 |
| フルスタックエンジニア | フロント〜バックエンド全般 | 幅広い技術力・設計力 |
| AI / LLM エンジニア | AI を活用したシステム構築 | LLM・RAG・プロンプト設計 |
| DevOps / SRE | インフラ・CI/CD・監視 | Docker・Kubernetes・AWS |
| モバイルエンジニア | iOS / Android アプリ | Swift / Kotlin・React Native |

### 職種別に必要なスキルレベル

| スキル | フロントエンド | バックエンド | フルスタック | AI エンジニア |
|--------|------------|-----------|-----------|------------|
| HTML / CSS | 高 | 低 | 中 | 低 |
| JavaScript / TypeScript | 高 | 中 | 高 | 中 |
| Python | 低 | 高 | 中 | 高 |
| SQL | 低 | 高 | 中 | 中 |
| React / Next.js | 高 | 低 | 高 | 低 |
| Git / GitHub | 高 | 高 | 高 | 高 |
| Docker | 低 | 高 | 中 | 中 |
| Claude Code 活用力 | 高 | 高 | 高 | 高 |

### 転職・就職の戦略

**未経験からの転職ステップ:**

| ステップ | やること | 期間の目安 |
|---------|---------|-----------|
| 1. 基礎学習 | Phase 1〜4 を完了する | 3〜5 ヶ月 |
| 2. ポートフォリオ | GitHub に 3〜5 プロジェクトを公開 | 1〜2 ヶ月 |
| 3. 公開・運用 | アプリを実際にデプロイする | 1 ヶ月 |
| 4. 発信 | ブログ・Qiita・Zenn で技術記事を書く | 継続的 |
| 5. コミュニティ | 勉強会参加・OSS コントリビュート | 継続的 |
| 6. 応募 | ポートフォリオを添えて応募 | — |

**転職時にアピールできる実績:**

| 実績 | 評価されるポイント |
|------|-----------------|
| GitHub の活動履歴 | 継続的な学習と実践の証明 |
| デプロイ済みアプリ | 「作って公開できる」実行力 |
| 技術ブログ | 思考プロセスと説明能力 |
| OSS コントリビュート | チーム開発・コードリーディング能力 |
| AI ツール活用の実績 | 生産性の高さ・最新技術への適応力 |

---

## 11. 学習を継続するための習慣

### 挫折しやすいポイントと対策

| 挫折ポイント | よくある状況 | 対策 |
|------------|------------|------|
| 環境構築で詰まる | エラーが出て先に進めない | Claude Code に「このエラーを解決して」と依頼する |
| 何を作ればいいかわからない | チュートリアルは終わったが次がない | 日常の不便を解決する小さなツールを作る |
| コードが理解できない | Claude Code が生成したコードが難しい | 「このコードを初心者向けに 1 行ずつ説明して」と依頼 |
| 学習範囲が広すぎる | 何から手をつけていいかわからない | このロードマップに従い、1 フェーズずつ進める |
| 他の人と比較して焦る | SNS で上級者の成果を見て自信を失う | 過去の自分と比較する。1 ヶ月前にできなかったことを確認 |
| モチベーションの低下 | 成長実感がない・飽きる | 小さなプロジェクトを完成させて達成感を得る |
| 最新技術に追われる | 次々と新しいものが出て焦る | 基礎が最重要。最新技術は基礎の上に成り立つ |

### Claude Code を活用した効果的な学習法

| 手法 | やり方 | 効果 |
|------|--------|------|
| ペアプログラミング | Claude Code と対話しながらコードを書く | リアルタイムで疑問を解決 |
| コードリーディング | 「このコードを説明して」と依頼 | 他者のコードを読む力が身につく |
| リファクタリング | 「このコードを改善して。理由も説明して」 | 良いコードの書き方を学ぶ |
| エラー学習 | エラーを Claude Code に解説してもらう | デバッグ力が身につく |
| 設計相談 | 「この機能をどう設計すべきか」と相談 | 設計力が身につく |
| コードレビュー | 「このコードをレビューして」と依頼 | 品質を意識する習慣がつく |

### 効果的な学習習慣

| 習慣 | 内容 | 効果 |
|------|------|------|
| 毎日のコーディング | 30 分でも毎日コードを書く | 知識の定着・習慣化 |
| アウトプット駆動 | 学んだことをブログ・ノートに書く | 理解の深化・ポートフォリオ |
| プロジェクトベース | 「作りたいもの」を起点に学ぶ | 実践力の養成・モチベーション維持 |
| コミュニティ参加 | Discord・勉強会に参加 | モチベーション維持・情報収集 |
| 振り返り | 週 1 で学習の振り返りを書く | 学習方法の改善 |

### 学習時間の確保

| 戦略 | 方法 |
|------|------|
| 朝の時間を使う | 出勤前の 1 時間を学習に充てる |
| 通勤時間 | 技術ブログ・動画で知識をインプット |
| 週末にまとめて | 平日 30 分 + 週末 3〜4 時間 |
| ポモドーロ | 25 分集中 + 5 分休憩のサイクル |
| 学習仲間を作る | 一緒に学ぶことで継続しやすくなる |

---

## 12. まとめ — レベル別チェックリスト

### Phase 1 完了チェック（Mac・環境構築）

- [ ] Mac のキーボードショートカット（Cmd+C/V/Z/S/Tab）が使える
- [ ] Finder でファイルの作成・移動・コピーができる
- [ ] VS Code でフォルダを開き、ファイルを編集・保存できる
- [ ] ターミナルで `pwd`・`ls`・`cd`・`mkdir` が使える
- [ ] パスの概念を理解している
- [ ] Homebrew で Node.js をインストールした

### Phase 2 完了チェック（Claude Code 入門）

- [ ] Claude Code をインストールし、起動・終了ができる
- [ ] 日本語で指示を出し、ファイルを作成・編集できる
- [ ] スラッシュコマンドとパーミッションモードを使える
- [ ] CLAUDE.md を作成し、プロジェクト情報を記述できる
- [ ] 3 つ以上の小さなプロジェクトを作成した
- [ ] Claude Code が生成したコードを読んで大まかな意味が理解できる

### Phase 3 完了チェック（Git・開発フロー）

- [ ] Git の `add`・`commit`・`log`・`diff` が使える
- [ ] GitHub にリポジトリを作成し、`push` できる
- [ ] 「調査 → 計画 → 実装 → 確認 → 記録」のフローで開発できる
- [ ] `/plan` モードで実装計画を立てられる
- [ ] エラーメッセージを Claude Code に貼り付けてデバッグできる
- [ ] API キーをコードに直接書いてはいけないことを理解している

### Phase 4 完了チェック（アプリ開発）

- [ ] pyenv と venv で Python 環境を構築できる
- [ ] Python の基本文法を理解している
- [ ] HTML・CSS・JavaScript の役割の違いを説明できる
- [ ] Streamlit で Web アプリを作れる
- [ ] SQLite でデータの保存・検索ができる
- [ ] API からデータを取得するスクリプトを作れる
- [ ] pytest でテストを書いて実行できる
- [ ] GitHub にプロジェクトを 3 つ以上公開した

### Phase 5 完了チェック（応用・自動化）

- [ ] 設定ファイルの 3 スコープを理解し、使い分けられる
- [ ] カスタムコマンドを 3 つ以上作成している
- [ ] フックで自動テストやリントを設定できる
- [ ] MCP で外部ツールと連携できる
- [ ] ヘッドレスモードでバッチ処理を実行できる
- [ ] ブランチとプルリクエストを活用できる
- [ ] Docker でアプリをコンテナ化して実行できる

### Phase 6 完了チェック（公開・運用）

- [ ] README を整備し、他の人がプロジェクトを理解・実行できる
- [ ] 秘密情報を安全に管理できる
- [ ] 1 つ以上のアプリをインターネットに公開した
- [ ] GitHub Actions で自動テストを設定した
- [ ] Issue 駆動で開発を進められる
- [ ] ポートフォリオプロジェクトが 3 つ以上ある

### Phase 7 完了チェック（プロフェッショナル）

- [ ] スキル（Skills）を 3 つ以上作成・運用している
- [ ] Agent Teams で並行開発を実行できる
- [ ] Agent SDK でプログラムから Claude Code を制御できる
- [ ] フロントエンド + バックエンドのアプリを一人で作れる
- [ ] Docker でアプリをコンテナ化できる
- [ ] コードレビューを実施し、改善点を指摘できる
- [ ] 最新の技術トレンドを定期的にキャッチアップしている

### 本シリーズの参照マップ

| フェーズ | 参照すべきガイド |
|---------|----------------|
| Phase 1 | [00 - VS Code](00-vscode-guide.md)、[01 - Mac 基礎](01-mac-basics-guide.md) |
| Phase 2 | [10 - Claude Code 基本](10-claude-code-guide.md) |
| Phase 3 | [11 - Claude Code 実践](11-claude-code-practical-guide.md)、[20 - セキュリティ](20-security-basics-guide.md)、[21 - テスト](21-testing-intro-guide.md) |
| Phase 4 | [26 - Python 環境](26-python-setup-guide.md)、[13 - アプリ開発](13-claude-code-app-dev-guide.md)、[23 - Web](23-web-basics-guide.md)、[24 - DB](24-database-intro-guide.md)、[25 - API](25-api-guide.md)、[27 - データ分析](27-data-analysis-guide.md) |
| Phase 5 | [12 - 応用・自動化](12-claude-code-advanced-guide.md)、[22 - Docker](22-docker-intro-guide.md) |
| Phase 6 | [14 - 公開・運用](14-claude-code-deploy-guide.md)、[03 - CLI ツール](03-terminal-tools-guide.md) |
| Phase 7 | [15 - スキル](15-claude-code-skills-guide.md)、[16 - マルチエージェント](16-claude-code-multi-agent-guide.md) |
| 全フェーズ | [02 - おすすめアプリ](02-mac-apps-guide.md)、[04 - Web サイト](04-web-resources-guide.md)、[05 - SNS](05-sns-guide.md) |

---

**関連ガイド:**

- [00 - VS Code 基本操作ガイド](00-vscode-guide.md) — VS Code の使い方
- [01 - Mac 基礎操作ガイド](01-mac-basics-guide.md) — Mac の基本操作
- [02 - Mac おすすめアプリガイド](02-mac-apps-guide.md) — 開発・生産性アプリ
- [03 - ターミナル CLI ツールガイド](03-terminal-tools-guide.md) — モダン CLI ツール
- [04 - おすすめ Web サイトガイド](04-web-resources-guide.md) — 学習・AI・開発支援サイト
- [05 - 開発者向け SNS・情報発信ガイド](05-sns-guide.md) — SNS・コミュニティ
- [10 - Claude Code 基本操作ガイド](10-claude-code-guide.md) — ターミナルと Claude Code の基礎
- [11 - Claude Code 実践ガイド](11-claude-code-practical-guide.md) — Git・GitHub・開発フロー
- [12 - Claude Code 応用・自動化ガイド](12-claude-code-advanced-guide.md) — 設定・コマンド・フック・MCP
- [13 - Claude Code アプリケーション開発ガイド](13-claude-code-app-dev-guide.md) — Python・Web・DB・API
- [14 - Claude Code 公開・運用ガイド](14-claude-code-deploy-guide.md) — デプロイ・CI/CD・保守
- [15 - Claude Code スキル・プラグインガイド](15-claude-code-skills-guide.md) — スキル・プラグイン
- [16 - Claude Code マルチエージェントガイド](16-claude-code-multi-agent-guide.md) — 複数 AI の協調・SDK
- [20 - セキュリティ基礎ガイド](20-security-basics-guide.md) — パスワード・API キー・SSH・OWASP
- [21 - テスト入門ガイド](21-testing-intro-guide.md) — pytest・TDD・カバレッジ
- [22 - Docker 入門ガイド](22-docker-intro-guide.md) — コンテナ・Dockerfile・docker-compose
- [23 - Web 開発基礎ガイド](23-web-basics-guide.md) — HTML/CSS/JS・React・Next.js
- [24 - データベース入門ガイド](24-database-intro-guide.md) — SQLite・SQL・PostgreSQL・ORM
- [25 - API 設計・連携ガイド](25-api-guide.md) — REST・FastAPI・Claude API
- [26 - Python 環境構築ガイド](26-python-setup-guide.md) — pyenv・venv・pip・VS Code
- [27 - データ分析入門ガイド](27-data-analysis-guide.md) — pandas・matplotlib・Jupyter
