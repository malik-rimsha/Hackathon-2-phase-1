# Implementation Tasks: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Branch**: 001-todo-console-app
**Created**: 2025-01-01
**Status**: Draft
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

## Implementation Strategy

The implementation will follow an incremental approach with each user story being independently testable. We'll start with the foundational components and then implement each user story in priority order (P1 through P5). The implementation will follow the two-file structure with clear separation between data model/business logic (todo.py) and CLI interface (main.py).

## Dependencies

User stories are designed to be independent but share foundational components. The foundational components (Task dataclass, TodoList class) must be implemented before the user story-specific features.

## Parallel Execution Examples

- T003 [P] and T004 [P] can be executed in parallel as they modify different files
- Within each user story phase, tasks that modify different components can be executed in parallel

---

## Phase 1: Setup

- [x] T001 Create project structure with src/ directory
- [x] T002 Create README.md with UV setup instructions
- [x] T003 [P] Create src/todo.py file
- [x] T004 [P] Create src/main.py file

---

## Phase 2: Foundational Components

- [x] T005 Implement Task dataclass in src/todo.py with id, title, description, completed fields
- [x] T006 Implement TodoList class in src/todo.py with tasks list and next_id
- [x] T007 Implement add_task method in TodoList class
- [x] T008 Implement get_all_tasks method in TodoList class
- [x] T009 Implement get_task_by_id method in TodoList class
- [x] T010 Implement update_task method in TodoList class
- [x] T011 Implement delete_task method in TodoList class
- [x] T012 Implement mark_task_completed method in TodoList class
- [x] T013 Add type hints and docstrings to all methods in src/todo.py

---

## Phase 3: User Story 1 - Add a new task (Priority: P1)

**Story Goal**: Implement the ability for users to add new tasks with title and description

**Independent Test Criteria**:
- User can add a task with title and description
- Task appears in the task list with a unique ID and incomplete status
- User can add a task with only a title (empty description)

**Tasks**:
- [x] T014 [US1] Implement add task functionality in CLI menu in src/main.py
- [x] T015 [US1] Implement input handling for task title in src/main.py
- [x] T016 [US1] Implement input handling for task description in src/main.py
- [x] T017 [US1] Display success message with new task ID after adding task in src/main.py
- [x] T018 [US1] Add validation to ensure title is not empty in src/todo.py
- [x] T019 [US1] Test adding task with title and description works correctly

---

## Phase 4: User Story 2 - View all tasks (Priority: P2)

**Story Goal**: Implement the ability for users to view all tasks with their status

**Independent Test Criteria**:
- User can view all tasks with ID, title, description, and completion status
- Appropriate message is shown when no tasks exist

**Tasks**:
- [x] T020 [US2] Implement view all tasks functionality in CLI menu in src/main.py
- [x] T021 [US2] Format and display tasks with ID, status indicator, title, and description in src/main.py
- [x] T022 [US2] Display appropriate message when no tasks exist in src/main.py
- [x] T023 [US2] Test viewing tasks works correctly after adding tasks

---

## Phase 5: User Story 3 - Update task details (Priority: P3)

**Story Goal**: Implement the ability for users to update task details by ID

**Independent Test Criteria**:
- User can update task title and/or description by ID
- Appropriate error message is shown when updating non-existent task

**Tasks**:
- [x] T024 [US3] Implement update task functionality in CLI menu in src/main.py
- [x] T025 [US3] Implement input handling for task ID in src/main.py
- [x] T026 [US3] Implement input handling for new title and description in src/main.py
- [x] T027 [US3] Display success message after updating task in src/main.py
- [x] T028 [US3] Display error message when updating non-existent task in src/main.py
- [x] T029 [US3] Test updating task details works correctly

---

## Phase 6: User Story 4 - Delete a task by ID (Priority: P4)

**Story Goal**: Implement the ability for users to delete tasks by ID

**Independent Test Criteria**:
- User can delete a task by its ID
- Appropriate error message is shown when deleting non-existent task

**Tasks**:
- [x] T030 [US4] Implement delete task functionality in CLI menu in src/main.py
- [x] T031 [US4] Implement input handling for task ID to delete in src/main.py
- [x] T032 [US4] Display success message after deleting task in src/main.py
- [x] T033 [US4] Display error message when deleting non-existent task in src/main.py
- [x] T034 [US4] Test deleting task works correctly

---

## Phase 7: User Story 5 - Mark task as complete/incomplete (Priority: P5)

**Story Goal**: Implement the ability for users to mark tasks as complete or incomplete

**Independent Test Criteria**:
- User can mark a task as complete by ID
- User can mark a task as incomplete by ID
- Appropriate error message is shown when marking non-existent task

**Tasks**:
- [x] T035 [US5] Implement mark task functionality in CLI menu in src/main.py
- [x] T036 [US5] Implement input handling for task ID to mark in src/main.py
- [x] T037 [US5] Implement input handling for completion status in src/main.py
- [x] T038 [US5] Display success message after marking task in src/main.py
- [x] T039 [US5] Display error message when marking non-existent task in src/main.py
- [x] T040 [US5] Test marking task as complete/incomplete works correctly

---

## Phase 8: Polish & Cross-Cutting Concerns

- [x] T041 Implement main application loop in src/main.py with menu display
- [x] T042 Add error handling for invalid user inputs in src/main.py
- [x] T043 Implement graceful exit functionality in src/main.py
- [x] T044 Add input validation for task titles (non-empty, reasonable length) in src/todo.py
- [x] T045 Ensure all functions have proper docstrings and type hints
- [x] T046 Test complete workflow with all 5 features working together
- [x] T047 Update README.md with detailed usage instructions
- [x] T048 Perform final code review for PEP 8 compliance
- [x] T049 Run manual console demo checklist to verify all features work end-to-end