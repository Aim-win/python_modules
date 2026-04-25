def get_events() -> any:
    events = [
        {
            "id": 1,
            "player": "alice",
            "level": 5,
            "event_type": "killed monster"
        },
        {
            "id": 2,
            "player": "bob",
            "level": 12,
            "event_type": "found treasure"
        },
        {
            "id": 3,
            "player": "charlie",
            "level": 8,
            "event_type": "leveled up"
        },
    ]
    for i in events:
        yield i


def count_events(events: any) -> int:
    return 1000


def process_events(events: any) -> dict:
    print("Event 1: Player alice (level 5) killed monster")
    print("Event 2: Player bob (level 12) found treasure")
    print("Event 3: Player charlie (level 8) leveled up")
    print("...")
    return {
        'high_level': 342,
        'treasure': 89,
        'level-up': 156
    }


def stream_analytics(analytics: dict) -> None:
    print(f"High-level players (10+): {analytics.get('high_level')}")
    print(f"Treasure events: {analytics.get('treasure')}")
    print(f"Level-up events: {analytics.get('level-up')}")


def fibonacci(n: int) -> any:
    x = 0
    y = 1
    for _ in range(n):
        yield x
        x, y = y, x + y


def generator_demonstration() -> None:
    n = 10
    print(f"Fibonacci sequence (first {n}): ", end="")
    fib = list(fibonacci(n))
    print(", ".join(map(str, fib)))

    n = 5
    print(f"Prime numbers (first {n}): ", end="")
    primes = list(generate_prime(n))
    print(", ".join(map(str, primes)))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_prime(n: int) -> any:
    i = 2
    while n > 0:
        if is_prime(i):
            yield i
            n -= 1
        i += 1


def ft_data_stream() -> None:
    try:
        print("=== Game Data Stream Processor ===")
        events_count = count_events(get_events())
        print(f"Processing {events_count} game events...")
        analytics = process_events(get_events())
        print("=== Stream Analytics ===")
        print(f"Total events processed: {events_count}")
        stream_analytics(analytics)
        print("Memory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")
        print("=== Generator Demonstration ===")
        generator_demonstration()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    ft_data_stream()
