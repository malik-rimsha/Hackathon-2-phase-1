"""
Notification service for the Todo application.
Handles browser notifications for due tasks and console warnings for overdue tasks.
"""
from datetime import datetime, timedelta
from typing import List, Optional
import sys

try:
    import js
    import pyscript
    BROWSER_ENV = True
except ImportError:
    BROWSER_ENV = False

from ..models.task import Task
from ..services.task_service import TaskService


class NotificationService:
    """
    Service to handle notifications for due tasks.
    """
    def __init__(self, task_service: Optional[TaskService] = None):
        self.browser_notifications_supported = BROWSER_ENV
        self.task_service = task_service

    def check_due_tasks(self) -> List[Task]:
        """
        Check for tasks that are due within the next 5 minutes.

        Returns:
            List of tasks due within the next 5 minutes
        """
        now = datetime.now()
        five_minutes_later = now + timedelta(minutes=5)

        due_tasks = []
        all_tasks = self.get_all_tasks()

        for task in all_tasks:
            if task.due_datetime and not task.completed:
                # Check if task is due within the next 5 minutes
                if now <= task.due_datetime <= five_minutes_later:
                    due_tasks.append(task)

        return due_tasks

    def request_notification_permission(self) -> bool:
        """
        Request permission to show browser notifications.

        Returns:
            Boolean indicating if permission was granted
        """
        if not self.browser_notifications_supported:
            return False

        try:
            # In PyScript, we can request notification permission
            # Note: This returns a promise, so we handle it appropriately
            permission = js.Notification.requestPermission()
            # For simplicity in this implementation, we'll assume it returns the permission state
            return str(permission) == "granted"
        except Exception:
            return False

    def show_notification(self, task: Task) -> bool:
        """
        Show a browser notification for the given task.

        Args:
            task: Task to show notification for

        Returns:
            Boolean indicating if notification was shown successfully
        """
        if not self.browser_notifications_supported:
            return False

        try:
            # Check if notifications are permitted
            if str(js.Notification.permission) == "granted":
                # Create and show notification
                notification_options = {
                    "body": f"Task due: {task.description}" if task.description else "Task due soon!",
                }
                # Add icon if available
                if hasattr(self, 'icon_url'):
                    notification_options["icon"] = self.icon_url

                notification = js.Notification.new(task.title, notification_options)
                return True
            else:
                # Permission not granted
                return False
        except Exception as e:
            print(f"Error showing notification: {e}")
            return False

    def show_console_warning(self, task: Task):
        """
        Show a console warning for overdue tasks.

        Args:
            task: Task that is overdue
        """
        if task.due_datetime and task.due_datetime < datetime.now():
            print(f"⚠️  OVERDUE TASK: {task.title} (was due: {task.due_datetime.strftime('%Y-%m-%d %H:%M')})")
        elif task.due_datetime and task.due_datetime.date() == datetime.now().date():
            print(f"📅 DUE TODAY: {task.title} (due: {task.due_datetime.strftime('%H:%M')})")

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks from the task service.

        Returns:
            List of all Task objects
        """
        if self.task_service:
            return self.task_service.get_all_tasks()
        return []

    def start_polling(self, interval_seconds: int = 60):
        """
        Start a polling mechanism to check for due tasks.

        Args:
            interval_seconds: Interval in seconds between checks (default 60)
        """
        if self.browser_notifications_supported:
            try:
                # Use JavaScript setInterval to run the check periodically
                from js import setInterval
                def check_and_notify():
                    due_tasks = self.check_due_tasks()
                    for task in due_tasks:
                        self.show_notification(task)

                # Start the polling
                self.polling_interval = setInterval(check_and_notify, interval_seconds * 1000)
            except Exception as e:
                print(f"Error starting polling: {e}")
        else:
            print("Polling only works in browser environment with PyScript")