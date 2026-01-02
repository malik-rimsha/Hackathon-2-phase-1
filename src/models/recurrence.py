from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass


class RecurrenceInterval(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


@dataclass
class RecurrenceRule:
    interval: RecurrenceInterval
    created_at: datetime
    next_occurrence: datetime
    end_date: Optional[datetime] = None  # optional end date for recurrence