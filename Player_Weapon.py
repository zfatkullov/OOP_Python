class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return f'{self.name} hits for {self.damage}'

    def __repr__(self):
        return f'Weapon(name={self.name!r}, damage={self.damage!r})'

class Player:
    def __init__(self, nickname, weapon):
        self.nickname = nickname
        self.weapon = weapon

    def attack(self):
        return f'{self.nickname}: {self.weapon.attack()}'

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def __repr__(self):
        return f'Player(nickname={self.nickname!r}, weapon={self.weapon!r})'

sword = Weapon("Sword", 10)
bow = Weapon("Bow", 7)
p = Player("Hero", sword)

print(p.attack())              # Hero: Sword hits for 10
p.change_weapon(bow)
print(p.attack())              # Hero: Bow hits for 7
print(p)                       # Player(nickname='Hero', weapon=Weapon(name='Bow', damage=7))
print(p.weapon is bow)         # True