from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Document(BaseModel):
    id: str
    title: str
    content: str
    source: str
    created_at: datetime
    updated_at: datetime

class DocumentChunk(BaseModel):
    id: str
    document_id: str
    content: str
    chunk_index: int
    embedding: Optional[List[float]] = None

class DocumentIngestionRequest(BaseModel):
    source_path: str
    chunk_size: int = 1000
    chunk_overlap: int = 200

class DocumentIngestionResponse(BaseModel):
    document_id: str
    chunks_count: int
    status: str