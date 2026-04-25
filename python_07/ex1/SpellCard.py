from ex0.Card import Card
from typing import Dict, List
from enum import Enum


class EffectType(Enum):
    damage = "damage"
    heal = "heal"
    buff = "buff"
    debuff = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid SpellCard Name Type")
        if not isinstance(cost, int):
            raise ValueError("Invalid SpellCard Cost Type")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid SpellCard Rarity Type")
        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("Invalid SpellCard Effect Type")
        self.effect_type = effect_type
        self._used = False

    def play(self, game_state: Dict) -> Dict:
        if game_state and isinstance(game_state, dict):
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, self.effect_type]
            result = {}
            for key, value in zip(keys, values):
                result[key] = value
            self._used = True
            return result
        raise ValueError(
            f"Error: {game_state} is not dict or Dict is Empty !"
        )

    def resolve_effect(self, targets: List) -> Dict:
        if isinstance(targets, list) and targets:
            return {
                "spell_resolved": self.name,
                "type": self.effect_type,
                "targets_affected": len(targets),
                "status": "Spell consumed and moved to graveyard",
            }
        raise ValueError(
            f"{targets} is Not A List or List is Empty !"
        )

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info
