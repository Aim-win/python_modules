import sys


def count_items(data: dict) -> int:
    count = 0
    unique_items = set()
    for k, v in data.items():
        count += int(v.get('quantity'))
        unique_items.add(k)
    print(f"Total items in inventory: {count}")
    print(f"Unique item types: {len(unique_items)}\n")
    return count


def count_percentages(data: dict, total_items: int) -> dict:
    items = {}
    for k, v in data.items():
        if k not in items:
            items.update({k: v.get('quantity')})
        else:
            print(items.get(k))
            items.update({k: items.get(k) + v.get('quantity')})
    for k, v in items.items():
        percentage = (v / total_items) * 100
        items.update({k: {"units": v, "percentage": percentage}})
        print(f"{k}: {v} units ({percentage:.1f}%)")
    return items


def ft_inventory_system() -> None:
    try:
        print("=== Inventory System Analysis ===")
        if len(sys.argv) == 1:
            raise ValueError('Error: No Data Provided')
        data = {}
        argv = sys.argv
        val = 200
        types = ['Scarce', 'Moderate']
        index = 0
        for i in argv[1:]:
            name, quantity = i.split(':')
            if int(quantity) < 1:
                raise ValueError("Error: Quantity Should be Positive")
            if not data.get(name):
                data.update(
                    {
                        name: {
                            'quantity': int(quantity),
                            'value': int(val),
                            'type': types[index]
                        }
                    }
                )
            else:
                quantity = int(quantity) + data.get(name).get('quantity')
                data.update({
                    name: {
                        'quantity': int(quantity),
                        'value': int(val), 'type': types[index]
                    }
                })
            val += 320
            if index == 0:
                index = 1
            else:
                index = 0
        total_items = count_items(data)
        print("=== Current Inventory ===")
        items = count_percentages(data, total_items)
        print("\n=== Inventory Statistics ===")
        most_least_abundant(items)
        print("\n=== Item Categories ===")
        display_item_categories(data)
        print("\n=== Management Suggestions ===")
        print("Restock needed: ", end="")
        restock_items = [k for k, v in items.items() if v.get('units') <= 1]
        print(restock_items)
        print("\n=== Dictionary Properties Demo ===")
        dict_keys = [k for k in data.keys()]
        dict_values = [
            v.get('value') for v in data.values()
        ]
        print("Dictionary keys: ", dict_keys)
        print("Dictionary values: ", dict_values)
        print("Sample lookup - 'sword' in inventory: ", end="")
        print(f"{lookup_for_item(data, 'sword')}")
    except Exception as e:
        print(e)


def lookup_for_item(data: dict, item: str) -> bool:
    for k in data.keys():
        if k == item:
            return True
    return False


def display_item_categories(data: dict) -> None:
    moderate = {}
    scarce = {}
    for k, v in data.items():
        if v.get("type").lower() == 'moderate':
            if k in moderate:
                moderate.update({k: moderate.get(k) + v.get('quantity')})
            else:
                moderate.update({k: int(v.get('quantity'))})
        elif v.get("type").lower() == 'scarce':
            if k in scarce:
                scarce.update({k: scarce.get(k) + v.get('quantity')})
            else:
                scarce.update({k: v.get('quantity')})
    print("Moderate: ", moderate)
    print("Scarce: ", scarce)


def most_least_abundant(items: dict) -> None:
    most_abundant = None
    biggest_percentage = -1
    least_abundant = None
    lowest_percentage = 101
    for k, v in items.items():
        p = v.get('percentage')
        if p > biggest_percentage:
            most_abundant = {k: v}
            biggest_percentage = p
        if p < lowest_percentage:
            least_abundant = {k: v}
            lowest_percentage = p
    u = list(most_abundant.values())[0]
    n = list(most_abundant.keys())[0]
    print(f"Most abundant: {n} ({u.get('units')} units)")
    u = list(least_abundant.values())[0]
    n = list(least_abundant.keys())[0]
    print(f"Least abundant: {n} ({u.get('units')} units)")


if __name__ == '__main__':
    ft_inventory_system()
