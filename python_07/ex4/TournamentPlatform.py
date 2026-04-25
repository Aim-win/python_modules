from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform():

    def __init__(self) -> None:
        self.cards: TournamentCard = []
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if isinstance(card, TournamentCard):
            self.cards.append(card)
            return card.name
        raise ValueError(f"{card} is not A TournamentCard")

    def create_match(self, card1_id: str, card2_id: str) -> Dict:

        if not isinstance(card1_id, str):
            raise ValueError(f"{card1_id} is not A Valid ID [Must Be String]")
        if not isinstance(card2_id, str):
            raise ValueError(f"{card2_id} is not A Valid ID [Must Be String]")

        card_1 = None
        card_2 = None
        for card in self.cards:
            if card.card_id == card1_id:
                card_1 = card
            elif card.card_id == card2_id:
                card_2 = card
            else:
                raise ValueError("Card ID Not Found !")

        winner = card1_id if card_1.wins > card_2.wins else card2_id
        loser = card1_id if card_1.wins < card_2.wins else card2_id

        rating_winner = card_1.rating if card_1.card_id == \
            winner else card_2.rating
        rating_loser = card_1.rating if card_1.card_id != \
            winner else card_2.rating

        self.match_played += 1

        return {
            'winner': winner,
            'loser': loser,
            'winner_rating': rating_winner,
            'loser_rating': rating_loser
        }

    def get_leaderboard(self) -> List:

        sorted_cards = sorted(self.cards, key=lambda card: card.rating,
                              reverse=True)
        leaderboard = []
        i = 1

        for card in sorted_cards:
            leaderboard.append({f'card {i}': {'name': card.name,
                                              'rating': card.rating,
                                              'wins': card.wins,
                                              'loses': card.loses}})
            i += 1

        return leaderboard

    def generate_tournament_report(self) -> Dict:

        total = 0
        for card in self.cards:
            total += card.rating

        if len(self.cards) > 0:
            average = total / len(self.cards)
        else:
            average = 0
        return {
            'total_cards': len(self.cards),
            'matches_played': self.match_played,
            'avg_rating': average,
            'platform_status': 'active' if len(self.cards) > 0 else 'inactive'
        }
