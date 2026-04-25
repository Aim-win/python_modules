from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, rating: int, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.attack_attr = attack
        self.health = health
        self.wins = 0
        self.loses = 0

        if not isinstance(name, str) or not name:
            raise ValueError("Card name Type is Invalid")
        if not isinstance(cost, int):
            raise ValueError("Cost Type is Invalid")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Rarity Type is Invalid")
        if not isinstance(card_id, str):
            raise ValueError("Card ID Invalid !")
        if not isinstance(rating, int):
            raise ValueError("Rating Invalid !")
        if not isinstance(attack, int):
            raise ValueError("Attack Type is Invalid")
        if not isinstance(health, int):
            raise ValueError("Health Type is Invalid")
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

    def play(self, game_state: Dict) -> Dict:
        if game_state:
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, "Creature summoned to battlefield"]
            result = {}

            for key, value in zip(keys, values):
                result[key] = value
            return result
        return {}

    def attack(self, target: str) -> Dict:
        result = self.get_card_info()
        if not target:
            print("Error: Target Cannot Be Empty !")
            return {}
        if result:
            keys = ['attacker', 'target', 'damage_dealt', 'combat_resolved']
            values = [self.name, target, self.attack_attr, True]
            attack_info = {}

            for key, value in zip(keys, values):
                attack_info[key] = value
            return attack_info

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

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.rating += 16 * wins
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.rating -= 16 * losses
        self.loses += losses

    def get_rank_info(self) -> dict:

        return {
            'Card Name': self.name,
            'Card Rank': self.rating
        }

    def get_tournament_stats(self) -> dict:
        return {
            'Card Name': self.name,
            'Rating Update': self.rating,
            'Wins': self.wins,
            'Loses': self.loses
        }
