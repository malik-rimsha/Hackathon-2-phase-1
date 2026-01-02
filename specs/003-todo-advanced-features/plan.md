# Implementation Plan: Advanced Todo Features with Recurring Tasks and Time-Based Reminders

**Branch**: `003-todo-advanced-features` | **Date**: 2026-01-02 | **Spec**: [link to spec.md](spec.md)
**Input**: Feature specification from `/specs/003-todo-advanced-features/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements Advanced Level features for the Todo application, specifically recurring tasks and time-based reminders with browser notifications. The implementation extends the existing Basic and Intermediate level functionality by adding recurrence and due date/time attributes to the Task model, implementing auto-rescheduling logic for recurring tasks, and creating a notification system that works in both browser (with PyScript) and console environments. The solution uses Python standard library for core logic with PyScript for browser notifications, maintaining the in-memory storage approach as per the constitution.

## Technical Context

**Language/Version**: Python 3.13+ (as per constitution)
**Primary Dependencies**: Python standard library for core logic (datetime, enum, dataclasses); PyScript for browser notifications
**Storage**: In-memory (as per constitution - tasks lost on refresh/restart)
**Testing**: pytest (as per Python best practices)
**Target Platform**: Cross-platform console application with browser compatibility for notifications
**Project Type**: Single console application evolving through Basic → Intermediate → Advanced levels
**Performance Goals**: Fast response times for console operations; efficient polling for due date notifications
**Constraints**: Follow progressive feature implementation (Basic → Intermediate → Advanced); maintain all previous functionality
**Scale/Scope**: Single-user console application for task management evolving to include web notifications
**Architecture**: Extension of existing architecture with new attributes and notification system
**Runtime Environments**:
  - Console mode: Standard Python execution
  - Browser mode: PyScript for running Python in browser with notification support
**Key Libraries**:
  - Standard library: datetime, enum, dataclasses, json, argparse
  - Browser: PyScript for Python execution in browser, JavaScript bridge for notifications
**Data Model Extensions**:
  - Task model: Add recurrence (enum: DAILY, WEEKLY, MONTHLY) and due_datetime (datetime object)
  - Notification system: Polling mechanism for due tasks, browser notification API integration
**Integration Points**:
  - CLI commands: Extended to support recurrence and due date setting
  - Display: Enhanced to show recurrence indicators and due dates
  - Storage: In-memory storage extended with new attributes
**Security Considerations**: Minimal for this single-user application; focus on input validation
**Browser Compatibility**: Requires PyScript-compatible browser for notification features

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Confirm Python 3.13+ compatibility - CONFIRMED: Using Python 3.13+ as required
- [x] Verify dependencies align with feature level requirements (stdlib for Basic, additional as needed for Advanced) - CONFIRMED: Using standard library for core logic, PyScript for browser notifications
- [x] Ensure in-memory storage approach for Basic/Intermediate (evolve as needed for Advanced) - CONFIRMED: Maintaining in-memory storage as per constitution
- [x] Validate implementation follows progressive feature levels (Basic → Intermediate → Advanced) - CONFIRMED: Building on existing Basic and Intermediate functionality
- [x] Confirm adherence to clean code principles - CONFIRMED: Following Python best practices and PEP 8
- [x] Verify test-first approach will be followed - CONFIRMED: Will implement TDD as required
- [x] Ensure modular design for extensibility - CONFIRMED: Extending existing architecture with clear separation of concerns

## Project Structure

### Documentation (this feature)

```text
specs/003-todo-advanced-features/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   ├── __init__.py
│   ├── task.py          # Task model with title, description, status, ID, recurrence, due_datetime
│   └── recurrence.py    # Recurrence interval enum and rule model
├── services/
│   ├── __init__.py
│   ├── task_service.py  # Business logic for task operations
│   └── notification_service.py  # Notification logic for due tasks
├── cli/
│   ├── __init__.py
│   └── main.py          # Command-line interface with extended commands
├── lib/
│   ├── __init__.py
│   └── storage.py       # In-memory storage implementation
└── web/
    ├── __init__.py
    ├── pyscript_todo.py # PyScript-compatible version of the todo app
    └── index.html       # HTML file to run the todo app in browser with PyScript
```

### Tests (repository root)

```text
tests/
├── unit/
│   ├── __init__.py
│   ├── test_task.py     # Task model tests
│   ├── test_recurrence.py  # Recurrence model tests
│   ├── test_task_service.py  # Task service tests
│   └── test_notification_service.py  # Notification service tests
├── integration/
│   ├── __init__.py
│   └── test_cli.py      # CLI integration tests
└── browser/
    ├── __init__.py
    └── test_notifications.py  # Browser notification tests (if possible)
```

### Other Files

```text
├── README.md            # Updated with browser setup instructions
├── requirements.txt     # Python dependencies (if any beyond stdlib)
├── pyproject.toml       # Project configuration for UV
└── .gitignore          # Git ignore file
```

**Structure Decision**: Extending existing architecture with new modules for recurrence and notifications. Adding web directory for PyScript compatibility. Maintains clear separation of concerns between models, services, CLI interface, and storage. Follows constitution requirements for in-memory storage and stdlib-focused dependencies.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Browser dependency (PyScript) | For notification functionality as specified in requirements | Console-only would not meet requirement for browser notifications |
| Additional modules (recurrence, notification_service) | To maintain clean separation of concerns and extensibility | Adding everything to existing modules would create monolithic, hard-to-maintain code |
