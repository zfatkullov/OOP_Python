import time


class Timer:
    def __init__(self):
        self.start = None
        self.elapsed = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(self.elapsed)

# with Timer() as t:
#     raise ValueError('test')

with Timer() as t:
    time.sleep(0.5)
print(t.elapsed)