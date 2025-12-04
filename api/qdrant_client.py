from qdrant_client import QdrantClient, models

COLLECTION_NAME = "physical_ai_book"

def initialize_qdrant_client():
    client = QdrantClient(location=":memory:")  # In-memory Qdrant instance

    # Ensure the collection exists
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
        )
    except Exception as e:
        # Log or handle the exception if recreation fails for some reason
        print(f"Error recreating collection {COLLECTION_NAME}: {e}")

    return client
