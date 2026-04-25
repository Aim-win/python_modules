class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Error checking {self.message} "


class GardenManager:
    tank = 20

    def __init__(self, name: str) -> None:
        self.name = name
        self.garden = Garden(name)

    def add_plant(self, plant: list) -> None:
        if (plant.name == ""):
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        else:
            self.garden.list_plants += [plant]
            print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.garden.list_plants:
                if (plant):
                    print(f"Watering {plant.name} - success")
                else:
                    raise WaterError("Cannot water None - invalid plant!")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(name: str, water: int, sun: int) -> None:
        if (not (water >= 1 and water <= 10)):
            w = water
            raise WaterError(f"{name}: Water level {w} is too high (max 10)\n")
        elif (not (sun >= 2 and sun <= 12)):
            s = sun
            raise WaterError(f"Error: Sunlight hours {s} is too low (min 2)\n")
        else:
            print(f"{name}: healthy! (water: {water}, sun: {sun})")

    @staticmethod
    def check_tank() -> None:
        if (GardenManager.tank < 100):
            raise GardenError("Caught GardenError: Not enough water in tank")


class Garden:
    def __init__(self, manager: str) -> None:
        self.list_plants = []
        self.manager = manager


class Plant:
    def __init__(self, name: str, water: int, sun: int) -> None:
        self.name = name
        self.water = water
        self.sun = sun


class Main:
    @staticmethod
    def test_garden_management() -> None:
        print("=== Garden Management System ===\n")
        try:
            print("Adding plants to garden...")
            newton = GardenManager("newton")
            tomato = Plant("tomato", 5, 8)
            lettuce = Plant("lettuce", 15, 10)
            invalid = Plant("", 5, 11)
            newton.add_plant(tomato)
            newton.add_plant(lettuce)
            newton.add_plant(invalid)
        except PlantError as err:
            print(err)

        try:
            print("\nWatering plants...")
            newton.water_plants()
        except WaterError as err:
            print(err)

        try:
            print("\nChecking plant health...")
            for plant in newton.garden.list_plants:
                newton.check_plant_health(plant.name, plant.water, plant.sun)
        except WaterError as err:
            print(err)

        try:
            print("Testing error recovery...")
            newton.check_tank()
        except GardenError as err:
            print(err)
        finally:
            print("System recovered and continuing...\n")

        print("Garden management system test complete!")


if __name__ == "__main__":
    Main.test_garden_management()
