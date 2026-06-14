from datetime import datetime
from enum import Enum

class Priority(str, Enum):
    LOW= "baja"
    MEDIUM= "media"
    HIGH= "alta"

class Task:
    def __init__(self, id: int, title: str, priority: Priority = Priority.MEDIUM, done: bool = False):
        self.id = id
        self.title = title
        self.priority = priority
        self.done = done
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        return{
            "id":self.id,
            "title": self.title,
            "priority": self.priority.value,
            "done": self.done,
            "created_at": self.created_at,
        }