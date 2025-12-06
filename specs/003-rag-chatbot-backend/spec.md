# Feature Specification: RAG Chatbot Backend (V2 Stable)

**Feature Branch**: `003-rag-chatbot-backend`
**Created**: 2025-12-06
**Status**: Draft
**Input**: User description: "Feature: RAG Chatbot Backend (V2 Stable) Goal: Create a Python FastAPI backend using a stable, synchronous Qdrant client to ensure stability. Requirements: Project Structure: Create a folder named api in the root. Tech Stack: Use FastAPI, Qdrant in Local Memory Mode, and SentenceTransformers for embeddings. Client Constraint (CRITICAL): The implementation MUST use the synchronous QdrantClient and should NOT use async def or await on the search method. Ingestion/API Logic: Implement api/ingest.py (recursive read, chunk, embed) and api/main.py (/ask endpoint, filtering by chapter_id, returning top 3 chunks). CORS: Allow * (all origins)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a question about the book content (Priority: P1)
As a user, I want to ask a question to the chatbot and get a relevant answer from the book's content, so that I can quickly find information without reading the whole book.

**Why this priority**: This is the core functionality of the RAG chatbot.

**Independent Test**: The API can be called with a question and a chapter filter, and it should return relevant chunks of text.

**Acceptance Scenarios**:
1. **Given** the book content has been ingested, **When** I send a question to the `/ask` endpoint, **Then** I should receive a list of the top 3 most relevant text chunks from the book.
2. **Given** the book content has been ingested, **When** I send a question and a `chapter_id` to the `/ask` endpoint, **Then** I should receive a list of the top 3 most relevant text chunks from that specific chapter.

### User Story 2 - Ingest book content (Priority: P2)
As a developer, I want to be able to ingest the book's content into the vector store, so that the chatbot can use it to answer questions.

**Why this priority**: The chatbot cannot answer questions without the book content.

**Independent Test**: An ingestion script can be run to process and load the book's content into the vector store.

**Acceptance Scenarios**:
1. **Given** a directory of text files, **When** I run the ingestion process, **Then** the text is chunked, embedded, and stored in the vector database.
2. **Given** the content is ingested, **When** I query the vector store, **Then** I can find the embedded chunks with their metadata (like `chapter_id`).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide an API endpoint (`/ask`) that accepts a user's question.
- **FR-002**: The `/ask` endpoint MUST support filtering by `chapter_id`.
- **FR-003**: The `/ask` endpoint MUST return the top 3 most relevant text chunks based on the question.
- **FR-004**: The system MUST have a mechanism to ingest text content from a specified directory.
- **FR-005**: The ingestion process MUST recursively read text files, split them into chunks, generate embeddings, and store them in a vector database.
- **FR-006**: The system MUST allow cross-origin requests from any domain (CORS `*`).
- **FR-007**: The system's interaction with the vector database for search operations MUST be synchronous.

### Key Entities *(include if feature involves data)*

- **Text Chunk**: A piece of text from the book. It has content and metadata.
- **Metadata**: Information about the text chunk, including at least a `chapter_id`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The `/ask` endpoint responds to 95% of queries within 2 seconds.
- **SC-002**: For a set of predefined questions, the top 3 returned chunks are relevant to the question in at least 90% of cases.
- **SC-003**: The ingestion process can handle a 1000-page book (approx. 500,000 words) in under 10 minutes.