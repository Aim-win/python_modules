from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:

        if isinstance(hand, list):
            if hand:
                cards_palyed = []
                mana_used = 0
                targets_attacked = []
                enemies = [{2: "Enemy Player"},
                           {5: "Boss Player"},
                           {7: "Legendary Player"}]
                damage_dealt = 0

                attack_cards = [c for c in hand if hasattr(c, "attack")]

                for card in attack_cards:

                    card.play({"name": card.name, "cost": card.cost})

                    battlefield.append(card)
                    hand.remove(card)

                    cards_palyed.append(card.name)
                    mana_used += card.cost

                    attack = \
                        card.attack_target(self.prioritize_targets(enemies))

                    targets_attacked = attack['target']
                    damage_dealt += attack["damage_dealt"]

                return {
                    "card_played": cards_palyed,
                    "mana_used": mana_used,
                    "targets_attacked": targets_attacked,
                    "damage_dealt": damage_dealt
                }
            else:
                raise ValueError("Hand Cannot Be Empty List !")
        raise ValueError("Hand Must Be A List !")

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: List) -> List:
        valid_targets = []

        for target_dict in available_targets:
            for key, target_name in target_dict.items():
                if key <= 2:
                    valid_targets.append(target_name)

        return valid_targets
