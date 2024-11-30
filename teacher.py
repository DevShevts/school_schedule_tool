
from subject import Subject

class Teacher:
    def __init__(self, name: str, subject: Subject):
        self.name = name
        self.subject = subject

    def __repr__(self):
        return f"{self.name} {self.subject}"