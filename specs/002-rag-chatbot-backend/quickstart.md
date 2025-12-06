# Quickstart for RAG Chatbot Backend

This guide provides instructions for setting up and running the RAG Chatbot Backend.

## Prerequisites

- Python 3.11
- pip (Python package installer)

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    A `requirements.txt` file will be created in the `api/` directory.
    ```bash
    pip install -r api/requirements.txt
    ```

## Running the Service

1.  **Run the FastAPI application:**
    ```bash
    uvicorn api.src.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Ingesting Content

1.  **Run the ingestion script:**
    ```bash
    python api/src/ingest.py
    ```
    This will read the markdown files from `web/docs`, chunk them, and upsert them into the in-memory Qdrant collection.

## API Usage

You can interact with the API via its documentation at `http://127.0.0.1:8000/docs` or by sending requests to the `/ask` endpoint.

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/ask" -H "Content-Type: application/json" -d '{
  "question": "What is Embodied Intelligence?",
  "chapter_id": "01-foundations"
}'
```
