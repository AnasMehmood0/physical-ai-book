from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# 1. Create a client
client = QdrantClient(path="qdrant_test_db")
collection_name = "test_collection"

# 2. Create a collection
try:
    client.get_collection(collection_name=collection_name)
    print("Collection already exists")
except Exception:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
    print("Collection created")


# 3. Add a document
model = SentenceTransformer("all-MiniLM-L6-v2")
doc = "This is a test document about ROS 2."
embedding = model.encode(doc)

client.upsert(
    collection_name=collection_name,
    points=[
        models.PointStruct(
            id=1,
            vector=embedding.tolist(),
            payload={"text": doc},
        )
    ],
    wait=True,
)
print("Document upserted")


# 4. Query for the document
query_text = "What is ROS 2?"
query_embedding = model.encode(query_text)

search_result = client.query_points(
    collection_name=collection_name,
    query=query_embedding.tolist(),
    limit=1,
    with_payload=True,
)

print(f"Search result: {search_result}")
