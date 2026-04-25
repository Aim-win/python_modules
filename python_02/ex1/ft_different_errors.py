def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int('abc')
    except (ValueError):
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        int(10 / 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("file.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'file.txt'\n")

    try:
        print("Testing KeyError...")
        dict = {"fname": "newton"}
        print(dict["lname"])
    except KeyError:
        print("Caught KeyError: 'lname'\n")

    try:
        print("Testing multiple errors together...")
        int('abc')
        int(10 / 0)
        open("file.txt")
        dict = {"fname": "newton"}
        print(dict["lname"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
