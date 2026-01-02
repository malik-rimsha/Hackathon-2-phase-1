# Internal API Contracts: Todo In-Memory Python Console App

## Task Class Interface

### Properties
- `id: int` - Unique identifier for the task
- `title: str` - Title of the task (required, non-empty)
- `description: str` - Description of the task (optional)
- `completed: bool` - Completion status (default False)

## TodoList Class Interface

### Methods

#### `add_task(title: str, description: str = "") -> int`
- **Purpose**: Add a new task to the list
- **Parameters**: 
  - `title`: Task title (required, non-empty)
  - `description`: Task description (optional)
- **Returns**: ID of the newly created task
- **Side effects**: Increments internal ID counter
- **Error conditions**: Returns -1 if title is empty

#### `get_all_tasks() -> List[Task]`
- **Purpose**: Retrieve all tasks in the list
- **Parameters**: None
- **Returns**: List of all Task objects in the order they were added
- **Side effects**: None
- **Error conditions**: None

#### `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- **Purpose**: Update an existing task's title and/or description
- **Parameters**:
  - `task_id`: ID of the task to update
  - `title`: New title (optional, if provided will update)
  - `description`: New description (optional, if provided will update)
- **Returns**: True if update was successful, False if task not found
- **Side effects**: Modifies existing Task object
- **Error conditions**: Returns False if task_id doesn't exist

#### `delete_task(task_id: int) -> bool`
- **Purpose**: Remove a task from the list
- **Parameters**: `task_id`: ID of the task to delete
- **Returns**: True if deletion was successful, False if task not found
- **Side effects**: Removes Task object from internal list
- **Error conditions**: Returns False if task_id doesn't exist

#### `mark_task_completed(task_id: int, completed: bool) -> bool`
- **Purpose**: Update the completion status of a task
- **Parameters**:
  - `task_id`: ID of the task to update
  - `completed`: New completion status
- **Returns**: True if update was successful, False if task not found
- **Side effects**: Updates completed property of Task object
- **Error conditions**: Returns False if task_id doesn't exist

#### `get_task_by_id(task_id: int) -> Optional[Task]`
- **Purpose**: Retrieve a specific task by its ID
- **Parameters**: `task_id`: ID of the task to retrieve
- **Returns**: Task object if found, None otherwise
- **Side effects**: None
- **Error conditions**: Returns None if task_id doesn't exist

## CLI Interface Functions

### `display_menu() -> None`
- **Purpose**: Show the main menu options to the user
- **Parameters**: None
- **Returns**: None
- **Side effects**: Prints menu to console

### `handle_user_input(choice: str) -> bool`
- **Purpose**: Process the user's menu selection
- **Parameters**: `choice`: User's menu selection as string
- **Returns**: True if application should continue, False to exit
- **Side effects**: Performs the selected operation, may update task list
- **Error conditions**: Handles invalid input gracefully with error message