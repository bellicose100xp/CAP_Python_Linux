class Player:
    def __init__(self):
        self.health: int = 10
        self.max_health: int = 10
        self.inventory: list[int] = []
        self.stamina: int = 10
        self.strength: int = 5
        self.max_stamina: int = 10
        self.location: str = "Hall"

    def move(self, new_location):
        self.location = new_location
        print("You moved to", new_location)

    def attack(self, target):
        target.health -= self.strength


zack = Player()
gen = Player()

print("Zack Zombie's Health", zack.health)

gen.attack(zack)
print("Zack Zombie's Health", zack.health)
