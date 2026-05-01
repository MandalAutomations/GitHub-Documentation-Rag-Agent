# GitHub Documentation Agent

A Retrieval-Augmented Generation (RAG) system that answers questions about GitHub's official documentation using local Ollama LLMs and a PostgreSQL pgvector database.

## Overview

This project creates a question-answering system that:
- Fetches and processes GitHub's official documentation
- Generates embeddings for document chunks using local Ollama models
- Stores embeddings in a PostgreSQL vector database
- Returns contextually relevant answers to GitHub-related questions

## Architecture

### Core components

- **`src/llama.py`** — Interface for Ollama LLM operations (text generation and embeddings).
- **`src/postgres_db.py`** — PostgreSQL vector database operations using pgvector.
- **`load.ipynb`** — Data loading pipeline that fetches and processes GitHub docs.
- **`main.ipynb`** — Query interface for asking questions and getting answers.

### Docker services

The project uses Docker Compose with the following services:
- **Ollama** — Local LLM server for text generation and embeddings.
- **PostgreSQL with pgvector** — Vector database for similarity search.

## Getting started

This project is designed to run in a **VS Code Dev Container** with all dependencies and services pre-configured.

### Prerequisites

- Docker and Docker Compose
- VS Code with the Dev Containers extension
- Git

### Option 1: Dev Container (recommended)

1. Clone the repository:

   ```bash
   git clone https://github.com/MandalAutomations/GitHub-Documentation-Rag-Agent.git
   cd GitHub-Documentation-Rag-Agent
   ```

2. Open in VS Code:

   ```bash
   code .
   ```

3. Reopen in the container — VS Code will prompt automatically, or use the Command Palette: `Dev Containers: Reopen in Container`.

The dev container will automatically:
- Start all required services (Ollama, PostgreSQL with pgvector).
- Install Python dependencies.
- Configure the development environment.
- Open `main.ipynb` for immediate use.

### Option 2: Manual setup

1. Clone and navigate to the repository:

   ```bash
   git clone https://github.com/MandalAutomations/GitHub-Documentation-Rag-Agent.git
   cd GitHub-Documentation-Rag-Agent
   ```

2. Start the services:

   ```bash
   docker-compose -f .devcontainer/docker-compose.yml up -d ollama db
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Note: you'll need to adjust the host configurations in the notebooks to connect to the services.

## Usage

### 1. Load GitHub documentation

Run the `load.ipynb` notebook to:
- Clone the GitHub docs repository
- Fetch documentation content via GitHub's API
- Chunk documents
- Generate embeddings and store them in the vector database

Key configuration:
- **Embedding model**: `granite-embedding:30m` (384 dimensions)
- **Chunk size**: 5000 characters with 100-character overlap

### 2. Ask questions

Use `main.ipynb` to:
- Submit questions about GitHub features
- Retrieve relevant documentation chunks
- Generate contextual answers using the LLM

Example query:

```python
prompt = "How much do GitHub Actions cost for Linux runners?"
```

## Configuration

### Environment variables

- `OLLAMA_HOST` — Ollama server URL (default: `http://ollama:11434`).
- `POSTGRES_HOST` — PostgreSQL server host (default: `vector-postgres`).

### Models

- **Text generation**: `llama3.2:1b`
- **Embeddings**: `granite-embedding:30m`

Find more models at the [Ollama Library](https://ollama.com/library).

## Project structure

```
.
├── README.md
├── requirements.txt
├── main.ipynb              # Query interface
├── load.ipynb              # Data loading pipeline
├── AVAILABLE_MODELS.md     # Model documentation
├── main.py                 # Script entrypoint
├── src/
│   ├── llama.py            # Ollama LLM interface
│   └── postgres_db.py      # Vector database operations
└── .devcontainer/          # Dev Container + Docker Compose configs
```

## How it works

### Document processing pipeline
1. Clone the GitHub docs repository.
2. Extract Markdown files.
3. Fetch rendered content via the API.
4. Split into 5000-character chunks.
5. Generate 384-dimensional embeddings.
6. Store in PostgreSQL with pgvector.

### Query processing pipeline
1. Generate an embedding for the user question.
2. Search for the top-k similar document chunks.
3. Combine the retrieved context.
4. Generate a response using the LLM with that context.

## Performance considerations

- **Rate limiting**: API requests are throttled to avoid GitHub rate limits.
- **Batch processing**: Documents are processed in batches with progress tracking.
- **Memory efficiency**: Large documents are chunked to fit model context windows.

## Troubleshooting

1. **Ollama connection** — Ensure the Ollama service is running and accessible.
2. **Model downloads** — First-time model usage requires downloading (may take time).
3. **PostgreSQL** — Verify the pgvector extension is installed and enabled.
4. **API rate limits** — GitHub's API has rate limits; increase delays if needed.
