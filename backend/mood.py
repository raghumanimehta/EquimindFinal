from datetime import datetime
from enum import Enum
from typing import List, Optional

class MoodLevel(Enum):
    TERRIBLE = 1
    BAD = 2
    NEUTRAL = 3
    GOOD = 4
    GREAT = 5

class SleepQuality(Enum):
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4

class StressLevel(Enum):
    NONE = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    SEVERE = 5

class Mood:
    def __init__(self, 
                 level: MoodLevel,
                 timestamp: datetime = None,
                 sleep_quality: Optional[SleepQuality] = None,
                 stress_level: Optional[StressLevel] = None,
                 sleep_hours: Optional[float] = None,
                 physical_activity: Optional[bool] = None,
                 activities: List[str] = None,
                 notes: str = None):
        self.level = level
        self.timestamp = timestamp or datetime.now()
        self.sleep_quality = sleep_quality
        self.stress_level = stress_level
        self.sleep_hours = sleep_hours
        self.physical_activity = physical_activity
        self.activities = activities or []
        self.notes = notes

    def add_activity(self, activity: str) -> None:
        self.activities.append(activity)
        
    def add_note(self, note: str) -> None:
        self.notes = note
        
    def get_numerical_score(self) -> int:
        return self.level.value

    

        