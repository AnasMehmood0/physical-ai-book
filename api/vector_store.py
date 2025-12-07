import uuid
import os
from qdrant_client import QdrantClient, models

from api.embedding_model import EmbeddingModel


class VectorStore:
    def __init__(
        self,
        collection_name: str = None,
        qdrant_mode: str = None,
        qdrant_path: str = None,
        qdrant_url: str = None,
        qdrant_api_key: str = None
    ):
        """
        Initializes the vector store.
        Args:
            collection_name: The name of the Qdrant collection to use.
            qdrant_mode: Mode of operation ('local' or 'cloud').
            qdrant_path: Path for local Qdrant storage.
            qdrant_url: URL for cloud Qdrant instance.
            qdrant_api_key: API key for cloud Qdrant instance.
        """
        # Load from environment variables if not provided
        self.collection_name = collection_name or os.getenv("QDRANT_COLLECTION_NAME", "book_chunks")
        mode = qdrant_mode or os.getenv("QDRANT_MODE", "local")

        # Initialize Qdrant client based on mode
        if mode == "cloud":
            url = qdrant_url or os.getenv("QDRANT_URL")
            api_key = qdrant_api_key or os.getenv("QDRANT_API_KEY")
            if not url or not api_key:
                raise ValueError("QDRANT_URL and QDRANT_API_KEY must be set for cloud mode")
            self.client = QdrantClient(url=url, api_key=api_key)
        else:
            # Local mode
            path = qdrant_path or os.getenv("QDRANT_PATH", "./qdrant_storage")
            self.client = QdrantClient(path=path)

        self.embedding_model = EmbeddingModel()

        # Only create collection if it doesn't exist
        try:
            self.client.get_collection(collection_name=self.collection_name)
        except Exception:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.embedding_model.get_sentence_embedding_dimension(),
                    distance=models.Distance.COSINE,
                ),
            )

    def add_documents(self, documents: list[str], metadatas: list[dict]):
        """
        Adds documents to the vector store.
        Args:
            documents: A list of documents to add.
            metadatas: A list of metadata dictionaries corresponding to the documents.
        """
        embeddings = [self.embedding_model.get_embedding(doc) for doc in documents]
        ids = [str(uuid.uuid4()) for _ in documents]

        self.client.upsert(
            collection_name=self.collection_name,
            points=models.Batch(
                ids=ids,
                vectors=embeddings,
                payloads=metadatas,
            ),
            wait=True,
        )

    def query(self, query: str, filter_dict: dict = None, top_k: int = 3):
        """
        Queries for documents in the vector store.
        Args:
            query: The query to search for.
            filter_dict: A dictionary to filter the search results.
            top_k: The number of results to return.
        Returns:
            A list of search results.
        """
        query_embedding = self.embedding_model.get_embedding(query)

        query_filter = None
        if filter_dict:
            query_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key=key, match=models.MatchValue(value=value)
                    )
                    for key, value in filter_dict.items()
                ]
            )

        search_result = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            query_filter=query_filter,
            limit=top_k,
            with_payload=True
        )
        return search_result.points
