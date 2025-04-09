# CONTRIBUTING.md

This document outlines our guidelines and best practices for contributing to the Titanic Survivor Prediction Application codebase. This is an internal document for our team members and our AI system – it is not intended for public release.

---

## 1. Code Contribution Guidelines

### Commit Messages
- Use the format: `type(scope): subject`
  - **Example:** `feat(auth): add JWT authentication endpoint`
- **Types** include, but are not limited to:
  - `feat` for new features
  - `fix` for bug fixes
  - `refactor` for code improvements without changing behavior
  - `docs` for documentation changes
  - `chore` for non-functional tasks (e.g. dependency updates)

### Branch Strategy
- **Protected Main Branch:**  
  - Do not commit directly to the main branch.
- **Dev Branch:**  
  - Use the `dev` branch for integrating ongoing work.
- **Feature Branches:**  
  - Create a separate branch for each new feature or fix (e.g., `feat/login`, `fix/api-timeout`).
  - Merge feature branches into `dev` via a pull request with appropriate reviews.

### Pull Request Process
- Ensure pull requests (PR) include a brief description of the changes.
- Reference any related issues or tasks.
- PRs must pass all automated tests and code style checks before merging.
- Request team reviews to maintain code quality and adherence to guidelines.

---

## 2. Code Quality and Documentation

### Code Standards
- Write well-commented, production-grade code.
- Follow the established coding standards (e.g., PEP 8 for Python, consistent style for TypeScript/React).
- Update inline documentation and READMEs where necessary.  

## Communication and Collaboration
- Use our internal communication channels (aka. team/random_iceberg WhatsApp group) for any questions or clarifications. 
- Regularly sync with the team during standups and code reviews.
- Document any significant changes or decisions in your PRs and the project documentation.

---

By following these guidelines, we maintain a clean, organized, and efficient development environment that supports rapid, iterative improvements.

Happy coding!