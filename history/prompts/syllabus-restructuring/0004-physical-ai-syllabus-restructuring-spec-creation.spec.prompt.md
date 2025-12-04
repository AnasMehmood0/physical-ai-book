---
id: 0004
title: Physical AI Syllabus Restructuring Spec Creation
stage: spec
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: syllabus-restructuring
branch: 001-syllabus-restructuring
user: unknown
command: /sp.specify
labels: ["specification", "feature"]
links:
  spec: specs/001-syllabus-restructuring/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-syllabus-restructuring/spec.md
 - specs/001-syllabus-restructuring/checklists/requirements.md
tests:

---

## Prompt

Feature: Physical AI Syllabus Restructuring

Goal: Rebuild the entire documentation structure to match the "Physical AI & Humanoid Robotics" syllabus.

Requirements:

Clean Slate: Remove ALL existing files in web/docs/. We are starting fresh.

Project Identity: Update docusaurus.config.ts (or .js):

Title: "Physical AI & Humanoid Robotics"

Tagline: "Bridging the Digital Brain and the Physical Body"

Folder Structure: Create the following folders in web/docs/ to match the course modules:

01-foundations (Weeks 1-2: Embodied Intelligence, Hardware)

02-ros2-nervous-system (Module 1: ROS 2, Nodes, URDF)

03-digital-twin (Module 2: Gazebo, Unity, Physics)

04-isaac-robot-brain (Module 3: NVIDIA Isaac Sim, VSLAM)

05-humanoid-dev (Weeks 11-12: Kinematics, Balance)

06-vla-and-capstone (Module 4: Voice-to-Action, Capstone)

The Specs: Inside EACH of these 6 folders, create a file named _spec.md.

This file should contain the Learning Outcomes and Key Topics for that specific module based on the provided syllabus context.

Example: 02-ros2-nervous-system/_spec.md should list "Nodes, Topics, Services, rclpy, URDF".

## Response snapshot

The `spec.md` file has been successfully created and updated in `specs/001-syllabus-restructuring/spec.md`. All clarification questions have been resolved, and the specification has passed all quality checks.

Branch Name: `001-syllabus-restructuring`
Spec File Path: `specs/001-syllabus-restructuring/spec.md`
Checklist: `specs/001-syllabus-restructuring/checklists/requirements.md` (All items passed)

The feature specification is now ready for the next phase, which could be `/sp.clarify` or `/sp.plan`.

## Outcome

- ✅ Impact: Feature specification created and validated.
- 🧪 Tests: No automated tests run, but specification content was validated against a checklist.
- 📁 Files: specs/001-syllabus-restructuring/spec.md, specs/001-syllabus-restructuring/checklists/requirements.md created/modified.
- 🔁 Next prompts: User to proceed with /sp.clarify or /sp.plan.
- 🧠 Reflection: Successfully created the feature specification, handling errors and clarifications.

## Evaluation notes (flywheel)

- Failure modes observed: Initial script failure, AskUserQuestion option limit.
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): Improve error handling and option limiting for AskUserQuestion.
