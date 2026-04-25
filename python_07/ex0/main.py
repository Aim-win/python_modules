from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    info = creature.get_card_info()
    print(info)
    print()

    mana = 6
    if not isinstance(mana, int):
        print("Error: Mana Must Be A Numeric Value")
        return

    print(f"Playing {info['name']} with {mana} mana available:")
    print("Playable:", creature.is_playable(mana))
    if creature.is_playable(mana):
        print("Play result:", creature.play(info))

        target = "Goblin Warrior"
        print(f"\n{info['name']} attacks {target}:")
        print("Attack result:", creature.attack_target(target))
    else:
        print("Play result: Mana Insufficient")

    try:
        mana = 3
        if not isinstance(mana, int):
            print("\nError: Mana Must Be A Numeric Value")
            return
        if not creature.is_playable(mana):
            print(f"\nTesting insufficient mana ({mana} available):")
            print("Playable:", creature.is_playable(mana))
        else:
            print(f"\nTesting with sufficient mana ({mana} available):")
            print("Playable:", creature.is_playable(mana))
    except TypeError:
        print("Error: TypeError Raised !")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
