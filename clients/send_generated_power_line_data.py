from typing import List
import sys

from utils import (
    factory_zmq_context,
    senoidal_data_args_to_kwargs,
    send_msg,
    generate_senoidal_data,
)


def main(args: List[str]) -> None:
    kwargs = senoidal_data_args_to_kwargs(args)
    _, socket = factory_zmq_context()
    try:
        print("Starting connection...")
        for msg in generate_senoidal_data(**kwargs):
            send_msg(socket, msg)

    except Exception as e:
        print(e)
        print("Ending connection...")
    finally:
        socket.close()


if __name__ == "__main__":
    main(sys.argv)
