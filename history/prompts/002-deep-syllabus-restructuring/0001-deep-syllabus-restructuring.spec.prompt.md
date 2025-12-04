---
id: 0001
title: Deep Syllabus Restructuring Specification
stage: spec
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: 002-deep-syllabus-restructuring
branch: 002-deep-syllabus-restructuring
user: user
command: /sp.specify
labels: ["spec", "restructuring"]
links:
  spec: C:\Users\HP\specs\002-deep-syllabus-restructuring\spec.md
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\HP\specs\002-deep-syllabus-restructuring\spec.md
 - C:\Users\HP\specs\002-deep-syllabus-restructuring\checklists\requirements.md
tests:
null
---

## Prompt

Feature: Deep Syllabus Restructuring

Goal: Rebuild the book with a nested folder structure to match the detailed "Physical AI" syllabus.

Requirements:

Clean Slate: Delete all existing flat files in web/docs/.

Module 1 (Foundations): Create folder web/docs/01-foundations/.

Create 01-embodied-intelligence.md (Intro, Why Physical AI).

Create 02-hardware-lab.md (Sim Rig vs Edge Kit specs).

Module 2 (ROS 2): Create folder web/docs/02-ros2/.

Create 01-architecture.md (Nodes, Topics, Services).

Create 02-python-code.md (rclpy examples).

Module 3 (Simulation): Create folder web/docs/03-simulation/.

Create 01-gazebo-physics.md (URDF, Gravity, Collisions).

Create 02-unity-hri.md (High-fidelity rendering).

Module 4 (Isaac Sim): Create folder web/docs/04-isaac/.

Create 01-isaac-sdk.md (VSLAM, Nav2).

Create 02-reinforcement-learning.md (Sim-to-Real).

Module 5 (VLA & Capstone): Create folder web/docs/05-vla/.\n\nCreate 01-whisper-voice.md (Voice-to-Action).\n\nCreate 02-capstone-project.md (The Autonomous Humanoid pipeline).\n
Content Constraint: Fill all files with detailed academic content based on the provided syllabus.

## Response snapshot

Generated specification for 'Deep Syllabus Restructuring' at C:\Users\HP\specs\002-deep-syllabus-restructuring\spec.md.
All items in the specification quality checklist (C:\Users\HP\specs\002-deep-syllabus-restructuring\checklists\requirements.md) have passed.
The feature is ready for planning.

## Outcome

- ✅ Impact: The specification for the "Deep Syllabus Restructuring" feature has been successfully created, detailing user scenarios, functional requirements, and measurable success criteria.
- 🧪 Tests: No tests were run during the specification generation.
- 📁 Files: C:\Users\HP\specs\002-deep-syllabus-restructuring\spec.md and C:\Users\HP\specs\002-deep-syllabus-restructuring\checklists\requirements.md were created/modified.
- 🔁 Next prompts: The next step is to run `/sp.plan` to develop an implementation plan based on this specification.
- 🧠 Reflection: Overcame persistent issues with `create-new-feature.ps1` by manually creating the spec directory and writing the spec file, followed by creating and passing the quality checklist. This ensured the /sp.specify command completed successfully despite environmental challenges with the automated script.

## Evaluation notes (flywheel)

- Failure modes observed: Initial failures of `create-new-feature.ps1` due to quoting issues and "file already exists" errors.
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Investigate `create-new-feature.ps1` script behavior in the current environment or provide an alternative mechanism for spec file creation.
