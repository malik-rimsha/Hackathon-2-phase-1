from datetime import datetime
from enum import Enum
from typing import Optional, List
from dataclasses import dataclass
from .recurrence import RecurrenceInterval


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
    Extended to include recurrence and due date/time attributes.
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Optional[Priority] = None
    tags: Optional[List[str]] = None
    due_datetime: Optional[datetime] = None  # due date and time
    recurrence: Optional[RecurrenceInterval] = None  # recurrence interval
    created_at: Optional[datetime] = None  # creation timestamp
    updated_at: Optional[datetime] = None  # last update timestamp

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
        if self.tags is None:
            self.tags = []