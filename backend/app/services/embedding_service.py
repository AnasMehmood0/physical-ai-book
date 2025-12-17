from typing import List, Optional
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

class EmbeddingService:
    def __init__(self):
        # Initialize Qdrant client
        qdrant_host = os.getenv("QDRANT_HOST", "localhost")
        qdrant_port = int(os.getenv("QDRANT_PORT", 6333))
        qdrant_api_key = os.getenv("QDRANT_API_KEY")

        # Check if we're using Qdrant Cloud (has protocol in host) or local instance
        if qdrant_host and ("http://" in qdrant_host or "https://" in qdrant_host):
            # If host contains protocol, use URL instead of host/port
            self.qdrant_client = QdrantClient(
                url=qdrant_host,
                api_key=qdrant_api_key
            )
        elif qdrant_api_key:
            # For cloud instances with API key but without protocol in host
            self.qdrant_client = QdrantClient(
                host=qdrant_host,
                port=qdrant_port,
                api_key=qdrant_api_key,
                https=True  # Use HTTPS for cloud instances
            )
        else:
            # For local instance without API key
            self.qdrant_client = QdrantClient(
                host=qdrant_host,
                port=qdrant_port,
                https=False  # Don't use HTTPS for local instances
            )

        # Initialize embedding model
        self.embedding_model = SentenceTransformer(os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"))

        # Collection name
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_book")

        # Create collection if it doesn't exist
        self._create_collection()

    def _create_collection(self):
        """Create Qdrant collection if it doesn't exist"""
        try:
            self.qdrant_client.get_collection(self.collection_name)
        except:
            # Collection doesn't exist, create it
            vector_size = len(self.embedding_model.encode("test"))
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE)
            )

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts"""
        return self.embedding_model.encode(texts).tolist()

    def store_embeddings(self, texts: List[str], metadatas: List[dict]) -> List[str]:
        """Store embeddings in Qdrant and return IDs"""
        embeddings = self.generate_embeddings(texts)

        # Generate IDs for the points
        ids = [f"{text[:20].replace(' ', '_')}_{i}" for i, text in enumerate(texts)]

        # Prepare points for insertion
        points = [
            models.PointStruct(
                id=ids[i],
                vector=embeddings[i],
                payload={
                    "text": texts[i],
                    **metadatas[i]
                }
            )
            for i in range(len(texts))
        ]

        # Upload points to Qdrant
        self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        return ids

    def search_similar(self, query: str, limit: int = 5) -> List[dict]:
        """Search for similar texts in the vector database"""
        query_embedding = self.embedding_model.encode([query])[0].tolist()

        search_results = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit
        )

        return [
            {
                "text": result.payload["text"],
                "score": result.score,
                "metadata": {k: v for k, v in result.payload.items() if k != "text"}
            }
            for result in search_results
        ]

    def search_with_context(self, query: str, selected_context: str, limit: int = 5) -> List[dict]:
        """Search for similar texts with user-selected context"""
        # Combine query and selected context for better search
        combined_query = f"{query} {selected_context}"
        return self.search_similar(combined_query, limit)