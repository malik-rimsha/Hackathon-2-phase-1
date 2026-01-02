"""
Task service for the Todo application.
Handles business logic for tasks including recurring tasks and due dates.
"""
from datetime import datetime, timedelta
from typing import List, Optional
import calendar

from ..models.task import Task, Priority
from ..models.recurrence import RecurrenceInterval
from ..lib.storage import InMemoryStorage


class TaskService:
    """
    Service class to handle task business logic.
    """
    def __init__(self):
        self.storage = InMemoryStorage()

    def add_task(self, title: str, description: str = "", recurrence: Optional[RecurrenceInterval] = None, due_datetime: Optional[datetime] = None) -> int:
        """
        Add a new task with optional recurrence settings.

        Args:
            title: Task title
            description: Task description
            recurrence: Optional recurrence interval (DAILY, WEEKLY, MONTHLY)
            due_datetime: Optional due date and time

        Returns:
            ID of the newly created task
        """
        if not title or not title.strip():
            return -1

        # Create a new task with the provided parameters
        task = Task(
            id=0,  # Will be set by storage
            title=title.strip(),
            description=description.strip(),
            recurrence=recurrence,
            due_datetime=due_datetime
        )

        return self.storage.add_task(task)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a specific task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.storage.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            List of all Task objects
        """
        return self.storage.get_all_tasks()

    def update_task(self, task_id: int, title: str = None, description: str = None, 
                    priority: Priority = None, tags: List[str] = None, 
                    due_datetime: datetime = None, recurrence: RecurrenceInterval = None) -> bool:
        """
        Update an existing task's details.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)
            tags: New tags (optional)
            due_datetime: New due date/time (optional)
            recurrence: New recurrence (optional)

        Returns:
            True if update was successful, False if task not found
        """
        task = self.storage.get_task(task_id)
        if not task:
            return False

        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if priority is not None:
            task.priority = priority
        if tags is not None:
            task.tags = tags
        if due_datetime is not None:
            task.due_datetime = due_datetime
        if recurrence is not None:
            task.recurrence = recurrence

        # Update the timestamp
        task.updated_at = datetime.now()

        return self.storage.update_task(task_id, task)

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion was successful, False if task not found
        """
        return self.storage.delete_task(task_id)

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete; if the task is recurring, creates a new instance.

        Args:
            task_id: ID of the task to mark complete

        Returns:
            True if operation was successful, False if task not found
        """
        task = self.storage.get_task(task_id)
        if not task:
            return False

        # Mark the current task as complete
        task.completed = True
        task.updated_at = datetime.now()

        # If the task is recurring, create a new instance
        if task.recurrence:
            self._create_next_instance(task)

        return self.storage.update_task(task_id, task)

    def _create_next_instance(self, task: Task) -> Optional[Task]:
        """
        Create a new instance of a recurring task with the next occurrence date.

        Args:
            task: The original recurring task

        Returns:
            New task instance if created, None otherwise
        """
        if not task.recurrence:
            return None

        # Calculate the next occurrence date based on the recurrence interval
        next_due_datetime = self._calculate_next_occurrence(task.due_datetime, task.recurrence)

        # Create a new task with the same properties as the original
        new_task = Task(
            id=0,  # Will be set by storage
            title=task.title,
            description=task.description,
            completed=False,
            priority=task.priority,
            tags=task.tags.copy() if task.tags else [],
            due_datetime=next_due_datetime,
            recurrence=task.recurrence,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        # Add the new task to storage
        new_task_id = self.storage.add_task(new_task)
        return new_task if new_task_id != -1 else None

    def _calculate_next_occurrence(self, current_due: Optional[datetime], interval: RecurrenceInterval) -> Optional[datetime]:
        """
        Calculate the next occurrence date based on the recurrence interval.

        Args:
            current_due: Current due date
            interval: Recurrence interval

        Returns:
            Next occurrence date
        """
        if not current_due:
            return None

        if interval == RecurrenceInterval.DAILY:
            return current_due + timedelta(days=1)
        elif interval == RecurrenceInterval.WEEKLY:
            return current_due + timedelta(weeks=1)
        elif interval == RecurrenceInterval.MONTHLY:
            # Calculate next month, handling month boundaries correctly
            if current_due.month == 12:
                next_month = 1
                next_year = current_due.year + 1
            else:
                next_month = current_due.month + 1
                next_year = current_due.year

            # Handle cases where the day doesn't exist in the next month (e.g., Jan 31 -> Feb 31 doesn't exist)
            max_day_next_month = calendar.monthrange(next_year, next_month)[1]
            next_day = min(current_due.day, max_day_next_month)

            return current_due.replace(year=next_year, month=next_month, day=next_day)
        
        return None

    def set_due_date(self, task_id: int, date_str: str, time_str: Optional[str] = None) -> bool:
        """
        Set a due date for an existing task.

        Args:
            task_id: ID of the task to update
            date_str: Date string in format "YYYY-MM-DD" or relative terms like "tomorrow"
            time_str: Optional time string in format "HH:MM"

        Returns:
            Boolean indicating success
        """
        task = self.storage.get_task(task_id)
        if not task:
            return False

        # Parse the date string
        due_datetime = self._parse_date_string(date_str, time_str)
        if due_datetime is None:
            return False

        task.due_datetime = due_datetime
        task.updated_at = datetime.now()

        return self.storage.update_task(task_id, task)

    def _parse_date_string(self, date_str: str, time_str: Optional[str] = None) -> Optional[datetime]:
        """
        Parse a date string and return a datetime object.

        Args:
            date_str: Date string in format "YYYY-MM-DD" or relative terms like "tomorrow"
            time_str: Optional time string in format "HH:MM"

        Returns:
            Parsed datetime object or None if parsing fails
        """
        from datetime import datetime, timedelta

        # Handle relative dates
        if date_str.lower() == "today":
            base_date = datetime.now().date()
        elif date_str.lower() == "tomorrow":
            base_date = (datetime.now() + timedelta(days=1)).date()
        elif date_str.lower() == "yesterday":
            base_date = (datetime.now() - timedelta(days=1)).date()
        elif "next" in date_str.lower():
            if "week" in date_str.lower():
                base_date = (datetime.now() + timedelta(weeks=1)).date()
            elif "month" in date_str.lower():
                # Add approximately one month
                current = datetime.now()
                if current.month == 12:
                    base_date = current.replace(year=current.year + 1, month=1, day=1).date()
                else:
                    base_date = current.replace(month=current.month + 1, day=1).date()
            else:
                # Default to next week if just "next" is specified
                base_date = (datetime.now() + timedelta(weeks=1)).date()
        else:
            # Handle absolute dates in YYYY-MM-DD format
            try:
                from datetime import datetime
                if time_str:
                    # Parse date and time
                    datetime_str = f"{date_str} {time_str}"
                    base_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
                    return base_datetime
                else:
                    # Parse just the date, defaulting to start of day
                    base_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return None

        # If we have a time string, combine it with the date
        if time_str:
            try:
                time_obj = datetime.strptime(time_str, "%H:%M").time()
                return datetime.combine(base_date, time_obj)
            except ValueError:
                return None
        else:
            # Default to start of the day if no time specified
            return datetime.combine(base_date, datetime.min.time())

    def set_recurrence(self, task_id: int, interval: RecurrenceInterval) -> bool:
        """
        Set recurrence for an existing task.

        Args:
            task_id: ID of the task to update
            interval: Recurrence interval (DAILY, WEEKLY, MONTHLY)

        Returns:
            Boolean indicating success
        """
        task = self.storage.get_task(task_id)
        if not task:
            return False

        task.recurrence = interval
        task.updated_at = datetime.now()

        return self.storage.update_task(task_id, task)

    def get_tasks_with_filter(self, filter_type: Optional[str] = None) -> List[Task]:
        """
        Retrieve tasks with optional filtering.

        Args:
            filter_type: Optional filter type ("overdue", "due-today", "due-soon", "recurring")

        Returns:
            List of Task objects matching the filter
        """
        all_tasks = self.get_all_tasks()
        
        if not filter_type:
            return all_tasks

        filtered_tasks = []
        now = datetime.now()

        for task in all_tasks:
            if filter_type == "overdue" and task.due_datetime and task.due_datetime < now and not task.completed:
                filtered_tasks.append(task)
            elif filter_type == "due-today" and task.due_datetime and task.due_datetime.date() == now.date() and not task.completed:
                filtered_tasks.append(task)
            elif filter_type == "due-soon" and task.due_datetime and now <= task.due_datetime <= (now + timedelta(hours=24)) and not task.completed:
                filtered_tasks.append(task)
            elif filter_type == "recurring" and task.recurrence:
                filtered_tasks.append(task)

        return filtered_tasks