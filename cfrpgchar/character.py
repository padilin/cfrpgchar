import random
from dataclasses import dataclass


@dataclass
class CFRPGChar:
    name: str

    # Unique
    rage_level: int = 0
    rage_ability: bool = False

    # Stats
    strength: int = 3
    dexterity: int = 3
    vitality: int = 3
    looks: int = 3
    aptitude: int = 3
    social: int = 3
    magic: int = 3
    piety: int = 3

    # GM Skills
    combat_arts: int = 0

    # Skills


    # Bonus Health
    head_bonus: int = 0
    head_roll: int = random.randint(0, 4)

    @property
    def speed(self) -> int:
        return self.dexterity * 5

    @property
    def rage_strength(self) -> int:
        rage_levels = {0: 1, 1: 2, 2: 3, 3: 4}
        return self.strength * rage_levels[self.rage_level]

    @property
    def health_head(self) -> int:
        return self.head_roll + self.head_bonus + self.vitality

    def __repr__(self):
        description = f"My name is {self.name}."
        if self.rage_ability:
            description += f" I am {self.rage_level} mad."
        return description

    def __str__(self):
        return self.__repr__()
