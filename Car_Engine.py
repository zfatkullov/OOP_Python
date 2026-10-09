class Engine:
    def __init__(self, power: int, fuel: str):
        self.power = power
        self.fuel = fuel

    def start(self):
        return f'Engine {self.power} hp started'

    def __repr__(self):
        return f'Engine(power={self.power!r}, fuel={self.fuel!r})'

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start(self):
        return f'{self.brand}: {self.engine.start()}'

    def replace_engine(self, new_engine):
        self.engine = new_engine

    def __repr__(self):
        return f'Car(brand={self.brand!r}, engine={self.engine!r})'

engine = Engine(150, "petrol")
car = Car("Toyota", engine)
print(car.start())   # Toyota: Engine 150 hp started
car.replace_engine(Engine(300, "diesel"))
print(car.start())   # Toyota: Engine 300 hp started
print(car)