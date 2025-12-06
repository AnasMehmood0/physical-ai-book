import os
import shutil
import pytest
from api.ingest import ingest_documents
from api.vector_store import VectorStore

@pytest.fixture
def temp_dir():
    dir_path = "temp_test_book"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(os.path.join(dir_path, "test_chapter.txt"), "w") as f:
        f.write("This is a test chapter.")
    yield dir_path
    shutil.rmtree(dir_path)

def test_ingest_documents(temp_dir):
    vector_store = VectorStore(collection_name="test_collection")
    ingest_documents(temp_dir, vector_store)
    
    # Search for a document to see if it was ingested
    search_result = vector_store.query("test chapter")
    
    assert len(search_result) > 0
    assert search_result[0].payload["source"] == "test_chapter.txt"
