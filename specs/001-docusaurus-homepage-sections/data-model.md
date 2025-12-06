# Data Model: Docusaurus Homepage Sections

**Feature Branch**: `001-docusaurus-homepage-sections`
**Created**: 2025-12-05

## Entities

- **Homepage Section**: A distinct visual and logical division of the homepage content.
    - Attributes: title (string), subtitle (string, optional), description (string, optional), ctaButtons (array of objects {label: string, link: string}), icons (array of strings, optional), backgroundColor (string, optional), containedModules (array of Learning Module IDs, optional), containedTechnologies (array of Technology Stack Item IDs, optional).
- **Learning Module**: Represents a key topic within the book.
    - Attributes: title (string), description (string), icon (string - path to image/SVG).
- **Hardware Platform**: Represents a type of hardware compatible with Physical AI concepts.
    - Attributes: icon (string - path to image/SVG).
- **Technology Stack Item**: Represents a specific technology used.
    - Attributes: name (string).
