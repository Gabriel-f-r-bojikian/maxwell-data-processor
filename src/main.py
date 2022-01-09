import multiprocessing as mp
import logging

from configs import LOG_CONFIGS
from processes import zmq_process

logging.basicConfig(**LOG_CONFIGS)
logger = logging.getLogger(__name__)


def main():
    try:
        # Create processes
        zeromq_p = mp.Process(
            target=zmq_process,
            # args=(),
        )
        zeromq_p.start()
        zeromq_p.join()

    except Exception as e:
        logger.warning(str(e))


if __name__ == "__main__":
    main()
