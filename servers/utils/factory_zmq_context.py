from typing import Tuple

import zmq
from zmq import Context, Socket

from py_types import ZeroMQDsn


def factory_zmq_context(
    ipv4: str = "127.0.0.1",
    port: str = "5555",
) -> Tuple[Context, Socket]:
    try:
        cnxn_str = ZeroMQDsn.build(ipv4, port)
        context = zmq.Context()
        context.setsockopt(zmq.RCVTIMEO, 5000)
        socket = context.socket(zmq.PUB)
        socket.bind(cnxn_str)
        return context, socket
    except Exception as e:
        print("ZMQ Failed: {}".format(str(e)))
        exit(-1)
