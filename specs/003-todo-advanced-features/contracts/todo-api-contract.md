# API Contract: Advanced Todo Features

## Overview
This document defines the API contracts for the advanced todo features, specifically for recurring tasks and due date/time reminders. These contracts represent the expected behavior of the CLI interface and internal service methods.

## Task Management Endpoints

### Add Task with Recurrence
**Method**: `add_task(title: str, description: str = "", recurrence: Optional[RecurrenceInterval] = None) -> Task`

**Description**: Creates a new task with optional recurrence settings

**Parameters**:
- `title` (str): Required task title
- `description` (str): Optional task description
- `recurrence` (Optional[RecurrenceInterval]): Optional recurrence interval (DAILY, WEEKLY, MONTHLY)

**Returns**: Task object with assigned ID and creation timestamp

**Validation**:
- Title must not be empty
- Recurrence must be one of the valid RecurrenceInterval values if provided

### Set Due Date
**Method**: `set_due_date(task_id: int, date_str: str, time_str: Optional[str] = None) -> bool`

**Description**: Sets a due date for an existing task

**Parameters**:
- `task_id` (int): ID of the task to update
- `date_str` (str): Date string in format "YYYY-MM-DD" or relative terms like "tomorrow"
- `time_str` (Optional[str]): Optional time string in format "HH:MM"

**Returns**: Boolean indicating success

**Validation**:
- Task with given ID must exist
- Date string must be in valid format or relative term

### Set Recurrence
**Method**: `set_recurrence(task_id: int, interval: RecurrenceInterval) -> bool`

**Description**: Sets recurrence for an existing task

**Parameters**:
- `task_id` (int): ID of the task to update
- `interval` (RecurrenceInterval): Recurrence interval (DAILY, WEEKLY, MONTHLY)

**Returns**: Boolean indicating success

**Validation**:
- Task with given ID must exist
- Interval must be one of the valid RecurrenceInterval values

### Mark Task Complete (with Recurrence Handling)
**Method**: `mark_complete(task_id: int) -> bool`

**Description**: Marks a task as complete; if the task is recurring, creates a new instance

**Parameters**:
- `task_id` (int): ID of the task to mark complete

**Returns**: Boolean indicating success

**Behavior**:
- If task is not recurring: Simply marks as complete
- If task is recurring: Marks as complete AND creates new instance with next occurrence date

### Get Tasks with Filters
**Method**: `get_tasks(filter_type: Optional[str] = None) -> List[Task]`

**Description**: Retrieves tasks with optional filtering

**Parameters**:
- `filter_type` (Optional[str]): Optional filter type ("overdue", "due-today", "due-soon", "recurring")

**Returns**: List of Task objects matching the filter

## Notification Service Endpoints

### Check Due Tasks
**Method**: `check_due_tasks() -> List[Task]`

**Description**: Returns tasks that are due within the next 5 minutes

**Returns**: List of Task objects due within 5 minutes

### Request Notification Permission
**Method**: `request_notification_permission() -> bool`

**Description**: Requests permission to show browser notifications

**Returns**: Boolean indicating if permission was granted

### Show Notification
**Method**: `show_notification(task: Task) -> bool`

**Description**: Shows a browser notification for the given task

**Parameters**:
- `task` (Task): Task to show notification for

**Returns**: Boolean indicating if notification was shown successfully

## Data Models

### Task
```python
class Task:
    id: int
    title: str
    description: str
    completed: bool
    priority: Optional[str]
    tags: List[str]
    due_datetime: Optional[datetime]
    recurrence: Optional[RecurrenceInterval]
    created_at: datetime
    updated_at: datetime
```

### RecurrenceInterval Enum
```python
class RecurrenceInterval(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
```

## Error Handling

### Common Error Responses
- `TaskNotFound`: When an operation is requested for a non-existent task ID
- `InvalidInput`: When input parameters don't meet validation requirements
- `PermissionDenied`: When notification permissions are not granted

### Error Format
```json
{
  "error": "error_code",
  "message": "descriptive error message",
  "details": "additional details if applicable"
}
```