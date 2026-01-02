# Data Model: Advanced Todo Features

## Task Model Extension

### Enhanced Task Class
```python
from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass

class RecurrenceInterval(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Optional[str] = None  # high, medium, low
    tags: Optional[list[str]] = None  # list of tags
    due_datetime: Optional[datetime] = None  # due date and time
    recurrence: Optional[RecurrenceInterval] = None  # recurrence interval
    created_at: datetime = None  # creation timestamp
    updated_at: datetime = None  # last update timestamp

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
        if self.tags is None:
            self.tags = []
```

### Recurrence Rule Model
```python
from datetime import datetime
from enum import Enum
from typing import Optional

class RecurrenceInterval(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class RecurrenceRule:
    interval: RecurrenceInterval
    created_at: datetime
    next_occurrence: datetime
    end_date: Optional[datetime] = None  # optional end date for recurrence
```

## Validation Rules

### Task Model Validation
1. **Title**: Required, non-empty string
2. **ID**: Auto-generated unique identifier
3. **Due datetime**: Must be a valid datetime object if provided
4. **Recurrence**: Must be one of the defined RecurrenceInterval values if provided
5. **Priority**: Must be one of "high", "medium", "low" if provided
6. **Tags**: List of strings if provided

### Recurrence Rule Validation
1. **Interval**: Must be one of the defined RecurrenceInterval values
2. **Next occurrence**: Must be a valid datetime object after the current date
3. **End date**: If provided, must be a valid datetime object after the next occurrence date

## State Transitions

### Task State Transitions
1. **Created**: When a new task is added to the system
   - `completed = False` (default)
   - `created_at = datetime.now()`
   - `updated_at = datetime.now()`

2. **Updated**: When task details are modified
   - `updated_at = datetime.now()`

3. **Completed**: When task is marked as complete
   - `completed = True`
   - `updated_at = datetime.now()`
   - If `recurrence` is set, create a new instance with next occurrence date

4. **Recurring Task Completion**: When a recurring task is marked complete
   - Original task: `completed = True`, `updated_at = datetime.now()`
   - New instance: Created with same properties except:
     - New `id` (auto-generated)
     - Updated `created_at = datetime.now()`
     - Updated `updated_at = datetime.now()`
     - New `due_datetime` based on recurrence interval

## Relationships

### Task Relationships
- **Recurrence Rule**: A task may have an optional recurrence rule (one-to-one)
- **Tags**: A task may have multiple tags (one-to-many)

### Recurrence Rule Relationships
- **Task**: A recurrence rule belongs to one task (many-to-one)

## Data Persistence

### In-Memory Storage
- Tasks stored in a dictionary with ID as key
- Example: `{1: Task(id=1, title="Sample task", ...), 2: Task(id=2, ...)}`
- Auto-incrementing ID generation for new tasks

### Data Access Patterns
1. **Get all tasks**: Retrieve all tasks from storage
2. **Get task by ID**: Retrieve specific task by its ID
3. **Create task**: Add new task with auto-generated ID
4. **Update task**: Modify existing task by ID
5. **Delete task**: Remove task by ID
6. **Filter tasks**: Filter tasks by various criteria (status, priority, due date, tags, etc.)
7. **Search tasks**: Search tasks by keyword in title or description