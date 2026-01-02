---

description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize Python 3.13+ project with dependencies as needed per feature level (as per constitution)
- [ ] T003 [P] Configure linting and formatting tools for Python (e.g., ruff, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Create in-memory storage implementation in src/lib/storage.py
- [ ] T005 [P] Create Task model in src/models/task.py with ID, title, description, status
- [ ] T006 [P] Setup CLI argument parser structure in src/cli/main.py
- [ ] T007 Create base TaskService in src/services/task_service.py
- [ ] T008 Configure error handling and validation infrastructure
- [ ] T009 Setup application entry point and basic structure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add a new task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks with title and description to in-memory storage

**Independent Test**: Can be fully tested by running the CLI command to add a task and verifying it appears in the task list, delivering the core value of task creation.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Unit test for Task model validation in tests/unit/test_task.py
- [ ] T011 [P] [US1] Unit test for TaskService.add_task() in tests/unit/test_task_service.py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Implement Task model validation in src/models/task.py
- [ ] T013 [P] [US1] Implement TaskService.add_task() method in src/services/task_service.py
- [ ] T014 [US1] Implement CLI command for adding tasks in src/cli/main.py
- [ ] T015 [US1] Add input validation for task creation
- [ ] T016 [US1] Add error handling for invalid inputs

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View all tasks (Priority: P2)

**Goal**: Allow users to view all tasks with their status information

**Independent Test**: Can be fully tested by adding tasks and then viewing the complete list, delivering the core value of task visibility.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T017 [P] [US2] Unit test for TaskService.get_all_tasks() in tests/unit/test_task_service.py
- [ ] T018 [P] [US2] Integration test for viewing tasks in tests/integration/test_cli.py

### Implementation for User Story 2

- [ ] T019 [P] [US2] Implement TaskService.get_all_tasks() method in src/services/task_service.py
- [ ] T020 [US2] Implement CLI command for viewing tasks in src/cli/main.py
- [ ] T021 [US2] Format task display with ID, title, description, and status

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update task details (Priority: P3)

**Goal**: Allow users to update task details by ID

**Independent Test**: Can be fully tested by updating a task's details and verifying the changes persist, delivering the value of task modification.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US3] Unit test for TaskService.update_task() in tests/unit/test_task_service.py
- [ ] T023 [P] [US3] Integration test for updating tasks in tests/integration/test_cli.py

### Implementation for User Story 3

- [ ] T024 [P] [US3] Implement TaskService.update_task() method in src/services/task_service.py
- [ ] T025 [US3] Implement CLI command for updating tasks in src/cli/main.py
- [ ] T026 [US3] Add validation for updating existing tasks

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Delete a task by ID (Priority: P4)

**Goal**: Allow users to delete tasks by their ID

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the task list, delivering the value of task removal.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US4] Unit test for TaskService.delete_task() in tests/unit/test_task_service.py
- [ ] T028 [P] [US4] Integration test for deleting tasks in tests/integration/test_cli.py

### Implementation for User Story 4

- [ ] T029 [P] [US4] Implement TaskService.delete_task() method in src/services/task_service.py
- [ ] T030 [US4] Implement CLI command for deleting tasks in src/cli/main.py
- [ ] T031 [US4] Add validation for deleting existing tasks

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Mark task as complete/incomplete (Priority: P5)

**Goal**: Allow users to mark tasks as complete or incomplete

**Independent Test**: Can be fully tested by marking a task as complete/incomplete and verifying the status change, delivering the value of progress tracking.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T032 [P] [US5] Unit test for TaskService.mark_task_status() in tests/unit/test_task_service.py
- [ ] T033 [P] [US5] Integration test for marking task status in tests/integration/test_cli.py

### Implementation for User Story 5

- [ ] T034 [P] [US5] Implement TaskService.mark_task_status() method in src/services/task_service.py
- [ ] T035 [US5] Implement CLI command for marking task status in src/cli/main.py
- [ ] T036 [US5] Add validation for marking existing tasks

**Checkpoint**: All 5 required features should now be implemented and functional

---

## Phase 8: User Story 6 - Assign priorities and tags/categories to tasks (Priority: P6)

**Goal**: Allow users to assign priority levels and tags/categories to tasks

**Independent Test**: Can be fully tested by assigning priorities and tags to tasks and verifying they are stored and displayed correctly, delivering the value of task organization.

### Tests for User Story 6 (OPTIONAL - only if tests requested) ⚠️

- [ ] T037 [P] [US6] Unit test for Task model priority/tag validation in tests/unit/test_task.py
- [ ] T038 [P] [US6] Unit test for TaskService.update_task_priority() in tests/unit/test_task_service.py

### Implementation for User Story 6

- [ ] T039 [P] [US6] Extend Task model with priority and tags in src/models/task.py
- [ ] T040 [US6] Implement TaskService.update_task_priority() method in src/services/task_service.py
- [ ] T041 [US6] Implement CLI command for assigning priorities in src/cli/main.py
- [ ] T042 [US6] Implement CLI command for assigning tags in src/cli/main.py

**Checkpoint**: At this point, User Stories 1-6 should all work independently

---

## Phase 9: User Story 7 - Search and filter tasks (Priority: P7)

**Goal**: Allow users to search and filter tasks by keyword, status, priority, or date

**Independent Test**: Can be fully tested by searching and filtering tasks and verifying the correct subset is displayed, delivering the value of task discovery.

