from abc import ABC, abstractmethod


class Combatable(ABC):

    def attack(self, target) -> dict:
        pass
    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> dict:
        pass
    defend = abstractmethod(defend)

    def get_combat_stats(self) -> dict:
        pass
    get_combat_stats = abstractmethod(get_combat_stats)
