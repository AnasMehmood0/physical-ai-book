# Tasks: Global Fixed Chat Widget (Corner Bubble)

**Input**: Design documents from `specs/004-global-chat-widget/`
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

**Purpose**: Basic component and styling file creation.

- [X] T001 Create the React component file `web/src/components/GlobalChatWidget.tsx`.
- [X] T002 Create the CSS Module file `web/src/components/GlobalChatWidget.module.css`.

---

## Phase 2: User Story 1 - Global Chat Access (Priority: P1) 🎯 MVP

**Goal**: See a chat bubble consistently available in the corner of every page, and toggle it to expand/collapse.

**Independent Test**: Navigate across different pages of the website and verify the presence and consistent positioning of the chat bubble, and its toggle functionality.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T003 [P] [US1] Create a test file `web/src/components/__tests__/GlobalChatWidget.test.tsx` for the component's initial rendering and toggle functionality.
- [X] T004 [P] [US1] In `web/src/components/__tests__/GlobalChatWidget.test.tsx`, add a test to verify the chat bubble is visible on load.
- [X] T005 [P] [US1] In `web/src/components/__tests__/GlobalChatWidget.test.tsx`, add a test to verify clicking the bubble toggles the chat box visibility.

### Implementation for User Story 1

- [X] T006 [P] [US1] Implement the basic structure of `GlobalChatWidget.tsx` with toggle state and a bubble icon.
- [X] T007 [P] [US1] Apply fixed positioning and initial bubble styling in `web/src/components/GlobalChatWidget.module.css`.
- [X] T008 [US1] Swizzle the Docusaurus `Layout` component by creating `web/src/theme/Layout/index.tsx`.
- [X] T009 [US1] Import and render `GlobalChatWidget` in `web/src/theme/Layout/index.tsx`.
- [X] T010 [US1] Create an empty `web/src/theme/Layout/styles.module.css` to satisfy module imports.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. The chat widget should appear globally and its bubble/box toggle should work.

---

## Phase 3: User Story 2 - Context-Aware Question Answering (Priority: P1)

**Goal**: Allow users to ask questions via the chat interface and display relevant AI responses.

**Independent Test**: Open the chat widget, type a question, click "Ask", and verify that a response is received and displayed.

### Tests for User Story 2 ⚠️

- [X] T011 [P] [US2] In `web/src/components/__tests__/GlobalChatWidget.test.tsx`, add a test to verify that submitting a question sends a POST request to the correct API endpoint with the expected payload. (Mock fetch API).
- [X] T012 [P] [US2] In `web/src/components/__tests__/GlobalChatWidget.test.tsx`, add a test to verify that the API response (JSON) is displayed correctly in the chat box.

### Implementation for User Story 2

- [X] T013 [US2] Implement the API connection logic within `web/src/components/GlobalChatWidget.tsx` (using `fetch` API).
- [X] T014 [US2] Implement logic to display the raw JSON response in `web/src/components/GlobalChatWidget.tsx`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. The chat widget should provide full question-answering functionality.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final touches and cleanup.

- [X] T015 [P] Clean up `web/src/pages/index.tsx` by removing any leftover `ChatInterface` components or imports.
- [ ] T016 Manually test the chat widget across different Docusaurus pages and various screen sizes to ensure responsiveness and consistent behavior.
- [X] T017 Update `package.json` with any new dependencies if necessary.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **User Story 1 (Phase 2)**: Depends on Setup completion.
- **User Story 2 (Phase 3)**: Depends on Setup completion. Can run in parallel with User Story 1's initial implementation (T006, T007) but needs the basic UI in place.
- **Polish (Phase 4)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (Global Chat Access)**: No dependencies on other stories.
- **User Story 2 (Context-Aware Question Answering)**: Requires the basic UI elements and toggle functionality from US1.

### Within Each User Story

- Tests MUST be written and FAIL before implementation.
- Basic UI and styling before complex logic.

### Parallel Opportunities

- Within US1, creating the component file and CSS module can be parallel.
- Test creation for each user story can be parallelized with initial component scaffolding.
- Once US1's basic UI is in place, US2's logic can be developed in parallel.

---

## Parallel Example: User Story 1

```bash
# Tests for User Story 1:
Task: "Create a test file web/src/components/__tests__/GlobalChatWidget.test.tsx"
Task: "In web/src/components/__tests__/GlobalChatWidget.test.tsx, add a test to verify the chat bubble is visible on load."
Task: "In web/src/components/__tests__/GlobalChatWidget.test.tsx, add a test to verify clicking the bubble toggles the chat box visibility."

# Implementation for User Story 1 (can start once tests are failing):
Task: "Implement the basic structure of GlobalChatWidget.tsx with toggle state and a bubble icon."
Task: "Apply fixed positioning and initial bubble styling in web/src/components/GlobalChatWidget.module.css."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently (global presence, toggle functionality)
4. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup together.
2. Once Setup is done:
   - Developer A: User Story 1 (UI, Toggle, Global Integration)
   - Developer B: User Story 2 (API Integration, Response Display)
3. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
