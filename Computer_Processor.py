class Processor:
    def __init__(self, model: str, cores: int):
        self.model = model
        self.cores = cores

    def run(self, task):
        return f'{self.model} ({self.cores} cores) runs: {task}'

    def __repr__(self):
        return f'Processor(model={self.model!r}, cores={self.cores!r})'


class Storage:
    def __init__(self, capacity_gb):
        self.capacity_gb = capacity_gb
        self.files = []

    def save(self, name, size_gb):
        if self.free_space < size_gb:
            raise ValueError('Not enough space')
        self.files.append((name, size_gb))

    @property
    def free_space(self):
        return self.capacity_gb - sum(size for _, size in self.files)

    def __repr__(self):
        return f'Storage(capacity={self.capacity_gb!r}, files={self.files!r})'


class Computer:
    def __init__(self, name, processor, storage):
        self.name = name
        self.processor = processor
        self.storage = storage

    def run(self, task):
        return f'{self.name}: {self.processor.run(task)}'

    def save(self, name, size):
        self.storage.save(name, size)

    def upgrade_processor(self, new_processor):
        self.processor = new_processor

    def __repr__(self):
        return f'Computer(name={self.name!r}, processor={self.processor!r}, storage={self.storage!r})'


cpu = Processor("Intel i5", 4)
disk = Storage(100)
pc = Computer("Home PC", cpu, disk)

print(pc.run("compile"))    # Home PC: Intel i5 (4 cores) runs: compile
pc.save("movie", 40)
pc.save("game", 50)
print(disk.free_space)      # 10 (тот же объект disk, что внутри pc)
pc.save("big", 20)          # ValueError

pc.upgrade_processor(Processor("Ryzen 9", 12))
print(pc.run("render"))     # Home PC: Ryzen 9 (12 cores) runs: render
print(pc)

pc2 = Computer("Work PC", Processor("Intel i3", 2), Storage(50))
print(pc2.storage.files is pc.storage.files)   # False