import sys


def system_header() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")


def stream_management() -> None:
    try:
        system_header()

        arch_id = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")

        sys.stdout.write("\n[STANDARD] Archive status"
                         f" from {arch_id}: {status}\n")

        sys.stderr.write("[ALERT] System diagnostic: "
                         "Communication channels verified\n")

        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print("\nThree-channel communication test successful.")
    except KeyboardInterrupt:
        print("\nThe keyboard was interrupted !!")


if __name__ == "__main__":
    try:
        stream_management()
    except Exception as e:
        print("Unexcpected error : ", e)
