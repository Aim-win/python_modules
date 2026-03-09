import sys


def system_header() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")


def stream_management() -> None:
    system_header()

    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}\n")

    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    stream_management()
