from collections import namedtuple
import random

from lessons import Lesson
from slot import Slot
from subject import Subject
from teacher import Teacher


class StudentsGroup:
    def __init__(self, grade: int, letter: str, data: dict, num_slots_per_day: int = 7, days_per_week: int = 5):
        self.data = data
        self.grade = grade
        self.letter = letter

        self.max_lessons_per_slot = 1
        self.days_per_week = 5
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * days_per_week)]

    def __repr__(self):
        return f"{self.grade}{self.letter}"

    def calculate_metric(self) -> int:
        metric = 50
        slots_binary = []

        for slot in self.slots:
            if slot.is_full():
                slots_binary.append(1)
            else:
                slots_binary.append(0)
     
        days = [slots_binary[i:i + 7] for i in range(0, len(slots_binary), 7)]    # 7 - num slots per day
        # days = [[1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 0]]
        for i, day in enumerate(days):
            if 1 in day:
                last_lesson_index = len(day) - day[::-1].index(1)
                days[i] = day[:last_lesson_index]      # убираем "окна" в конце дня

        average_lessons_per_day = sum(slots_binary) / self.days_per_week        
        metric -= 10 * sum(day.count(0) for day in days)
        
        ratio = 3 # коэффициент штрафа за несбалансированное распределение уроков по дням            
        for day in days: 
            metric -= ratio * abs(len(day) - average_lessons_per_day)
        
        return metric
    
    def list(self):
        result = []
        for subject, n in self.data.items():
            for i in range(n):
                result.append(subject)
        return result


Car = namedtuple('GroupData', ['subject' ,'number', 'teacher'])

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
        subject = teacher.subject
        if subject not in data:
            data[subject] = [teacher, 1]
        else:
            data[subject][1] += 1
    groups.append(StudentsGroup(10, chr(65 + i), data))
