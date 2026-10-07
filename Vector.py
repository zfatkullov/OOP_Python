class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return 2

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):
        return bool(self.x or self.y)

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return abs(self) < abs(other)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)                      # (4, 6)
print(repr(v1 - v2))                # Vector(-2, -2)
print(v1 * 3, 3 * v1)               # (3, 6) (3, 6)
print(v1 == Vector(1, 2))           # True
print(v1 == 5)                      # False
print(len(v1))                      # 2
print(abs(v2))                      # 5.0
print(bool(Vector(0, 0)))           # False
print(bool(v1))                     # True
print(v1 < v2)                      # True
print(len({v1, Vector(1, 2), v2}))  # 2
v1 + 5                              # TypeError