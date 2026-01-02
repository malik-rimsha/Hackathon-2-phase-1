# Data Model: Enhanced Todo Application

## Task Entity

The Task entity is extended from the Basic Level to include priority and tags attributes.

### Attributes

| Field | Type | Description | Default | Constraints |
|-------|------|-------------|---------|-------------|
| id | int | Auto-generated unique identifier | Auto-assigned | Positive integer, immutable |
| title | str | Task title/description | Required | Non-empty string |
| description | Optional[str] | Optional detailed description | None | String or None |
| status | bool | Completion status | False | Boolean (False = pending, True = complete) |
| priority | Optional[Priority] | Priority level | None | Enum value from Priority enum or None |
| tags | List[str] | List of tags/labels | [] | List of non-empty strings |

### Priority Enum

```python
from enum import Enum

class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
```

### Relationships

- Task has no direct relationships with other entities in this implementation
- All data is stored in-memory within the TodoList service

## TodoList Entity

The TodoList entity manages a collection of Task entities and provides methods for all task operations.

### Attributes

| Field | Type | Description |
|-------|------|-------------|
| tasks | List[Task] | Collection of Task entities | 
| next_id | int | Counter for generating unique task IDs |

### Methods

#### Basic Level Methods (inherited)
- `add_task(title: str, description: Optional[str] = None) -> int`
- `delete_task(task_id: int) -> bool`
- `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool`
- `get_all_tasks() -> List[Task]`
- `mark_complete(task_id: int) -> bool`
- `mark_incomplete(task_id: int) -> bool`

#### Intermediate Level Methods (new)
- `assign_priority(task_id: int, priority: Priority) -> bool`
- `add_tags(task_id: int, tags: List[str]) -> bool`
- `remove_tags(task_id: int, tags: List[str]) -> bool`
- `search_tasks(keyword: str) -> List[Task]`
- `filter_tasks(status: Optional[bool] = None, priority: Optional[Priority] = None, tags: Optional[List[str]] = None) -> List[Task]`
- `get_sorted_tasks(tasks: List[Task], sort_by: str = "priority") -> List[Task]`
- `get_task_by_id(task_id: int) -> Optional[Task]`

## Implementation Notes

### Data Validation
- All input parameters are validated before processing
- Priority values must be from the Priority enum
- Tag values must be non-empty strings
- Task IDs must exist in the collection

### Error Handling
- Invalid operations return appropriate boolean values or None
- Invalid inputs raise appropriate exceptions with descriptive messages
- Non-existent task IDs are handled gracefully

### Performance Considerations
- Search and filter operations use list comprehensions for efficiency
- Sorting is non-destructive to preserve original order
- In-memory storage provides fast access to all operations