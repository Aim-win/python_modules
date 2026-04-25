from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass
    create_creature = abstractmethod(create_creature)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass
    create_spell = abstractmethod(create_spell)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass
    create_artifact = abstractmethod(create_artifact)

    def create_themed_deck(self, size: int) -> dict:
        pass
    create_themed_deck = abstractmethod(create_themed_deck)

    def get_supported_types(self) -> dict:
        pass
    get_supported_types = abstractmethod(get_supported_types)
