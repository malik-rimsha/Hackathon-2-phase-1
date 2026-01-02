# Tasks: Todo Organization & Usability

**Feature**: Todo Organization & Usability
**Branch**: 002-todo-organization
**Input**: Feature specification from `/specs/002-todo-organization/spec.md`

## Summary

This document outlines the implementation tasks for the Todo Organization & Usability feature, extending the Basic Level console Todo app with Intermediate Level features. The implementation follows a phased approach organized by user story priority to enable independent development and testing.

## Dependencies

User stories are prioritized in dependency order:
1. User Story 1 (Priority Assignment) - Foundation for other features
2. User Story 2 (Tag Assignment) - Independent of priority
3. User Story 3 (Search) - Independent of priority/tags
4. User Story 4 (Filter) - Depends on priority and tags
5. User Story 5 (Combined Filters) - Depends on basic filtering
6. User Story 6 (Sorting) - Independent of other features
7. User Story 7 (Enhanced Display) - Depends on priority and tags

## Parallel Execution Examples

- T001-T003 can be executed in parallel with T004-T006
- US2 tasks can be developed in parallel with US3 tasks after foundational work
- US4 and US6 can be developed in parallel after US1 and US2

## Implementation Strategy

- MVP scope: Complete User Story 1 (Priority Assignment) with basic display
- Incremental delivery: Each user story builds on the previous to create a complete feature
- Test-driven approach: Each user story has independent test criteria

---

## Phase 1: Setup

- [x] T001 Create Priority enum in src/todo.py with HIGH, MEDIUM, LOW values
- [x] T002 Update Task dataclass in src/todo.py to include priority and tags attributes
- [x] T003 Update README.md to reflect upcoming Intermediate features

## Phase 2: Foundational

- [x] T004 [P] Add assign_priority method to TodoList class in src/todo.py
- [x] T005 [P] Add add_tags method to TodoList class in src/todo.py
- [x] T006 [P] Add remove_tags method to TodoList class in src/todo.py
- [x] T007 [P] Add search_tasks method to TodoList class in src/todo.py
- [x] T008 [P] Add filter_tasks method to TodoList class in src/todo.py
- [x] T009 [P] Add get_sorted_tasks method to TodoList class in src/todo.py

## Phase 3: [US1] Assign priority levels to tasks

**Goal**: Enable users to assign priority levels (High, Medium, Low) to tasks with clear indicators in list view.

**Independent Test Criteria**: Can be fully tested by assigning priority levels to tasks and verifying they are stored and displayed correctly with clear indicators in the list view, delivering the value of task prioritization.

**Tasks**:

- [x] T010 [US1] Update CLI to add assign-priority command in src/main.py
- [ ] T011 [US1] Implement assign-priority command logic in src/main.py
- [ ] T012 [US1] Update task display format to show priority indicators in src/main.py
- [ ] T013 [US1] Add validation for priority values in src/todo.py
- [ ] T014 [US1] Test priority assignment functionality with acceptance scenarios

## Phase 4: [US2] Assign tags/categories to tasks

**Goal**: Enable users to assign one or more tags/labels to tasks (e.g., work, home, personal, errands) with display in list view.

**Independent Test Criteria**: Can be fully tested by assigning tags to tasks and verifying they are stored and displayed correctly in the list view, delivering the value of task categorization.

**Tasks**:

- [ ] T015 [US2] Update CLI to add add-tags command in src/main.py
- [ ] T016 [US2] Implement add-tags command logic in src/main.py
- [ ] T017 [US2] Update task display format to show tags in src/main.py
- [ ] T018 [US2] Add validation for tag values in src/todo.py
- [ ] T019 [US2] Test tag assignment functionality with acceptance scenarios

## Phase 5: [US3] Search tasks by keyword

**Goal**: Enable users to search tasks by keyword in the title or description so that they can quickly find specific tasks among many.

