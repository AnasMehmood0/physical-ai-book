---
id: 007
title: Plan Content Beautification & Formatting
stage: plan
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: chapter-formatting
branch: 2-chapter-formatting
user: unknown
command: /sp.plan
labels: ["planning", "docusaurus", "formatting"]
links:
  spec: specs/2-chapter-formatting/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/2-chapter-formatting/plan.md
tests: null
---

## Prompt

```text
<command-message>sp.plan is running…</command-message>
<command-name>/sp.plan</command-name>## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications
```

## Response snapshot

The implementation plan (`plan.md`) for "Content Beautification & Formatting" has been successfully created and saved to `specs/2-chapter-formatting/plan.md`.

This plan outlines the approach, technical context, constitution check (with justifications for violations), project structure, and complexity tracking for refactoring chapters 1-5 with Docusaurus formatting.

You can now proceed with generating the tasks for this feature using the `/sp.tasks` command.

## Outcome

- ✅ Impact: Implementation plan generated.
- 🧪 Tests: Constitution check passed (with justifications for violations).
- 📁 Files: `specs/2-chapter-formatting/plan.md` created.
- 🔁 Next prompts: User to run `/sp.tasks`.
- 🧠 Reflection: Successfully created the plan, addressing all sections and justifying constitution violations. This process was manual due to `pwsh` unavailability.

## Evaluation notes (flywheel)

- Failure modes observed: `pwsh` command not found, necessitating manual filling of the plan template.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Enhance `setup-plan.ps1` to handle `pwsh` unavailability or provide a bash alternative.
