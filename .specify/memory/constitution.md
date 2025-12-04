<!-- Sync Impact Report:
Version change: 0.0.0 → 0.1.0
Modified principles:
  - [PROJECT_NAME] → Physical AI and Humanoid Robotics (Interactive Textbook)
  - [PRINCIPLE_1_NAME] → Spec-Driven Development
  - [PRINCIPLE_2_NAME] → Reusable Skills (Subagents)
  - [PRINCIPLE_3_NAME] → Context-Aware RAG for Chatbot
  - [PRINCIPLE_4_NAME] → Library-First
  - [PRINCIPLE_5_NAME] → CLI Interface
  - [PRINCIPLE_6_NAME] → Test-First (NON-NEGOTIABLE)
  - [SECTION_2_NAME] → Technology Stack and Deployment
  - [SECTION_3_NAME] → Quality Gates
  - [GOVERNANCE_RULES] → Governance details updated
  - [LAST_AMENDED_DATE] → 2025-12-01
Added sections: None
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending (Review "Constitution Check" section for alignment with new principles.)
  - .specify/templates/spec-template.md: ⚠ pending (Review how spec should explicitly reflect principles like "Context-Aware RAG" and "Reusable Skills".)
  - .specify/templates/tasks-template.md: ⚠ pending (Review task categorization and examples for alignment with "Reusable Skills" and "Context-Aware RAG" implementation.)
  - .specify/templates/commands/sp.constitution.md: ✅ updated (This file itself)
  - .specify/templates/commands/sp.phr.md: ❌ Not Applicable (file not found)
Follow-up TODOs:
  - TODO(RATIFICATION_DATE): To be determined by project stakeholders.
-->
# Physical AI and Humanoid Robotics (Interactive Textbook) Constitution

## Core Principles

### I. Spec-Driven Development
All code MUST be generated via the Specify -> Plan -> Task -> Implement loop. This ensures a structured and verifiable development process.

### II. Reusable Skills (Subagents)
DO NOT write one-off scripts. All complex or repeatable functionalities MUST be encapsulated as reusable 'Skills' (Subagents) within a 'skills/' folder.

### III. Context-Aware RAG for Chatbot
The AI Chatbot MUST implement Context-Aware RAG. It MUST send the `current_chapter_id` to the backend, enabling responses based *only* on the current chapter the student is reading.

### IV. Library-First
Every significant feature or component starts as a standalone library; Libraries MUST be self-contained, independently testable, and documented; A clear purpose is required - no organizational-only libraries.

### V. CLI Interface
Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats.

### VI. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced.

## Technology Stack and Deployment

Frontend: Docusaurus (React-based). Custom 'Ask AI' floating button implemented via Swizzling in the text layout.
Backend: Python FastAPI, with an endpoint `/ask` connecting to Qdrant.
Database: Qdrant (Vector Database) for storing book embeddings.
Deployment: GitHub Pages (Frontend) + Vercel (Backend).

## Quality Gates

All code MUST pass automated tests and adhere to code quality standards. Manual review is required for all pull requests.

## Governance

All PRs/reviews MUST verify compliance with these principles; Complexity MUST be justified; Use the official documentation for runtime development guidance.

**Version**: 0.1.0 | **Ratified**: TODO(RATIFICATION_DATE): To be determined by project stakeholders. | **Last Amended**: 2025-12-01
