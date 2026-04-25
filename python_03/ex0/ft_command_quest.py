import sys


def ft_command_quest() -> None:
    argc = len(sys.argv)
    argv = sys.argv
    count = 1
    print("=== Command Quest ===")
    if argc == 1:
        print("No arguments provided!")
    print(f"Program name: {argv[0]}")
    if (argc > 1):
        print(f"Arguments received: {argc - 1}")
        for i in argv[1:]:
            print(f"Argument {count}: {i}")
            count += 1
    print(f"Total arguments: {argc}")


if __name__ == '__main__':
    ft_command_quest()
