"""
Todo application data models and business logic.
"""
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

class Priority(Enum):
    """
    Priority levels for tasks.
    """
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Task:
    """
    Represents a single task with ID, title, description, and completion status.
    """
    id: int
    title: str
    description: str
    completed: bool = False
    priority: Optional[Priority] = None
    tags: List[str] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []


class TodoList:
    """
    Manages a collection of tasks in memory.
    """
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task to the list.

        Args:
            title: Task title (required, non-empty)
            description: Task description (optional)

        Returns:
            ID of the newly created task, or -1 if title is empty
        """
        if not title or not title.strip():
            return -1

        task = Task(id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        task_id = self.next_id
        self.next_id += 1
        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the list.

        Returns:
            List of all Task objects in the order they were added
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a specific task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update an existing task's title and/or description.

        Args:
            task_id: ID of the task to update
            title: New title (optional, if provided will update)
            description: New description (optional, if provided will update)

        Returns:
            True if update was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the list.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_completed(self, task_id: int, completed: bool) -> bool:
        """
        Update the completion status of a task.

        Args:
            task_id: ID of the task to update
            completed: New completion status

        Returns:
            True if update was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = completed
        return True

    def assign_priority(self, task_id: int, priority: Priority) -> bool:
        """
        Assign a priority level to a task.

        Args:
            task_id: ID of the task to update
            priority: Priority level to assign (HIGH, MEDIUM, LOW)

        Returns:
            True if update was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.priority = priority
        return True

    def add_tags(self, task_id: int, tags: List[str]) -> bool:
        """
        Add one or more tags to a task.

        Args:
            task_id: ID of the task to update
            tags: List of tags to add to the task

        Returns:
            True if update was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Add tags that are not already in the task's tags list
        for tag in tags:
            if tag and tag.strip() and tag.strip() not in task.tags:
                task.tags.append(tag.strip())

        return True

    def remove_tags(self, task_id: int, tags: List[str]) -> bool:
        """
        Remove one or more tags from a task.

        Args:
            task_id: ID of the task to update
            tags: List of tags to remove from the task

        Returns:
            True if update was successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Remove tags that exist in the task's tags list
        for tag in tags:
            if tag and tag.strip() and tag.strip() in task.tags:
                task.tags.remove(tag.strip())

        return True

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.

        Args:
            keyword: Keyword to search for in task titles and descriptions

        Returns:
            List of tasks that contain the keyword in their title or description
        """
        if not keyword:
            return []

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[bool] = None, priority: Optional[Priority] = None, tags: Optional[List[str]] = None) -> List[Task]:
        """
        Filter tasks by status, priority, or tags.

        Args:
            status: Optional status to filter by (True for completed, False for pending)
            priority: Optional priority to filter by
            tags: Optional list of tags to filter by (task must have at least one of these tags)

        Returns:
            List of tasks that match the specified criteria
        """
        filtered_tasks = []

        for task in self.tasks:
            # Check status filter
            if status is not None and task.completed != status:
                continue

            # Check priority filter
            if priority is not None and task.priority != priority:
                continue

            # Check tags filter
            if tags is not None and tags:
                # Check if task has at least one of the specified tags
                has_any_tag = any(tag in task.tags for tag in tags)
                if not has_any_tag:
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def get_sorted_tasks(self, tasks: List[Task], sort_by: str = "priority") -> List[Task]:
        """
        Return a sorted copy of the tasks list based on the specified criterion.

        Args:
            tasks: List of tasks to sort
            sort_by: Criterion to sort by ("priority", "title", "status")

        Returns:
            New sorted list of tasks
        """
        if sort_by == "priority":
            # Sort by priority: HIGH, MEDIUM, LOW, then by ID for tasks without priority
            return sorted(tasks, key=lambda t: (
                self._priority_value(t.priority) if t.priority else 999,  # Lower value = higher priority
                t.id  # Secondary sort by ID to maintain consistent order
            ))
        elif sort_by == "title":
            # Sort alphabetically by title (case-insensitive)
            return sorted(tasks, key=lambda t: t.title.lower())
        elif sort_by == "status":
            # Sort by status: completed tasks first, then by ID
            return sorted(tasks, key=lambda t: (t.completed, t.id))
        else:
            # Default to original order if sort_by is invalid
            return tasks.copy()

    def _priority_value(self, priority: Priority) -> int:
        """
        Helper method to get a numeric value for priority for sorting purposes.

        Args:
            priority: Priority enum value

        Returns:
            Numeric value (lower = higher priority)
        """
        if priority == Priority.HIGH:
            return 1
        elif priority == Priority.MEDIUM:
            return 2
        elif priority == Priority.LOW:
            return 3
        return 999  # Default for any other case