from typing import List, Dict, Any
from uuid import uuid4
from datetime import datetime
import os
import google.generativeai as genai  # type: ignore
from ..models.chat import ChatRequest, ContextChatRequest
from .embedding_service import EmbeddingService

class RAGService:
    def __init__(self, embedding_service: EmbeddingService):
        self.embedding_service = embedding_service
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-2.5-flash"))

    def get_relevant_context(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Retrieve relevant context from the vector database"""
        return self.embedding_service.search_similar(query, limit)

    def get_context_with_selection(self, query: str, selected_context: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Retrieve context based on user query and selected text"""
        return self.embedding_service.search_with_context(query, selected_context, limit)

    def generate_response(self, query: str, context: List[Dict[str, Any]], selected_context: str = None) -> str:
        """Generate a response using Google Gemini with the retrieved context"""
        # Format the context for the LLM
        context_str = "\n\n".join([item["text"] for item in context])

        if selected_context:
            # If user provided specific context, prioritize that
            prompt = f"""
            Answer the question based on the provided context. If the answer cannot be found in the context, say "I don't have enough information to answer that question based on the provided text."

            Selected Context:
            {selected_context}

            Additional Context:
            {context_str}

            Question: {query}
            Answer:
            """
        else:
            # Use only the retrieved context
            prompt = f"""
            Answer the question based on the following context. If the answer cannot be found in the context, say "I don't have enough information to answer that question based on the provided text."

            Context:
            {context_str}

            Question: {query}
            Answer:
            """

        # Call Google Gemini API to generate response
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=500,
                temperature=0.7,
            )
        )

        return response.text

    def chat(self, chat_request: ChatRequest) -> Dict[str, Any]:
        """Main chat method that orchestrates RAG process"""
        # Get relevant context from vector database
        if chat_request.selected_text:
            # If user provided specific context, use that with broader search
            context = self.get_context_with_selection(
                chat_request.message,
                chat_request.selected_text
            )
        else:
            # Otherwise, just search based on the query
            context = self.get_relevant_context(chat_request.message)

        # Generate response using the context
        response_text = self.generate_response(
            chat_request.message,
            context,
            chat_request.selected_text
        )

        # Extract sources for citation
        sources = [item["metadata"]["source"] for item in context if "source" in item["metadata"]]

        # Create response object
        response = {
            "response": response_text,
            "conversation_id": chat_request.conversation_id or str(uuid4()),
            "sources": list(set(sources)),  # Remove duplicates
            "timestamp": datetime.utcnow()
        }

        return response

    def context_chat(self, context_request: ContextChatRequest) -> Dict[str, Any]:
        """Chat method that focuses specifically on user-selected context"""
        # Get context based on both query and selected text
        context = self.get_context_with_selection(
            context_request.message,
            context_request.selected_context
        )

        # Generate response with emphasis on selected context
        response_text = self.generate_response(
            context_request.message,
            context,
            context_request.selected_context
        )

        # Extract sources
        sources = [item["metadata"]["source"] for item in context if "source" in item["metadata"]]

        # Create response object
        response = {
            "response": response_text,
            "conversation_id": context_request.conversation_id or str(uuid4()),
            "sources": list(set(sources)),  # Remove duplicates
            "timestamp": datetime.utcnow()
        }

        return response