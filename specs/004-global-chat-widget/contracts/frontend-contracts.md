# Frontend Contracts for Global Fixed Chat Widget (Corner Bubble)

This document defines the API contract expectations for the frontend `GlobalChatWidget` when communicating with the backend API.

## 1. Backend API Endpoint: `/ask`

The frontend widget interacts with the existing backend API `/ask` endpoint.

- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/ask` (local development URL)

### 1.1 Request Payload (Frontend -> Backend)

The frontend sends a JSON payload with the following structure:

```json
{
  "question": "string",
  "chapter_id": "string",
  "selected_text": "string (optional)"
}
```

- **`question`**: The user's query from the chat input.
- **`chapter_id`**: A hardcoded chapter identifier (e.g., "ros2/architecture") for context-aware filtering.
- **`selected_text`**: An optional field, currently unused but included for future extensibility, representing text selected by the user in the UI.

This payload conforms to the `AskRequest` schema defined in the backend's OpenAPI specification (`specs/002-rag-chatbot-backend/contracts/openapi.json`).

### 1.2 Response Payload (Backend -> Frontend)

The frontend expects a JSON payload with the following structure:

```json
{
  "results": [
    {
      "id": "string (UUID)",
      "payload": {
        "content": "string",
        "chapter_id": "string"
      }
    }
  ]
}
```

- **`results`**: An array of content chunks.
  - Each chunk object contains an `id` (UUID) and a `payload`.
  - The `payload` contains the `content` (text) of the chunk and its `chapter_id`.

This response conforms to the `AskResponse` schema defined in the backend's OpenAPI specification (`specs/002-rag-chatbot-backend/contracts/openapi.json`).

## 2. Error Handling

- The frontend should anticipate standard HTTP error codes (e.g., 4xx, 5xx).
- Upon receiving an error response or if the fetch operation fails, the frontend will display a generic error message to the user (e.g., "Failed to get response from AI").
