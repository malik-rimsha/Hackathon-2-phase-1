# Implementation Tasks: Advanced Todo Features with Recurring Tasks and Time-Based Reminders

**Feature**: Advanced Todo Features with Recurring Tasks and Time-Based Reminders
**Branch**: 003-todo-advanced-features
**Created**: 2026-01-02
**Status**: Draft

## Implementation Strategy

This implementation will follow a phased approach, building on the existing Basic and Intermediate level functionality. The tasks are organized by user story priority to enable independent development and testing of each feature. The implementation will maintain all previous functionality while adding the new advanced features.

## Dependencies

- Python 3.13+
- UV package manager
- Existing Basic and Intermediate level codebase

## Parallel Execution Examples

- [US1] and [US3] can be developed in parallel as they modify different components
- Models and services can be developed in parallel with CLI updates
- Browser and console notification systems can be developed separately

## Phases

### Phase 1: Setup Tasks

- [x] T001 Create project structure per implementation plan in src/models/, src/services/, src/cli/, src/lib/, and src/web/
- [x] T002 Create __init__.py files in all new directories
- [x] T003 Set up pyproject.toml with required dependencies
- [x] T004 Update README.md with browser setup instructions

### Phase 2: Foundational Tasks

- [x] T005 [P] Create RecurrenceInterval enum in src/models/recurrence.py
- [x] T006 [P] Update Task model in src/models/task.py with recurrence and due_datetime attributes
- [x] T007 [P] Create RecurrenceRule model in src/models/recurrence.py
- [x] T008 Update storage implementation in src/lib/storage.py to handle new Task attributes
- [x] T009 Create notification service in src/services/notification_service.py

### Phase 3: [US1] Create Recurring Tasks

**Goal**: Enable users to create recurring tasks with repeat intervals (daily, weekly, monthly)

**Independent Test Criteria**:
- Users can create recurring tasks with daily, weekly, or monthly intervals
- Recurring tasks appear in the task list with clear recurrence indicators (e.g., 🔁 Daily)

**Tasks**:

- [x] T010 [US1] Implement add_task method in task_service.py to accept recurrence parameter
- [x] T011 [US1] Update CLI main.py to accept --recurrence parameter for add command
- [x] T012 [US1] Update task display in CLI to show recurrence indicators (e.g., 🔁 Daily)
- [x] T013 [US1] Implement validation for recurrence intervals (daily, weekly, monthly)
- [ ] T014 [US1] Test creating recurring tasks with different intervals

### Phase 4: [US2] Mark Recurring Tasks as Complete

**Goal**: When a recurring task is marked complete, automatically create a new instance with the next due date

**Independent Test Criteria**:
- When a recurring task is marked complete, a new instance is created with the next occurrence date
- New instance has the same properties as the original except for ID and dates

**Tasks**:

- [x] T015 [US2] Implement logic to calculate next occurrence date based on recurrence interval
- [x] T016 [US2] Update mark_complete method in task_service.py to handle recurring tasks
- [x] T017 [US2] Create new task instance with next occurrence date when marking recurring task complete
- [x] T018 [US2] Update CLI to handle recurring task completion properly
- [ ] T019 [US2] Test marking recurring tasks complete and verifying new instances are created

### Phase 5: [US3] Set Due Dates for Tasks

**Goal**: Allow users to assign due dates and times to tasks using simple input formats

**Independent Test Criteria**:
- Users can set due dates in YYYY-MM-DD format
- Users can set due dates with time in YYYY-MM-DD HH:MM format
- Users can set due dates using relative terms like "tomorrow" or "next week"

**Tasks**:

- [x] T020 [US3] Implement set_due_date method in task_service.py
- [x] T021 [US3] Create date parsing utility to handle different date formats
- [x] T022 [US3] Implement relative date parsing (tomorrow, next week, etc.)
- [x] T023 [US3] Update CLI main.py to add set-due command
- [x] T024 [US3] Update task display to show due dates in readable format
- [ ] T025 [US3] Test setting due dates with different formats

### Phase 6: [US4] Receive Browser Notifications for Due Tasks

**Goal**: Show desktop notifications for tasks due within the next 5 minutes when running in browser

**Independent Test Criteria**:
- Tasks due within 5 minutes trigger browser notifications
- Notification permissions are requested appropriately
- Notifications show task details

**Tasks**:

- [x] T026 [US4] Implement check_due_tasks method in notification_service.py
- [x] T027 [US4] Create polling mechanism to check for due tasks every 60 seconds
- [x] T028 [US4] Implement browser notification functionality using PyScript
- [x] T029 [US4] Create request_notification_permission method
- [x] T030 [US4] Create show_notification method for browser notifications
- [x] T031 [US4] Create PyScript-compatible version of the todo app in src/web/pyscript_todo.py
- [x] T032 [US4] Create HTML interface with PyScript in src/web/index.html
- [ ] T033 [US4] Test browser notifications for due tasks

### Phase 7: [US5] Receive Console Warnings for Overdue Tasks

**Goal**: Show warning messages for overdue tasks when viewing the task list in console mode

**Independent Test Criteria**:
- Overdue tasks are highlighted with warning messages in console mode
- Tasks due today are clearly indicated

**Tasks**:

- [x] T034 [US5] Implement overdue task detection in task_service.py
- [x] T035 [US5] Update task list display to show overdue warnings in console mode
- [x] T036 [US5] Add filter options for overdue, due-today, and due-soon tasks
- [ ] T037 [US5] Test console warnings for overdue tasks

### Phase 8: [US6] View Tasks with Due Dates and Recurrence Info

**Goal**: Display due dates and recurrence information clearly in the task list

**Independent Test Criteria**:
- Due dates are displayed in a clear, readable format
- Recurrence information is displayed with clear indicators (e.g., 🔁 Daily)
- Both due dates and recurrence info are displayed without confusion

**Tasks**:

- [x] T038 [US6] Enhance task display format to show both due dates and recurrence info
- [x] T039 [US6] Implement consistent formatting for due dates and recurrence indicators
- [x] T040 [US6] Update CLI list command to show enhanced task information
- [ ] T041 [US6] Test display of tasks with various combinations of due dates and recurrence

### Phase 9: Polish & Cross-Cutting Concerns

- [x] T042 Update CLI help text to include new commands and options
- [x] T043 Add error handling for invalid date formats and recurrence intervals
- [x] T044 Implement validation for all new functionality
- [x] T045 Update documentation in README.md with new features
- [ ] T046 Test all functionality works together without conflicts
- [ ] T047 Ensure all previous Basic and Intermediate features continue to work
- [ ] T048 Performance test with 100+ tasks with due dates and recurrence
- [ ] T049 Final integration testing of all advanced features