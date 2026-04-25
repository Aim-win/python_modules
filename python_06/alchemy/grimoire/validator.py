def validate_ingredients(ingredients: str) -> str:
    ingred = ["fire", "water", "earth", "air"]
    data = ingredients.split()

    for d in data:
        if d not in ingred:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
