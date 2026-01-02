# Research Summary: Advanced Todo Features

## Decisions Made

### 1. Recurrence Representation
**Decision**: Use an Enum for recurrence intervals (DAILY, WEEKLY, MONTHLY) with optional end date
**Rationale**: Simple enum approach is sufficient for hackathon demo and easier to implement and understand than complex cron expressions
**Alternatives considered**: Full cron-like string expressions vs. simple enum with basic intervals

### 2. Due Date Input Format
**Decision**: Use strict formatted input (YYYY-MM-DD [HH:MM]) with simple parsing
**Rationale**: Strict format with simple parsing (using datetime.strptime) avoids external dependencies and keeps reliability high
**Alternatives considered**: Free natural language parsing vs. strict formatted input

### 3. Due Date/Time Storage
**Decision**: Use datetime.datetime object for storage
**Rationale**: datetime.datetime provides easy comparison and calculation operations
**Alternatives considered**: Separate date/time strings vs. datetime.datetime object

### 4. Notification Implementation
**Decision**: Browser notifications (using PyScript + window.Notification) for real demo impact, with console fallback
**Rationale**: Provides the required notification functionality while maintaining console compatibility
**Alternatives considered**: Pure console warnings vs. browser desktop notifications

### 5. Runtime Environment for Notifications
**Decision**: PyScript for browser execution
**Rationale**: PyScript is modern, actively maintained, has simple HTML setup, and good Python 3.10+ support
**Alternatives considered**: Brython, Pyodide, PyScript

### 6. Auto-Rescheduling Timing
**Decision**: Immediate reschedule on mark-complete
**Rationale**: Simpler implementation without need for background threads
**Alternatives considered**: On mark-complete vs. background scheduler

## Technical Unknowns Resolved

### 1. Timezone Handling
**Decision**: Use local system timezone for due date calculations
**Rationale**: Simplifies implementation while meeting requirements
**Research**: Python's datetime module works with local timezone by default

### 2. PyScript Integration
**Decision**: Create separate PyScript-compatible version of the app
**Rationale**: Maintains console functionality while adding browser notifications
**Research**: PyScript allows running Python in browsers with JavaScript API access

### 3. Notification Permissions
**Decision**: Request notification permission when first needed
**Rationale**: Follows browser security model and user expectations
**Research**: Browser notification APIs require explicit user permission

### 4. Polling Mechanism
**Decision**: Implement polling loop (every 60 seconds) to check for tasks due within next 5 minutes
**Rationale**: Simple and effective approach for checking due tasks
**Research**: setInterval in JavaScript can be used to implement periodic checks

## Architecture Considerations

### 1. Data Model Extensions
- Extend Task model with recurrence (Optional[RecurrenceInterval]) and due_datetime (Optional[datetime.datetime])
- Create RecurrenceRule model to handle recurrence patterns

### 2. Service Layer Extensions
- Extend TodoList class with set_due_date(task_id, date_str, time_str=None) and set_recurrence(task_id, interval)
- Add _create_next_instance(task) method called after marking recurring task complete

### 3. Notification System
- Browser (PyScript): Use JavaScript bridge to request Notification.permission and show notifications
- Console fallback: Print warning for overdue tasks on list view

### 4. Display Enhancements
- Show due date: e.g., (2026-01-10 15:00) or (Overdue!)
- Show recurrence: 🔁 Weekly

## Implementation Strategy

### Phase 1: Core Extensions
1. Extend Task model with recurrence and due_datetime
2. Implement recurrence logic: set_recurrence and auto-reschedule on complete
3. Implement due date parsing and storage

### Phase 2: CLI Extensions
4. Add CLI commands for setting recurrence and due dates
5. Update display format to show due dates and recurrence indicators

### Phase 3: Notification System
6. Implement browser notification system (PyScript HTML + JS bridge)
7. Add polling loop for checking due tasks (browser only)
8. Implement console fallback warnings

### Phase 4: Integration
9. Create index.html with PyScript setup to run the app in browser
10. Update README.md with browser setup instructions and demo steps
11. Polish user messages and error handling