from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any, Dict, List, cast


def spell_reducer(spells: List[int], operation: str) -> int:

    if not isinstance(spells, list) or not isinstance(operation, str):
        raise ValueError("Error: Input Must Be, List And str")

    ops = {
        'add': add,
        'multiply': mul,
        'max': max,
        'min': min
    }

    if operation not in ops:
        raise ValueError(f"Operation '{operation}' is not supported")

    return reduce(cast(Callable[[int, int], int], ops[operation]), spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    if not callable(base_enchantment):
        raise ValueError(f"{base_enchantment} is not callable !")

    return {
        'fire_enchant': partial(base_enchantment, 50, 'fire'),
        'ice_enchant': partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': partial(base_enchantment, 50, 'lightning')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if not isinstance(n, int):
        raise ValueError("The Input Must Be int")

    if n <= 1:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:

    @singledispatch
    def cast_spell(spell: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast_spell


def main() -> None:
    print("\n\nTesting spell reducer...")
    val = [10, 20, 30, 40]

    print("Sum:", spell_reducer(val, 'add'))
    print("Product:", spell_reducer(val, 'multiply'))
    print("Max:", spell_reducer(val, 'max'))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print("\nTesting spell dispatcher...")
    caster = spell_dispatcher()

    print(caster(42))
    print(caster("fireball"))
    print(caster([1, 2, 3]))
    print(caster(3.14))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
