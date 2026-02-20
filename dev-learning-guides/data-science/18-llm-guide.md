# LLM / 生成 AI 活用ガイド

## 0. はじめに

このガイドは **データサイエンティストが LLM（大規模言語モデル）・生成 AI を業務に活用するための実践ガイドをまとめた自分用リファレンス** です。

- **想定読者**: DS・ML の基礎は理解している。LLM を使った分析・アプリケーション開発を始めたい
- **ゴール**: LLM の主要な活用パターン・API の使い方・RAG・ファインチューニングを理解できるようになる
- **前提**: Python の基礎と ML の概念を理解していること
- **関連ガイド**: [12 - DS 向け Web サイトガイド](12-web-resources-guide.md)、[15 - DS ワークフローガイド](15-workflow-guide.md)

> **このガイドの位置づけ**: LLM の理論的な解説ではなく、**DS が実務で LLM をどう使うか** に焦点を当てた実践ガイド。

### セクション一覧

| セクション | 内容 |
|-----------|------|
| [1. LLM の全体像](#1-llm-の全体像) | 主要モデル・用途・選択基準 |
| [2. API の利用](#2-api-の利用) | Claude API・OpenAI API の基本 |
| [3. プロンプトエンジニアリング](#3-プロンプトエンジニアリング) | 効果的なプロンプトの設計パターン |
| [4. RAG（検索拡張生成）](#4-rag検索拡張生成) | 外部知識を LLM に与える手法 |
| [5. 埋め込み（Embeddings）](#5-埋め込みembeddings) | テキストのベクトル化・類似検索 |
| [6. ファインチューニング](#6-ファインチューニング) | モデルのカスタマイズ |
| [7. DS 実務での活用パターン](#7-ds-実務での活用パターン) | データ分析・前処理・レポート作成での LLM 活用 |
| [8. ツール・フレームワーク](#8-ツールフレームワーク) | LangChain・LlamaIndex・Hugging Face |
| [9. まとめ — LLM 活用のロードマップ](#9-まとめ--llm-活用のロードマップ) | 段階的な学習・導入手順 |

---

## 1. LLM の全体像

### 主要な LLM

| モデル | 提供元 | 特徴 | API 料金 |
|--------|--------|------|---------|
| **Claude** | Anthropic | 長文理解・分析・コード生成に強い | 入力: $3/MTok〜 |
| **GPT-4o** | OpenAI | 汎用性が高い。マルチモーダル対応 | 入力: $2.5/MTok〜 |
| **Gemini** | Google | Google サービスとの統合。長いコンテキスト | 無料枠あり |
| **Llama** | Meta | オープンソース。ローカル実行可能 | 無料（自前インフラ） |
| **Mistral** | Mistral AI | 軽量で高性能。オープンソースモデルあり | 無料枠あり |
| **Command R+** | Cohere | RAG に特化。多言語対応 | 無料枠あり |

### DS における LLM の用途

| 用途 | 説明 | 具体例 |
|------|------|--------|
| **コード生成** | Python・SQL のコード生成・デバッグ | 「pandas で欠損値を補完するコードを書いて」 |
| **データ分析支援** | EDA の自動化・レポート作成 | CSV をアップロードして分析を依頼 |
| **テキスト分析** | 分類・要約・感情分析・情報抽出 | レビューデータの感情分析 |
| **RAG** | 社内ドキュメントを検索して回答 | 社内 Wiki に基づく Q&A システム |
| **構造化データ抽出** | 非構造化テキストから情報を抽出 | 論文から実験結果をテーブルに変換 |

---

## 2. API の利用

### Claude API（Anthropic）

```bash
pip install anthropic
```

```python
import anthropic

client = anthropic.Anthropic()  # ANTHROPIC_API_KEY 環境変数を使用

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "pandas で欠損値を中央値で補完するコードを書いてください。"}
    ]
)
print(message.content[0].text)
```

**システムプロンプトの活用:**

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="あなたはデータサイエンスの専門家です。回答は Python コードと簡潔な説明で返してください。",
    messages=[
        {"role": "user", "content": "時系列データの季節性を検出する方法を教えてください。"}
    ]
)
```

### OpenAI API

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI()  # OPENAI_API_KEY 環境変数を使用

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "あなたはデータサイエンスの専門家です。"},
        {"role": "user", "content": "LightGBM のハイパーパラメータチューニングのベストプラクティスを教えてください。"}
    ]
)
print(response.choices[0].message.content)
```

### API 利用のベストプラクティス

| ポイント | 説明 |
|---------|------|
| API キーは環境変数で管理 | コードに直接書かない。`.env` ファイルを使用 |
| レート制限に対応 | リトライロジックを実装。`tenacity` ライブラリが便利 |
| コストの監視 | トークン数を把握し、不要に長いプロンプトを避ける |
| 温度パラメータ | 分析用は `temperature=0`（決定的）。創造的タスクは `0.7〜1.0` |
| 構造化出力 | JSON モードを使って解析しやすい出力を得る |

---

## 3. プロンプトエンジニアリング

LLM の出力品質はプロンプトの設計で大きく変わる。

### 基本パターン

| パターン | 説明 | 例 |
|---------|------|-----|
| **役割の指定** | LLM に役割を与える | 「あなたはシニアデータサイエンティストです」 |
| **具体的な指示** | 曖昧さを排除する | 「Python の pandas を使って、CSV の欠損値を中央値で補完するコードを書いてください」 |
| **出力形式の指定** | 期待する出力を明示 | 「結果を Markdown のテーブルで出力してください」 |
| **Few-shot** | 例を示す | 入力例 → 出力例を数組提示 |
| **Chain-of-Thought** | 段階的に考えさせる | 「ステップバイステップで考えてください」 |

### DS 向けプロンプト例

**データ分析:**

```
以下の CSV データの概要を分析してください。

データ:
{CSVデータの先頭行}

以下の観点で分析してください:
1. 各列のデータ型と欠損率
2. 数値列の基本統計量
3. 注目すべきパターンや異常値
4. 推奨する前処理ステップ

結果は Markdown のテーブル形式で出力してください。
```

**コード生成:**

```
以下の要件を満たす Python 関数を書いてください。

要件:
- pandas DataFrame を入力として受け取る
- 数値列の欠損値を中央値で、カテゴリ列の欠損値を最頻値で補完する
- 補完前後の欠損率をログ出力する
- 型アノテーション付き

制約:
- scikit-learn の SimpleImputer を使用
- 関数名は impute_missing_values
```

**構造化データ抽出:**

```
以下の論文のアブストラクトから情報を抽出し、JSON 形式で出力してください。

アブストラクト:
{論文のアブストラクト}

出力する JSON のスキーマ:
{
  "task": "タスクの種類",
  "method": "提案手法",
  "dataset": "使用データセット",
  "metric": "評価指標",
  "score": "達成スコア",
  "baseline_comparison": "ベースラインとの比較"
}
```

---

## 4. RAG（検索拡張生成）

LLM の知識を外部データで拡張する手法。社内ドキュメントや最新情報に基づく回答を生成。

### RAG の基本フロー

```
1. ドキュメントをチャンクに分割
2. 各チャンクを埋め込みベクトルに変換
3. ベクトルデータベースに保存
4. ユーザーの質問を埋め込みベクトルに変換
5. 類似するチャンクを検索（類似度検索）
6. 検索結果をコンテキストとして LLM に渡す
7. LLM がコンテキストに基づいて回答を生成
```

### シンプルな RAG の実装

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# 1. ドキュメントの読み込み
loader = PyPDFLoader("data/documents/report.pdf")
documents = loader.load()

# 2. チャンクに分割
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# 3. ベクトルデータベースに保存
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 4. RAG チェーンの構築
llm = ChatOpenAI(model="gpt-4o", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
)

# 5. 質問
answer = qa_chain.invoke("このレポートの主な発見は何ですか？")
print(answer["result"])
```

### RAG の改善ポイント

| 改善項目 | 手法 |
|---------|------|
| チャンク戦略 | チャンクサイズの調整・セマンティック分割 |
| 検索精度 | ハイブリッド検索（ベクトル + キーワード） |
| リランキング | 検索結果を LLM で再ランキング |
| メタデータ | ドキュメントのメタデータ（日付・カテゴリ）でフィルタ |

---

## 5. 埋め込み（Embeddings）

テキストを数値ベクトルに変換し、類似度計算・検索・クラスタリングに活用。

### 埋め込みの活用パターン

| 用途 | 説明 |
|------|------|
| **類似検索** | クエリに類似するドキュメントを検索 |
| **クラスタリング** | テキストをベクトル化し、k-means 等でクラスタリング |
| **分類** | 埋め込みベクトルを特徴量として分類モデルに入力 |
| **異常検出** | 通常のテキストから離れたベクトルを異常として検出 |
| **可視化** | t-SNE / UMAP でベクトルを 2D に投影して可視化 |

### 埋め込みの取得

```python
# OpenAI Embeddings
from openai import OpenAI

client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=["データサイエンスとは", "機械学習の基礎"]
)
embeddings = [item.embedding for item in response.data]
```

```python
# Hugging Face（ローカル実行）
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = ["データサイエンスとは", "機械学習の基礎", "今日の天気"]
embeddings = model.encode(texts)

# 類似度の計算
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(embeddings)
```

### 埋め込みの可視化

```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# t-SNE で 2D に次元削減
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

plt.figure(figsize=(10, 8))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
for i, text in enumerate(texts):
    plt.annotate(text[:20], (embeddings_2d[i, 0], embeddings_2d[i, 1]))
plt.title("Text Embeddings Visualization")
plt.savefig("reports/figures/embeddings.png")
```

---

## 6. ファインチューニング

既存の LLM を特定のタスク・ドメインに適応させる。

### ファインチューニングの種類

| 種類 | 説明 | コスト | 用途 |
|------|------|--------|------|
| **Full Fine-tuning** | 全パラメータを更新 | 高い（大量 GPU） | 大規模なドメイン適応 |
| **LoRA / QLoRA** | 低ランクの追加パラメータのみ更新 | 低い（1 GPU で可能） | タスク特化・効率的な適応 |
| **プロンプトチューニング** | プロンプト部分のベクトルのみ学習 | 最も低い | 軽量な適応 |

### LoRA によるファインチューニング

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

# モデルとトークナイザーの読み込み
model_name = "meta-llama/Llama-2-7b-hf"
model = AutoModelForCausalLM.from_pretrained(model_name, load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# LoRA の設定
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)

# 学習
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        learning_rate=2e-4,
    ),
)
trainer.train()
```

### いつファインチューニングするか

| 状況 | 推奨アプローチ |
|------|-------------|
| 一般的な質問応答 | プロンプトエンジニアリング（ファインチューニング不要） |
| 特定のドメイン知識が必要 | RAG（外部データを検索して提供） |
| 特定の出力形式・スタイルが必要 | Few-shot プロンプト or ファインチューニング |
| 大量の特定タスクを高速処理 | ファインチューニング（小さいモデルに知識を蒸留） |

---

## 7. DS 実務での活用パターン

### データ分析の自動化

```python
import anthropic
import pandas as pd

client = anthropic.Anthropic()

df = pd.read_csv("data/raw/sales.csv")
data_summary = df.describe().to_string()
sample = df.head(5).to_string()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system="あなたはシニアデータサイエンティストです。データ分析の結果を日本語で簡潔にレポートしてください。",
    messages=[{
        "role": "user",
        "content": f"""以下の販売データを分析し、主要な洞察を 5 つ挙げてください。

データの概要:
{data_summary}

サンプルデータ:
{sample}

分析の観点:
1. 売上のトレンド
2. カテゴリ別の特徴
3. 異常値や注目すべきパターン
4. ビジネスへの示唆
5. 追加で分析すべき点"""
    }]
)
print(message.content[0].text)
```

### テキスト分類（LLM ベース）

```python
def classify_review(text: str) -> dict:
    """レビューテキストを LLM で分類する。"""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[{
            "role": "user",
            "content": f"""以下のレビューを分析し、JSON 形式で出力してください。

レビュー: {text}

出力形式:
{{"sentiment": "positive/negative/neutral", "category": "品質/価格/サービス/配送/その他", "confidence": 0.0-1.0}}"""
        }]
    )
    return message.content[0].text
```

### 構造化データの生成

```python
def extract_entities(text: str) -> dict:
    """テキストから構造化データを抽出する。"""
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"""以下のテキストから情報を抽出し、JSON で出力してください。

テキスト: {text}

抽出する情報:
- 人名
- 組織名
- 日付
- 金額
- 場所"""
        }]
    )
    return message.content[0].text
```

---

## 8. ツール・フレームワーク

### LLM アプリケーションのツール一覧

| ツール | URL | 用途 | 料金 |
|--------|-----|------|------|
| **LangChain** | https://www.langchain.com | LLM アプリケーションの構築フレームワーク | 無料（OSS） |
| **LlamaIndex** | https://www.llamaindex.ai | RAG に特化したフレームワーク | 無料（OSS） |
| **Hugging Face Transformers** | https://huggingface.co/docs/transformers | モデルの利用・ファインチューニング | 無料（OSS） |
| **vLLM** | https://github.com/vllm-project/vllm | 高速な LLM 推論エンジン | 無料（OSS） |
| **Ollama** | https://ollama.com | ローカルで LLM を実行 | 無料 |
| **ChromaDB** | https://www.trychroma.com | 埋め込みベクトルのデータベース | 無料（OSS） |
| **FAISS** | https://github.com/facebookresearch/faiss | Meta 製の高速ベクトル検索 | 無料（OSS） |
| **Gradio** | https://gradio.app | ML デモアプリを数行で作成 | 無料（OSS） |

### Ollama — ローカルで LLM を実行

```bash
# Ollama のインストール
brew install ollama

# モデルのダウンロード・実行
ollama pull llama3.1
ollama run llama3.1 "pandas で欠損値を処理するコードを書いて"

# Python から利用
pip install ollama
```

```python
import ollama

response = ollama.chat(
    model="llama3.1",
    messages=[{"role": "user", "content": "LightGBM の特徴量重要度を計算するコードを書いて"}]
)
print(response["message"]["content"])
```

### Gradio — ML デモアプリ

```python
import gradio as gr

def predict_sentiment(text):
    # LLM or ML モデルで予測
    return classify_review(text)

demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label="レビューテキスト"),
    outputs=gr.JSON(label="分析結果"),
    title="レビュー感情分析",
)
demo.launch()
```

---

## 9. まとめ — LLM 活用のロードマップ

### 段階的な学習・導入手順

| 段階 | 内容 | 期間目安 |
|------|------|---------|
| 1. API の基本 | Claude / OpenAI API を Python から呼び出す | 1 日 |
| 2. プロンプト設計 | 効果的なプロンプトのパターンを学ぶ | 1 週間 |
| 3. DS 実務での活用 | データ分析・テキスト分類・コード生成に LLM を活用 | 2 週間 |
| 4. RAG の構築 | 社内ドキュメントを検索・回答するシステムの構築 | 2 週間 |
| 5. 埋め込みの活用 | テキストの類似検索・クラスタリング | 1 週間 |
| 6. ファインチューニング | 特定タスク向けにモデルをカスタマイズ | 2〜4 週間 |

### LLM 活用の判断フローチャート

| 状況 | 推奨アプローチ |
|------|-------------|
| API で十分な精度が出る | そのまま API を使う |
| 特定のドメイン知識が必要 | RAG を構築 |
| 出力形式のカスタマイズが必要 | プロンプトエンジニアリング or Few-shot |
| コストを下げたい | 小さいモデル + ファインチューニング |
| オフラインで使いたい | Ollama でローカル実行 |
| 大量のテキストを処理 | 埋め込み + 類似検索 |

---

**関連ガイド:**

- [12 - DS 向け Web サイトガイド](12-web-resources-guide.md) — Hugging Face・ML プラットフォーム
- [15 - DS ワークフローガイド](15-workflow-guide.md) — DS のワークフロー全体像
- [11 - DS 向けターミナル CLI ツールガイド](11-terminal-tools-guide.md) — ML 実験管理ツール
