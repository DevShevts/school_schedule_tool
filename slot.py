from copy import deepcopy
from lessons import Lesson


class Slot:
    def __init__(self, index, max_lessons_per_slot):
        self.index = index
        self.lessons = []
        self.max_lessons_per_slot = max_lessons_per_slot

    def add_lesson(self, new_lesson: Lesson, add_teacher_group=True):
        if self.can_add(new_lesson):
            self.lessons.append(new_lesson)
            if add_teacher_group:
                new_lesson.group.slots[self.index].add_lesson(new_lesson, add_teacher_group=False)
                new_lesson.teacher.slots[self.index].add_lesson(new_lesson, add_teacher_group=False)
            return True
        else:
            return False
        
    def get_lesson(self, index):
        return self.lessons[index]

    def is_full(self):
        return len(self.lessons) == self.max_lessons_per_slot

    def is_empty(self):
        return len(self.lessons) == 0

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

class SlotList(list):
    def calculate_metrics(self):
        return 0