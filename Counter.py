class Counter:
    def __init__(self, step = 1):
        self.count = 0
        self.step = step

    def __call__(self):
        self.count += self.step
        return self.count

c = Counter(step=5)
c(); c()
print(c())
print(callable(c))
