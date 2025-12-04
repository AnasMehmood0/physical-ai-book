# Feature Specification: Physical AI Syllabus Restructuring

**Feature Branch**: `001-syllabus-restructuring`
**Created**: 2025-12-04
**Status**: Draft
**Input**: User description: "Feature: Physical AI Syllabus Restructuring

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

Example: 02-ros2-nervous-system/_spec.md should list "Nodes, Topics, Services, rclpy, URDF"."

## User Scenarios & Testing

### User Story 1 - Restructure Documentation (Priority: P1)

As a course administrator, I want the documentation structure to reflect the "Physical AI & Humanoid Robotics" syllabus, so that students can easily navigate and find content relevant to each module.

**Why this priority**: This is the core requirement, affecting all users and the primary goal of the feature.

**Independent Test**: The documentation site's sidebar navigation and URL paths should match the new syllabus structure.

**Acceptance Scenarios**:

1. **Given** the current documentation, **When** the restructuring is applied, **Then** all old documentation files are removed.
2. **Given** the current documentation, **When** the restructuring is applied, **Then** the Docusaurus title is "Physical AI & Humanoid Robotics" and the tagline is "Bridging the Digital Brain and the Physical Body".
3. **Given** the current documentation, **When** the restructuring is applied, **Then** the `web/docs/` directory contains `01-foundations`, `02-ros2-nervous-system`, `03-digital-twin`, `04-isaac-robot-brain`, `05-humanoid-dev`, and `06-vla-and-capstone` folders.
4. **Given** the new module folders, **When** the restructuring is applied, **Then** each module folder contains an `_spec.md` file with relevant Learning Outcomes and Key Topics.

### Edge Cases

- What happens if `docusaurus.config.ts` (or `.js`) does not exist?
- How does the system handle an empty `web/docs/` directory before cleanup?

## Requirements

### Functional Requirements

- **FR-001**: The system MUST remove all existing files in the `web/docs/` directory.
- **FR-002**: The system MUST update the `docusaurus.config.ts` (or `.js`) file to set the title to "Physical AI & Humanoid Robotics".
- **FR-003**: The system MUST update the `docusaurus.config.ts` (or `.js`) file to set the tagline to "Bridging the Digital Brain and the Physical Body".
- **FR-004**: The system MUST create the following directories in `web/docs/`: `01-foundations`, `02-ros2-nervous-system`, `03-digital-twin`, `04-isaac-robot-brain`, `05-humanoid-dev`, `06-vla-and-capstone`.
- **FR-005**: The system MUST create an `_spec.md` file within each of the newly created module directories.
- **FR-006**: Each `_spec.md` file MUST contain the Learning Outcomes and Key Topics relevant to its module as specified in the syllabus context.
    - Example for `02-ros2-nervous-system/_spec.md`: "Nodes, Topics, Services, rclpy, URDF".
    - `01-foundations/_spec.md`:
        - Topic: Introduction to Physical AI (Weeks 1-2)
        - Key Concepts: Embodied Intelligence vs. Digital AI, The shift to physical laws.
        - Hardware Setup: Detailed guide on "The Sim Rig" (RTX 4070+, Ubuntu 22.04) and "Edge Brain" (Jetson Orin Nano).
        - Sensors: Technical deep dive into LiDAR, Depth Cameras (RealSense), and IMUs.
    - `03-digital-twin/_spec.md`:
        - Topic: Module 2 - The Digital Twin (Gazebo & Unity) (Weeks 6-7)
        - Core Skills: Setting up Gazebo simulation environments.
        - Formats: Differences between URDF and SDF.
        - Physics: Simulating gravity, collisions, and sensor noise.
        - Visualization: Using Unity for high-fidelity rendering.
    - `04-isaac-robot-brain/_spec.md`:
        - Topic: Module 3 - NVIDIA Isaac Platform (Weeks 8-10)
        - Tools: NVIDIA Isaac SDK and Isaac Sim.
        - Perception: AI-powered perception pipelines and VSLAM.
        - Navigation: Using Nav2 for path planning.
        - Training: Intro to Reinforcement Learning for controls.
    - `05-humanoid-dev/_spec.md`:
        - Topic: Humanoid Robot Development (Weeks 11-12)
        - Physics: Kinematics and Dynamics of bipedal robots.
        - Locomotion: Bipedal walking, ZMP (Zero Moment Point), and Balance Control.
        - Manipulation: Grasping objects with humanoid hands.
    - - `06-vla-and-capstone/_spec.md`:
    - Topic: Module 4 - Vision-Language-Action (VLA) & Capstone
    - Context: Week 13 and Final Project
    - VLA Concepts:
        - Voice-to-Action: Using OpenAI Whisper to convert speech to text commands.
        - Cognitive Planning: Using LLMs to translate natural language (e.g., "Clean the room") into executable ROS 2 action sequences.
    - Capstone Project: "The Autonomous Humanoid"
        - The Pipeline: Voice Command -> Path Planning -> Obstacle Navigation -> Computer Vision (Object ID) -> Manipulation.
        - Integration: Combining Module 1 (ROS 2), Module 2 (Simulation), and Module 3 (Isaac) into a single functional demo.

## Success Criteria

### Measurable Outcomes

- **SC-001**: The `web/docs/` directory contains exactly 6 new module folders and no other files from the previous structure.
- **SC-002**: The `docusaurus.config.ts` (or `.js`) file reflects the new title and tagline.
- **SC-003**: Each of the 6 module folders contains a non-empty `_spec.md` file.
