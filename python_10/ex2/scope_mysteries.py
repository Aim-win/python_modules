from typing import Dict, Any, Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:

    if not isinstance(initial_power, int):
        raise ValueError("The Input Must Be A Valid int !")

    total_power = initial_power

    def accumulator(amount: int) -> int:
        if not isinstance(amount, int):
            raise ValueError("The Input Must Be A Valid int !")

        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    if not isinstance(enchantment_type, str):
        raise ValueError("The Input Must Be A Valid string !")

    def enchant(item_name: str) -> str:
        if not isinstance(item_name, str):
            raise ValueError("The Input Must Be A Valid string !")

        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable]:
    storage = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print("Base 100, add 20:", accumulator(20))
    print("Base 100, add 30:", accumulator(30))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
