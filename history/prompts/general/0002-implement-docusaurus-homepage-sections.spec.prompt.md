---
id: 0002
title: Implement Docusaurus Homepage Sections
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: docusaurus-homepage-sections
branch: 002-deep-syllabus-restructuring
user: unknown
command: null
labels: ["docusaurus", "homepage", "ui", "sections", "styling"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - none
tests:
  - none
---

## Prompt

Hero Section:

Headline: "Physical AI & Humanoid Robotics"

Subtitle: "From ROS 2 to Vision-Language-Action Models"

Description: "Master robotics from fundamentals to advanced AI. Learn ROS 2, robot simulation, NVIDIA Isaac Sim, and build intelligent robots with VLA models."

Primary Button: "Start Learning" (Green background #25c2a0, links to /docs/foundations/01-embodied-intelligence).

Secondary Button: "Sign Up Free" (White background, Green text).

Modules Grid (4 Cards):

Create a clean 4-column grid section.

Card 1: "ROS 2 (Nervous System)" - Master Robot Operating System 2.

Card 2: "Simulation (Digital Twin)" - Learn Gazebo and physics.

Card 3: "Isaac Sim (Brain)" - Explore NVIDIA Isaac Sim.

Card 4: "VLA (Capstone)" - Build Vision-Language-Action models.

Hardware-Adaptive Section:

A distinct section with a Light Green Background.

Heading: "Hardware-Adaptive Learning"

Text: "Get personalized content tailored to your hardware setup."

Icons/Grid: Display icons for Laptop, RTX 4090, Jetson, and Cloud.

Tech Stack Footer:

A section at the bottom titled "Powered by Modern AI Stack".

List: Gemini 1.5 Flash, Qdrant Vector DB, FastAPI Backend, React + Docusaurus.

Styling: Update web/src/css/custom.css to support these new layouts (Grid, Hero, Feature Cards) using a modern, clean academic aesthetic.

## Response snapshot

Acknowledged new feature request for Docusaurus homepage sections. Proceeding to create a Prompt History Record for this request.

## Outcome

- ✅ Impact: Recorded the new feature request. Ready to create the specification.
- 🧪 Tests: None
- 📁 Files: None
- 🔁 Next prompts: Proceed with `/sp.specify` to create the feature specification.
- 🧠 Reflection: Successfully created PHR manually due to script absence. Prepared to initiate the new feature specification process.

## Evaluation notes (flywheel)

- Failure modes observed: The script `.specify/scripts/bash/create-phr.sh` is still missing, necessitating manual PHR generation.
- Graders run and results (PASS/FAIL): unspecified
- Prompt variant (if applicable): unspecified
- Next experiment (smallest change to try): The persistent absence of `create-phr.sh` indicates a need to either resolve the script path or fully transition PHR creation to agent-native tools, ensuring no reliance on external scripts for this core functionality.
