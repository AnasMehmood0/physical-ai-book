from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.session import get_db
from ..models.documents import DocumentIngestionRequest, DocumentIngestionResponse
from ..services.document_service import DocumentService
from ..services.embedding_service import EmbeddingService

router = APIRouter()

@router.post("/documents/ingest", response_model=DocumentIngestionResponse)
async def ingest_documents(
    request: DocumentIngestionRequest,
    db: Session = Depends(get_db)
):
    """
    Ingest Docusaurus documentation into the vector database
    """
    try:
        # Initialize services
        embedding_service = EmbeddingService()
        document_service = DocumentService(db, embedding_service)

        # Perform ingestion - use the provided source_path or default to web/docs
        result = document_service.ingest_docusaurus_docs(
            chunk_size=request.chunk_size,
            chunk_overlap=request.chunk_overlap,
            source_path=request.source_path
        )

        return DocumentIngestionResponse(
            document_id="batch_ingestion",  # This is a batch operation
            chunks_count=result['chunks_count'],
            status=result['status']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/documents/status")
async def get_ingestion_status():
    """
    Get the status of document ingestion
    """
    # This would check the database and vector store for ingested documents
    # For now, returning a simple status
    return {"status": "ready", "documents_count": 0, "chunks_count": 0}