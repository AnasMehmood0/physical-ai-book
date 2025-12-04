import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from api.main import app

# Mocking dependencies for isolation
# These mocks will be used by all tests in this file
pytest.qdrant_client = MagicMock()
pytest.embedding_model = MagicMock()

# Override FastAPI dependencies for testing
app.dependency_overrides[initialize_qdrant_client] = lambda: pytest.qdrant_client
app.dependency_overrides[load_embedding_model] = lambda: pytest.embedding_model

client = TestClient(app)

# Test T016: Create unit test for /ask endpoint request parsing
def test_ask_endpoint_request_parsing():
    response = client.post(
        "/ask", json={
            "question": "What is AI?",
            "chapter_id": "chapter1"
            }
    )
    assert response.status_code == 200
    # Further assertions can be added to check if the mock client was called correctly

# Test T017: Create unit test for Qdrant filtering by chapter_id
def test_qdrant_filtering_by_chapter_id():
    # Mock the Qdrant client's search method
    pytest.qdrant_client.search.return_value = [
        MagicMock(payload={"chapter_id": "chapter1", "chunk_content": "AI content 1"}),
        MagicMock(payload={"chapter_id": "chapter1", "chunk_content": "AI content 2"}),
    ]

    # Make a dummy request to trigger the search logic
    client.post(
        "/ask", json={
            "question": "Test question",
            "chapter_id": "chapter1"
            }
    )

    # Assert that qdrant_client.search was called with the correct filter
    pytest.qdrant_client.search.assert_called_once()
    args, kwargs = pytest.qdrant_client.search.call_args
    assert kwargs["query_filter"].field == "chapter_id"
    assert kwargs["query_filter"].range.gte == "chapter1"
    assert kwargs["query_filter"].range.lte == "chapter1"

# Test T018: Create integration test for /ask endpoint (full RAG flow)
def test_ask_endpoint_full_rag_flow():
    # Mock embedding model to return consistent embeddings
    pytest.embedding_model.embed_documents.return_value = [[0.1] * 384]

    # Mock Qdrant client search to return predefined chunks
    pytest.qdrant_client.search.return_value = [
        MagicMock(payload={"chapter_id": "chapter1", "chunk_content": "Relevant chunk 1"}),
        MagicMock(payload={"chapter_id": "chapter1", "chunk_content": "Relevant chunk 2"}),
    ]

    response = client.post(
        "/ask", json={
            "question": "What is AI?",
            "chapter_id": "chapter1"
            }
    )
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 2
    assert data["results"][0]["chunk_content"] == "Relevant chunk 1"
    assert data["results"][1]["chunk_content"] == "Relevant chunk 2"
