class Plant:
    def __init__(self, name: str, height: int, Age: int) -> None:
        self.name = name
        self.height = height
        self.Age = Age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.Age += 1

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.Age} days)")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)

    Plants = [plant1, plant2, plant3, plant4, plant5]
    i = 0
    print("=== Plant Factory Output ===")
    for plant_i in Plants:
        plant_i.get_info()
        i += 1

    print("\nTotal plants created: ", i)
