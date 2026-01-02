# Data Model: Todo In-Memory Python Console App

## Task Entity

### Fields
- **id**: `int` (auto-incrementing, unique identifier)
- **title**: `str` (required, non-empty)
- **description**: `str` (optional, can be empty)
- **completed**: `bool` (default False)

### Validation Rules
- Title must not be empty or contain only whitespace
- ID must be unique within the application session
- ID is auto-generated when a new task is created

### State Transitions
- `pending` (default) → `completed` (when marked as complete)
- `completed` → `pending` (when marked as incomplete)

## TodoList Container

### Fields
- **tasks**: `List[Task]` (in-memory storage of all tasks)
- **next_id**: `int` (next available ID for new tasks)

### Operations
- `add_task(title: str, description: str) -> int` (returns the ID of the new task)
- `get_all_tasks() -> List[Task]` (returns all tasks)
- `update_task(task_id: int, title: str = None, description: str = None) -> bool` (returns True if successful)
- `delete_task(task_id: int) -> bool` (returns True if successful)
- `mark_task_completed(task_id: int, completed: bool) -> bool` (returns True if successful)
- `get_task_by_id(task_id: int) -> Optional[Task]` (returns the task or None if not found)

### Validation Rules
- Task ID must exist when performing update, delete, or mark operations
- Operations return appropriate status indicators for error handling