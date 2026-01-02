# Quickstart Guide: Advanced Todo Features

## Prerequisites

- Python 3.13+
- UV package manager
- For browser notifications: A modern browser that supports PyScript

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies
```bash
uv sync
```

## Running the Application

### Console Mode (Standard)
```bash
cd src
python cli/main.py
```

### Browser Mode (with Notifications)
1. Navigate to the web directory:
```bash
cd src/web
```

2. Start a local server:
```bash
python -m http.server 8000
```

3. Open your browser and go to:
```
http://localhost:8000
```

## New Features

### 1. Creating Recurring Tasks
```bash
# Create a daily recurring task
python cli/main.py add "Daily exercise" --recurrence daily

# Create a weekly recurring task
python cli/main.py add "Weekly team meeting" --recurrence weekly

# Create a monthly recurring task
python cli/main.py add "Monthly budget review" --recurrence monthly
```

### 2. Setting Due Dates
```bash
# Set a due date for a task
python cli/main.py set-due 1 "2026-01-15"

# Set a due date with time
python cli/main.py set-due 1 "2026-01-15 14:30"

# Set a due date using relative terms
python cli/main.py set-due 1 "tomorrow"
python cli/main.py set-due 1 "next week"
```

### 3. Marking Recurring Tasks Complete
```bash
# When you complete a recurring task, a new instance is automatically created
python cli/main.py complete 1
```

## New Commands

### Task Management
- `add <title> [description] [--recurrence daily|weekly|monthly]`: Add a new task (with optional recurrence)
- `set-due <task_id> <date> [time]`: Set a due date for a task
- `set-recurrence <task_id> <interval>`: Set recurrence for a task
- `list [--overdue] [--due-today] [--due-soon]`: List tasks with optional filters

### Browser Mode Features
- Tasks due within 5 minutes will trigger browser notifications
- Overdue tasks will be highlighted in the list
- Recurring tasks will automatically generate new instances when completed

## Data Model Changes

### Task Model Extensions
The Task model now includes:
- `due_datetime`: Optional datetime for task due date/time
- `recurrence`: Optional recurrence interval (daily, weekly, monthly)

### Display Format Updates
Tasks now display with additional information:
- Due dates: (2026-01-10 15:00) or (Overdue!)
- Recurrence: 🔁 Daily/Weekly/Monthly

## Architecture Overview

### New Modules
- `src/models/recurrence.py`: Defines recurrence interval enum and rules
- `src/services/notification_service.py`: Handles notification logic
- `src/web/`: Contains PyScript-compatible version and HTML interface

### Core Extensions
- Extended `Task` model with recurrence and due_datetime attributes
- Enhanced `TodoList` service with recurrence and due date logic
- Updated CLI with new commands for managing advanced features
- Notification system with browser and console fallbacks

## Development

### Running Tests
```bash
# Unit tests
python -m pytest tests/unit/

# Integration tests
python -m pytest tests/integration/

# All tests
python -m pytest tests/
```

### Adding New Features
1. Update the data model in `src/models/`
2. Implement business logic in `src/services/`
3. Add CLI commands in `src/cli/main.py`
4. Write tests in `tests/`
5. Update documentation as needed

## Troubleshooting

### Browser Notifications Not Working
- Ensure you're using a PyScript-compatible browser
- Check that you've granted notification permissions
- Verify that the index.html file is served via HTTP (not file://)

### Due Date Parsing Issues
- Use the format YYYY-MM-DD for dates
- Use the format YYYY-MM-DD HH:MM for date and time
- For relative dates, use "tomorrow", "next week", etc.