### Tests for User Story 7 (OPTIONAL - only if tests requested) ⚠️

- [ ] T043 [P] [US7] Unit test for TaskService.search_tasks() in tests/unit/test_task_service.py
- [ ] T044 [P] [US7] Unit test for TaskService.filter_tasks() in tests/unit/test_task_service.py

### Implementation for User Story 7

- [ ] T045 [P] [US7] Implement TaskService.search_tasks() method in src/services/task_service.py
- [ ] T046 [US7] Implement TaskService.filter_tasks() method in src/services/task_service.py
- [ ] T047 [US7] Implement CLI command for searching tasks in src/cli/main.py
- [ ] T048 [US7] Implement CLI command for filtering tasks in src/cli/main.py

**Checkpoint**: At this point, User Stories 1-7 should all work independently

---

## Phase 10: User Story 8 - Sort tasks (Priority: P8)

**Goal**: Allow users to sort tasks by due date, priority, or alphabetically

**Independent Test**: Can be fully tested by sorting tasks and verifying they appear in the correct order, delivering the value of task organization.

### Tests for User Story 8 (OPTIONAL - only if tests requested) ⚠️

- [ ] T049 [P] [US8] Unit test for TaskService.sort_tasks() in tests/unit/test_task_service.py

### Implementation for User Story 8

- [ ] T050 [P] [US8] Implement TaskService.sort_tasks() method in src/services/task_service.py
- [ ] T051 [US8] Implement CLI command for sorting tasks in src/cli/main.py

**Checkpoint**: At this point, User Stories 1-8 should all work independently

---

## Phase 11: User Story 9 - Create recurring tasks (Priority: P9)

**Goal**: Allow users to create recurring tasks that auto-reschedule

**Independent Test**: Can be fully tested by creating a recurring task and verifying it reschedules automatically, delivering the value of task automation.

### Tests for User Story 9 (OPTIONAL - only if tests requested) ⚠️

- [ ] T052 [P] [US9] Unit test for Task model recurrence validation in tests/unit/test_task.py
- [ ] T053 [P] [US9] Unit test for TaskService.create_recurring_task() in tests/unit/test_task_service.py

### Implementation for User Story 9

- [ ] T054 [P] [US9] Extend Task model with recurrence settings in src/models/task.py
- [ ] T055 [US9] Implement TaskService.create_recurring_task() method in src/services/task_service.py
- [ ] T056 [US9] Implement CLI command for creating recurring tasks in src/cli/main.py
- [ ] T057 [US9] Implement auto-scheduling mechanism for recurring tasks

**Checkpoint**: At this point, User Stories 1-9 should all work independently

---

## Phase 12: User Story 10 - Set due dates and receive reminders (Priority: P10)

**Goal**: Allow users to set due dates and receive time-based reminders/notifications

**Independent Test**: Can be fully tested by setting due dates and receiving notifications, delivering the value of task time management.

### Tests for User Story 10 (OPTIONAL - only if tests requested) ⚠️

- [ ] T058 [P] [US10] Unit test for Task model due date validation in tests/unit/test_task.py
- [ ] T059 [P] [US10] Unit test for TaskService.set_due_date() in tests/unit/test_task_service.py

### Implementation for User Story 10

- [ ] T060 [P] [US10] Extend Task model with due date in src/models/task.py
- [ ] T061 [US10] Implement TaskService.set_due_date() method in src/services/task_service.py
- [ ] T062 [US10] Implement reminder/notification system in src/services/task_service.py
- [ ] T063 [US10] Implement CLI command for setting due dates in src/cli/main.py
- [ ] T064 [US10] Implement CLI command for managing notifications in src/cli/main.py

**Checkpoint**: All 10 required features should now be implemented and functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring to follow clean code principles (as per constitution)
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Input validation hardening
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 7 (P7)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 8 (P8)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 9 (P9)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 10 (P10)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before CLI implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### Basic Level Implementation

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add task)
4. Complete Phase 4: User Story 2 (View tasks)
5. Complete Phase 5: User Story 3 (Update task)
6. Complete Phase 6: User Story 4 (Delete task)
7. Complete Phase 7: User Story 5 (Mark complete/incomplete)
8. **STOP and VALIDATE**: Basic level features are complete and tested

### Intermediate Level Implementation

1. Complete Phase 8: User Story 6 (Priorities & Tags)
2. Complete Phase 9: User Story 7 (Search & Filter)
3. Complete Phase 10: User Story 8 (Sort tasks)
4. **STOP and VALIDATE**: Intermediate level features are complete and tested

### Advanced Level Implementation

1. Complete Phase 11: User Story 9 (Recurring tasks)
2. Complete Phase 12: User Story 10 (Due dates & Reminders)
3. **STOP and VALIDATE**: Advanced level features are complete and tested

### Progressive Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add Basic features (US1-5) → Test independently → Deploy/Demo (Basic level!)
3. Add Intermediate features (US6-8) → Test independently → Deploy/Demo (Intermediate level!)
4. Add Advanced features (US9-10) → Test independently → Deploy/Demo (Advanced level!)
5. Each level adds value without breaking previous levels

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Stories 1, 6, 9
   - Developer B: User Stories 2, 7, 10
   - Developer C: User Stories 3, 8
   - Developer D: User Stories 4, 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Ensure all implementations follow the constitution requirements: Python 3.13+, dependencies as needed per feature level, in-memory storage initially evolving as needed