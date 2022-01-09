import multiprocessing as mp
import logging

from configs import LOG_CONFIGS
from processes import fft_process, red_panda_process, zmq_process

logging.basicConfig(**LOG_CONFIGS)
logger = logging.getLogger(__name__)


def main():
    try:
        # Create processes
        mp_zeromq = mp.Process(
            target=zmq_process,
            # args=(),
        )

        mp_red_panda = mp.Process(
            target=red_panda_process,
        )

        mp_fft = mp.Process(
            target=fft_process,
        )

        mp_zeromq.start()
        mp_red_panda.start()
        mp_fft.start()

        mp_zeromq.join()
        mp_red_panda.join()
        mp_fft.join()

    except Exception as e:
        logger.warning(str(e))


if __name__ == "__main__":
    main()
