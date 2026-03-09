def system_header() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")


def archive_creation() -> None:
    system_header()

    file = None
    entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
    entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        file.write(entry1)
        print(entry1, end='')
        file.write(entry2)
        print(entry2, end='')
        file.write(entry3)
        print(entry3, end='')

        print("\nData inscription complete. Storage unit sealed.")
    except FileNotFoundError:
        print("Error :File not found")
    except PermissionError:
        print("Error :you don't have permissions")
    except Exception:
        print("Error :can't open/write the new_discovery.txt")
    else:
        print("Archive 'new_discovery.txt'ready for long-term preservation.")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    archive_creation()
