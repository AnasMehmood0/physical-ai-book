# Research for Global Fixed Chat Widget (Corner Bubble)

No specific research was required for this feature as the technical stack (React/Docusaurus) and implementation approach (swizzling) are well-understood. The backend API details are also well-defined.

## Decisions

- **Framework**: React, as it's the underlying framework for Docusaurus.
- **Integration Method**: Docusaurus Swizzling for the `Layout` component is chosen to ensure the widget appears globally on all pages.
- **Styling**: CSS Modules (`.module.css`) are used for component-specific styling to avoid global style collisions.
- **Backend Communication**: Standard `fetch` API for POST requests to the local FastAPI backend.
- **Chat Logic**: State management for toggle and input/response is handled directly within the `GlobalChatWidget` component using React's `useState` hook.
