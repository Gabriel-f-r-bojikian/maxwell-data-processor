from typing import List

from internal_queues import PARSED_DATA_QUEUE


def send_parsed_data_service(data: List[dict]):
    PARSED_DATA_QUEUE.put(data)  # , block=True
