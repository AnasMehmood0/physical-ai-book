from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    selected_text: Optional[str] = None  # For context selection feature

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    sources: List[str]  # List of source documents/references
    timestamp: datetime

class ContextChatRequest(BaseModel):
    message: str
    selected_context: str  # User-selected text for focused Q&A
    conversation_id: Optional[str] = None