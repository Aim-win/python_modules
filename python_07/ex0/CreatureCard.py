from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack Type is Invalid or Not Positive")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health Type is Invalid or Not Positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        if game_state and isinstance(game_state, dict):
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, "Creature summoned to battlefield"]
            result = {}
            for key, value in zip(keys, values):
                result[key] = value
            return result
        return {}

    def attack_target(self, target: str) -> Dict:
        if not target:
            raise ValueError("Error: Target Cannot Be Empty !")
        keys = ['attacker', 'target', 'damage_dealt', 'combat_resolved']
        values = [self.name, target, self.attack, True]
        attack_info = {}
        for key, value in zip(keys, values):
            attack_info[key] = value
        return attack_info

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        }
