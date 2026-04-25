class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age = 0

        print("=== Garden Security System ===")
        print(f"Plant created: {self.name}")

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> None:
        return self._height

    def get_age(self) -> None:
        return self._age

    def display(self) -> None:
        print(f"Current plant: {self.name}", end='')
        print(f"({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    plant1 = SecurePlant("Rose", 25, 30)

    print("")
    plant1.set_height(-5)
    print("")
    plant1.display()
