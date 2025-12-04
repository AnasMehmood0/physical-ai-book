import pytest
from fastapi.testclient import TestClient
from api.main import app
from api.qdrant_client import initialize_qdrant_client
from api.embedding_model import load_embedding_model
from api.ingest import ingest_chapter, read_markdown_file, recursive_character_chunking, upsert_chunks_to_qdrant
import os

# Mock data for testing
TEST_MD_CONTENT_E2E = """
# Chapter E2E Test

This is a test document for end-to-end ingestion and querying.
It discusses AI concepts like machine learning and deep learning.
"""

# Override FastAPI dependencies for testing, similar to test_main.py
pytest.qdrant_client = initialize_qdrant_client()
pytest.embedding_model = load_embedding_model()

app.dependency_overrides[initialize_qdrant_client] = lambda: pytest.qdrant_client
app.dependency_overrides[load_embedding_model] = lambda: pytest.embedding_model

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_e2e_data():
    # Setup: Ingest data before tests run
    chapter_id = "chapter_e2e"
    chunks = recursive_character_chunking(TEST_MD_CONTENT_E2E)
    upsert_chunks_to_qdrant(pytest.qdrant_client, pytest.embedding_model, chunks, chapter_id)
    yield
    # Teardown: Clear data after tests (optional, in-memory client will reset anyway)
    # For persistent clients, you would add client.delete_collection(collection_name="physical_ai_book") here

# T026: Add comprehensive integration tests covering the end-to-end flow
def test_e2e_ingestion_and_query():
    # Test querying the ingested data
    question = "What AI concepts are discussed?"
    chapter_id = "chapter_e2e"

    response = client.post(
        "/ask",
        json={
            "question": question,
            "chapter_id": chapter_id
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any("machine learning" in chunk["chunk_content"].lower() for chunk in data)
    assert any("deep learning" in chunk["chunk_content"].lower() for chunk in data)
    assert all(chunk["chapter_id"] == chapter_id for chunk in data)
