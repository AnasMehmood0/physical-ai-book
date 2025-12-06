import uuid
from qdrant_client import QdrantClient, models

from api.embedding_model import EmbeddingModel


class VectorStore:
    def __init__(self, collection_name: str = "book_chunks"):
        """
        Initializes the vector store.
        Args:
            collection_name: The name of the Qdrant collection to use.
        """
        self.client = QdrantClient(path="qdrant_db")  # Use file-based storage
        self.collection_name = collection_name
        self.embedding_model = EmbeddingModel()

        # Create collection if it doesn't exist
        try:
            self.client.get_collection(collection_name=self.collection_name)
            print(f"Collection '{self.collection_name}' already exists.")
        except Exception as e:
            print(f"Collection '{self.collection_name}' not found. Creating it. Error: {e}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.embedding_model.model.get_sentence_embedding_dimension(),
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
        print(f"Adding {len(documents)} documents to collection {self.collection_name}")
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
        print(f"Query: {query}")

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
        print(f"Search result from qdrant: {search_result}")

        if search_result.points:
            print(f"Found {len(search_result.points)} points.")
            return search_result.points
        else:
            print("No points found.")
            return []
