from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stats = {}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats


class SensorStream(DataStream):
    fields = ['temp', 'humidity', 'pressure']
    high_val = 100

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def filter_data(self, batch_data: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [
                reading for reading in batch_data
                if (any(reading.get(field) is not None
                        and reading.get(field) > self.high_val
                        for field in self.fields))
            ]
        return batch_data

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list) or not batch_data:
            raise ValueError("Data should not be an empty list")
        temperature_values = []
        total_processed = 0
        for entry in batch_data:
            if not (isinstance(entry, dict) and len(entry.keys()) == 1):
                raise ValueError("Data should be in key value pairs style")
            field_name, field_value = next(iter(entry.items()))
            if (not isinstance(field_name, str) or field_name
                    not in self.fields):
                raise ValueError("Invalid key")

            if (isinstance(field_value, bool)
                    or not isinstance(field_value, (float, int))):
                raise ValueError("Value should be a number")
            if field_name == 'temp':
                temperature_values.append(field_value)
                if field_value > self.high_val:
                    print(f"The temperature is too high "
                          f"[max :{self.high_val}]")
            total_processed += 1
        self.stats.update({
            'avg_temp': sum(temperature_values) / len(temperature_values) if
            len(temperature_values) > 0 else 0,
            'processed': total_processed
        })
        return f"Sensor analysis: {self.stats['processed']} processed"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats

    def get_type(self) -> str:
        return "Environmental Data"

    def print_analitics(self, processed: int):
        return f"\n- Sensor data: {processed} readings processed"


