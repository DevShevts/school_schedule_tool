from collections import namedtuple
import random

from subject import Subject
from teacher import Teacher


class StudentsGroup:
    def __init__(self, grade: int, letter: str, data: dict):
        self.data = data
        self.grade = grade
        self.letter = letter

    def __repr__(self):
        return f"{self.grade}{self.letter}"

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


