class WaterError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"Error : {self.message}"


def water_plants(plants_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants_list:
            if (plant):
                print(f"Watering {plant}")
            else:
                raise WaterError("Cannot water None - invalid plant!")
    except WaterError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering..")
    water_plants(plants)
    print("Watering completed successfully!\n")
    plants = ["tomato", None, "carrots"]
    print("Testing with error...")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
