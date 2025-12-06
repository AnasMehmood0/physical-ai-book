# Quickstart for Global Fixed Chat Widget (Corner Bubble)

This guide provides instructions on how to set up and verify the integration of the `GlobalChatWidget` into the Docusaurus website.

## Prerequisites

- Docusaurus development environment set up.
- Backend RAG Chatbot API running on `http://127.0.0.1:8000`.

## Setup (already completed by agent)

The agent has already performed the following steps:
1.  Created `web/src/components/GlobalChatWidget.tsx` (the React component for the chat interface).
2.  Created `web/src/components/GlobalChatWidget.module.css` (the CSS module for styling the widget).
3.  Manually swizzled the Docusaurus `Layout` component by creating `web/src/theme/Layout/index.tsx` and integrated `GlobalChatWidget` within it.
4.  Created an empty `web/src/theme/Layout/styles.module.css` to resolve module import errors.
5.  Cleaned up `web/src/pages/index.tsx` by removing the `ChatInterface` component.

## Verification

To verify the integration, you need to start the Docusaurus development server.

1.  **Ensure your backend API is running**:
    ```bash
    python -m uvicorn api.src.main:app --reload
    ```
    *(Note: This command should be run in a separate terminal or as a background process.)*

2.  **Navigate to the `web` directory**:
    ```bash
    cd web
    ```

3.  **Start the Docusaurus development server**:
    ```bash
    npx docusaurus start --port 3001
    ```
    *(If port 3000 is busy, try a different port like 3001.)*

4.  **Open your browser**: Navigate to `http://localhost:3001` (or the port you specified).

5.  **Observe the widget**: You should see a chat bubble icon in the bottom-right corner of the screen.

6.  **Test the chat functionality**:
    - Click the chat bubble to expand the interface.
    - Type a question (e.g., "What is ROS 2 architecture?") into the input field.
    - Click the "Ask" button.
    - Observe the raw JSON response from the API displayed within the chat box.
