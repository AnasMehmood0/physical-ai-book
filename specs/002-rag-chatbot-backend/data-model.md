# Data Model for RAG Chatbot Backend

This document outlines the data models used in the RAG Chatbot Backend.

## 1. Content Chunk

Represents a piece of text indexed in the Qdrant vector database.

**Fields**:

- **id**: (UUID) A unique identifier for the chunk.
- **payload**: (object) A dictionary containing the chunk's data and metadata.
    - **content**: (string) The text content of the chunk.
    - **chapter_id**: (string) The identifier for the chapter the chunk belongs to.
- **vector**: (array of floats) The embedding vector representing the content.

**State Transitions**:

- Content chunks are created during the ingestion process.
- They are read-only after creation.
- They can be deleted if the content needs to be re-indexed.

## 2. API Request Model (`/ask`)

This is not a database model, but it defines the structure of the data the API expects.

**Fields**:

- **question**: (string, required) The user's question.
- **chapter_id**: (string, required) The chapter the user is currently reading.
- **selected_text**: (string, optional) Any text the user has selected in the UI.

## 3. API Response Model (`/ask`)

This defines the structure of the data the API will return.

**Fields**:

- **results**: (array of objects) A list of the top 3 relevant content chunks.
    - Each object in the array will be a **Content Chunk** (without the vector).
