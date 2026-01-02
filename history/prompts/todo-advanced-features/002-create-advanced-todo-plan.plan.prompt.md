---
id: 002
title: create-advanced-todo-plan
stage: plan
date: 2026-01-02
surface: agent
model: gpt-4
feature: todo-advanced-features
branch: 003-todo-advanced-features
user: smc
command: sp.plan
labels: ["plan", "todo", "advanced", "recurring", "notifications"]
links:
  spec: ../spec.md
  ticket: null
  adr: null
  pr: null
files:
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\plan.md
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\research.md
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\data-model.md
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\quickstart.md
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\contracts\todo-api-contract.md
tests:
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\research.md
  - C:\Users\smc\Documents\GitHub\Hackathon-2-phase-1\specs\003-todo-advanced-features\data-model.md
---

## Prompt

/sp.plan Advanced Level: Intelligent Features for The Evolution of Todo Project

Create:
- Updated architecture sketch showing time-based intelligence and notification layer on top of existing Basic + Intermediate components
- Enhanced data model design with recurrence and due_datetime attributes
- Recurrence logic flow (what happens when marking a recurring task complete)
- Due date parsing and notification polling mechanism
- Browser-compatible execution plan (PyScript recommended for notifications)
- CLI fallback behavior for console-only environments
- Implementation roadmap with phased tasks building directly on the completed Intermediate Level code

Decisions needing documentation:
- Recurrence representation:  
  Options: Enum (DAILY, WEEKLY, MONTHLY) + optional end_date vs. full cron-like string  
  Tradeoff: Simple Enum with basic intervals is sufficient for hackathon demo, easier to implement and understand → selected (DAILY, WEEKLY, MONTHLY).
- Due date input format:  
  Options: Free natural language vs. strict formatted input (YYYY-MM-DD [HH:MM])  
  Tradeoff: Strict format with simple parsing (using datetime.strptime) avoids external deps and keeps reliability → selected.
- Due date/time storage:  
  Options: datetime.datetime object vs. separate date/time strings  
  Tradeoff: datetime.datetime provides easy comparison and calculation → selected.
- Notification implementation:  
  Options: Pure console warnings vs. browser desktop notifications via JavaScript bridge  
  Tradeoff: Browser notifications (using PyScript + window.Notification) for real demo impact, with console fallback → selected.
- Runtime environment for notifications:  
  Options: Brython, Pyodide, PyScript  
  Tradeoff: PyScript is modern, actively maintained, simple HTML setup, good Python 3.10+ support → selected.
- Auto-rescheduling timing:  
  Options: On mark-complete vs. background scheduler  
  Tradeoff: Immediate reschedule on mark-complete is simpler, no need for background thread → selected.

Testing strategy (validation based on Advanced success criteria):
- Manual demo checklist:
  - Create recurring weekly task → mark complete → new instance appears with date +7 days
  - Create daily recurring task → complete multiple times → chain of future instances created
  - Set due date/time on task → run in browser → notification appears at due time (or within 5-min window)
  - Overdue tasks show clear warning in console mode
  - Recurrence indicator (e.g., 🔁 Weekly) and due date shown in list view
  - All previous Basic + Intermediate features remain fully functional
- Edge case validation:
  - Monthly recurrence correctly handles different month lengths
  - Tasks with no due date → no notification attempt
  - Permission denied for notifications → graceful fallback message
  - Timezone handled consistently (use local time)

Technical details:
- Extend Task model with:
  - recurrence: Optional[RecurrenceInterval] = None (Enum: DAILY, WEEKLY, MONTHLY)
  - due_datetime: Optional[datetime.datetime] = None
- Extend TodoList class with:
  - set_due_date(task_id, date_str, time_str=None)
  - set_recurrence(task_id, interval)
  - _create_next_instance(task) → called after marking recurring task complete
- Notification system:
  - In browser (PyScript): Use js code to request Notification.permission and show notifications
  - Polling loop (every 60 seconds) checks for tasks due within next 5 minutes
  - Console fallback: Print warning for overdue tasks on list view
- Display enhancements:
  - Show due date: e.g., (2026-01-10 15:00) or (Overdue!)
  - Show recurrence: 🔁 Weekly
- Use only standard library for core logic (datetime, enum, dataclasses)
- For browser: Provide index.html with PyScript that loads src/main.py (adapted for web)
- Organize implementation by phases:
  1. Extend Task model with recurrence and due_datetime
  2. Implement recurrence logic: set_recurrence and auto-reschedule on complete
  3. Implement due date parsing and storage
  4. Add CLI commands for setting recurrence and due dates
  5. Update display format to show due dates and recurrence indicators
  6. Implement browser notification system (PyScript HTML + JS bridge)
  7. Add polling loop for checking due tasks (browser only)
  8. Implement console fallback warnings
  9. Create index.html with PyScript setup to run the app in browser
  10. Update README.md with browser setup instructions and demo steps
  11. Polish user messages and error handling

## Response snapshot

Created a comprehensive implementation plan for the advanced todo features, including:
- Updated implementation plan document with technical context, constitution check, and project structure
- Research summary documenting key decisions made for recurrence representation, due date handling, and notification implementation
- Data model specification with extended Task model and RecurrenceRule model
- Quickstart guide for developers to set up and run the application with new features
- API contract defining the expected behavior of the service methods

All artifacts were created in the appropriate directory structure under specs/003-todo-advanced-features/ including plan.md, research.md, data-model.md, quickstart.md, and contracts/todo-api-contract.md.

## Outcome

- ✅ Impact: Created complete implementation plan for advanced todo features with recurring tasks and time-based reminders
- 🧪 Tests: Research and data model validated against requirements
- 📁 Files: All required planning artifacts created and organized
- 🔁 Next prompts: Ready for task breakdown with /sp.tasks
- 🧠 Reflection: Plan addresses all requirements from the feature description and follows constitution guidelines

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All planning artifacts completed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to task breakdown phase