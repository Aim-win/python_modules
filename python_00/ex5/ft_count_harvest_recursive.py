def ft_recursive(day, total):
    print("Day ", day)
    if day < total:
        ft_recursive(day + 1, total)
    if day == total:
        print("Harvest time!")


def ft_count_harvest_recursive():
    total = int(input("Days until harvest: "))
    if total > 0:
        ft_recursive(1, total)
