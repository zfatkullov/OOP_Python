from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    title: str
    price: float

    def __post_init__(self):
        if self.price < 0 or not self.title.strip():
            raise ValueError

@dataclass
class Order:
    order_id: int
    items: list = field(default_factory=list)
    status: str = 'new'

    def __post_init__(self):
        if self.order_id <= 0: raise ValueError

    def add_item(self, item):
        self.items.append(item)

    @property
    def total(self):
        result = 0
        for item in self.items:
            result += item.price
        return result

i1 = Item("Book", 10.0)
o = Order(1)
o.add_item(i1)
o.add_item(Item("Pen", 2.5))
print(o.total)                            # 12.5
print(o)                                  # Order(order_id=1, items=[...], status='new')
print(Order(2).items is o.items)          # False
print(Item("A", 1) == Item("A", 1))       # True
print(len({Item("A", 1), Item("A", 1)}))  # 1