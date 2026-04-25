def ft_harvest_total():
    day1 = day2 = day3 = -1
    while day1 < 0:
        day1 = int(input("Day 1 harvest: "))
    while day2 < 0:
        day2 = int(input("Day 2 harvest: "))
    while day3 < 0:
        day3 = int(input("Day 3 harvest: "))
    print("Total harvest", day1 + day2 + day3)