**Independent Test Criteria**: Can be fully tested by searching for tasks with specific keywords and verifying the correct subset is displayed, delivering the value of task discovery.

**Tasks**:

- [ ] T020 [US3] Update CLI to add search command in src/main.py
- [ ] T021 [US3] Implement search command logic in src/main.py
- [ ] T022 [US3] Add case-insensitive search functionality in src/todo.py
- [ ] T023 [US3] Handle empty search queries gracefully in src/main.py
- [ ] T024 [US3] Test search functionality with acceptance scenarios

## Phase 6: [US4] Filter tasks by status, priority, or tag

**Goal**: Enable users to filter tasks by status (pending/complete), priority (High/Medium/Low), or tag/category so that they can focus on specific subsets of their tasks.

**Independent Test Criteria**: Can be fully tested by filtering tasks by different criteria and verifying the correct subset is displayed, delivering the value of task filtering.

**Tasks**:

- [ ] T025 [US4] Update CLI to add filter command in src/main.py
- [ ] T026 [US4] Implement filter command logic for status in src/main.py
- [ ] T027 [US4] Implement filter command logic for priority in src/main.py
- [ ] T028 [US4] Implement filter command logic for tags in src/main.py
- [ ] T029 [US4] Test filter functionality with acceptance scenarios

## Phase 7: [US5] Apply combined filters

**Goal**: Enable users to apply combined filters (e.g., "show all High priority work tasks") so that they can focus on very specific subsets of their tasks.

**Independent Test Criteria**: Can be fully tested by applying multiple filters simultaneously and verifying the correct subset is displayed, delivering the value of advanced task filtering.

**Tasks**:

- [ ] T030 [US5] Enhance filter command to support combined filters in src/main.py
- [ ] T031 [US5] Update filter_tasks method to handle multiple criteria in src/todo.py
- [ ] T032 [US5] Test combined filter functionality with acceptance scenarios
- [ ] T033 [US5] Handle case where no tasks match all criteria in src/main.py

## Phase 8: [US6] Sort tasks by priority, alphabetical, or custom order

**Goal**: Enable users to sort tasks by priority (High → Low), alphabetically (by title), or by custom order so that they can view them in a preferred order.

**Independent Test Criteria**: Can be fully tested by sorting tasks by different criteria and verifying they appear in the correct order, delivering the value of task organization.

**Tasks**:

- [ ] T034 [US6] Update CLI to add sort command in src/main.py
- [ ] T035 [US6] Implement sort command logic for different criteria in src/main.py
- [ ] T036 [US6] Ensure sorting is non-destructive to original list in src/todo.py
- [ ] T037 [US6] Test sort functionality with acceptance scenarios

## Phase 9: [US7] Enhanced task list display

**Goal**: Enable the task list view to show priority indicators (e.g., [H], [M], [L]) and tags (e.g., #work #home) so that users can quickly understand task importance and categorization.

**Independent Test Criteria**: Can be fully tested by viewing the task list and verifying that priority indicators and tags are displayed clearly, delivering the value of enhanced task visibility.

**Tasks**:

- [ ] T038 [US7] Update view command to support optional filters and sorting in src/main.py
- [ ] T039 [US7] Enhance display format to include priority and tags in src/main.py
- [ ] T040 [US7] Implement view command with --filter-status, --filter-priority, --filter-tag, --sort, --search options in src/main.py
- [ ] T041 [US7] Test enhanced display functionality with acceptance scenarios

## Phase 10: Polish & Cross-Cutting Concerns

- [ ] T042 Update README.md with new feature demos and usage instructions
- [ ] T043 Add error handling for edge cases in src/todo.py
- [ ] T044 Ensure all existing Basic Level features continue to work perfectly
- [ ] T045 Perform final integration testing of all Intermediate Level features
- [ ] T046 Validate performance goals (response times under 3-4 seconds)
- [ ] T047 Document any additional edge cases and error handling