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
        self.num_slots_per_day = num_slots_per_day
        self.max_lessons_per_slot = 1
        self.days_per_week = 5
        self.slots = [Slot(i, self.max_lessons_per_slot) for i in range(num_slots_per_day * days_per_week)]

    def __repr__(self):
        return f"{self.grade}{self.letter}"

    def calculate_metric(self) -> int:
        metric = 0
        slots_binary = []

        for slot in self.slots:
            if slot.is_full():
                slots_binary.append(1)
            else:
                slots_binary.append(0)
     
        days = [slots_binary[i:i + self.num_slots_per_day] for i in range(0, len(slots_binary), self.num_slots_per_day)]    
        for i, day in enumerate(days):
            if 1 in day:
                last_lesson_index = len(day) - day[::-1].index(1)
                days[i] = day[:last_lesson_index]      # убираем "окна" в конце дня

        average_lessons_per_day = sum(slots_binary) / self.days_per_week        
        metric += 10 * sum(day.count(0) for day in days)    # повышаем метрику за пустые уроки
        
        ratio = 3 # коэффициент штрафа за несбалансированное распределение уроков по дням            
        for day in days: 
            metric += ratio * abs(len(day) - average_lessons_per_day)
        
        
        
        return metric
    
    def list(self):
        result = []
        for subject, n in self.data.items():
            for i in range(n):
                result.append(subject)
        return result
