from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Dict, List
import random


class Deck():
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("card must be an instance of Card")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("The Deck is Empty !!!")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        creature_count = 0
        spell_count = 0
        artifact_count = 0
        costs = 0

        for card in self.cards:
            if isinstance(card, CreatureCard):
                creature_count += 1
            elif isinstance(card, SpellCard):
                spell_count += 1
            elif isinstance(card, ArtifactCard):
                artifact_count += 1
            costs += card.cost

        raw_average = costs / total if total else 0
        average = f"{raw_average:.2f}"

        return {
            'total_cards': total,
            'creatures': creature_count,
            'spells': spell_count,
            'artifacts': artifact_count,
            'avg_cost': average,
        }
