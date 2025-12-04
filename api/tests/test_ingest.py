import os
from unittest.mock import MagicMock
import pytest
from api.ingest import read_markdown_file, recursive_character_chunking, upsert_chunks_to_qdrant

# Mock data for testing
TEST_MD_CONTENT = """
# Chapter 1

## Section 1

This is some content for section 1.

## Section 2

This is some content for section 2.
"""

# Test T008: Create unit test for markdown file reading
def test_read_markdown_file(tmp_path):
    file_path = tmp_path / "test.md"
    file_path.write_text(TEST_MD_CONTENT)
    content = read_markdown_file(str(file_path))
    assert content == TEST_MD_CONTENT

# Test T009: Create unit test for recursive character chunking
def test_recursive_character_chunking():
    chunks = recursive_character_chunking(TEST_MD_CONTENT)
    assert isinstance(chunks, list)
    assert len(chunks) > 0
    for chunk in chunks:
        assert isinstance(chunk, str)
        assert len(chunk) <= 1000  # Default chunk size

# Test T010: Create integration test for upserting chunks into Qdrant
def test_upsert_chunks_to_qdrant():
    # Mock Qdrant client and embedding model
    mock_qdrant_client = MagicMock()
    mock_embedding_model = MagicMock()
    mock_embedding_model.embed_documents.return_value = [[0.1]*384, [0.2]*384]

    # Dummy chunks and chapter_id
    chunks = ["chunk 1", "chunk 2"]
    chapter_id = "chapter_test"

    upsert_chunks_to_qdrant(mock_qdrant_client, mock_embedding_model, chunks, chapter_id)

    mock_embedding_model.embed_documents.assert_called_once_with(chunks)
    mock_qdrant_client.upsert.assert_called_once()
    args, kwargs = mock_qdrant_client.upsert.call_args
    assert kwargs["collection_name"] == "physical_ai_book"
    points = kwargs["points"]
    assert len(points) == len(chunks)
    for point in points:
        assert point.payload["chapter_id"] == chapter_id
        assert "chunk_content" in point.payload
        assert len(point.vector) == 384

