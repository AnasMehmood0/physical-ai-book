# Starting the RAG Chatbot System

This guide shows you how to start both the backend API and frontend website for the RAG chatbot.

## Prerequisites

Make sure you have:
- Python 3.8+ installed
- Node.js 16+ installed
- Dependencies installed for both backend and frontend

## Quick Start

### Step 1: Start the Backend API

Open a terminal and run:

```bash
cd api
python -m pip install -r requirements.txt
cd ..
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Test the API at: http://localhost:8000

### Step 2: Start the Frontend (Docusaurus)

Open a **new** terminal and run:

```bash
cd web
npm install
npm start
```

You should see:
```
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

### Step 3: Test the Chatbot

1. Open http://localhost:3000 in your browser
2. Look for the chat widget button (💬) in the bottom-right corner
3. Click it to open the chat
4. Ask a question like "What is physical AI?"

## Configuration

### Backend Configuration (.env in root)

```env
QDRANT_MODE=local
QDRANT_PATH=./qdrant_storage
QDRANT_COLLECTION_NAME=book_chunks
EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
DOCS_DIRECTORY=web/docs
CHUNK_SIZE=256
CHUNK_OVERLAP=32
API_HOST=0.0.0.0
API_PORT=8000
CORS_ORIGINS=*
```

### Frontend Configuration (web/.env)

```env
REACT_APP_API_URL=http://localhost:8000
```

## Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Use a different port
uvicorn api.main:app --reload --port 8001
# Update web/.env with: REACT_APP_API_URL=http://localhost:8001
```

**Module not found errors:**
```bash
# Install dependencies
cd api
pip install -r requirements.txt
```

**Qdrant storage errors:**
```bash
# Delete and recreate storage
rm -rf qdrant_storage
# Restart the API - it will recreate the collection
```

### Frontend Issues

**Port 3000 already in use:**
```bash
# Docusaurus will automatically try port 3001, 3002, etc.
```

**API connection failed:**
1. Check backend is running: http://localhost:8000
2. Verify CORS is enabled in backend
3. Check browser console for specific errors
4. Verify REACT_APP_API_URL in web/.env

**Chat widget not appearing:**
1. Clear Docusaurus cache: `cd web && npm run clear`
2. Rebuild: `npm start`
3. Check browser console for errors

## Architecture Overview

```
┌─────────────────┐         ┌──────────────────┐
│                 │         │                  │
│  Docusaurus     │ ──────> │  FastAPI         │
│  Frontend       │  HTTP   │  Backend         │
│  (Port 3000)    │ <────── │  (Port 8000)     │
│                 │         │                  │
└─────────────────┘         └────────┬─────────┘
                                     │
                                     ▼
                           ┌──────────────────┐
                           │                  │
                           │  Qdrant          │
                           │  Vector DB       │
                           │  (Local Storage) │
                           │                  │
                           └──────────────────┘
```

## Development Workflow

1. **Make backend changes:**
   - Edit files in `api/`
   - FastAPI will auto-reload (with `--reload` flag)

2. **Make frontend changes:**
   - Edit files in `web/src/`
   - Docusaurus will hot-reload automatically

3. **Update environment variables:**
   - Backend: Edit `.env` in root, restart API
   - Frontend: Edit `web/.env`, restart Docusaurus

## Production Deployment

### Backend

```bash
# Install production dependencies
cd api
pip install -r requirements.txt gunicorn

# Run with gunicorn
gunicorn api.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
# Build static files
cd web
npm run build

# Serve with any static file server
npm run serve
# or use nginx, Apache, etc.
```

## Testing the System

### Test Backend

```bash
# Health check
curl http://localhost:8000/

# Test query
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is physical AI?"}'
```

### Test Frontend

1. Open http://localhost:3000
2. Open browser DevTools (F12)
3. Check Console for errors
4. Check Network tab when using chat

## Stopping the System

1. Press `CTRL+C` in the backend terminal
2. Press `CTRL+C` in the frontend terminal

## Next Steps

- Read `api/README.md` for backend details
- Read `web/CHATBOT_README.md` for frontend details
- Customize the chatbot UI in `web/src/components/GlobalChatWidget.tsx`
- Add more documents to `web/docs` for the chatbot to search
