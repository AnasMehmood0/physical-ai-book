from fastapi.testclient import TestClient
from api.main import app
import os
import shutil

# This setup is a bit tricky, because the main app ingests data on startup.
# For a robust test, we should control the data ingestion.
# One way is to have a separate endpoint for testing to trigger ingestion,
# or to mock the vector_store object.

# For now, let's rely on the startup event and the dummy data.
# We'll create the dummy data here again to make the test self-contained.

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    if not os.path.exists("temp_book"):
        os.makedirs("temp_book")
    with open("temp_book/chapter1.txt", "w") as f:
        f.write("This is a test about AI.\n")
    with open("temp_book/chapter2.txt", "w") as f:
        f.write("This is a test about LLMs.\n")

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    if os.path.exists("temp_book"):
        shutil.rmtree("temp_book")


def test_ask_endpoint():
    with TestClient(app) as client:
        response = client.post("/ask", json={"question": "What is this about?"})
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert len(data["results"]) > 0
        assert "payload" in data["results"][0]
        assert "score" in data["results"][0]

def test_ask_endpoint_with_filter():
    with TestClient(app) as client:
        response = client.post("/ask", json={"question": "What is this about?", "chapter_id": "chapter1"})
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert len(data["results"]) > 0
        # Check if all results are from chapter1
        for result in data["results"]:
            assert result["payload"]["chapter_id"] == "chapter1"
