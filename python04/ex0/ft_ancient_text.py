def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_name}")

    try:
        file = open(file_name, "r")
        data = file.read()

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("-You don't have permission to read!")

    except Exception:
        print("-Error: Unexpected ERROR.")

    else:
        print("Connection established...")
        print(data)
        print("\nData recovery complete.", end=' ')

    finally:
        print("Storage system disconnected.")


if __name__ == "__main__":
    main()
