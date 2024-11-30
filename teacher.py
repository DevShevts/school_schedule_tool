
from slot import Slot
from subject import Subject

class Teacher:
    def __init__(self, name: str, subject: Subject, num_slots_per_day: int = 7):
        self.name = name
        self.subject = subject

        self.max_lessons_per_slot = 1
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * 5)]

    def calculate_metric(self):
        metric = 50
        for slot in self.slots:
            pass

    def __repr__(self):
        return f"{self.name} {self.subject}"