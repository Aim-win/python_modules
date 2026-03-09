from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, bool) and isinstance(data, (int, float)):
            return True
        elif isinstance(data, list) and len(data) > 0:
            return all(not isinstance(item, bool)
                       and isinstance(item, (float, int))
                       for item in data)
        else:
            return False

    def process(self, data: Union[list, int]) -> Optional[str]:
        if not self.validate(data):
            raise ValueError("Not valid numeric data")
        else:
            if isinstance(data, (int, float)):
                numeric_values = [data]
            else:
                numeric_values = data
            total_sum = sum(numeric_values)
            total_count = len(numeric_values)
            output = (f"Processed {total_count} numeric values, sum="
                      f"{total_sum}, avg={total_sum / total_count}\n")
            return output

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Not valid text data")
        word_tokens = data.split()
        word_count = len(word_tokens)
        char_count = len(data)

        return f"Processed text: {char_count} characters, {word_count} words\n"

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.log_levels = {'info': 'INFO', 'alert': 'ALERT', 'error': 'ERROR'}

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            parts = data.split(":")
            return len(parts) == 2 and all(part != "" for part in parts)
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Not valid log data")
        else:
            error_type, message = data.split(':', 1)
            tag = self.log_levels.get(
                error_type.lower(), error_type.upper())
            output = f"[{tag}] {error_type.upper()} level detected:{message}\n"
            return output

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def run_processing_suite() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    processors = [
        (NumericProcessor(), [0, 5, 4, 5]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "Error: Connection timeout"),
    ]

    for processor, data in processors:
        try:
            processor_name = processor.__class__.__name__
            data_type = processor_name.split("P")[0]
            # if processor_name == "NumericProcessor":
            print(f"\nInitializing {processor_name} ...")
            print(f'Processing data: "{data}"')
            result = processor.process(data)
            print(f"Validation: {data_type} data verified")
            print(processor.format_output(result))
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    test_data: Dict = {
        0: [1, 2, 3],
        1: "word wordddd ",
        2: "Alert: Storage is nearly full"
    }
    for index, processor in enumerate(processors):
        try:
            result = processor.process(test_data[index])
            print(f"Result: {index + 1} {result}", end="")
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == '__main__':
    run_processing_suite()
