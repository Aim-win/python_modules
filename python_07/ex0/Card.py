from abc import ABC, abstractmethod
from typing import Dict, List
from enum import Enum


class RarityValidater(Enum):
    rare = "Rare"
    legendary = "Legendary"
    regular = "Regular"
    epic = "Epic"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("Card Name Must Be A Valid String !")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Card Cost Must Be A Valid Positive int !")
        valid_rarities: List[str] = [r.value for r in RarityValidater]
        if rarity not in valid_rarities:
            raise ValueError("Rarity Invalid !")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: Dict) -> Dict:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        try:
            int(available_mana)
            return available_mana >= self.cost
        except (ValueError, TypeError):
            print("ValueError Raised: The Mana is Not A Valid Number !")
            return False
