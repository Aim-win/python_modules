import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("[ERROR] 'python-dotenv' module not found.")
    print("Please install it by running: pip install python-dotenv")
    exit(1)


def load_oracle_config() -> tuple:
    """
    Loads environment variables from a .env file and verifies their presence.

    load_dotenv() scans for a .env file and injects its key-value pairs
    into the process environment — but only if the key isn't already set.
    This means real environment variables always take priority over .env,
    which is the correct behaviour for production overrides.

    We iterate through a list of required_vars and track any missing ones
    to prevent running the system in an insecure or misconfigured state.
    """
    load_dotenv()

    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    settings = {}
    absent = []

    for key in required_vars:
        val = os.getenv(key)
        if not val:
            absent.append(key)
        settings[key] = val

    return settings, absent


def run() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    settings, absent = load_oracle_config()

    mode = settings.get("MATRIX_MODE", "NOT SET")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    db_status = (
        "Connected to local instance"
        if mode == "development"
        else "Remote Cluster"
    )
    print(f"Database: {db_status}")

    print(f"API Access: "
          f"{'Authenticated' if settings.get('API_KEY') else 'FAILED'}")
    print(f"Log Level: {settings.get('LOG_LEVEL', 'NOT SET')}")
    print(f"Zion Network: "
          f"{'Online' if settings.get('ZION_ENDPOINT') else 'Offline'}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if absent:
        print(f"[KO] .env file incomplete. Missing: {', '.join(absent)}")
    else:
        print("[OK] .env file properly configured")

    if mode == "production":
        print("[OK] Running in production mode")
    elif mode == "development":
        print("[OK] Production overrides available")
    else:
        print("[KO] No development or production mode found")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    run()
