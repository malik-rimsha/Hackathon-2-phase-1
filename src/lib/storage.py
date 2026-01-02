"""
Storage implementation for the Todo application.
Uses in-memory storage with support for enhanced Task attributes.
"""
from typing import Dict, List
from ..models.task import Task


class InMemoryStorage:
    """
    In-memory storage implementation for Task objects.
    """
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1

    def add_task(self, task: Task) -> int:
        """
        Add a new task to storage.

        Args:
            task: Task object to add

        Returns:
            ID of the newly created task
        """
        task.id = self.next_id
        self.tasks[self.next_id] = task
        task_id = self.next_id
        self.next_id += 1
        return task_id

    def get_task(self, task_id: int) -> Task:
        """
        Retrieve a specific task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in storage.

        Returns:
            List of all Task objects in the order they were added
        """
        return list(self.tasks.values())

    def update_task(self, task_id: int, updated_task: Task) -> bool:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            updated_task: Updated Task object

        Returns:
            True if update was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        self.tasks[task_id] = updated_task
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from storage.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        del self.tasks[task_id]
        return True

    def clear(self):
        """
        Clear all tasks from storage.
        """
        self.tasks.clear()
        self.next_id = 1