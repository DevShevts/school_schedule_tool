
import random
from students_group import StudentsGroup
from subject import Subject
from teacher import Teacher


class Lesson:
    def __init__(self, group, teacher):
        self.group = group
        self.teacher = teacher

    def __repr__(self):
        return f"{self.group} {self.teacher}"

class Slot:
    def __init__(self, index, max_lessons_per_slot):
        self.index = index
        self.lessons = []
        self.max_lessons_per_slot = max_lessons_per_slot

    def add_lesson(self, new_lesson: Lesson):
        if self.can_add(new_lesson):
            self.lessons.append(new_lesson)
            return True
        else:
            return False
        
    def get_lesson(self, index):
        return self.lessons(index)

    def can_add(self, new_lesson: Lesson):
        if new_lesson.group in self.get_groups():
            return False

        if new_lesson.teacher.name in self.get_teachers_names():
            return False

        if self.is_full():
            return False

        return True

    def get_teachers_names(self):
        return [lesson.teacher.name for lesson in self.lessons]

    def get_groups(self):
        return [lesson.group for lesson in self.lessons]

    def __repr__(self):
        result = f'\n slot {self.index}\n'
        for lesson in self.lessons:
            result += f"-- {lesson}\n"

        return result

    def is_full(self):
        return len(self.lessons) == self.max_lessons_per_slot


class Schedule:
    def __init__(self, groups: list, num_slots_per_day: int = 7):
        self.groups = groups

        teachers = set()
        for group in groups:
            teachers.update(group.data.keys())
        self.teachers = list(teachers)

        max_lessons_per_slot = min(len(groups), len(teachers))
        self.slots = [Slot(i, max_lessons_per_slot) for i in range(num_slots_per_day * 5)]

    def init_random_schedule__(self):
        slot_ptr = 0
        for group in self.groups:
            if self.slots[slot_ptr].is_full():
                slot_ptr += 1

            for teacher in group.data:
                number_per_week = group.data[teacher]
                for i in range(number_per_week):
                    result_flag = self.slots[slot_ptr + i].add_lesson(Lesson(group, teacher))

    def init_random_schedule(self):
        ptr = 0
        for group in self.groups:
            for teacher in group.data:
                for _ in range(group.data[teacher]):
                    for i in range(len(self.slots)):
                        result = self.slots[i].add_lesson(Lesson(group, teacher))
                        if result:
                            break
                        
    def print_schedule_for_group(schedule, index):
        groups[index]

    def calculate_metric(self) -> int:
        metric = 50
        for slot in self.slots:
            if len(slot.lessons) < 8:      #8 - колво классов; нужно для того чтобы не было ситуаций, когда в одном из классов нет урока
                metric -= 10
            # if slot.lessons
                            
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
schedule = schedule.init_random_schedule()
# print(schedule.slots)


print(Schedule.print_schedule_for_group(schedule, 1))