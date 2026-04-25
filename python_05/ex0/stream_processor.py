from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class defining the common data processing interface."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Specialized processor for numeric list data."""

    def validate(self, data: Any) -> bool:
        """Validate that data is a non-empty list of numbers."""
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        """Compute sum and average of numeric values."""
        if not self.validate(data):
            raise ValueError("Invalid numeric data:"
                             " expected a list of numbers.")
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Specialized processor for text/string data."""

    def validate(self, data: Any) -> bool:
        """Validate that data is a non-empty string."""
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: Any) -> str:
        """Count characters and words in the text."""
        if not self.validate(data):
            raise ValueError("Invalid text data: expected a non-empty string.")
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Specialized processor for log entry strings."""

    LOG_LEVELS: List[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def validate(self, data: Any) -> bool:
        """Validate that data is a string containing a known log level."""
        if not isinstance(data, str):
            return False
        return any(level in data.upper() for level in self.LOG_LEVELS)

    def process(self, data: Any) -> str:
        """Extract log level and message from the log entry."""
        if not self.validate(data):
            raise ValueError("Invalid log data: no"
                             " recognized log level found.")
        detected_level = "UNKNOWN"
        for level in self.LOG_LEVELS:
            if level in data.upper():
                detected_level = level
                break
        separator = f"{detected_level}: "
        if separator in data:
            message = data.split(separator, 1)[1]
        else:
            message = data
        if detected_level in ("ERROR", "CRITICAL", "WARNING"):
            tag = "ALERT"
        else:
            tag = "INFO"
        return f"[{tag}] {detected_level} level detected: {message}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def demo_individual(processor: DataProcessor, data: Any, label: str) -> None:
    """Run a single processor demo with validation and output."""
    class_name = type(processor).__name__
    print(f"Initializing {class_name}...")
    print(f"Processing data: {label}")
    try:
        if processor.validate(data):
            print("Validation: "
                  f"{class_name.replace('Processor', '')} data verified")
            result = processor.process(data)
            print(processor.format_output(result))
        else:
            print("Validation: FAILED - data rejected")
    except ValueError as e:
        print(f"Error: {e}")
    print()


def demo_polymorphic(processors: List[DataProcessor],
                     dataset: List[Any]
                     ) -> None:
    """Demonstrate polymorphic processing through a unified interface."""
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for idx, (processor, data) in enumerate(zip(processors, dataset), start=1):
        try:
            result = processor.process(data)
            print(f"Result {idx}: {result}")
        except ValueError as e:
            print(f"Result {idx}: Error - {e}")
    print()


def main() -> None:
    """Entry point: demonstrate the polymorphic data processing system."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    demo_individual(numeric, [1, 2, 3, 4, 5], "[1, 2, 3, 4, 5]")
    demo_individual(text, "Hello Nexus World", '"Hello Nexus World"')
    demo_individual(log, "ERROR: Connection timeout",
                    '"ERROR: Connection timeout"')

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    dataset: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready",
    ]
    demo_polymorphic(processors, dataset)

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
