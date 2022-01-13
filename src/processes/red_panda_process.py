import logging

from internal_queues import PARSED_DATA_QUEUE

logger = logging.getLogger(__name__)


def red_panda_process():
    while parsed_data := PARSED_DATA_QUEUE.get(block=True):
        # Send parsed data to Red Panda
        logger.debug(parsed_data)
