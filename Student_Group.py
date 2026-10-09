from dataclasses import dataclass, field


@dataclass(frozen=True)
class Grade:
    subject: str
    value: int

    def __post_init__(self):
        if not (1 <= self.value <= 5): raise ValueError
        if not self.subject.strip(): raise ValueError


@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average(self):
        res = 0
        if not self.grades:
            return 0.0
        for v in self.grades:
            res += v.value
        return res / len(self.grades)

    def __post_init__(self):
        if not self.name.strip(): raise ValueError


class Group:
    def __init__(self, title):
        self.students = []
        self.title = title

    def add_student(self, student):
        if student in self.students: raise ValueError
        self.students.append(student)

    def best(self):
        return max(self.students, key = lambda s: s.average)

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)


g = Group("A1")
s1 = Student("Ivan"); s2 = Student("Anna")
s1.add_grade(Grade("math", 4)); s1.add_grade(Grade("art", 5))
s2.add_grade(Grade("math", 5))
g.add_student(s1); g.add_student(s2)

print(s1.average)        # 4.5
print(Student("X").average)  # 0.0
print(g.best())          # Student(name='Anna', ...)
print(len(g))            # 2
for s in g:
    print(s.name)
# g.add_student(Student("Ivan"))   # ValueError
# Grade("math", 6)                 # ValueError