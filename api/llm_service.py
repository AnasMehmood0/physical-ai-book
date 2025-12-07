"""
LLM Service for generating conversational responses
Uses Google Gemini API to generate explanations based on retrieved context
"""

import os
import requests
from typing import List, Dict, Optional


class LLMService:
    def __init__(self, api_key: str = None, model: str = "gemini-2.5-flash"):
        """
        Initialize the LLM service.
        Args:
            api_key: Gemini API key (if not provided, loads from env)
            model: Gemini model to use (default: gemini-2.5-flash)
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY must be set in environment or provided")

    def generate_answer(
        self,
        question: str,
        context_chunks: List[Dict],
        max_tokens: int = 500
    ) -> str:
        """
        Generate a conversational answer using retrieved context.

        Args:
            question: User's question
            context_chunks: List of relevant document chunks with metadata
            max_tokens: Maximum tokens in response

        Returns:
            Generated answer as string
        """
        # Build context from retrieved chunks
        context = self._build_context(context_chunks)

        # Create the prompt
        prompt = self._create_prompt(question, context)

        # Call Gemini API
        try:
            response = self._call_gemini_api(prompt, max_tokens)
            return response
        except Exception as e:
            print(f"Error generating answer: {e}")
            return f"I'm sorry, I encountered an error while generating a response: {str(e)}"

    def _build_context(self, chunks: List[Dict]) -> str:
        """Build context string from retrieved chunks."""
        if not chunks:
            return "No relevant information found."

        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            payload = chunk.get("payload", {})
            score = chunk.get("score", 0)

            # Extract text from payload (assuming it's stored as 'text' or similar)
            # Adjust this based on your actual payload structure
            chunk_text = payload.get("text", str(payload))
            source = payload.get("source", "unknown")
            chapter = payload.get("chapter_id", "unknown")

            context_parts.append(
                f"[Source {i}: {source}, Chapter: {chapter}, Relevance: {score:.2f}]\n{chunk_text}"
            )

        return "\n\n".join(context_parts)

    def _create_prompt(self, question: str, context: str) -> str:
        """Create a RAG prompt for the LLM."""
        return f"""You are a helpful AI assistant for the Physical AI Book. Your role is to explain concepts from the book in a clear, educational, and friendly manner.

Context from the book:
{context}

User Question: {question}

Instructions:
1. Answer the question based ONLY on the provided context from the book
2. If the context doesn't contain relevant information, say "I don't have enough information in the book to answer that question."
3. Be conversational and helpful, like a knowledgeable tutor
4. Cite which chapter or source you're referencing when possible
5. If asked for examples, provide them if they're in the context
6. Keep your answer concise but informative (2-4 paragraphs)

Your Answer:"""

    def _call_gemini_api(self, prompt: str, max_tokens: int) -> str:
        """Call the Gemini API to generate a response."""
        url = f"{self.base_url}/{self.model}:generateContent"

        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": max_tokens,
                "topP": 0.8,
                "topK": 40
            }
        }

        # Add API key as query parameter
        params = {"key": self.api_key}

        response = requests.post(
            url,
            headers=headers,
            params=params,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(f"Gemini API error: {response.status_code} - {response.text}")

        result = response.json()

        # Extract the generated text from the response
        try:
            generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return generated_text.strip()
        except (KeyError, IndexError) as e:
            raise Exception(f"Unexpected API response format: {str(e)}")

    def generate_direct_answer(self, question: str, max_tokens: int = 500) -> str:
        """
        Generate a direct answer without RAG context (normal chatbot mode).

        Args:
            question: User's question
            max_tokens: Maximum tokens in response

        Returns:
            Generated answer as string
        """
        prompt = f"""You are a helpful AI assistant specializing in Physical AI, robotics, and embodied intelligence.

User Question: {question}

Instructions:
1. Provide a helpful, informative answer about Physical AI topics
2. Be conversational and educational, like a knowledgeable tutor
3. If the question is about Physical AI topics (sensors, actuators, locomotion, computer vision, control systems, manipulation, sim-to-real, etc.), provide a detailed explanation
4. If you're not sure about specific details, be honest about it
5. Keep your answer concise but informative (2-4 paragraphs)

Note: You are currently running in normal chatbot mode. For answers based on the Physical AI Book content, the book database needs to be ingested.

Your Answer:"""

        try:
            return self._call_gemini_api(prompt, max_tokens)
        except Exception as e:
            return f"I apologize, but I'm having trouble generating a response right now: {str(e)}"

    def generate_simple_response(self, question: str, max_tokens: int = 300) -> str:
        """
        Generate a response without context (fallback).

        Args:
            question: User's question
            max_tokens: Maximum tokens in response

        Returns:
            Generated answer as string
        """
        prompt = f"""You are a helpful AI assistant for the Physical AI Book.

User Question: {question}

Please provide a brief, helpful response explaining that you need more context from the book to give a detailed answer, but you can provide a general explanation about Physical AI if helpful.

Your Answer:"""

        try:
            return self._call_gemini_api(prompt, max_tokens)
        except Exception as e:
            return f"I apologize, but I'm having trouble generating a response right now: {str(e)}"
