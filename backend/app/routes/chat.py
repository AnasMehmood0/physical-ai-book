from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.session import get_db
from ..models.chat import ChatRequest, ChatResponse, ContextChatRequest
from ..services.rag_service import RAGService
from ..services.embedding_service import EmbeddingService

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """
    Main chat endpoint that uses RAG to answer questions about the Physical AI book
    """
    try:
        # Initialize services
        embedding_service = EmbeddingService()
        rag_service = RAGService(embedding_service)

        # Process the chat request using RAG
        response = rag_service.chat(request)

        return ChatResponse(
            response=response["response"],
            conversation_id=response["conversation_id"],
            sources=response["sources"],
            timestamp=response["timestamp"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat/context", response_model=ChatResponse)
async def context_chat_endpoint(
    request: ContextChatRequest,
    db: Session = Depends(get_db)
):
    """
    Chat endpoint that focuses on user-selected context
    """
    try:
        # Initialize services
        embedding_service = EmbeddingService()
        rag_service = RAGService(embedding_service)

        # Create a ChatRequest from the ContextChatRequest
        chat_request = ChatRequest(
            message=request.message,
            conversation_id=request.conversation_id,
            selected_text=request.selected_context
        )

        # Process the chat request using RAG with selected context
        response = rag_service.chat(chat_request)

        return ChatResponse(
            response=response["response"],
            conversation_id=response["conversation_id"],
            sources=response["sources"],
            timestamp=response["timestamp"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chat/models")
async def get_available_models():
    """
    Get available models for the chat interface
    """
    # This would return the models available based on the configuration
    return {"models": ["gemini-2.5-flash", "gemini-pro", "gemini-1.5-pro"]}