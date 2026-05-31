from dataclasses import dataclass

@dataclass
class TowerTroop:
    name: str
    rarity: str

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity
