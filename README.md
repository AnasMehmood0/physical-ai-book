# Physical AI Book RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot for the Physical AI Book Docusaurus site. The system allows users to ask questions about the book content and get accurate responses based on the source material.

## Architecture

- **Frontend**: Docusaurus site with React chat widget
- **Backend**: FastAPI server
- **Vector Database**: Qdrant Cloud (for document embeddings)
- **SQL Database**: Neon Serverless Postgres (for metadata)
- **LLM**: Google Gemini API

## Features

1. **Context-Aware Chat**: Answers based on book content
2. **Text Selection**: Ask questions about specific selected text
3. **Source Attribution**: Shows which documents were used
4. **Conversation History**: Maintains context across interactions

## Setup Instructions

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd physical-ai-book/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. Start the backend server:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

### 2. Ingest Documentation

Before using the chatbot, you need to ingest the Docusaurus documentation:

1. Make sure your backend server is running
2. Send a request to the ingestion endpoint:
   ```bash
   curl -X POST http://localhost:8000/api/documents/ingest \
     -H "Content-Type: application/json" \
     -d '{"source_path": "../web/docs", "chunk_size": 1000, "chunk_overlap": 200}'
   ```

### 3. Frontend Setup

1. Navigate to the web directory:
   ```bash
   cd physical-ai-book/web
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Docusaurus development server:
   ```bash
   npm start
   ```

### 4. Configuration

#### Environment Variables

You need to configure the following environment variables in `backend/.env`:

- `QDRANT_HOST`: Your Qdrant Cloud cluster URL
- `QDRANT_PORT`: Qdrant port (default 6333)
- `QDRANT_API_KEY`: Your Qdrant API key
- `QDRANT_COLLECTION_NAME`: Collection name (default physical_ai_book)
- `NEON_DATABASE_URL`: Your Neon Postgres connection string
- `GEMINI_API_KEY`: Your Google Gemini API key
- `GEMINI_MODEL`: Model to use (default gemini-2.5-flash)
- `EMBEDDING_MODEL`: Embedding model (default all-MiniLM-L6-v2)

## Usage

1. The chat widget appears as a 💬 icon in the bottom-right corner of the page
2. Click it to open the chat interface
3. Ask questions about the Physical AI Book content
4. Optionally select text on the page and ask questions about that specific content
5. The chatbot will respond with answers based on the book content and provide source citations

## API Endpoints

- `GET /` - Health check
- `GET /health` - Health check
- `POST /api/chat` - Main chat endpoint
- `POST /api/chat/context` - Context-aware chat endpoint
- `POST /api/documents/ingest` - Document ingestion endpoint
- `GET /api/documents/status` - Document status endpoint

## Testing

To test the system, you can use the API endpoints directly:

```bash
# Test regular chat
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Physical AI?", "conversation_id": "test123"}'

# Test context-aware chat
curl -X POST http://localhost:8000/api/chat/context \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain this concept", "selected_context": "Physical AI is AI systems that interact with the physical world through embodied agents", "conversation_id": "test123"}'
```

## Troubleshooting

1. **Backend not starting**: Ensure all environment variables are set correctly
2. **Qdrant connection errors**: Verify your Qdrant Cloud credentials and network connectivity
3. **No responses from chatbot**: Ensure documentation has been ingested into the system
4. **API errors**: Check backend logs for detailed error messages

## Development

To extend the system:

1. Add new API endpoints in `backend/app/routes/`
2. Create new services in `backend/app/services/`
3. Add new frontend components in `web/src/components/`
4. Modify the layout wrapper in `web/src/theme/Layout/`