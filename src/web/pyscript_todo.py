"""
PyScript-compatible version of the todo app.
This version is designed to run in a browser environment with PyScript.
"""
from datetime import datetime
from typing import Optional

from ..services.task_service import TaskService
from ..services.notification_service import NotificationService
from ..models.task import Task, Priority
from ..models.recurrence import RecurrenceInterval


class PyScriptTodoApp:
    """
    PyScript-compatible Todo application class.
    """
    def __init__(self):
        self.task_service = TaskService()
        self.notification_service = NotificationService(self.task_service)
        
        # Request notification permission when the app starts
        self.notification_service.request_notification_permission()
        
        # Start the polling mechanism to check for due tasks
        self.notification_service.start_polling()

    def add_task(self, title: str, description: str = "", recurrence: Optional[str] = None, due_date_str: Optional[str] = None) -> int:
        """
        Add a new task with optional recurrence settings and due date.

        Args:
            title: Task title
            description: Task description
            recurrence: Optional recurrence string ('daily', 'weekly', 'monthly')
            due_date_str: Optional due date string in format 'YYYY-MM-DD HH:MM'

        Returns:
            ID of the newly created task
        """
        # Parse recurrence if provided
        recurrence_interval = None
        if recurrence:
            if recurrence.lower() == 'daily':
                recurrence_interval = RecurrenceInterval.DAILY
            elif recurrence.lower() == 'weekly':
                recurrence_interval = RecurrenceInterval.WEEKLY
            elif recurrence.lower() == 'monthly':
                recurrence_interval = RecurrenceInterval.MONTHLY

        # Parse due date if provided
        due_datetime = None
        if due_date_str:
            try:
                # Parse date and time
                due_datetime = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    # Try parsing just the date
                    date_only = datetime.strptime(due_date_str, "%Y-%m-%d")
                    # Set time to 00:00 (start of day)
                    due_datetime = datetime.combine(date_only.date(), datetime.min.time())
                except ValueError:
                    # Invalid format, leave as None
                    pass

        return self.task_service.add_task(title, description, recurrence_interval, due_datetime)

    def get_all_tasks(self) -> list:
        """
        Get all tasks.

        Returns:
            List of all tasks
        """
        return self.task_service.get_all_tasks()

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: ID of the task to mark complete

        Returns:
            True if successful, False otherwise
        """
        return self.task_service.mark_complete(task_id)

    def set_due_date(self, task_id: int, date_str: str, time_str: Optional[str] = None) -> bool:
        """
        Set a due date for a task.

        Args:
            task_id: ID of the task
            date_str: Date string in format "YYYY-MM-DD" or relative terms like "tomorrow"
            time_str: Optional time string in format "HH:MM"

        Returns:
            True if successful, False otherwise
        """
        return self.task_service.set_due_date(task_id, date_str, time_str)

    def set_recurrence(self, task_id: int, interval_str: str) -> bool:
        """
        Set recurrence for a task.

        Args:
            task_id: ID of the task
            interval_str: Recurrence interval string ('daily', 'weekly', 'monthly')

        Returns:
            True if successful, False otherwise
        """
        interval = None
        if interval_str.lower() == 'daily':
            interval = RecurrenceInterval.DAILY
        elif interval_str.lower() == 'weekly':
            interval = RecurrenceInterval.WEEKLY
        elif interval_str.lower() == 'monthly':
            interval = RecurrenceInterval.MONTHLY
        else:
            return False

        return self.task_service.set_recurrence(task_id, interval)

    def format_task_display(self, task: Task) -> str:
        """
        Format a task for display with due dates and recurrence indicators.

        Args:
            task: The task to format

        Returns:
            Formatted string representation of the task
        """
        status = "[x]" if task.completed else "[ ]"

        # Get priority indicator
        priority_indicator = ""
        if task.priority == Priority.HIGH:
            priority_indicator = "[H]"
        elif task.priority == Priority.MEDIUM:
            priority_indicator = "[M]"
        elif task.priority == Priority.LOW:
            priority_indicator = "[L]"
        else:
            priority_indicator = "   "  # Three spaces for no priority

        # Format due date
        due_date_str = ""
        if task.due_datetime:
            if task.due_datetime < datetime.now():
                due_date_str = f" (Overdue: {task.due_datetime.strftime('%Y-%m-%d %H:%M')})"
            elif task.due_datetime.date() == datetime.now().date():
                due_date_str = f" (Due Today: {task.due_datetime.strftime('%H:%M')})"
            else:
                due_date_str = f" (Due: {task.due_datetime.strftime('%Y-%m-%d %H:%M')})"

        # Format recurrence
        recurrence_str = ""
        if task.recurrence:
            recurrence_map = {
                RecurrenceInterval.DAILY: "🔁 Daily",
                RecurrenceInterval.WEEKLY: "🔁 Weekly", 
                RecurrenceInterval.MONTHLY: "🔁 Monthly"
            }
            recurrence_str = f" {recurrence_map.get(task.recurrence, '')}"

        # Format tags
        tags_display = ""
        if task.tags:
            tags_display = " " + " ".join([f"#{tag}" for tag in task.tags])

        return f"{task.id} {priority_indicator} {status} {task.title} {task.description}{due_date_str}{recurrence_str}{tags_display}"


# Create a global instance for PyScript to use
app = PyScriptTodoApp()