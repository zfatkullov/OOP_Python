from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Product:
    name: str
    price: float
    stock: int = 0

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Название не может быть пустым.")
        if self.price < 0:
            raise ValueError('Цена не может быть отрицательной')
        if self.stock < 0:
            raise ValueError('Остаток на складе не может быть отрицательным')

    def __str__(self):
        return f'{self.name}: {self.price} руб. (на складе: {self.stock})'

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError('Цена не может быть отрицательной')
        self.price = new_price


@dataclass
class OrderItem:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError('Количество должно быть больше нуля')

    def total(self):
        return self.product.price * self.quantity


@dataclass
class Order:
    items: list[OrderItem] = field(default_factory=list)

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(i.total() for i in self.items)

    def __len__(self):
        return len(self.items)


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product):
        ...

    @abstractmethod
    def get(self, name):
        ...

    @abstractmethod
    def list_all(self):
        ...


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.storage = {}

    def add(self, product):
        if product.name in self.storage:
            raise ValueError('Уже есть')
        self.storage[product.name] = product

    def get(self, name):
        return self.storage[name]

    def list_all(self):
        return list(self.storage.values())

def create_product(name, price, stock=0):
    if isinstance(price, str):
        try:
            price = int(price.strip())
        except:
            raise ValueError('Цена должна быть числом')
    return Product(name, price, stock=0)

print(create_product("Мышь", "-5").price)   # 4) что выведется?
create_product("Мышь", "abc")                 # 5) что должно случиться?