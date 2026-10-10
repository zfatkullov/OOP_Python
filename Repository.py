from abc import abstractmethod, ABC
from dataclasses import dataclass, field


class StudentRepository(ABC):
    @abstractmethod
    def add(self, student):
        """Добавляет студента, если имя занято бросает ValueError"""
        pass

    @abstractmethod
    def get(self, name):
        """Получение имени, если имени нету бросает KeyError"""
        pass

    @abstractmethod
    def list_all(self):
        """Возвращает список студентов в порядке добавления"""
        pass


class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self.storage = {}

    def add(self, student):
        if student.name in self.storage:
            raise ValueError(f'{student.name} уже есть')
        self.storage[student.name] = student

    def get(self, name):
        if name not in self.storage:
            raise KeyError(f'{name} нету в хранилище')
        return self.storage[name]

    def list_all(self):
        return list(self.storage.values())


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
        if not self.grades:
            return 0.0
        res = sum(v.value for v in self.grades)
        return res / len(self.grades)

    def __post_init__(self):
        if not self.name.strip(): raise ValueError


class FakeDBStudentRepository(StudentRepository):
    def __init__(self):
        self.storage = []

    def _to_student(self, row):
        r = []
        for subject, value in row[1]:
            r.append(Grade(subject, value))
        return Student(row[0], r)

    def add(self, student):
        if student.name in [row[0] for row in self.storage]:
            raise ValueError(f'{student.name} уже есть')
        self.storage.append((student.name, [(g.subject, g.value) for g in student.grades]))

    def get(self, name):
        for row in self.storage:
            if row[0] == name:
                return self._to_student(row)
        raise KeyError(f'{name} нету в хранилище')

    def list_all(self):
        return [self._to_student(row) for row in self.storage]

class Group:
    def __init__(self, title, repo):
        self.title = title
        self.repo = repo

    def add_student(self, student):
        self.repo.add(student)

    def best(self):
        students = self.repo.list_all()
        if not students:
            return None
        return max(students, key = lambda x: x.average)

    def __len__(self):
        return len(self.repo.list_all())

    def __iter__(self):
        return iter(self.repo.list_all())

def check(repo):
    g = Group("A1", repo)
    s1 = Student("Ivan")
    s1.add_grade(Grade("math", 4))
    s1.add_grade(Grade("art", 5))
    s2 = Student("Anna")
    s2.add_grade(Grade("math", 5))
    g.add_student(s1)
    g.add_student(s2)
    print(len(g))
    print(g.best().name)
    for s in g:
        print(s.name, s.average)
    try:
        g.add_student(Student("Ivan"))
    except ValueError as e:
        print("ValueError:", e)

check(InMemoryStudentRepository())
check(FakeDBStudentRepository())