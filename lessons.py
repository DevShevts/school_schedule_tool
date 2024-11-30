class Lesson:
    def __init__(self, group, teacher):
        self.group = group
        self.teacher = teacher

    def __repr__(self):
        return f"{self.group} {self.teacher}"
