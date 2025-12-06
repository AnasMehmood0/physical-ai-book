# Tasks: RAG Chatbot Backend (V2 Stable)

**Input**: Design documents from `specs/003-rag-chatbot-backend/`
**Prerequisites**: `plan.md`, `spec.md`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [ ] T001 [P] Create the `api` directory at the repository root.
- [ ] T002 [P] Create the `api/tests` directory.
- [ ] T003 [P] Create an empty `api/__init__.py` file.
- [ ] T004 [P] Create an empty `api/tests/__init__.py` file.
- [ ] T005 [P] Create `api/requirements.txt` with initial dependencies: `fastapi`, `uvicorn`, `qdrant-client`, `sentence-transformers`, `langchain`, `pytest`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that must be complete before any user story can be implemented.

- [ ] T006 [P] Implement the embedding model wrapper in `api/embedding_model.py`. It should load a `SentenceTransformer` model.
- [ ] T007 Implement the vector store abstraction in `api/vector_store.py`. It should encapsulate the synchronous `QdrantClient` and provide methods for adding and searching documents. This depends on T006.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 2 - Ingest book content (Priority: P2)

**Goal**: To process and load the book's content into the vector store so the chatbot can use it.

**Independent Test**: The ingestion script can be run, and the data can be verified in the Qdrant vector store.

### Implementation for User Story 2

- [ ] T008 [US2] Implement the ingestion logic in `api/ingest.py`. This script will recursively read text files, chunk them, and use the services from `api/embedding_model.py` and `api/vector_store.py` to store the embedded chunks.
- [ ] T009 [US2] Create a test for the ingestion process in `api/tests/test_ingest.py`. This test should check if a sample document is correctly ingested.

**Checkpoint**: At this point, User Story 2 should be fully functional and testable. Content can be loaded into the application.

---

## Phase 4: User Story 1 - Ask a question about the book content (Priority: P1) 🎯 MVP

**Goal**: To allow users to ask questions and get relevant answers from the book.

**Independent Test**: The API can be called with a question, and it should return relevant text chunks.

### Implementation for User Story 1

- [ ] T010 [US1] Implement the FastAPI application in `api/main.py`.
- [ ] T011 [US1] Add the `/ask` endpoint to `api/main.py`. It should accept a question and an optional `chapter_id`. It will use `api/vector_store.py` to retrieve relevant chunks.
- [ ] T012 [US1] Implement CORS middleware in `api/main.py` to allow all origins.
- [ ] T013 [US1] Create a test for the `/ask` endpoint in `api/tests/test_main.py`. This test should check if the endpoint returns the expected format and relevant chunks for a sample query.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. The application is now feature-complete for the MVP.

---

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T014 [P] Add detailed docstrings to all public functions and classes.
- [ ] T015 [P] Add logging to the application to trace requests and errors.
- [ ] T016 Run `pytest` to ensure all tests pass.
- [ ] T017 Validate the implementation against the `quickstart.md` (to be created).
