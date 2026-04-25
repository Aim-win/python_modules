import sys
import os


def is_virtual_env() -> bool:
    """Checks if the script is running inside a virtual environment.

    Returns:
        bool: True if inside a virtual env, False otherwise.
    """
    has_dif = sys.prefix != sys.base_prefix
    return has_dif


def main() -> None:

    if not is_virtual_env():
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv --without-pip matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")

        print("\nThen run this program again.")

    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)

        venv_name = os.path.basename(sys.prefix)
        print("Virtual Environment:", venv_name)

        env_path = os.environ.get('VIRTUAL_ENV')
        print("Environment Path:", env_path)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        check = sys.path

        for p in check:
            if "site-packages" in p:
                print(p)
                break


if __name__ == "__main__":
    main()