class TransactionStream(DataStream):
    transactions = ['buy', 'sell']

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def sum_transactions(
            self, operation_type: str, amount: float) -> None:
        if operation_type in self.stats:
            self.stats[operation_type] += amount
        else:
            self.stats[operation_type] = amount

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list) or len(batch_data) == 0:
            raise ValueError("Data is Invalid")

        total_operations = 0
        for entry in batch_data:
            if not (isinstance(entry, dict) and len(entry.keys()) == 1):
                raise ValueError("Data is Invalid")
            operation_type, transaction_amount = next(iter(entry.items()))
            operation_type = operation_type.lower()

            if (not isinstance(operation_type, str) or operation_type
                not in self.transactions
                    or isinstance(transaction_amount, bool)
                    or not isinstance(transaction_amount, (int, float))):
                raise ValueError("Data is Invalid")

            self.sum_transactions(operation_type, transaction_amount)
            total_operations += 1

        self.stats.update({'processed': total_operations})
        buy_total = self.stats.get('buy', 0)
        sell_total = self.stats.get('sell', 0)
        self.stats.update({"net_flow": buy_total - sell_total})
        return f"Transaction analysis: {self.stats.get('processed')} " +\
            "operations"

    def filter_data(self, batch_data: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [
                entry for entry in batch_data
                if any(isinstance(entry.get(op), (int, float)) and
                       entry.get(op) > 100 for op in self.transactions)
            ]
        return batch_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats

    def get_type(self) -> str:
        return "Financial Data"

    def print_analitics(self, processed: int):
        return f"\n- Transaction data: {processed} operations processed"


class EventStream(DataStream):
    ERROR_EVENT_KEYWORD = 'error'

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, batch_data: List[Any]) -> str:
        if not isinstance(batch_data, list):
            raise ValueError("Data is Invalid")

        processed_events = 0
        for event_entry in batch_data:
            if not isinstance(event_entry, str) or not event_entry:
                raise ValueError("Data is Invalid")
            if event_entry.lower() == self.ERROR_EVENT_KEYWORD:
                self.stats['error_count'] = self.stats.get(
                    'error_count', 0) + 1

            processed_events += 1
        if 'error_count' not in self.stats:
            self.stats.update({'error_count': 0})
        self.stats.update({"processed": processed_events})
        return f"Event analysis: {len(batch_data)} events"

    def filter_data(self, batch_data: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == 'high':
            return [
                event for event in batch_data
                if event.lower() == self.ERROR_EVENT_KEYWORD
            ]
        return batch_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats

    def get_type(self) -> str:
        return "System Events"

    def print_analitics(self, processed: int):
        return f"\n- Event data: {processed} events processed"


class StreamProcessor():
    STREAMS = {
        'SensorStream': 'readings',
        'TransactionStream': 'operations',
        'EventStream': 'error_count'
    }

    STREAM_KEYS = {
        'SensorStream': 'sensor_count',
        'TransactionStream': 'transaction_count',
        'EventStream': 'events_count'
    }

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_streams(self, batch_data: List[List[Any]]) -> None:
        for index, stream in enumerate(self.streams):
            stream.process_batch(batch_data[index])
            analytics = stream.get_stats()
            stream_type = stream.__class__.__name__
            if stream_type in self.STREAMS:
                print(stream.print_analitics(analytics.get("processed")))

    def filter_streams(self, batch_data: List[List[Any]]) -> Dict[str, int]:
        result = {key: 0 for key in self.STREAM_KEYS.values()}

        for idx, stream in enumerate(self.streams):
            stream_type = stream.__class__.__name__
            if stream_type in self.STREAM_KEYS:
                result_key = self.STREAM_KEYS[stream_type]
                filtered_count = len(stream.filter_data(
                    batch_data[idx], 'high'))
                result[result_key] = filtered_count

        return result


def run_stream_analysis() -> None:
    stream_test_configs = [
        (SensorStream('SENSOR_001'), [{"temp": 24.5}, {"humidity": 55},
                                      {'pressure': 1012}]),
        (TransactionStream('TRANS_001'), [{'buy': 300}, {'sell': 120},
                                          {'buy': 70}]),
        (EventStream('EVENT_001'), ['logged', 'error', 'info'])
    ]
    streams = []

    for stream_obj, data in stream_test_configs:
        try:
            stream_name = stream_obj.__class__.__name__
            print(f"\nInitializing {stream_name}...")
            print(f"Stream ID: {stream_obj.stream_id}, Type: "
                  f"{stream_obj.get_type()}")
            print(f"Processing {stream_name} batch: {data}")
            analysis_result = stream_obj.process_batch(data)
            stream_stats = stream_obj.get_stats()

            if stream_name == 'SensorStream':
                print(
                      f"{analysis_result}, "
                      f"avg temp: {stream_stats.get('avg_temp')}°C\n"
                      )
            elif stream_name == 'TransactionStream':
                net_val = stream_stats.get('net_flow')
                sign = '+' if net_val > 0 else ''
                print(f"{analysis_result}, net flow: {sign}{net_val} units\n")
            elif stream_name == 'EventStream':
                print(f"{analysis_result}, "
                      f"{stream_stats.get('error_count')} error dectected\n")

            streams.append(stream_obj)
        except Exception as e:
            print(f"Type: {e.__class__.__name__}, {e}")
    try:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        batch_data = [
            [{'temp': 120}, {"humidity": 45}, {'pressure': 98}],
            [{'buy': 80}, {'sell': 150}, {'buy': 40}],
            ['login', 'error', 'logout']
        ]
        stream_processor = StreamProcessor()
        for stream in streams:
            stream_processor.add_stream(stream)

        print("Batch 1 Results:")
        stream_processor.process_streams(batch_data)
        print("\nStream filtering active: High-priority data only")
        filter_result = stream_processor.filter_streams(
            batch_data)
        print(f"Filtered results: "
              f"{filter_result.get('sensor_count')} ", end="")
        print(f"critical sensor alerts, "
              f"{filter_result.get('transaction_count')} large transaction\n"
              )
        print("All streams processed successfully. Nexus throughput optimal.")
    except Exception as e:
        print(f"Type: {e.__class__.__name__}, {e}")


if __name__ == '__main__':
    run_stream_analysis()
