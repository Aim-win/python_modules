def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        out = f"{quantity} packets available"
    elif unit == "grams":
        out = f"{quantity} grams total"
    elif unit == "area":
        out = f"covers {quantity} square meters"
    else:
        out = "Unknown unit type"

    print(f"{seed_type.capitalize()} seeds: {out} ")
