def check_temperature(temp_str: str) -> None:
    try:
        value = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number\n")
    if (value >= 0 and value <= 40):
        return value
    elif (value > 40):
        raise ValueError(
            f"Error: {value}°C is too hot for plants (max 40°C)\n")
    else:
        raise ValueError(
            f"Error: {value}°C is too cold for plants (min 0°C)\n")


def test_temperature_input() -> None:
    list_of_tests = ['25', 'abc', '100', '-50']
    print("=== Garden Temperature Checker ===\n")
    for value in list_of_tests:
        try:
            print(f"Testing temperature: {value}")
            print(f"Temperature {check_temperature(value)}", end="")
            print("°C is perfect for plants!\n")
        except ValueError as err:
            print(err)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
