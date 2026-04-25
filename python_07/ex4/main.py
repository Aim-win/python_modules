from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    platform = TournamentPlatform()

    card_1 = TournamentCard("Fire Dragon", 7,
                            "Legendary", "dragon_001", 1200, 5, 3)
    card_2 = TournamentCard("Ice Wizard", 5, 'Regular',
                            "wizard_001", 1150, 2, 4)
    cards = [card_1, card_2]
    bases = [name.__name__ for name in TournamentCard.__bases__]

    for card in cards:
        print(platform.register_card(card), f"(ID: {card.card_id})")
        print("- Interfaces:", bases)
        print("- Rating:", card.rating)
        print(f"- Record: {card.wins}-{card.loses}\n")

    # update wins and loses
    card_1.update_wins(1)
    card_1.update_losses(0)

    # update wins and loses
    card_2.update_wins(0)
    card_2.update_losses(1)

    print("Creating tournament match...")
    print("Match result:", platform.create_match(card_1.card_id, card.card_id))
    print("\nTournament Leaderboard:")
    lead = platform.get_leaderboard()

    for i, c in enumerate(lead, 1):
        card_stats = c[f'card {i}']

        name = card_stats['name']
        rating = card_stats['rating']
        wins = card_stats['wins']
        loses = card_stats['loses']

        print(f"{i}. {name} - Rating: {rating} ({wins}-{loses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===\n"
          "All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
