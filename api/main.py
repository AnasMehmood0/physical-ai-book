from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import contextlib
import logging
import os
from dotenv import load_dotenv

# Use relative imports that work better on Vercel
try:
    from vector_store import VectorStore
    from ingest import ingest_documents
    from llm_service import LLMService
except ImportError:
    from api.vector_store import VectorStore
    from api.ingest import ingest_documents
    from api.llm_service import LLMService

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize VectorStore with error handling
    try:
        vector_store = VectorStore()
        app.state.vector_store = vector_store
        logger.info("VectorStore initialized successfully")

        # Only ingest documents on startup in local mode
        # For cloud mode, documents should be ingested separately
        qdrant_mode = os.getenv("QDRANT_MODE", "local")
        if qdrant_mode == "local":
            docs_dir = os.getenv("DOCS_DIRECTORY", "web/docs")
            if os.path.exists(docs_dir):
                ingest_documents(docs_dir, vector_store)
    except Exception as e:
        logger.error(f"Failed to initialize VectorStore: {e}")
        app.state.vector_store = None

    # Initialize LLM service
    try:
        llm_service = LLMService()
        app.state.llm_service = llm_service
        logger.info("LLM service initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize LLM service: {e}")
        app.state.llm_service = None

    yield

    # Clean up
    if hasattr(app.state, 'vector_store') and app.state.vector_store:
        try:
            app.state.vector_store.client.close()
            logger.info("Qdrant client closed")
        except Exception as e:
            logger.error(f"Error closing Qdrant client: {e}")

app = FastAPI(lifespan=lifespan)

# Enable CORS with configurable origins
cors_origins = os.getenv("CORS_ORIGINS", "*")
origins_list = [cors_origins] if cors_origins != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    chapter_id: Optional[str] = None

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Physical AI RAG Chatbot API", "status": "online"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(request: Request, ask_request: AskRequest):
    """
    Accepts a question and returns a conversational answer.
    Uses RAG (Retrieval-Augmented Generation) when vector database is available,
    otherwise falls back to normal chatbot mode.
    """
    vector_store: Optional[VectorStore] = request.app.state.vector_store
    llm_service: Optional[LLMService] = request.app.state.llm_service

    # Try to retrieve relevant context from the book (if vector store available)
    response_chunks = []
    rag_mode = False
    
    if vector_store:
        try:
            filter_dict = None
            if ask_request.chapter_id:
                filter_dict = {"chapter_id": ask_request.chapter_id}

            search_results = vector_store.query(
                query=ask_request.question,
                filter_dict=filter_dict,
                top_k=3
            )

            # Format search results for response
            for result in search_results:
                response_chunks.append({
                    "payload": result.payload,
                    "score": result.score,
                })
            
            if response_chunks:
                rag_mode = True
                logger.info(f"RAG mode: Found {len(response_chunks)} relevant chunks")
        except Exception as e:
            logger.warning(f"Error querying vector store: {e}. Falling back to normal chatbot mode.")
            response_chunks = []
            rag_mode = False

    # Generate answer using LLM
    answer = None
    if llm_service:
        try:
            if rag_mode:
                # RAG mode: Use context from vector database
                answer = llm_service.generate_answer(
                    question=ask_request.question,
                    context_chunks=response_chunks
                )
            else:
                # Normal chatbot mode: Direct LLM response
                answer = llm_service.generate_direct_answer(ask_request.question)
                logger.info("Normal chatbot mode: Using LLM without RAG")
        except Exception as e:
            logger.error(f"Error generating answer: {e}")
            # Fallback to simple response
            if response_chunks:
                answer = _generate_fallback_answer(ask_request.question, response_chunks)
            else:
                answer = "I'm having trouble processing your question right now. Please try again later."
    else:
        # No LLM service available
        if response_chunks:
            answer = _generate_fallback_answer(ask_request.question, response_chunks)
        else:
            answer = "The chatbot service is not available. Please check the server configuration."

    # Return both the answer and the source chunks (empty if normal mode)
    return {
        "answer": answer,
        "sources": response_chunks,
        "mode": "rag" if rag_mode else "normal"
    }

def _generate_fallback_answer(question: str, chunks: List[Dict]) -> str:
    """
    Generate a simple answer without LLM by combining retrieved chunks.
    """
    if not chunks:
        return "I couldn't find any relevant information in the book to answer your question. Try rephrasing or asking about a different topic."

    # Build a simple answer from the chunks
    intro = f"Based on the book content, here's what I found about your question:\n\n"

    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        payload = chunk.get("payload", {})
        text = payload.get("text", "")
        source = payload.get("source", "unknown")
        chapter = payload.get("chapter_id", "unknown")

        if text:
            context_parts.append(f"From {source} (Chapter: {chapter}):\n{text}")

    if not context_parts:
        return "I found relevant sections but couldn't extract the text. Please check the document ingestion."

    answer = intro + "\n\n".join(context_parts[:2])  # Show top 2 chunks
    answer += f"\n\nNote: I'm currently running in simple mode. For more conversational explanations, please configure a valid Gemini API key."

    return answer
