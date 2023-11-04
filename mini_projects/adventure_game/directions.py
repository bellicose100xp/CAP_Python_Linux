from enum import Enum


class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


def get_direction_from_str(direction_as_str: str) -> Direction | None:
    for direction in Direction:
        if direction.value == direction_as_str:
            return direction
    return None
