from dataclasses import dataclass, field


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int

    def __post_init__(self):
        if self.year <= 0 or not self.title.strip():
            raise ValueError


@dataclass
class Reader:
    name: str
    borrowed: list = field(default_factory=list)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        if book in self.books:
            raise ValueError
        self.books.append(book)

    def register(self, reader):
        self.readers.append(reader)

    def lend(self, book, reader):
        if book not in self.books:
            raise ValueError
        self.books.remove(book)
        reader.borrowed.append(book)

    def give_back(self, book, reader):
        if book in reader.borrowed:
            reader.borrowed.remove(book)
        else:
            raise ValueError
        self.books.append(book)

    @property
    def available_count(self):
        return len(self.books)