from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import contextlib
import logging

from api.vector_store import VectorStore
from api.ingest import ingest_documents
import os

logger = logging.getLogger(__name__)

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize VectorStore and ingest documents on startup
    vector_store = VectorStore()
    if os.path.exists("web/docs"):
        ingest_documents("web/docs", vector_store)
    app.state.vector_store = vector_store
    yield
    print("Closing Qdrant client")
    app.state.vector_store.client.close()

app = FastAPI(lifespan=lifespan)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    return {"message": "Hello RAG Chatbot!"}

@app.post("/ask")
def ask(request: Request, ask_request: AskRequest):
    """
    Accepts a question and returns relevant chunks from the book.
    """
    vector_store: VectorStore = request.app.state.vector_store
    
    filter_dict = None
    if ask_request.chapter_id:
        filter_dict = {"chapter_id": ask_request.chapter_id}
        
    search_results = vector_store.query(
        query=ask_request.question,
        filter_dict=filter_dict,
        top_k=3
    )
    
    # Format the response
    response_chunks = []
    for result in search_results:
        response_chunks.append(
            {
                "payload": result.payload,
                "score": result.score,
            }
        )
        
    return {"results": response_chunks}
