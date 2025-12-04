from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams


def initialize_qdrant_client():
    client = QdrantClient(location=":memory:")  # Use in-memory Qdrant
    collection_name = "physical_ai_book"

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print(f"Qdrant client initialized and collection '{collection_name}' created/recreated.")
    return client
