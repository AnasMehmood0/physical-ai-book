# Data Model for Global Fixed Chat Widget (Corner Bubble)

This document outlines the primary data (state) managed by the frontend `GlobalChatWidget` component.

## 1. GlobalChatWidget Internal State

Represents the transient state of the chat widget within the user's browser session.

**Fields**:

- **isOpen**: (boolean) Indicates whether the chat box is expanded (`true`) or collapsed to a bubble icon (`false`).
  - *Default*: `false` (collapsed)
- **question**: (string) Stores the current text input by the user in the chat input field.
  - *Default*: `""` (empty string)
- **response**: (object | null) Stores the last received JSON response from the backend API.
  - *Default*: `null`
  - *Structure*: Expected to match the `AskResponse` schema defined in the backend's OpenAPI specification.
    - `results`: (array of objects) Each object represents a content chunk with `id` and `payload` (containing `content` and `chapter_id`).
- **chapter_id**: (string) A hardcoded identifier for the chapter context being sent with the user's question.
  - *Default*: `"ros2/architecture"` (for demonstration purposes as per spec)

**State Transitions**:

- `isOpen`: Toggled by clicking the chat bubble/close button.
- `question`: Updated dynamically as the user types into the input field.
- `response`: Updated upon successful receipt of a response from the backend API, or with an error object if the API call fails.
