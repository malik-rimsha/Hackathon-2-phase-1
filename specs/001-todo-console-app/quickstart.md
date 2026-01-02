# Quickstart Guide: Todo In-Memory Python Console App

## Prerequisites

- Python 3.13+ installed
- UV package manager installed

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies (if any):
   ```bash
   uv pip install -r requirements.txt  # If requirements file exists
   # Or if no requirements file:
   # No additional dependencies needed (using only Python stdlib)
   ```

## Running the Application

1. Navigate to the project root directory
2. Run the application:
   ```bash
   python src/main.py
   ```

## Using the Application

The application provides a menu-driven interface:

1. **Add a new task**: Enter title and description
2. **View all tasks**: Shows all tasks with ID, status indicator, title, and description
3. **Update a task**: Enter task ID and new title/description
4. **Delete a task**: Enter task ID to remove
5. **Mark task as complete/incomplete**: Enter task ID and completion status
6. **Exit**: Quit the application

## Example Usage

```
Todo Application
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Mark task as complete/incomplete
6. Exit

Enter your choice (1-6): 1
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added with ID: 1

Enter your choice (1-6): 2
ID  Status  Title            Description
1   [ ]     Buy groceries    Milk, bread, eggs
```

## Development

To modify the application:

- `src/todo.py`: Contains the Task dataclass and TodoList class with all business logic
- `src/main.py`: Contains the CLI interface and user interaction loop

## Testing

Manual console demo checklist covering all 5 features end-to-end:
- Add multiple tasks → correct listing with IDs and status
- Update/Delete/Mark with invalid ID → graceful error message, no crash
- Empty list operations → appropriate "no tasks" messages
- Mark complete/incomplete toggle works correctly
- Code quality checks: Type hints present, docstrings on public functions/classes, PEP 8 compliance