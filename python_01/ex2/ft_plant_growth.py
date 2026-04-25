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
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant1.get_info()
    for i in range(1, 7):
        plant1.grow()
        plant1.age()
    print(f"=== Day {i+1} ===")
    plant1.get_info()
    print(f"Growth this week: +{i}cm")
