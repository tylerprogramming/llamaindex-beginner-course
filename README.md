
# LlamaIndex Document Query System

This project demonstrates a simple document querying system using LlamaIndex, a powerful tool for building AI-powered applications with large language models.

## What Will We Build?

- We will build a simple document querying system that allows you to ask questions about a set of documents and get answers.
- We will use a language model to answer questions.
- We will use a vector store index to store and query the documents.
- Create a RAG application (Query Engine)
- Create a simple chatbot (ChatEngine)
- Create the engine code first, then the chatbot loop to talk to the engine
```python
while True:
    text_input = input("User: ")
    if text_input == "exit":
        break
    response = agent.chat(text_input)
    print(f"Agent: {response}")
```
- Observability (Logging, Metrics, Traces) - https://docs.llamaindex.ai/en/stable/module_guides/observability/
- Documents vs. Nodes
- LlamaParse
- LlamaHub
- LlamaCloud (is a waitlist, but promising features)
- NEEDED (copy `.env.example` to `.env` and fill these in):
    - OPENAI_API_KEY
    - PHOENIX_API_KEY (https://llamatrace.com/login)
    - LLAMA_CLOUD_API_KEY for `07 - llama parse.py` (https://cloud.llamaindex.ai)


## Overview

The core lessons (`01 - get it running.py`, `05 - observability.py`, `07 - llama parse.py`) follow the same flow:

1. Loads documents from a PDF directory
2. Creates or loads a vector store index
3. Executes a query on the indexed documents

## Dependencies

- LlamaIndex 0.11 (pinned in `requirements.txt`, the September 2024 versions used in the video)
- OpenAI API (for the underlying language model)

## Setup

`requirements.txt` pins `onnxruntime==1.16.3` (pulled in by chromadb), which only ships wheels for Python 3.8 to 3.11, so use **Python 3.10 or 3.11**:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in the keys listed above
```

On Apple Silicon Macs, `hdbscan==0.8.38.post1` has no arm64 wheel and is built from source during the install, so you need the Xcode command line tools (`xcode-select --install`).

Run the lessons from this folder in order, for example:

```bash
python "01 - get it running.py"
```

`04 - rag pipeline.py` loads its index from a local Chroma database in `chroma_db/`. On the first run that folder is empty, so uncomment the `VectorStoreIndex.from_documents(...)` block once to build it.

## Code Explanation
### Environment Setup

The project uses `pip` to manage dependencies; see Setup above.

### Loading Documents

The lesson scripts use `SimpleDirectoryReader` from LlamaIndex to load the PDF in `pdf/` or the essays in `data/paul_graham/`.

### Creating or Loading a Vector Store Index

`05 - observability.py` creates a new vector store index in `storage/` if it doesn't exist; otherwise it loads the existing index.

### Query Execution

The query engine uses the OpenAI API to answer a query over the indexed documents.

## Usage

Each numbered script is a standalone lesson. Run one with `python "<number> - <name>.py"` from this folder.


