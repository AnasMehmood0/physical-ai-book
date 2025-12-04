---
id: 001
title: Created RAG Chatbot Backend Specification
stage: spec
date: 2025-12-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: rag-chatbot-backend
branch: 001-rag-chatbot-backend
user: unknown
command: /sp.specify Feature: RAG Chatbot Backend Goal: Create a Python FastAPI backend in a new api/ folder that serves as the "Brain" for the textbook, integrating the required components for the hackathon. Requirements: Project Structure: Create a folder named api in the root. Tech Stack: Use FastAPI, Qdrant in Local Memory Mode (location=":memory:"), and FastEmbed or SentenceTransformers for embeddings. Skill 1 (Bonus Points) - Ingestion (api/ingest.py): A script that reads all .md files from ../web/docs/, chunks them, and upserts them into Qdrant collection "physical_ai_book". Metadata: Store chapter_id with every chunk (for context-awareness). Skill 2 - The Brain (api/main.py): POST Endpoint /ask. It must accept {"question": "...", "chapter_id": "chapter1"}. It must filter Qdrant by chapter_id, retrieve the top 3 chunks, and return those chunks as the response. CORS: Configure CORS to allow * (all origins) for frontend communication.
labels: ["specification", "backend", "rag", "fastapi"]
links:
  spec: specs/001-rag-chatbot-backend/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/001-rag-chatbot-backend/spec.md
- specs/001-rag-chatbot-backend/checklists/requirements.md
tests:
null
---

## Prompt

Feature: RAG Chatbot Backend

Goal: Create a Python FastAPI backend in a new api/ folder that serves as the "Brain" for the textbook, integrating the required components for the hackathon.

Requirements:

Project Structure: Create a folder named api in the root.

Tech Stack: Use FastAPI, Qdrant in Local Memory Mode (location=":memory:"), and FastEmbed or SentenceTransformers for embeddings.

Skill 1 (Bonus Points) - Ingestion (api/ingest.py): A script that reads all .md files from ../web/docs/, chunks them, and upserts them into Qdrant collection "physical_ai_book". Metadata: Store chapter_id with every chunk (for context-awareness).

Skill 2 - The Brain (api/main.py): POST Endpoint /ask. It must accept {"question": "...", "chapter_id": "chapter1"}. It must filter Qdrant by chapter_id, retrieve the top 3 chunks, and return those chunks as the response.

CORS: Configure CORS to allow * (all origins) for frontend communication.

## Response snapshot

The RAG Chatbot Backend specification has been created and validated. Branch '001-rag-chatbot-backend' and spec file 'specs/001-rag-chatbot-backend/spec.md' are ready. All quality checks passed. The specification is ready for the '/sp.plan' phase.

## Outcome

- ✅ Impact: The feature specification for the RAG Chatbot Backend was successfully created and validated.
- 🧪 Tests: No tests were run during the spec creation phase.
- 📁 Files: specs/001-rag-chatbot-backend/spec.md, specs/001-rag-chatbot-backend/checklists/requirements.md
- 🔁 Next prompts: The next step is to run `/sp.plan`.
- 🧠 Reflection: The process of creating the spec involved identifying user scenarios, functional requirements, key entities, and success criteria based on the user's detailed feature description. The specification was then validated against a quality checklist.

## Evaluation notes (flywheel)

- Failure modes observed: Initial issues with `create-new-feature.ps1` due to incorrect JSON parsing/escaping for PowerShell, and `create-phr.sh` not being executable directly via Bash in the current environment. Resolved by manually crafting the PHR content and using the `Write` tool.
- Graders run and results (PASS/FAIL): Manual validation of spec against checklist: PASS.
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Improve robustness of script execution for cross-platform environments or provide clearer instructions/examples for complex string arguments.
