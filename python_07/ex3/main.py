from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()

    print("Factory:", FantasyCardFactory.__name__)
    print("Strategy:", AggressiveStrategy.__name__)

    types = factory.get_supported_types()
    if types:
        print("Available types:", types)
    else:
        raise ValueError("Invalid Types !!!")

    my_hand = [
        factory.create_creature('dragon'),
        factory.create_creature('goblin'),
        factory.create_spell('lightning')
    ]
    if isinstance(my_hand, list) and my_hand:
        print("\nSimulating aggressive turn...")
        print("Hand:", [f"{card.name} ({card.cost})" for card in my_hand])
    else:
        raise ValueError("Hand Must Be A Valid List !")

    aggresive = AggressiveStrategy()
    print("\nTurn execution:")
    print("Strategy:", aggresive.get_strategy_name())
    print("Actions:", aggresive.execute_turn(my_hand, []))

    engine = GameEngine()
    engine.configure_engine(factory, aggresive)
    engine.simulate_turn()

    print("\nGame Report:\n", engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
