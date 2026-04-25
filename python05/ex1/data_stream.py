from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class providing core streaming functionality."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._processed_count: int = 0
        self._error_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data items and return a summary string."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data batch. Subclasses may override
        for domain-specific logic."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed": self._processed_count,
            "errors": self._error_count,
        }


class SensorStream(DataStream):
    """Stream handler for environmental sensor readings."""

    STREAM_TYPE: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse sensor readings and compute average temperature."""
        if not data_batch:
            raise ValueError("Empty sensor batch.")
        temps: List[float] = []
        for item in data_batch:
            try:
                # Items expected as "key:value" strings, e.g. "temp:22.5"
                if isinstance(item, str) and item.startswith("temp:"):
                    temps.append(float(item.split(":")[1]))
            except (ValueError, IndexError):
                self._error_count += 1
        self._processed_count += len(data_batch)
        count = len(data_batch)
        if temps:
            avg = sum(temps) / len(temps)
            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg:.1f}\u00b0C"
            )
        return f"Sensor analysis: {count} readings processed"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter sensor readings; 'alert'
                criteria keeps only high-value temps."""

        if criteria == "alert":
            result: List[Any] = []
            for item in data_batch:
                try:
                    if isinstance(item, str) and item.startswith("temp:"):
                        if float(item.split(":")[1]) > 30.0:
                            result.append(item)
                except (ValueError, IndexError):
                    pass
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.STREAM_TYPE
        return stats


class TransactionStream(DataStream):
    """Stream handler for financial transaction data."""

    STREAM_TYPE: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Parse buy/sell transactions and compute net flow."""
        if not data_batch:
            raise ValueError("Empty transaction batch.")
        net: float = 0.0
        for item in data_batch:
            try:
                if isinstance(item, str):
                    action, amount_str = item.split(":")
                    amount = float(amount_str)
                    net += amount if action.strip() == "buy" else -amount
            except (ValueError, IndexError):
                self._error_count += 1
        self._processed_count += len(data_batch)
        sign = "+" if net >= 0 else ""
        return (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {sign}{net:.0f} units"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter transactions; 'large' criteria keeps amounts above 90."""
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                try:
                    if isinstance(item, str):
                        amount = float(item.split(":")[1])
                        if amount > 90:
                            result.append(item)
                except (ValueError, IndexError):
                    pass
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.STREAM_TYPE
        return stats


class EventStream(DataStream):
    """Stream handler for system event data."""

    STREAM_TYPE: str = "System Events"
    ERROR_KEYWORDS: List[str] = ["error", "fail", "critical"]

    def process_batch(self, data_batch: List[Any]) -> str:
        """Count events and detect errors."""
        if not data_batch:
            raise ValueError("Empty event batch.")
        error_count = sum(
            1 for item in data_batch
            if any(kw in str(item).lower() for kw in self.ERROR_KEYWORDS)
        )
        self._processed_count += len(data_batch)
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{error_count} error detected"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter events; 'high-priority' criteria
                    keeps error/critical events."""

        if criteria == "high-priority":
            return [
                item for item in data_batch
                if any(kw in str(item).lower() for kw in self.ERROR_KEYWORDS)
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.STREAM_TYPE
        return stats


class StreamProcessor:
    """Manages and processes multiple DataStream types polymorphically."""

    def __init__(self) -> None:
        self._streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a stream for processing."""
        self._streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        """Process each registered stream with its corresponding batch."""
        results: List[str] = []
        for stream, batch in zip(self._streams, batches):
            try:
                results.append(stream.process_batch(batch))
            except ValueError as e:
                results.append(f"Stream error [{stream.stream_id}]: {e}")
        return results

    def filter_stream(
        self,
        stream: DataStream,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Delegate filtering to the specific stream implementation."""
        return stream.filter_data(data_batch, criteria)


def demo_individual_streams() -> None:
    """Demonstrate each stream type individually."""
    sensor = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.STREAM_TYPE}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))
    print()

    transaction = TransactionStream("TRANS_001")
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id},"
          f" Type: {transaction.STREAM_TYPE}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_batch}")
    print(transaction.process_batch(trans_batch))
    print()

    event = EventStream("EVENT_001")
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.STREAM_TYPE}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))
    print()


def demo_polymorphic_processing(processor: StreamProcessor) -> None:
    """Process mixed stream types through the unified StreamProcessor."""
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    batches: List[List[Any]] = [
        ["temp:20.0", "humidity:50"],
        ["buy:100", "sell:50", "buy:200", "sell:80"],
        ["login", "logout", "error"],
    ]
    results = processor.process_all(batches)
    print("\nBatch 1 Results:")
    labels = ["Sensor data", "Transaction data", "Event data"]
    for label, result in zip(labels, results):
        count_part = result.split(":")[1].strip().split(" ")[0]
        unit = "readings" if "Sensor" in label else (
            "operations" if "Transaction" in label else "events"
        )
        print(f"- {label}: {count_part} {unit} processed")
    print()


def demo_filtering(
    sensor: SensorStream,
    transaction: TransactionStream,
) -> None:
    """Demonstrate stream filtering capabilities."""
    print("Stream filtering active: High-priority data only")
    sensor_data = ["temp:35.2", "temp:18.0", "temp:40.1", "humidity:60"]
    critical_sensors = sensor.filter_data(sensor_data, "alert")
    large_trans = transaction.filter_data(
        ["buy:100", "sell:50", "buy:200", "sell:15"], "large"
    )
    print(
        f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
        f"{len(large_trans)} large transaction"
    )
    print()


def main() -> None:
    """Entry point: demonstrate the full polymorphic stream system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    demo_individual_streams()

    sensor = SensorStream("SENSOR_002")
    transaction = TransactionStream("TRANS_002")
    event = EventStream("EVENT_002")

    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(transaction)
    manager.add_stream(event)

    demo_polymorphic_processing(manager)
    demo_filtering(sensor, transaction)

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
