from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Dict


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        if not isinstance(factory, CardFactory):
            raise ValueError("factory is Not A CardFactory !")
        if not isinstance(strategy, GameStrategy):
            raise ValueError("Strategy is Not A GameStrategy !")

        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured before simulating!")

        hand = [
            self.factory.create_creature('dragon'),
            self.factory.create_creature('goblin'),
            self.factory.create_spell('lightning')
        ]

        self.cards_created += len(hand)

        battlefield = []

        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1

        if "damage_dealt" in turn_result:
            self.total_damage += turn_result["damage_dealt"]

        return turn_result

    def get_engine_status(self) -> Dict:

        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name()
            if self.strategy else "None",
            'total_damage': self.total_damage,
            'cards_created': self.cards_created,
        }
