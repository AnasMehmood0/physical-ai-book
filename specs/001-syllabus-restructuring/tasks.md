# Tasks: Physical AI Syllabus Restructuring

**Input**: Design documents from `/specs/001-syllabus-restructuring/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: No specific tests were requested in the feature specification, so test tasks are not included here.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `frontend/src/` (Docusaurus is a frontend framework)
- Paths shown below assume Docusaurus project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Delete all existing files in `web/docs/`
- [x] T002 Update Docusaurus `title` to "Physical AI & Humanoid Robotics" in `docusaurus.config.ts` (or `.js`)
- [x] T003 Update Docusaurus `tagline` to "Bridging the Digital Brain and the Physical Body" in `docusaurus.config.ts` (or `.js`)

---

## Phase 3: User Story 1 - Restructure Documentation (Priority: P1) 🎯 MVP

**Goal**: The documentation structure reflects the "Physical AI & Humanoid Robotics" syllabus, allowing easy navigation.

**Independent Test**: The documentation site's sidebar navigation and URL paths should match the new syllabus structure, and all module `_spec.md` files are present and correctly populated.

### Implementation for User Story 1

- [ ] T004 [US1] Create directory `web/docs/01-foundations`
- [ ] T005 [US1] Create `_spec.md` for `01-foundations` with content in `web/docs/01-foundations/_spec.md`
- [ ] T006 [US1] Create directory `web/docs/02-ros2-nervous-system`
- [ ] T007 [US1] Create `_spec.md` for `02-ros2-nervous-system` with content in `web/docs/02-ros2-nervous-system/_spec.md`
- [ ] T008 [US1] Create directory `web/docs/03-digital-twin`
- [ ] T009 [US1] Create `_spec.md` for `03-digital-twin` with content in `web/docs/03-digital-twin/_spec.md`
- [ ] T010 [US1] Create directory `web/docs/04-isaac-robot-brain`
- [ ] T011 [US1] Create `_spec.md` for `04-isaac-robot-brain` with content in `web/docs/04-isaac-robot-brain/_spec.md`
- [ ] T012 [US1] Create directory `web/docs/05-humanoid-dev`
- [ ] T013 [US1] Create `_spec.md` for `05-humanoid-dev` with content in `web/docs/05-humanoid-dev/_spec.md`
- [ ] T014 [US1] Create directory `web/docs/06-vla-and-capstone`
- [ ] T015 [US1] Create `_spec.md` for `06-vla-and-capstone` with content in `web/docs/06-vla-and-capstone/_spec.md`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **User Stories (Phase 3+)**: All depend on Setup completion
  - User Story 1 can then proceed sequentially.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Setup (Phase 1) - No dependencies on other stories

### Within Each User Story

- Directories before files.

### Parallel Opportunities

- The tasks for creating directories and then populating their respective `_spec.md` files can be executed in parallel across different modules, assuming no file system conflicts. However, for clarity and sequential execution, they are listed here in order.

---

## Parallel Example: User Story 1

```bash
# Example of parallel creation of module directories (if not already existing):
Task: "Create directory web/docs/01-foundations"
Task: "Create directory web/docs/02-ros2-nervous-system"
# ... and so on for all 6 module directories

# Example of parallel creation of _spec.md files (after directories are created):
Task: "Create _spec.md for 01-foundations with content in web/docs/01-foundations/_spec.md"
Task: "Create _spec.md for 02-ros2-nervous-system with content in web/docs/02-ros2-nervous-system/_spec.md"
# ... and so on for all 6 _spec.md files
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 3: User Story 1
3. **STOP and VALIDATE**: Test User Story 1 independently by checking the file structure and Docusaurus configuration.
4. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup → Setup ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)

---

## Notes

- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
