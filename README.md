# Advanced Todo Application with Recurring Tasks and Time-Based Reminders

This is an advanced todo application that extends the basic functionality with recurring tasks and time-based reminders with browser notifications.

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
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

## Features

- Add, view, update, and delete tasks
- Assign priorities and tags to tasks
- Search and filter tasks
- Sort tasks by various criteria
- **NEW**: Create recurring tasks (daily, weekly, monthly)
- **NEW**: Set due dates and times for tasks
- **NEW**: Receive browser notifications for tasks due within 5 minutes
- **NEW**: Console warnings for overdue tasks

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

## Architecture

The application follows a modular architecture with clear separation of concerns:

- `src/models/` - Data models (Task, RecurrenceRule, etc.)
- `src/services/` - Business logic (TaskService, NotificationService, etc.)
- `src/cli/` - Command-line interface
- `src/lib/` - Common utilities and storage
- `src/web/` - Browser-specific code and HTML interface