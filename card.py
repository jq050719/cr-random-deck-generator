from dataclasses import dataclass
from enum import Enum

class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    CHAMPION = "Champion"

@dataclass(frozen=True)
class Card:
    name: str
    rarity: Rarity
