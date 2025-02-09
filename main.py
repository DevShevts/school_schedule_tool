import random
import os
from lessons import Lesson
from teacher import Teacher
from subject import Subject
from students_group import StudentsGroup
from schedule import Schedule

random.seed(9001)

filtered_files = [f for f in os.listdir('data')]
groups = []
for class_file in filtered_files:
    data = dict()
    with open('data/' + class_file, 'r') as f:
        for line in f:
            name, subject, n = line.split(sep=' | ')
            teacher = Teacher(name, Subject[subject])
            data[teacher] = int(n)
        class_grade_letter = class_file.split('.')[0]
        letter = class_grade_letter[-1]
        grade = int(class_grade_letter[:-1])
        groups.append(StudentsGroup(grade, letter, data))

schedule = Schedule(groups, num_slots_per_day=7)
schedule.create_schedule()

with open ('full schedule.txt', 'w') as f:
    f.write('metric = ')
    f.write(str(schedule.calculate_metric()))
    f.write('\n\n')
    for i, slot in enumerate(schedule.slots):
        if i % 7 == 0:
            f.write('__________________')
        f.write(str(schedule.slots[i]))

for group in groups:
    with open (f'groups schedules/{group.grade}{group.letter} schedule.txt', 'w') as f:
        for i, slot in enumerate(group.slots):
            if i % 7 == 0:
                f.write('__________________')
            f.write(str(group.slots[i]))