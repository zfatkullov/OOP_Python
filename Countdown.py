class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        temp = self.start
        self.start -= 1
        return temp

c = Countdown(3)
for n in c:
    print(n)
for n in c:
    print(n)
