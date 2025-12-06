# Implementation Plan: RAG Chatbot Backend (V2 Stable)

**Branch**: `003-rag-chatbot-backend` | **Date**: 2025-12-06 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-rag-chatbot-backend/spec.md`

## Summary
This plan outlines the implementation of a RAG (Retrieval-Augmented Generation) chatbot backend. The backend will be a Python FastAPI application that provides an API for answering questions based on the content of a book. It will use a vector database to store and retrieve relevant text chunks. The implementation will prioritize stability by using a synchronous client for database interactions.

## Technical Context
**Language/Version**: Python 3.11
**Primary Dependencies**:
- fastapi
- uvicorn
- qdrant-client
- sentence-transformers
- langchain (for text splitting)
**Storage**: Qdrant (in-memory/local mode)
**Testing**: pytest
**Target Platform**: Linux server (or any OS that can run Python)
**Project Type**: Web application (backend only)
**Performance Goals**:
- `/ask` endpoint response time < 2 seconds (p95)
- Ingestion of a large book in under 10 minutes
**Constraints**:
- Must use the synchronous `qdrant_client.QdrantClient`.
- `async def` and `await` must not be used for search methods.
**Scale/Scope**:
- The service will handle one book's content.
- The API will be exposed to a front-end application.

## Constitution Check
*This section to be filled based on `.specify/memory/constitution.md`.*

## Project Structure

### Documentation (this feature)
```text
specs/003-rag-chatbot-backend/
├── plan.md              # This file
├── research.md          # Not yet created
├── data-model.md        # Not yet created
├── quickstart.md        # Not yet created
├── contracts/           # Not yet created
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)
```text
api/
├── __init__.py
├── main.py              # FastAPI application, /ask endpoint
├── ingest.py            # Ingestion script
├── vector_store.py      # Abstraction for Qdrant client
├── embedding_model.py   # Wrapper for SentenceTransformers
├── requirements.txt     # Python dependencies
└── tests/
    ├── __init__.py
    ├── test_main.py
    └── test_ingest.py
```
**Structure Decision**: A single `api` directory will be created at the root of the repository to contain all the backend code. This matches the user's request and is a simple structure for a single service.
