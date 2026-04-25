def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
     ) -> None:
    if (plant_name == ""):
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif (not (water_level >= 1 and water_level <= 10)):
        w = water_level
        raise ValueError(f"Error: Water level {w} is too high (max 10)\n")
    elif (not (sunlight_hours >= 2 and sunlight_hours <= 12)):
        s = sunlight_hours
        raise ValueError(f"Error: Sunlight hours {s} is too low (min 2)\n")
    else:
        print(f"Plant {plant_name} is healthy!\n")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 10)
    except ValueError as error:
        print(error)
    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 10)
    except ValueError as error:
        print(error)
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 10)
    except ValueError as error:
        print(error)
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as error:
        print(error)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
