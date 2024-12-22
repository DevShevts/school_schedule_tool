
from slot import Slot
from subject import Subject

class Teacher:
    def __init__(self, name: str, subject: Subject, num_slots_per_day: int = 7, days_per_week: int = 5):
        self.name = name
        self.subject = subject

        self.max_lessons_per_slot = 1
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * days_per_week)]

    def calculate_metric(self):
        pass

    def __repr__(self):
        return f"{self.name} {self.subject}"