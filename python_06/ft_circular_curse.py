from alchemy.grimoire import validate_ingredients, record_spell


def circular_curse() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")

    print('validate_ingredients("fire air"):',
          validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")

    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print('record_spell("Lightning", "air"):', record_spell("Lighting", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    circular_curse()
