from abc import ABC, abstractmethod


class Magical(ABC):

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass
    cast_spell = abstractmethod(cast_spell)

    def channel_mana(self, amount: int) -> dict:
        pass
    channel_mana = abstractmethod(channel_mana)

    def get_magic_stats(self) -> dict:
        pass
    get_magic_stats = abstractmethod(get_magic_stats)
