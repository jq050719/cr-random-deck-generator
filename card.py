from dataclasses import dataclass

@dataclass
class Card:
    name: str
    rarity: str

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity
