from dataclasses import dataclass
from enum import Enum


class PlayerState(Enum):
    ALIVE = 1
    DEAD = 0


@dataclass
class Player:
    name: str
    steps: int
    items: list[str]
    weapons: list[str]
    state: PlayerState
