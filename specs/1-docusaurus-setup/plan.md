# Implementation Plan: Initial Docusaurus Setup & Chapter Structure

**Branch**: `1-docusaurus-setup` | **Date**: 2025-12-01 | **Spec**: specs/1-docusaurus-setup/spec.md
**Input**: Feature specification from `specs/1-docusaurus-setup/spec.md`

## Summary

This plan outlines the steps to initialize a Docusaurus project within a 'web' folder, configure a 5-chapter sidebar structure, enable support for custom React components in Markdown for future "Swizzling" of the Docusaurus theme, and apply a modern, clean, academic color scheme. This foundational work is crucial for building the "Physical AI and Humanoid Robotics (Interactive Textbook)" platform.

## Technical Context

**Language/Version**: JavaScript (React), Node.js (LTS for Docusaurus CLI)
**Primary Dependencies**: Docusaurus, React, (npm/yarn)
**Storage**: N/A (Static site, content managed as Markdown files)
**Testing**: Docusaurus' built-in development server verification, visual inspection, potential Jest/React Testing Library for custom components (future)
**Target Platform**: Web (Static site generation), deployed to GitHub Pages
**Project Type**: Web application (Frontend)
**Performance Goals**: Fast page loads, smooth client-side navigation, minimal build times for static assets.
**Constraints**: Must reside in a `web/` directory. Must support custom React components embedded in Markdown for future 'Swizzling'. Must use a modern, clean, academic color scheme.
**Scale/Scope**: Initial setup for an interactive textbook with 5 primary chapters, designed to be easily extensible for future content and interactive features.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Spec-Driven Development**: This plan is directly derived from the feature specification (`specs/1-docusaurus-setup/spec.md`), ensuring alignment with the project's development methodology.
- [ ] **II. Reusable Skills (Subagents)**: While not directly implemented in this foundational setup, the plan explicitly accounts for future 'Swizzling' to integrate custom React components, which will be the interface for the Context-Aware AI Chatbot and potentially other reusable skills. (✅ Pending integration points for future skills)
- [x] **III. Context-Aware RAG for Chatbot**: The plan includes preparing Docusaurus configuration to support custom React components in Markdown, which is a prerequisite for the "Ask AI" button and the Context-Aware RAG chatbot's frontend integration.
- [x] **IV. Library-First**: Docusaurus itself is a framework, but the approach for custom React components (which will house future interactive elements and chatbot integration) will adhere to library-first principles, promoting modularity and testability.
- [x] **V. CLI Interface**: Docusaurus development heavily utilizes its own CLI (e.g., `docusaurus start`, `docusaurus build`), aligning with the principle of CLI-driven operations.
- [x] **VI. Test-First (NON-NEGOTIABLE)**: This plan includes explicit verification steps for project initialization, sidebar structure, and custom component rendering, ensuring a test-first approach to foundational setup.

## Project Structure

### Documentation (this feature)

```text
specs/1-docusaurus-setup/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command) - N/A for this plan
├── data-model.md        # Phase 1 output (/sp.plan command) - N/A for this plan
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command) - N/A for this plan
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
web/
├── blog/
├── docs/                 # Contains chapter markdown files
│   ├── intro.md          # Example intro page
│   ├── chapter1.md
│   ├── chapter2.md
│   ├── chapter3.md
│   ├── chapter4.md
│   └── chapter5.md
├── src/
│   ├── components/       # Custom React components, e.g., for Ask AI button
│   └── css/              # Custom CSS for academic theme
├── static/
├── docusaurus.config.js  # Main configuration file
├── sidebars.js           # Sidebar structure definition
└── package.json

```

**Structure Decision**: The chosen structure is a single Docusaurus project within a `web/` directory at the repository root. This aligns with standard Docusaurus project layouts and supports the specified requirements for documentation, custom components, and configuration.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| N/A | N/A | N/A |


## Phase 0: Outline & Research

**Purpose**: Identify and resolve any ambiguities in the technical context. For this feature, all technical context points are clear and actionable; therefore, no dedicated research phase or `research.md` is required at this time.

**Output**: No `research.md` generated.

## Phase 1: Design & Contracts

**Prerequisites:** Phase 0 (implicitly complete as no research was needed)

**Purpose**: Define data models and API contracts. For this feature, the focus is on frontend setup and content structure, so formal data models or API contracts are not generated in this phase. The only 'entity' is a `Chapter`, which is conceptualized in the Docusaurus sidebar/docs structure.

1.  **Extract entities from feature spec** → `data-model.md`:
    *   No formal `data-model.md` will be created as this phase is purely frontend structure and content organization.

2.  **Generate API contracts** from functional requirements:
    *   No API contracts (`contracts/`) are generated as this phase does not involve backend API development.

3.  **Generate quickstart.md**:
    *   Create `specs/1-docusaurus-setup/quickstart.md` with instructions for initializing the project, running the dev server, and verifying the sidebar structure.

4.  **Agent context update**:
    *   Update agent context to reflect Docusaurus, React, and Markdown as relevant technologies.

**Output**: `specs/1-docusaurus-setup/quickstart.md` created. Agent context updated.

