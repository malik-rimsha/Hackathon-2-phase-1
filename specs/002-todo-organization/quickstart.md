# Quickstart Guide: Todo Organization & Usability

## Overview

This guide will help you get started with the enhanced Todo application featuring organization and usability improvements. The application extends the basic functionality with priorities, tags, search, filter, and sort capabilities.

## Prerequisites

- Python 3.13+ installed
- UV package manager (optional, for dependency management)
- Console/terminal access

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Navigate to the Source Directory
```bash
cd src
```

### 3. Run the Application
```bash
python main.py
```

## Basic Usage

### Adding a Task
```bash
add "Task title" "Optional description"
```

### Viewing Tasks
```bash
view
```

### Updating a Task
```bash
update 1 "New title" "New description"
```

### Marking a Task Complete
```bash
complete 1
```

### Deleting a Task
```bash
delete 1
```

## New Intermediate Features

### Assigning Priority
Assign a priority level (high, medium, low) to a task:
```bash
assign-priority 1 high
```

### Adding Tags
Add one or more tags to a task:
```bash
add-tags 1 work urgent
```

### Searching Tasks
Search tasks by keyword in title or description:
```bash
search "groceries"
```

### Filtering Tasks
Filter tasks by various criteria:
```bash
# Filter by status
filter status=pending

# Filter by priority
filter priority=high

# Filter by tag
filter tag=work

# Combined filters
filter status=pending priority=high
```

### Sorting Tasks
Sort tasks by different criteria:
```bash
# Sort by priority (High to Low)
sort priority

# Sort alphabetically by title
sort title
```

### Enhanced View Command
View tasks with optional filtering and sorting:
```bash
# View with priority filter
view --filter-priority=high

# View with search
view --search=groceries

# View sorted by priority
view --sort=priority

# Combined options
view --filter-status=pending --sort=priority
```

## Display Format

Tasks are displayed with priority indicators and tags:
```
[1] [H] Buy groceries  #shopping #urgent  [ ]
[2] [M] Finish report  #work #important  [X]
[3] [L] Call mom  #personal  [ ]
```

- `[H]`, `[M]`, `[L]` indicate High, Medium, Low priority
- `#tag` shows assigned tags
- `[ ]` indicates pending task, `[X]` indicates completed task

## Example Workflow

1. Add a task:
   ```bash
   add "Prepare presentation" "Prepare slides for team meeting"
   ```

2. Assign priority:
   ```bash
   assign-priority 1 high
   ```

3. Add tags:
   ```bash
   add-tags 1 work important
   ```

4. View with priority indicator:
   ```bash
   view
   ```

5. Filter by priority:
   ```bash
   filter priority=high
   ```

6. Sort by priority:
   ```bash
   sort priority
   ```

## Troubleshooting

### Common Issues

- **Invalid task ID**: Ensure the task ID exists before trying to modify it
- **Invalid priority**: Use only "high", "medium", or "low" for priority values
- **Empty tags**: Tags cannot be empty strings

### Error Messages

- "Task not found": The specified task ID does not exist
- "Invalid priority": Priority must be one of: high, medium, low
- "Invalid tag": Tags cannot be empty strings