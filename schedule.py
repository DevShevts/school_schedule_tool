
import random
from lessons import Lesson
from slot import Slot
from students_group import StudentsGroup
from subject import Subject
from teacher import Teacher


class Schedule:
    def __init__(self, groups: list, num_slots_per_day: int = 7):
        self.groups = groups

        teachers = set()
        for group in groups:
            teachers.update(group.data.keys())
        self.teachers = list(teachers)

        self.max_lessons_per_slot = min(len(groups), len(teachers))
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * 5)]

    def init_random_schedule(self):
        ptr = 0
        for group in self.groups:
            for teacher in group.data:
                for _ in range(group.data[teacher]):
                    for i in range(len(self.slots)):
                        result = self.slots[i].add_lesson(Lesson(group, teacher))
                        # calculate metric
                        if result:
                            break
                        
    def get_schedule_for_group(self, idx):
        group = self.groups[idx]
        result = []
        for slot in self.slots:
            for lesson in slot.lessons:
                if lesson.group == group:
                    pass

    def calculate_metric(self) -> int:
        metric = 50
        for slot in self.slots:
            pass
            '''if len(slot.lessons) < self.max_lessons_per_slot:
                metric -= 10'''



        return metric

    def swap(self, slot1_index, slot2_index, lesson1_index, lesson2_index):
        lesson1 = Slot[slot1_index].get_lesson(lesson1_index)
        lesson2 = Slot[slot2_index].get_lesson(lesson2_index)
        lesson1, lesson2 = lesson2, lesson1



teacher1 = Teacher('AA', Subject.MATH)
teacher2 = Teacher('BB', Subject.PHYSICS)
teacher3 = Teacher('CC', Subject.CHEMISTRY)
teacher4 = Teacher('DD', Subject.RUSSIAN)
teacher5 = Teacher('EE', Subject.ENGLISH)
teacher6 = Teacher('FF', Subject.ENGLISH)
teacher7 = Teacher('GG', Subject.SPORTS)
teacher8 = Teacher('HH', Subject.SPORTS)
teacher9 = Teacher('AA', Subject.PHYSICS)
teacher10 = Teacher('BB', Subject.MATH)

groups = []
for i in range(12):
    data = {}
    for j in range(8):
        teacher = random.choice([teacher1, teacher2, teacher3, teacher4, teacher5, teacher6, teacher7, teacher8])
        if teacher not in data:
            data[teacher] = 1
        else:
            data[teacher] += 1
    groups.append(StudentsGroup(10, chr(65 + i), data))

schedule = Schedule(groups, num_slots_per_day=7)
schedule.init_random_schedule()
print(groups[0].slots)
print(groups[0].grade, groups[0].letter)
print(groups[0].list())
print(teacher1.slots)


