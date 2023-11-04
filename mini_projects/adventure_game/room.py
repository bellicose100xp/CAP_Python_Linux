"""Creates room class and instantiates different rooms"""
from __future__ import annotations
from directions import Direction
from styling import Color, Style


class Room:
    "Room Class"

    def __init__(
        self,
        name: str,
        directions: dict[Direction, Room],
        items: list[str] | None = None,
        weapon: str | None = None,
        danger: str | None = None,
    ):
        self.name = name
        self.items = items
        self.weapon = weapon
        self.danger = danger
        self.directions = directions

    def go_to_adjacent_room(self, direction: Direction) -> Room:
        return self.directions[direction]

    def get_description(self) -> str:
        # Add directions to the description
        description = f"{Color.YELLOW}{Style.BRIGHT}>>> You are in {self.name} <<<{Color.RESET}\n"
        description += f"Directions from {self.name}: "
        for direction, room in self.directions.items():
            description += f"{Color.GREEN}{Style.BRIGHT}{direction.value}{Color.RESET} ⟶  {Color.GREEN}{room.name}{Color.RESET}, "

        description = (
            description.rstrip(", ")
            + f". Use {Color.CYAN}'go <direction>'{Color.RESET} to move."
        )

        # Add items to the description
        if self.items:
            description += f"\nYou see {Color.BLUE}{self.items}{Color.RESET} in the room. Use {Color.CYAN}'collect <item_name>'{Color.RESET} to collect it."

        # Add weapon to the description
        if self.weapon:
            description += f"\nYou spot a weapon: {Color.MAGENTA}'{self.weapon}'{Color.RESET}. Use {Color.CYAN}'get <weapon_name>'{Color.RESET} to arm yourself."

        return description


# Create all rooms
kitchen = Room("Kitchen", directions={}, danger="monster")
living_room = Room("Living Room", directions={}, weapon="flamethrower")
dining_room = Room("Dining Room", directions={}, items=["potion"])
hall = Room("Hall", directions={}, items=["key", "watch"], weapon="spell")
basement = Room("Basement", directions={}, items=["broomstick"], danger="witch")
garden = Room("Garden", directions={})

# Add directions to rooms
dining_room.directions = {
    Direction.WEST: kitchen,
    Direction.EAST: living_room,
    Direction.SOUTH: garden,
}

kitchen.directions = {Direction.SOUTH: hall, Direction.EAST: dining_room}
hall.directions = {Direction.NORTH: kitchen}
living_room.directions = {Direction.WEST: dining_room, Direction.SOUTH: basement}
basement.directions = {Direction.NORTH: living_room}
garden.directions = {Direction.NORTH: dining_room}
