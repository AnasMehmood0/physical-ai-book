# Feature Specification: Global Fixed Chat Widget (Corner Bot)

**Feature Branch**: `003-global-chat-widget`  
**Created**: 2025-12-06
**Status**: Draft  
**Input**: User description: "Task: Implement Global Fixed Chat Widget (Corner Bot) Goal: Create a final, polished, fixed-position chat interface that appears on ALL pages of the website, matching the professional bubble style. Instructions: Create a new React Component (GlobalChatWidget.tsx) containing the chat input/button logic (sending POST to http://127.0.0.1:8000/ask). Styling: Apply CSS to this component to give it a fixed position (position: fixed; bottom: 20px; right: 20px). Include a minimal, togglable design (a bubble icon that expands into the chat box). Global Integration (Swizzle Layout): Find the appropriate Docusaurus theme layout file (e.g., src/theme/Layout/index.tsx) and import/render GlobalChatWidget there. This makes the bot appear on every page. Cleanup: Remove the previous, messy ChatInterface import from web/src/pages/index.tsx. Logic: Ensure the chat logic sends the query to http://127.0.0.1:8000/ask and displays the retrieved chunk response."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Global Chat Access (Priority: P1)

As a user browsing the website, I want to see a chat bubble consistently available in the corner of every page, so I can easily initiate a conversation with the AI assistant at any time.

**Why this priority**: This is the core user experience for the global chat widget, ensuring discoverability and constant access to the AI assistant.

**Independent Test**: This can be fully tested by navigating across different pages of the website and verifying the presence and consistent positioning of the chat bubble.

**Acceptance Scenarios**:

1. **Given** I am on any page of the Docusaurus website, **When** the page loads, **Then** a chat bubble icon is displayed in a fixed position (e.g., bottom-right corner) of the viewport.
2. **Given** the chat bubble is displayed, **When** I click on the chat bubble, **Then** the chat interface expands, revealing an input field and a "Ask" button.
3. **Given** the chat interface is expanded, **When** I click on the chat bubble again (which now acts as a close button), **Then** the chat interface collapses back to just the bubble icon.

---

### User Story 2 - Context-Aware Question Answering (Priority: P1)

As a user interacting with the expanded chat interface, I want to ask a question and receive a relevant answer from the AI, demonstrating its understanding of the textbook's content.

**Why this priority**: This is the primary function of the chat widget, providing value by leveraging the backend RAG capabilities.

**Independent Test**: This can be tested by opening the chat widget, typing a question, and verifying that a response is received and displayed.

**Acceptance Scenarios**:

1. **Given** the chat interface is expanded, **When** I type a question into the input field and click the "Ask" button, **Then** a POST request is sent to the backend API (`http://127.0.0.1:8000/ask`).
2. **Given** a request is sent to the API, **Then** the request body includes my `question` and a hardcoded `chapter_id` (e.g., "ros2/architecture").
3. **Given** a response is received from the API, **Then** the raw JSON response content is displayed within the chat interface.

---

### Edge Cases

- What happens if the backend API is unreachable or returns an error? How is this communicated to the user?
- How does the chat interface handle very long questions or responses?
- What is the visual behavior of the chat bubble/widget across different screen sizes (responsive design)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST implement a React component (`GlobalChatWidget.tsx`) responsible for the chat interface logic.
- **FR-002**: The `GlobalChatWidget` MUST be integrated into the Docusaurus theme's `Layout` component to ensure its presence on all pages.
- **FR-003**: The `GlobalChatWidget` MUST have a togglable design, initially appearing as a minimal bubble icon that expands into a full chat box upon user interaction.
- **FR-004**: The `GlobalChatWidget` MUST send user questions as POST requests to the backend API at `http://127.0.0.1:8000/ask`.
- **FR-005**: API requests from the `GlobalChatWidget` MUST include the user's `question` and a predefined `chapter_id` (e.g., "ros2/architecture").
- **FR-006**: The `GlobalChatWidget` MUST display the raw JSON response received from the backend API.
- **FR-007**: The previous `ChatInterface` component and its integration in `web/src/pages/index.tsx` MUST be removed.

### Key Entities *(include if feature involves data)*

- **GlobalChatWidget**: The React component encapsulating the chat interface, logic, and styling.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The chat bubble icon is visible and consistently positioned on 100% of website pages.
- **SC-002**: The chat interface expands/collapses smoothly within 0.5 seconds of clicking the toggle button.
- **SC-003**: The AI assistant responds to 95% of valid questions within 5 seconds.
- **SC-004**: The chat widget functions correctly across common browser and device viewport sizes (e.g., desktop, tablet, mobile).