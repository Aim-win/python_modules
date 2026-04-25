from abc import ABC, abstractmethod
# from ex0.Card import Card
# from ex2.Combatable import Combatable


class Rankable(ABC):
    def calculate_rating(self) -> int:
        pass
    calculate_rating = abstractmethod(calculate_rating)

    def update_wins(self, wins: int) -> None:
        pass
    update_wins = abstractmethod(update_wins)

    def update_losses(self, losses: int) -> None:
        pass
    update_losses = abstractmethod(update_losses)

    def get_rank_info(self) -> dict:
        pass
    get_rank_info = abstractmethod(get_rank_info)
