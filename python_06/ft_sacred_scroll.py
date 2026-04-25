import alchemy


def sacred_scroll() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", alchemy.elements.create_air())

    print("\nTesting package-level access (controlled by __init__.py):")

    print("alchemy.create_fire(): ", end="")
    try:
        fire = alchemy.create_fire()
        print(fire)
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_water(): ", end="")
    try:
        water = alchemy.create_water()
        print(water)
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_earth(): ", end="")
    try:
        earth = alchemy.create_earth()
        print(earth)
    except AttributeError:
        print("AttributeError - not exposed")

    print("alchemy.create_air(): ", end="")
    try:
        air = alchemy.create_air()
        print(air)
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    try:
        print(alchemy.__version__)
        print(alchemy.__author__)
    except AttributeError:
        print("AttributeError - No Attribute Found !")


if __name__ == "__main__":
    sacred_scroll()
