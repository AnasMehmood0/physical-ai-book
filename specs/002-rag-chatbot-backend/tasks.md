# Tasks: RAG Chatbot Backend

**Input**: Design documents from `specs/002-rag-chatbot-backend/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks are included as per the 'Test-First' principle in the constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- Paths are relative to the repository root.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [X] T001 Create the directory structure `api/src/core`, `api/src/models`, and `api/tests` as defined in `plan.md`.
- [X] T002 Create a `requirements.txt` file in `api/` with initial dependencies: `fastapi`, `uvicorn`, `qdrant-client`, `fastembed`, `pytest`.
- [X] T003 Create empty `__init__.py` files in `api/`, `api/src`, `api/src/core`, `api/src/models`, and `api/tests` to make them Python packages.

---

## Phase 2: User Story 1 - Content Ingestion (Priority: P1) 🎯 MVP

**Goal**: Process the textbook's markdown files so that they are searchable and can be used to answer user questions.

**Independent Test**: Run the ingestion script and verify that the content is correctly added to the Qdrant collection.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T004 [P] [US1] Create a test file `api/tests/test_ingest.py` with a test case for a successful ingestion of a dummy markdown file.
- [X] T005 [P] [US1] In `api/tests/test_ingest.py`, add a test case to handle an empty `web/docs` directory.
- [X] T006 [P] [US1] In `api/tests/test_ingest.py`, add a test case to ensure non-markdown files are ignored.

### Implementation for User Story 1

- [X] T007 [P] [US1] In `api/src/models/models.py`, define the Pydantic models for `ContentChunk` based on `data-model.md`.
- [X] T008 [US1] In `api/src/core/db.py`, implement the Qdrant client initialization and a function to get or create the "physical_ai_book" collection.
- [X] T009 [US1] In `api/src/core/embed.py`, implement the embedding generation logic using `FastEmbed`.
- [X] T010 [US1] In `api/src/ingest.py`, implement the logic to:
    - Recursively read `.md` files from the `web/docs` directory.
    - Chunk the text.
    - Generate embeddings for each chunk using the embedding service from `api/src/core/embed.py`.
    - Upsert the chunks with metadata (including `chapter_id`) into the Qdrant collection using the db service from `api/src/core/db.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. The ingestion script should run and populate the Qdrant collection.

---

## Phase 3: User Story 2 - Question Answering (Priority: P1)

**Goal**: Provide an API endpoint that returns relevant content chunks for a user's question, filtered by chapter.

**Independent Test**: Send a request to the `/ask` endpoint and verify that the response contains relevant content chunks from the correct chapter.

### Tests for User Story 2 ⚠️

- [X] T011 [P] [US2] In `api/tests/test_main.py`, write a test case for a successful request to the `/ask` endpoint. This test should mock the Qdrant client and embedding generation.
- [X] T012 [P] [US2] In `api/tests/test_main.py`, add a test case for a question that has no relevant chunks in the specified chapter.
- [X] T013 [P] [US2] In `api/tests/test_main.py`, add a test case for a request with a non-existent `chapter_id`.

### Implementation for User Story 2

- [X] T014 [US2] In `api/src/models/models.py`, define the Pydantic models for `AskRequest` and `AskResponse` based on `data-model.md`.
- [X] T015 [US2] In `api/src/main.py`, create the FastAPI application.
- [X] T016 [US2] In `api/src/main.py`, implement the `/ask` endpoint that:
    - Takes an `AskRequest` as input.
    - Generates an embedding for the question.
    - Queries the Qdrant collection, filtering by `chapter_id`.
    - Returns the top 3 results in an `AskResponse`.
- [X] T017 [US2] In `api/src/main.py`, configure CORS to allow all origins.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. The API should be runnable and respond to questions.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T018 [P] Add detailed docstrings to all functions in `api/src`.
- [ ] T019 Update `README.md` with instructions on how to run the backend, using content from `quickstart.md`.
- [ ] T020 Manually run through the `quickstart.md` to ensure it is accurate and complete.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **User Story 1 (Phase 2)**: Depends on Setup completion.
- **User Story 2 (Phase 3)**: Depends on Setup completion. Can run in parallel with User Story 1.
- **Polish (Phase 4)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (Content Ingestion)**: No dependencies on other stories.
- **User Story 2 (Question Answering)**: No hard dependency on US1 for implementation (can use mocked data for tests), but requires ingested data for end-to-end testing.

### Parallel Opportunities

- Once Setup is complete, User Story 1 and User Story 2 can be developed in parallel.
- Within each user story, test creation can be parallelized.
- Model creation can be parallelized with test creation.
