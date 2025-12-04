import logging
import json

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from qdrant_client.http.models import Filter, FieldCondition, Range

from api.vector_store import initialize_qdrant_client
from api.embedding_model import load_embedding_model

# Configure structured logging
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel:
    question: str
    chapter_id: str

class Chunk(BaseModel):
    chapter_id: str
    chunk_content: str

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello RAG Chatbot!"}

@app.post("/ask", response_model=List[Chunk])
async def ask_question(
    request: AskRequest,
    qdrant_client = Depends(initialize_qdrant_client),
    embedding_model = Depends(load_embedding_model),
):
    try:
        logger.info(f"Received ask_question request for chapter_id: {request.chapter_id}")
        # Embed the question
        query_embedding = embedding_model.embed_documents([request.question])[0].tolist()

        # Filter for the specific chapter_id and retrieve top 3 relevant chunks
        search_result = qdrant_client.search(
            collection_name="physical_ai_book",
            query_vector=query_embedding,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="chapter_id",
                        range=Range(
                            gte=request.chapter_id,
                            lte=request.chapter_id
                        )
                    )
                ]
            ),
            limit=3,
        )

        # Extract and return the relevant chunk content
        results = [
            Chunk(chapter_id=hit.payload["chapter_id"], chunk_content=hit.payload["chunk_content"])
            for hit in search_result
        ]
        logger.info(f"Successfully processed ask_question request, returned {len(results)} chunks")
        return results
    except Exception as e:
        logger.error(f"Error processing ask_question: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
