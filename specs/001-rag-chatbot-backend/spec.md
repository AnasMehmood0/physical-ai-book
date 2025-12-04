# Feature Specification: RAG Chatbot Backend

**Feature Branch**: `001-rag-chatbot-backend`
**Created**: 2025-12-03
**Status**: Draft
**Input**: User description: "Feature: RAG Chatbot Backend

Goal: Create a Python FastAPI backend in a new api/ folder that serves as the "Brain" for the textbook, integrating the required components for the hackathon.

Requirements:

Project Structure: Create a folder named api in the root.

Tech Stack: Use FastAPI, Qdrant in Local Memory Mode (location=":memory:"), and FastEmbed or SentenceTransformers for embeddings.

Skill 1 (Bonus Points) - Ingestion (api/ingest.py): A script that reads all .md files from ../web/docs/, chunks them, and upserts them into Qdrant collection "physical_ai_book". Metadata: Store chapter_id with every chunk (for context-awareness).

Skill 2 - The Brain (api/main.py): POST Endpoint /ask. It must accept {"question": "...", "chapter_id": "chapter1"}. It must filter Qdrant by chapter_id, retrieve the top 3 chunks, and return those chunks as the response.

CORS: Configure CORS to allow * (all origins) for frontend communication."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest Markdown Files (Priority: P1)

As a backend administrator, I want to ingest markdown files from the `../web/docs/` directory so that their content can be used for chatbot responses.

**Why this priority**: This is fundamental for the RAG chatbot to have any knowledge base.

**Independent Test**: Can be fully tested by running the ingestion script and verifying that Qdrant contains the chunks with correct metadata.

**Acceptance Scenarios**:

1. **Given** markdown files exist in `../web/docs/`, **When** the ingestion script is run, **Then** the content of these files is chunked and upserted into the "physical_ai_book" Qdrant collection, each chunk having a `chapter_id` metadata.

---

### User Story 2 - Ask Question (Priority: P1)

As a user, I want to ask a question with a specified chapter ID, so that I receive relevant chunks from that chapter as a response.

**Why this priority**: This is the core functionality of the chatbot.

**Independent Test**: Can be fully tested by sending a POST request to `/ask` with a question and `chapter_id`, and verifying that the top 3 relevant chunks are returned.

**Acceptance Scenarios**:

1. **Given** the Qdrant collection "physical_ai_book" contains chunks, **When** a POST request is sent to `/ask` with a `question` and `chapter_id`, **Then** the system filters by `chapter_id`, retrieves the top 3 relevant chunks, and returns them in the response.

---

### Edge Cases

- What happens when there are no `.md` files in `../web/docs/` during ingestion?
- How does the system handle an invalid `chapter_id` in the `/ask` endpoint?
- What if no relevant chunks are found for a given `question` and `chapter_id`?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create a folder named `api` in the root of the project.
- **FR-002**: System MUST use FastAPI for the backend.
- **FR-003**: System MUST use Qdrant in Local Memory Mode (location=":memory:").
- **FR-004**: System MUST use either FastEmbed or SentenceTransformers for embeddings.
- **FR-005**: System MUST provide a script `api/ingest.py` to read all `.md` files from `../web/docs/`.
- **FR-006**: System MUST chunk the content of the markdown files.
- **FR-007**: System MUST upsert the chunks into a Qdrant collection named "physical_ai_book".
- **FR-008**: System MUST store `chapter_id` as metadata with every chunk for context-awareness.
- **FR-009**: System MUST expose a POST endpoint `/ask` in `api/main.py`.
- **FR-010**: The `/ask` endpoint MUST accept a JSON payload with `{"question": "...", "chapter_id": "chapter1"}`.
- **FR-011**: The `/ask` endpoint MUST filter Qdrant results by `chapter_id`.
- **FR-012**: The `/ask` endpoint MUST retrieve the top 3 chunks based on the `question`.
- **FR-013**: The `/ask` endpoint MUST return the retrieved chunks as the response.
- **FR-014**: System MUST configure CORS to allow `*` (all origins) for frontend communication.

### Key Entities *(include if feature involves data)*

- **Chunk**: A segment of text from a markdown file, associated with a `chapter_id`.
- **Question**: User's query to the chatbot.
- **Chapter ID**: Identifier for a specific chapter, used for filtering.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The ingestion script successfully processes all `.md` files from `../web/docs/` and populates the Qdrant collection with relevant chunks and metadata.
- **SC-002**: The `/ask` endpoint responds to a user's question with the top 3 contextually relevant chunks from the specified `chapter_id` within 500ms (P95 latency).
- **SC-003**: Frontend applications can successfully make requests to the `/ask` endpoint without CORS issues.
- **SC-004**: The backend can handle at least 10 concurrent `/ask` requests without degradation in response time.