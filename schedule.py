from lessons import Lesson
from slot import Slot
from students_group import StudentsGroup
from subject import Subject
from teacher import Teacher

class Schedule:
    def __init__(self, groups: list, num_slots_per_day: int = 7, days_per_week: int = 5):
        self.groups = groups

        teachers = set()
        for group in groups:
            teachers.update(group.data.keys())
        self.teachers = list(teachers)

        self.max_lessons_per_slot = min(len(groups), len(teachers))
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * days_per_week)]

    def calculate_metric(self):
        s = 0
        for group in self.groups:
            group.calculate_metric()
            s += group.calculate_metric()
        return s / len(self.groups)    
                                
    def create_schedule(self):
        ptr = 0
        for group in self.groups:
            for teacher in group.data:
                for _ in range(group.data[teacher]):
                    min_metric  = float("inf")
                    min_metric_index = 0
                    for i in range(len(self.slots)):
                        lesson = Lesson(group, teacher)
                        if self.slots[i].can_add(lesson):
                            self.slots[i].add_lesson(lesson)
                            current_metric = self.calculate_metric()   
                            if current_metric < min_metric:
                                min_metric = current_metric
                                min_metric_index = i
                            self.slots[i].remove_lesson(-1)
                    self.slots[min_metric_index].add_lesson(Lesson(group, teacher))