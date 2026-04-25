from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    spellcard = SpellCard("Lightning Bolt", 3, "Rare",
                          "Deal 3 damage to target")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    artifactcard = ArtifactCard("Mana Crystal", 2, "Regular", 3,
                                "+1 mana per turn")

    cards = [spellcard, artifactcard, creature]
    deck = Deck()

    for card in cards:
        deck.add_card(card)
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    drew_first = deck.draw_card()
    print(f"Drew: {drew_first.name} ({drew_first.__class__.__name__})")
    print(f"Play result: {drew_first.play(drew_first.get_card_info())}")

    print()

    drew_second = deck.draw_card()
    print(f"Drew: {drew_second.name} ({drew_second.__class__.__name__})")
    print(f"Play result: {drew_second.play(drew_second.get_card_info())}")

    print()

    drew_third = deck.draw_card()
    print(f"Drew: {drew_third.name} ({drew_third.__class__.__name__})")
    print(f"Play result: {drew_third.play(drew_third.get_card_info())}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
