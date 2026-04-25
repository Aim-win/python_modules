class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return f"Caught garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught WaterError:: {self.message}"


class main:
    def test_custom_errors() -> None:
        print("=== Custom Garden Errors Demo ===\n")
        try:
            print("Testing PlantError...")
            raise PlantError("The tomato plant is wilting!\n")
        except PlantError as error:
            print(error)

        try:
            print("Testing WaterError...")
            raise WaterError("Not enough water in the tank!\n")
        except WaterError as error:
            print(error)

        print("Testing catching all garden errors...")
        try:
            raise GardenError("The tomato plant is wilting!")
        except GardenError as error:
            print(error)

        try:
            raise GardenError("Not enough water in the tank!\n")
        except GardenError as error:
            print(error)
        print("All custom error types work correctly!")

    test_custom_errors = staticmethod(test_custom_errors)


if __name__ == "__main__":
    main.test_custom_errors()
