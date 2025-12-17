import requests
import json

# Test the backend API
BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_chat():
    """Test the chat endpoint"""
    try:
        payload = {
            "message": "What is this Physical AI book about?",
            "conversation_id": "test_conversation"
        }
        response = requests.post(f"{BASE_URL}/api/chat",
                                headers={"Content-Type": "application/json"},
                                data=json.dumps(payload))
        print(f"Chat test: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Chat test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing RAG Chatbot API...")
    print("=" * 50)

    if test_health():
        print("✓ Health check passed")
    else:
        print("✗ Health check failed")

    print("\nNote: For full functionality, you need to:")
    print("1. Set up your Qdrant Cloud and Neon Postgres")
    print("2. Configure your Google Gemini API key")
    print("3. Ingest the documentation using the /api/documents/ingest endpoint")
    print("4. Then test the chat functionality")