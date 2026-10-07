class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return '...'

    def info(self):
        return f'{self.name}, {self.age} years'

    def __repr__(self):
        return f"Animal(name={self.name!r}, age={self.age!r})"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return 'Woof'

    def info(self):
        base = super().info()
        return f'{base}, breed: {self.breed}'

    def __repr__(self):
        return f'Dog(name={self.name!r}, age={self.age!r}, breed={self.breed!r})'

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return 'Meow'

    def info(self):
        base = super().info()
        return f'{base}, indoor: {self.indoor}'

    def __repr__(self):
        return f'Cat(name={self.name!r}, age={self.age!r}, indoor={self.indoor!r})'

class Puppy(Dog):
    def __init__(self, name, age, breed, age_months):
        super().__init__(name, age, breed)
        self.age_months = age_months

    def info(self):
        base = super().info()
        return f'{base}, age_months={self.age_months}'

    def __repr__(self):
        return f'Puppy(name={self.name!r}, age={self.age!r}, breed={self.breed!r}, age_months={self.age_months!r})'

animals = [Dog("Rex", 3, "Husky"), Cat("Tom", 2, True), Animal("Generic", 1)]

for animal in animals:
    print(animal.speak(), '|', animal.info())

dog = animals[0]
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(issubclass(Dog, Animal))

p=Puppy('nikita',1, 'husky', 12)
print(p.info())
print(p.__repr__())
print(Puppy.__mro__)
