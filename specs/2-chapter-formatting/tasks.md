# Tasks: Content Beautification & Formatting

**Input**: Design documents from `/specs/2-chapter-formatting/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Not explicitly requested in spec.md. Manual visual inspection will be performed as per the Independent Test.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `web/docs/` for chapter files

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: No explicit setup required for this refactoring task.

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: No foundational tasks are explicitly required that block user story implementation.

## Phase 3: User Story 1 - Enhance Readability of Chapter Content (Priority: P1) 🎯 MVP

**Goal**: Make book chapters (web/docs/chapter1.md through web/docs/chapter5.md) more visually appealing and easier to read using Docusaurus features.

**Independent Test**: Visually inspect each chapter file (web/docs/chapter1.md through web/docs/chapter5.md) to confirm that key concepts are highlighted with appropriate admonitions, key acronyms are bolded on first appearance, and important statements use blockquotes, without altering the original content or the `<MyCustomComponent />` tag.

### Implementation for User Story 1

- [ ] T001 [P] [US1] Read content of `web/docs/chapter1.md` for processing.
- [ ] T002 [P] [US1] Apply `:::info` admonitions for definitions in `web/docs/chapter1.md`.
- [ ] T003 [P] [US1] Apply `:::tip` admonitions for interesting facts/history in `web/docs/chapter1.md`.
- [ ] T004 [P] [US1] Apply `:::danger` or `:::warning` admonitions for challenges in `web/docs/chapter1.md`.
- [ ] T005 [P] [US1] Bold first occurrence of key acronyms (ZMP, SLAM, LiDAR) in `web/docs/chapter1.md`.
- [ ] T006 [P] [US1] Apply `> Blockquotes` for important statements in `web/docs/chapter1.md`.
- [ ] T007 [P] [US1] Write formatted content back to `web/docs/chapter1.md`.

- [ ] T008 [P] [US1] Read content of `web/docs/chapter2.md` for processing.
- [ ] T009 [P] [US1] Apply `:::info` admonitions for definitions in `web/docs/chapter2.md`.
- [ ] T010 [P] [US1] Apply `:::tip` admonitions for interesting facts/history in `web/docs/chapter2.md`.
- [ ] T011 [P] [US1] Apply `:::danger` or `:::warning` admonitions for challenges in `web/docs/chapter2.md`.
- [ ] T012 [P] [US1] Bold first occurrence of key acronyms (ZMP, SLAM, LiDAR) in `web/docs/chapter2.md`.
- [ ] T013 [P] [US1] Apply `> Blockquotes` for important statements in `web/docs/chapter2.md`.
- [ ] T014 [P] [US1] Write formatted content back to `web/docs/chapter2.md`.

- [ ] T015 [P] [US1] Read content of `web/docs/chapter3.md` for processing.
- [ ] T016 [P] [US1] Apply `:::info` admonitions for definitions in `web/docs/chapter3.md`.
- [ ] T017 [P] [US1] Apply `:::tip` admonitions for interesting facts/history in `web/docs/chapter3.md`.
- [ ] T018 [P] [US1] Apply `:::danger` or `:::warning` admonitions for challenges in `web/docs/chapter3.md`.
- [ ] T019 [P] [US1] Bold first occurrence of key acronyms (ZMP, SLAM, LiDAR) in `web/docs/chapter3.md`.
- [ ] T020 [P] [US1] Apply `> Blockquotes` for important statements in `web/docs/chapter3.md`.
- [ ] T021 [P] [US1] Write formatted content back to `web/docs/chapter3.md`.

- [ ] T022 [P] [US1] Read content of `web/docs/chapter4.md` for processing.
- [ ] T023 [P] [US1] Apply `:::info` admonitions for definitions in `web/docs/chapter4.md`.
- [ ] T024 [P] [US1] Apply `:::tip` admonitions for interesting facts/history in `web/docs/chapter4.md`.
- [ ] T025 [P] [US1] Apply `:::danger` or `:::warning` admonitions for challenges in `web/docs/chapter4.md`.
- [ ] T026 [P] [US1] Bold first occurrence of key acronyms (ZMP, SLAM, LiDAR) in `web/docs/chapter4.md`.
- [ ] T027 [P] [US1] Apply `> Blockquotes` for important statements in `web/docs/chapter4.md`.
- [ ] T028 [P] [US1] Write formatted content back to `web/docs/chapter4.md`.

- [ ] T029 [P] [US1] Read content of `web/docs/chapter5.md` for processing.
- [ ] T030 [P] [US1] Apply `:::info` admonitions for definitions in `web/docs/chapter5.md`.
- [ ] T031 [P] [US1] Apply `:::tip` admonitions for interesting facts/history in `web/docs/chapter5.md`.
- [ ] T032 [P] [US1] Apply `:::danger` or `:::warning` admonitions for challenges in `web/docs/chapter5.md`.
- [ ] T033 [P] [US1] Bold first occurrence of key acronyms (ZMP, SLAM, LiDAR) in `web/docs/chapter5.md`.
- [ ] T034 [P] [US1] Apply `> Blockquotes` for important statements in `web/docs/chapter5.md`.
- [ ] T035 [P] [US1] Write formatted content back to `web/docs/chapter5.md`.

**Checkpoint**: At this point, User Story 1 should be fully functional with all chapters formatted.

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Final review to ensure all formatting is correctly applied.

- [ ] T036 Manually review `web/docs/chapter1.md` for correct formatting.
- [ ] T037 Manually review `web/docs/chapter2.md` for correct formatting.
- [ ] T038 Manually review `web/docs/chapter3.md` for correct formatting.
- [ ] T039 Manually review `web/docs/chapter4.md` for correct formatting.
- [ ] T040 Manually review `web/docs/chapter5.md` for correct formatting.

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: N/A
- **Foundational (Phase 2)**: N/A
- **User Stories (Phase 3+)**: Can start immediately.
- **Polish (Final Phase)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies on other stories.

### Within Each User Story

- Read content before applying formatting.
- Apply formatting before writing back to the file.

### Parallel Opportunities

- Tasks related to different chapters can be performed in parallel (e.g., T001-T007 for chapter1 can run in parallel with T008-T014 for chapter2).
- Within each chapter's formatting sequence, tasks are generally sequential.

## Parallel Example: User Story 1

```bash
# Example of parallel processing for different chapters
Task: "Process and format web/docs/chapter1.md"
Task: "Process and format web/docs/chapter2.md"
Task: "Process and format web/docs/chapter3.md"
Task: "Process and format web/docs/chapter4.md"
Task: "Process and format web/docs/chapter5.md"
```

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 3: User Story 1 (all formatting tasks for chapters 1-5).
2. **STOP and VALIDATE**: Manually review all formatted chapters.

### Incremental Delivery

1. Format Chapter 1 → Manually test.
2. Format Chapter 2 → Manually test.
3. ...and so on for remaining chapters.

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
