def system_header() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def finish() -> None:
    print("All crisis scenarios handled successfully. Archives secure.")


def crisis_response() -> None:
    system_header()
    try:
        name = "lost_archive.txt"
        with open(name, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        name = "classified_data.txt"
        with open(name, 'r') as file:
            data = file.read()
            print(data, "\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    try:
        name = "standard_archive.txt"
        with open(name, 'r') as file:
            data = file.read()
        print(f"ROUTINE ACCESS: Attempting access to '{name}'...")
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(e)

    finish()


if __name__ == "__main__":
    try:
        crisis_response()
    except Exception as e:
        print("Unexcpected error : ", e)
