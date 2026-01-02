# API Contracts: Todo Organization & Usability

## Task Service Interface

### Priority Assignment
```
Method: assign_priority(task_id: int, priority: Priority) -> bool
Description: Assigns a priority level to a task
Parameters:
  - task_id: Unique identifier of the task
  - priority: Priority enum value (HIGH, MEDIUM, LOW)
Returns: True if successful, False otherwise
Errors: Raises ValueError if task_id doesn't exist or priority is invalid
```

### Tag Management
```
Method: add_tags(task_id: int, tags: List[str]) -> bool
Description: Adds one or more tags to a task
Parameters:
  - task_id: Unique identifier of the task
  - tags: List of tag strings to add
Returns: True if successful, False otherwise
Errors: Raises ValueError if task_id doesn't exist or tags are invalid

Method: remove_tags(task_id: int, tags: List[str]) -> bool
Description: Removes one or more tags from a task
Parameters:
  - task_id: Unique identifier of the task
  - tags: List of tag strings to remove
Returns: True if successful, False otherwise
Errors: Raises ValueError if task_id doesn't exist or tags are invalid
```

### Search Functionality
```
Method: search_tasks(keyword: str) -> List[Task]
Description: Searches tasks by keyword in title or description
Parameters:
  - keyword: String to search for
Returns: List of matching Task objects
Errors: None
```

### Filter Functionality
```
Method: filter_tasks(status: Optional[bool] = None, priority: Optional[Priority] = None, tags: Optional[List[str]] = None) -> List[Task]
Description: Filters tasks by various criteria
Parameters:
  - status: Optional boolean (True for complete, False for pending)
  - priority: Optional Priority enum value
  - tags: Optional list of tag strings to include
Returns: List of matching Task objects
Errors: Raises ValueError if parameters are invalid
```

### Sort Functionality
```
Method: get_sorted_tasks(tasks: List[Task], sort_by: str = "priority") -> List[Task]
Description: Returns a sorted copy of the tasks list
Parameters:
  - tasks: List of Task objects to sort
  - sort_by: String indicating sort criterion ("priority", "title", "status")
Returns: New sorted list of Task objects
Errors: Raises ValueError if sort_by is invalid
```

## CLI Command Interface

### New Commands
```
Command: assign-priority <task_id> <priority>
Description: Assigns a priority level to a task
Parameters:
  - task_id: Unique identifier of the task
  - priority: Priority level (high, medium, low)
Example: assign-priority 1 high

Command: add-tags <task_id> <tag1> [tag2] [tag3] ...
Description: Adds tags to a task
Parameters:
  - task_id: Unique identifier of the task
  - tags: One or more tag strings
Example: add-tags 1 work urgent

Command: search <keyword>
Description: Searches tasks by keyword
Parameters:
  - keyword: String to search for
Example: search groceries

Command: filter [status=<status>] [priority=<priority>] [tag=<tag>]
Description: Filters tasks by criteria
Parameters:
  - status: Optional status (pending, complete)
  - priority: Optional priority (high, medium, low)
  - tag: Optional tag to include
Example: filter status=pending priority=high

Command: sort <criterion>
Description: Sorts tasks by specified criterion
Parameters:
  - criterion: Sort criterion (priority, title, status)
Example: sort priority
```

### Enhanced View Command
```
Command: view [options]
Description: Displays tasks with optional filtering and sorting
Parameters:
  - --filter-status: Filter by status (pending, complete)
  - --filter-priority: Filter by priority (high, medium, low)
  - --filter-tag: Filter by tag
  - --sort: Sort by criterion (priority, title)
  - --search: Search by keyword
Example: view --filter-priority=high --sort=priority
```