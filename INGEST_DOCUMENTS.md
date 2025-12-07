# Document Ingestion Guide

The RAG chatbot needs the book content to be ingested into Qdrant Cloud before it can answer questions. Follow this guide to populate the vector database.

## Current Status

- **Web App**: https://physical-ai-book-qmkqvu03x-anasmehmood0s-projects.vercel.app  
- **API**: https://api-4xty2hu2q-anasmehmood0s-projects.vercel.app
- **API Status**: Online but vector database is empty

When you try to ask questions now, you'll get: "The vector database is not available. Please check the server configuration and ensure Qdrant Cloud is properly set up."

## Prerequisites

Before running ingestion, make sure you have:

1. **Qdrant Cloud account** with a cluster created
2. **Qdrant Cloud credentials** (URL and API key)
3. **Gemini API key** for generating embeddings
4. **Python 3.8+** installed locally

## Step 1: Set Up Environment Variables

Create a `.env` file in the `api/` directory:

```bash
cd api
cat > .env << 'ENVFILE'
# Qdrant Cloud Configuration
QDRANT_MODE=cloud
QDRANT_URL=https://your-cluster-url.qdrant.io
QDRANT_API_KEY=your-qdrant-api-key
QDRANT_COLLECTION_NAME=book_chunks

# Gemini API Configuration  
GEMINI_API_KEY=your-gemini-api-key

# Optional
DOCS_DIRECTORY=../web/docs
ENVFILE
```

**Important**: Replace the placeholder values with your actual credentials:
- `QDRANT_URL`: Your Qdrant Cloud cluster URL
- `QDRANT_API_KEY`: Your Qdrant Cloud API key  
- `GEMINI_API_KEY`: Your Google Gemini API key

## Step 2: Install Dependencies

Install the required Python packages locally:

```bash
cd api
pip install -r requirements.txt
```

This will install:
- `qdrant-client` - For vector database operations
- `google-generativeai` - For generating embeddings
- `langchain-text-splitters` - For chunking documents
- Other dependencies

## Step 3: Run Document Ingestion

Run the ingestion script:

```bash
python ingest.py
```

**What happens:**
1. Reads all markdown files from `web/docs/` directory
2. Splits them into chunks (500 characters with 100 character overlap)
3. Generates embeddings for each chunk using Gemini  
4. Uploads chunks + embeddings to Qdrant Cloud
5. Creates metadata (chapter ID, source file) for each chunk

**Expected output:**
```
Loading documents from: ../web/docs
Found X markdown files
Ingesting documents into Qdrant...
Successfully ingested X chunks
```

## Step 4: Verify Ingestion

Test if the API can now query the vector database:

```bash
curl -X POST https://api-4xty2hu2q-anasmehmood0s-projects.vercel.app/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is physical AI?"}'
```

You should get a response with:
- `answer`: A conversational answer based on the book content
- `sources`: Relevant chunks from the book with scores

## Troubleshooting

### Error: "QDRANT_URL and QDRANT_API_KEY must be set"
- Make sure your `.env` file exists in the `api/` directory
- Verify the credentials are correct

### Error: "Failed to initialize VectorStore"
- Check your Qdrant Cloud cluster is running
- Verify the URL format is correct (should include https://)
- Test credentials by logging into Qdrant Cloud dashboard

### Error: "GEMINI_API_KEY environment variable not set"
- Add your Gemini API key to `.env` file
- Get a free API key at: https://makersuite.google.com/app/apikey

### Ingestion is slow
- Gemini embedding API has rate limits
- For ~20,000 words across 10 chapters, expect 2-5 minutes
- Progress will be shown in terminal

### Collection already exists
- The script will add documents to existing collection
- To start fresh, delete the collection in Qdrant Cloud dashboard first

## What Gets Ingested?

The ingestion script processes all markdown files in `web/docs/`:

```
web/docs/
├── 01-introduction.md
├── 02-sensors-actuators.md
├── 03-humanoid-locomotion.md
├── 04-computer-vision.md
├── 05-future-ethics.md
├── 06-advanced-control.md
├── 07-manipulation.md
├── 08-learning-methods.md
├── 09-sim-to-real.md
└── 10-case-studies.md
```

Each file is:
1. Split into 500-character chunks
2. Given a chapter ID (extracted from filename)
3. Embedded using Gemini `text-embedding-004` model  
4. Stored in Qdrant with metadata

## Cost Considerations

**Gemini Embeddings (Free Tier)**:
- 1,500 requests per day (free)
- Each chunk = 1 request
- ~100-200 chunks for 10 chapters
- Well within free tier limits

**Qdrant Cloud (Free Tier)**:
- 1GB storage (free)
- Embeddings are 768 dimensions each
- ~100-200 chunks = ~1-2MB
- Well within free tier limits

## Alternative: Using OpenAI Embeddings

If you prefer OpenAI embeddings instead of Gemini:

1. Update `api/embedding_model.py` to use OpenAI API
2. Install `openai` package  
3. Set `OPENAI_API_KEY` in `.env`

This would require modifying the code but can be done if needed.

## After Ingestion

Once documents are ingested:

1. ✅ API will respond to questions with relevant answers
2. ✅ Chatbot widget on website will work
3. ✅ Users can ask about any chapter content
4. ✅ Sources are shown with each answer

The vector database persists in Qdrant Cloud, so you only need to ingest once (or when content changes).

## Re-ingesting After Content Updates

If you update the book content:

1. Make changes to markdown files in `web/docs/`
2. Run `python ingest.py` again
3. Script will add new chunks (duplicates may occur)
4. For clean re-ingest, delete collection in Qdrant Cloud first

## Security Notes

- Never commit `.env` file to git (already in .gitignore)
- Vercel environment variables are set separately in dashboard
- Local `.env` is only for running ingestion locally
- API reads from Vercel environment variables in production
