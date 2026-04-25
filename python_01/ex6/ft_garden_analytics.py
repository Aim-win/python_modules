class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def display(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def display(self) -> None:
        state = "blooming" if self.blooming else "not blooming"
        print(f"- {self.name}: {self.height}cm, "
              f"{self.color} flowers ({state})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def display(self) -> None:
        state = "blooming" if self.blooming else "not blooming"
        print(
            f"- {self.name}: {self.height}cm, {self.color} flowers "
            f"({state}), Prize points: {self.prize_points}"
        )


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0

        def record_add(self) -> None:
            self.plants_added += 1

        def record_growth(self, amount: int) -> None:
            self.total_growth += amount

        def report(self) -> None:
            print(
                f"Plants added: {self.plants_added}, "
                f"Total growth: {self.total_growth}cm"
            )

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.stats: GardenManager.GardenStats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.record_add()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth(1)

    def garden_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display()
        print("")
        self.stats.report()
        self._type_summary()

    def _type_summary(self) -> None:
        regular = 0
        flowering = 0
        prize = 0

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            else:
                regular += 1

        print(f"Plant types: {regular} regular, "
              f"{flowering} flowering, {prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> int:
        return cls.total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


def calculate_score(garden: GardenManager) -> int:
    score = 0
    for plant in garden.plants:
        score += plant.height
        if isinstance(plant, PrizeFlower):
            score += plant.prize_points
    return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")
    simo = GardenManager("Simo")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    print("")

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print("")
    alice.help_plants_grow()
    alice.garden_report()

    print("\nHeight validation test:", GardenManager.validate_height(10))

    simo.add_plant(Plant("Cactus", 92))

    alice_score = calculate_score(alice)
    simo_score = calculate_score(simo)
    print(f"Garden scores - Alice: {alice_score}, Simo: {simo_score}")
    print("Total gardens managed:", GardenManager.create_garden_network())
