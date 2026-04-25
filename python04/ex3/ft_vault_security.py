def system_header() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")


def finish() -> None:
    print("All vault operations completed with maximum security.")


def vault_security() -> None:
    try:
        system_header()
        print("Initiating secure vault access...")

        print("Vault connection established with failsafe protocols")

        print("\nSECURE EXTRACTION:")
        with open("classified_data.txt", "r") as vault:
            content = vault.read()

        print(content)

        new = "[CLASSIFIED] New security protocols archived"

        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as vault:
            vault.write(new)
        print(new)
        print("Vault automatically sealed upon completion\n")
        finish()
    except FileNotFoundError:
        print("Error: File not found!!")

    except PermissionError:
        print("Error :you don't have permissions")

    except Exception:
        print("Error while extracting files")


if __name__ == "__main__":
    try:
        vault_security()
    except Exception as e:
        print("Unexcpected error : ", e)
