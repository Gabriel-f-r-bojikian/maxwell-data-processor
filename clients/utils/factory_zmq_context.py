from typing import Tuple
import zmq
from zmq import Context, Socket


def factory_zmq_context() -> Tuple[Context, Socket]:
    try:
        context = zmq.Context()
        context.setsockopt(zmq.RCVTIMEO, 5000)
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://127.0.0.1:5555")
        return context, socket
    except Exception as e:
        print("ZMQ Failed: {}".format(str(e)))
        exit(-1)
