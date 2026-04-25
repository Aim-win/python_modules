from typing import Callable, Tuple, Any, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both inputs must be callable functions!")

    def combined_spell(target: str) -> Tuple[Any, Any]:
        res1 = spell1(target)
        res2 = spell2(target)
        return res1, res2

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell) or not isinstance(multiplier, int):
        raise ValueError("Base spell must be "
                         "callable and multiplier must be int!")

    def amplified_spell(item: dict) -> int:
        base_result = base_spell(item)
        return base_result * multiplier

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise ValueError("Both inputs must be callable functions!")

    def wrapper(target: Any) -> Any:
        if condition(target):
            return spell(target)
        return "Spell fizzled"

    return wrapper


def spell_sequence(spells: List[Callable]) -> Callable:
    if not isinstance(spells, list) or not all(callable(s) for s in spells):
        raise ValueError("Input must be a list of callable functions!")

    def sequence_wrapper(target: Any) -> List[Any]:
        results = []
        for spell in spells:
            res = spell(target)
            results.append(res)
        return results

    return sequence_wrapper


def main() -> None:

    def fireball(target: str):
        return f"Fireball hits {target}"

    def heal(target: str):
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    results = combined("Dragon")
    print("\nTesting spell combiner...")
    print(f"Combined spell result: {results[0]}, {results[1]}")

    print("\nTesting power amplifier...")
    dragon = {'name': 'Dragon', "power": 10}

    def fireball_power(card: dict):
        if isinstance(card, dict):
            return card['power']
        else:
            raise ValueError(f"{card} is not a dict")

    mega_fireball = power_amplifier(fireball_power, 3)
    result = mega_fireball(dragon)
    print(f"Original: {fireball_power(dragon)}, Amplified: {result}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
