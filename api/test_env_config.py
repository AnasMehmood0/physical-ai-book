"""
Test script to verify environment variable configuration is working correctly.
"""
import os
import sys
from pathlib import Path

# Add parent directory to path to enable imports
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_env_variables():
    """Test that all required environment variables are loaded."""
    print("Testing Environment Variable Configuration\n")
    print("=" * 50)

    # Qdrant Configuration
    print("\n[Qdrant Configuration]")
    print(f"QDRANT_MODE: {os.getenv('QDRANT_MODE')}")
    print(f"QDRANT_PATH: {os.getenv('QDRANT_PATH')}")
    print(f"QDRANT_COLLECTION_NAME: {os.getenv('QDRANT_COLLECTION_NAME')}")

    # Check if cloud mode credentials are available (masked for security)
    qdrant_url = os.getenv('QDRANT_URL')
    qdrant_api_key = os.getenv('QDRANT_API_KEY')
    print(f"QDRANT_URL: {qdrant_url[:30] + '...' if qdrant_url else 'Not set'}")
    print(f"QDRANT_API_KEY: {'***' + qdrant_api_key[-10:] if qdrant_api_key else 'Not set'}")

    # Embedding Model Configuration
    print("\n[Embedding Model Configuration]")
    print(f"EMBEDDING_MODEL_NAME: {os.getenv('EMBEDDING_MODEL_NAME')}")

    # Document Ingestion Configuration
    print("\n[Document Ingestion Configuration]")
    print(f"DOCS_DIRECTORY: {os.getenv('DOCS_DIRECTORY')}")
    print(f"CHUNK_SIZE: {os.getenv('CHUNK_SIZE')}")
    print(f"CHUNK_OVERLAP: {os.getenv('CHUNK_OVERLAP')}")

    # API Configuration
    print("\n[API Configuration]")
    print(f"API_HOST: {os.getenv('API_HOST')}")
    print(f"API_PORT: {os.getenv('API_PORT')}")
    print(f"CORS_ORIGINS: {os.getenv('CORS_ORIGINS')}")

    # Gemini Configuration (masked)
    print("\n[Gemini Configuration]")
    gemini_key = os.getenv('GEMINI_API_KEY')
    print(f"GEMINI_API_KEY: {'***' + gemini_key[-10:] if gemini_key else 'Not set'}")
    print(f"GEMINI_API_URL: {os.getenv('GEMINI_API_URL')}")

    print("\n" + "=" * 50)
    print("\nEnvironment configuration loaded successfully!")

def test_imports():
    """Test that all required modules can be imported."""
    print("\n\nTesting Module Imports\n")
    print("=" * 50)

    try:
        from api.embedding_model import EmbeddingModel
        print("[OK] EmbeddingModel imported successfully")
    except Exception as e:
        print(f"[FAIL] Failed to import EmbeddingModel: {e}")
        return False

    try:
        from api.vector_store import VectorStore
        print("[OK] VectorStore imported successfully")
    except Exception as e:
        print(f"[FAIL] Failed to import VectorStore: {e}")
        return False

    try:
        from api.ingest import ingest_documents
        print("[OK] ingest_documents imported successfully")
    except Exception as e:
        print(f"[FAIL] Failed to import ingest_documents: {e}")
        return False

    print("\n" + "=" * 50)
    print("All modules imported successfully!")
    return True

def test_embedding_model():
    """Test that the EmbeddingModel initializes with environment variables."""
    print("\n\nTesting EmbeddingModel Initialization\n")
    print("=" * 50)

    try:
        from api.embedding_model import EmbeddingModel
        model = EmbeddingModel()
        print(f"[OK] EmbeddingModel initialized successfully")
        print(f"  Model: {model.model}")

        # Test embedding generation
        test_text = "This is a test sentence."
        embedding = model.get_embedding(test_text)
        print(f"[OK] Generated embedding with dimension: {len(embedding)}")

        print("\n" + "=" * 50)
        print("EmbeddingModel test passed!")
        return True
    except Exception as e:
        print(f"[FAIL] EmbeddingModel test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print(" RAG Chatbot Environment Configuration Test")
    print("=" * 60)

    # Run tests
    test_env_variables()

    if test_imports():
        test_embedding_model()

    print("\n" + "=" * 60)
    print(" Test Complete!")
    print("=" * 60 + "\n")
