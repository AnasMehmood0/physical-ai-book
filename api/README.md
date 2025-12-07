# RAG Chatbot API

A FastAPI-based Retrieval-Augmented Generation (RAG) chatbot backend for querying book content using vector embeddings and Qdrant.

## Features

- FastAPI REST API with async support
- Vector-based document search using Qdrant
- Sentence embeddings with SentenceTransformers
- Document chunking and ingestion from Markdown/text files
- Environment-based configuration
- Support for both local and cloud Qdrant instances
- Chapter-specific filtering

## Setup

### 1. Install Dependencies

```bash
cd api
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file and configure it:

```bash
cp ../.env.example ../.env
```

Edit `.env` with your configuration:

```env
# Qdrant Configuration
QDRANT_MODE=local                    # 'local' or 'cloud'
QDRANT_PATH=./qdrant_storage         # Path for local storage
QDRANT_COLLECTION_NAME=book_chunks   # Collection name

# For cloud mode, uncomment and set:
# QDRANT_API_KEY=your_api_key
# QDRANT_URL=https://your-instance.cloud.qdrant.io

# Embedding Model
EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2

# Document Ingestion
DOCS_DIRECTORY=web/docs
CHUNK_SIZE=256
CHUNK_OVERLAP=32

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=*
```

### 3. Test Configuration

Run the configuration test to verify everything is set up correctly:

```bash
python test_env_config.py
```

## Running the API

### Development Mode

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Or from the project root:

```bash
cd ..
uvicorn api.main:app --reload
```

### Production Mode

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Endpoints

### GET /

Health check endpoint.

**Response:**
```json
{
  "message": "Hello RAG Chatbot!"
}
```

### POST /ask

Query the chatbot with a question.

**Request Body:**
```json
{
  "question": "What is physical AI?",
  "chapter_id": "01-introduction"  // Optional: filter by chapter
}
```

**Response:**
```json
{
  "results": [
    {
      "payload": {
        "chapter_id": "01-introduction",
        "source": "01-introduction.md"
      },
      "score": 0.85
    }
  ]
}
```

## Document Ingestion

### Automatic Ingestion

Documents are automatically ingested from the `DOCS_DIRECTORY` when the API starts.

### Manual Ingestion

To manually ingest documents:

```bash
python -m api.ingest <directory_path>
```

Example:
```bash
python -m api.ingest ../web/docs
```

## Configuration Options

### Qdrant Modes

**Local Mode** (default):
- Uses file-based storage
- No external dependencies
- Set `QDRANT_MODE=local`
- Configure `QDRANT_PATH`

**Cloud Mode**:
- Uses Qdrant Cloud service
- Set `QDRANT_MODE=cloud`
- Configure `QDRANT_URL` and `QDRANT_API_KEY`

### Embedding Models

You can use any model from [sentence-transformers](https://www.sbert.net/docs/pretrained_models.html):

- `all-MiniLM-L6-v2` (default) - Fast, lightweight (384 dimensions)
- `all-mpnet-base-v2` - Higher quality (768 dimensions)
- `paraphrase-multilingual-MiniLM-L12-v2` - Multilingual support

Set via `EMBEDDING_MODEL_NAME` in `.env`

### Chunking Configuration

Adjust text chunking parameters:

- `CHUNK_SIZE`: Maximum characters per chunk (default: 256)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 32)

## Project Structure

```
api/
├── __init__.py
├── main.py              # FastAPI application
├── vector_store.py      # Qdrant vector store wrapper
├── embedding_model.py   # Sentence transformer wrapper
├── ingest.py           # Document ingestion logic
├── test_env_config.py  # Configuration test script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── tests/
    ├── __init__.py
    ├── test_main.py
    └── test_ingest.py
```

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `QDRANT_MODE` | No | `local` | Operation mode: `local` or `cloud` |
| `QDRANT_PATH` | No | `./qdrant_storage` | Path for local Qdrant storage |
| `QDRANT_URL` | Cloud only | - | Qdrant Cloud instance URL |
| `QDRANT_API_KEY` | Cloud only | - | Qdrant Cloud API key |
| `QDRANT_COLLECTION_NAME` | No | `book_chunks` | Qdrant collection name |
| `EMBEDDING_MODEL_NAME` | No | `all-MiniLM-L6-v2` | Sentence transformer model |
| `DOCS_DIRECTORY` | No | `web/docs` | Directory containing documents |
| `CHUNK_SIZE` | No | `256` | Maximum characters per chunk |
| `CHUNK_OVERLAP` | No | `32` | Overlap between chunks |
| `API_HOST` | No | `0.0.0.0` | API server host |
| `API_PORT` | No | `8000` | API server port |
| `CORS_ORIGINS` | No | `*` | CORS allowed origins |

## Testing

Run tests:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_main.py
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure you're running from the project root:

```bash
cd /path/to/physical-ai-book
python -m api.main
```

### Qdrant Connection Issues

**Local Mode:**
- Ensure `QDRANT_PATH` directory is writable
- Check disk space

**Cloud Mode:**
- Verify `QDRANT_URL` and `QDRANT_API_KEY` are correct
- Check network connectivity

### Model Download Issues

First run will download the embedding model. Ensure:
- Internet connection is available
- Sufficient disk space (~100MB for default model)
- No firewall blocking huggingface.co

## Security Notes

- Never commit `.env` file to version control
- Keep API keys secure
- Use environment-specific `.env` files for different deployments
- Consider using secrets management for production

## License

[Add your license information here]
