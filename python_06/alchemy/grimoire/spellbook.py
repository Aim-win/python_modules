def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients

    if "invalid" in validate_ingredients(ingredients).lower():
        return (f"Spell rejected: {spell_name} "
                f"({validate_ingredients(ingredients)})")
    return (f"Spell recorded: {spell_name} "
            f"({validate_ingredients(ingredients)})")
