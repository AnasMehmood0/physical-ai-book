# Feature Specification: RAG Chatbot Backend

**Feature Branch**: `002-rag-chatbot-backend`  
**Created**: 2025-12-05
**Status**: Draft  
**Input**: User description: "Feature: RAG Chatbot Backend Goal: Create a Python FastAPI backend in a new api/ folder. Requirements: Tech Stack: FastAPI, Qdrant in Local Memory Mode (location=":memory:"), and FastEmbed or SentenceTransformers for embeddings. Skill 1 - Ingestion (api/ingest.py): Script that recursively reads all .md files in ../web/docs/. Store chapter_id metadata. Skill 2 - The Brain (api/main.py): POST Endpoint /ask. It must accept three parameters: {"question": "...", "chapter_id": "chapter1", "selected_text": "..."}. It must filter Qdrant by chapter_id, retrieve the top 3 chunks, and return those chunks as the response. CORS: Allow * (all origins)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Ingestion (Priority: P1)

As a content manager, I want to process the textbook's markdown files so that they are searchable and can be used to answer user questions.

**Why this priority**: This is the foundational step that makes the chatbot functional. Without the content, the chatbot cannot provide any answers.

**Independent Test**: This can be tested by running the ingestion script and verifying that the content is correctly added to the search index.

**Acceptance Scenarios**:

1. **Given** a set of markdown files in the `web/docs` directory, **When** the ingestion script is run, **Then** the content of the markdown files is chunked and stored in the search index.
2. **Given** a chunk of content in the search index, **When** it is inspected, **Then** it has a `chapter_id` associated with it.

---

### User Story 2 - Question Answering (Priority: P1)

As a user, I want to ask a question and get relevant information from the textbook, filtered by the chapter I am currently reading.

**Why this priority**: This is the core functionality of the chatbot and the primary way users will interact with it.

**Independent Test**: This can be tested by sending a request to the `/ask` endpoint and verifying that the response contains relevant content.

**Acceptance Scenarios**:

1. **Given** a question and a `chapter_id`, **When** a request is made to the `/ask` endpoint, **Then** the service returns the top 3 most relevant chunks of text from that chapter.
2. **Given** a question for a `chapter_id` that does not exist or has no content, **When** a request is made to the `/ask` endpoint, **Then** the service returns an empty or explanatory response.

---

### Edge Cases

- What happens when the ingestion script is run on an empty `web/docs` directory?
- How does the system handle non-markdown files in the `web/docs` directory?
- What is the expected response when a question has no relevant chunks in the specified chapter?
- How are very long questions or selected text handled?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a mechanism to ingest and index content from markdown files located in the `web/docs` directory.
- **FR-002**: Each indexed content chunk MUST be associated with a `chapter_id`.
- **FR-003**: The system MUST expose an API endpoint (`/ask`) that accepts a user's question, a `chapter_id`, and selected text.
- **FR-004**: The `/ask` endpoint MUST filter the search by the provided `chapter_id`.
- **FR-005**: The `/ask` endpoint MUST return the top 3 most relevant content chunks based on the user's question.
- **FR-006**: The API MUST be configured to allow requests from any origin (CORS `*`).

### Key Entities

- **Content Chunk**: A piece of text derived from the source markdown files. Each chunk has associated content and metadata (e.g., `chapter_id`).
- **Chapter**: A logical grouping of content, identified by a `chapter_id`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of valid questions for a given chapter return at least one relevant content chunk.
- **SC-002**: The average response time for the `/ask` endpoint is less than 2 seconds for a typical workload.
- **SC-003**: The ingestion process can handle 1000 markdown files in under 5 minutes.
- **SC-004**: The system can be deployed and run as a standalone service.