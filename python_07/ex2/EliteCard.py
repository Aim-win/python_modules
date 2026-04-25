from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict
from enum import Enum
import random


class Spells_Names(Enum):
    fireball = "Fireball"
    lightning_bolt = "Lightning Bolt"
    arcane_blast = "Arcane Blast"
    venomous_strike = "Venomous Strike"


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_attr: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)

        self.attack_attr = attack_attr
        self.health = health
        self.mana = mana

        if not isinstance(name, str):
            raise ValueError("Name Must Be A Valid String !")
        if not isinstance(cost, int):
            raise ValueError("Cost Must Be A Valid Integer !")
        if not isinstance(rarity, str):
            raise ValueError("Rarity Must Be A Valid String !")
        if not isinstance(attack_attr, int):
            raise ValueError("Cost Must Be A Valid Integer !")
        if not isinstance(health, int):
            raise ValueError("Cost Must Be A Valid Integer !")
        if not isinstance(mana, int):
            raise ValueError("Cost Must Be A Valid Integer !")

    def play(self, game_state: Dict) -> Dict:
        if game_state:
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, "Creature summoned to battlefield"]
            result = {}

            for key, value in zip(keys, values):
                result[key] = value
            return result
        return {}

    def attack(self, target: str) -> dict:
        combat_types = ['melle', 'gun', 'sword', 'katana']
        result = {'attacker': self.name,
                  'target': target,
                  'damage': self.attack_attr,
                  'combat_type': random.choice(combat_types)}
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        spell_names = [spell.value for spell in Spells_Names]
        if spell_name not in spell_names:
            return f"Error: Spell Name: {spell_name} Is Not Valid !"
        result = {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': len(targets) * 2
        }

        return result

    def defend(self, incoming_damage: int) -> dict:
        blocked = self.health - incoming_damage

        result = {'defender': self.name,
                  'damage_taken': incoming_damage,
                  'damage_blocked': blocked if blocked >= 0 else 0,
                  'still_alive': True if self.health - incoming_damage >= 0
                  else False}
        return result

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.attack_attr,
            'health': self.health
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int):
            return ("Ammoun Must Be A Valid Number : Ammount Provided: "
                    f"'{amount}'")
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana': self.mana
        }
