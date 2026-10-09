from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    weight: float
    value: int

    def __post_init__(self):
        if not self.name.strip(): raise ValueError
        if self.weight <= 0: raise ValueError
        if self.value < 0: raise ValueError


class Inventory:
    def __init__(self, capacity: float):
        if capacity <= 0: raise ValueError
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.capacity < item.weight + self.total_weight: raise ValueError
        if item in self.items: raise ValueError
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items: raise ValueError
        self.items.remove(item)

    @property
    def total_weight(self):
        res = 0
        for z in self.items:
            res += z.weight
        return res

    @property
    def total_value(self):
        res = 0
        for z in self.items:
            res += z.value
        return res

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

@dataclass
class Player:
    name: str
    inventory: Inventory

    def __post_init__(self):
        if not self.name.strip(): raise ValueError

    def pick_up(self, item):
        self.inventory.add_item(item)

    def drop(self, item):
        self.inventory.remove_item(item)

    @property
    def wealth(self):
        return self.inventory.total_value

sword = Item("Sword", 4.5, 100)
potion = Item("Potion", 0.5, 25)
shield = Item("Shield", 6.0, 80)

inv = Inventory(10.0)
player = Player("Alex", inv)

player.pick_up(sword)
player.pick_up(potion)

print(inv.total_weight)  # 5.0
print(inv.total_value)   # 125
print(len(inv))          # 2
print(player.wealth)     # 125

for item in inv:
    print(item.name)

player.drop(potion)

print(len(inv))          # 1
print(player.wealth)     # 100

player.pick_up(shield)   # ValueError: превышена вместимость