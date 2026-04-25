from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']

    total_power = sum(map(lambda m: m['power'], mages))
    avg_p = round(total_power / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


def main() -> None:
    artifacts = [{'name': "Fire Staff", 'power': 92, 'type': "Legendary"},
                 {'name': "before Crystal Orb", 'power': 85, 'type': "Epic"}]

    sorted_list = artifact_sorter(artifacts)

    print("\nTesting artifact sorter...")
    for i in range(0, len(sorted_list) - 1):
        first = sorted_list[i]
        second = sorted_list[i+1]
        print(f"{first['name']} ({first['power']} power) "
              f"comes before {second['name']} ({second['power']} power)")

    spells = ["fireball", "heal", "shield"]
    transformed_list = spell_transformer(spells)
    print("\nTesting spell transformer...")
    for spell in transformed_list:
        print(spell, end=" ")
    print()


if __name__ == "__main__":
    main()
