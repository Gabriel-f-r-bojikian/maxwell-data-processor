import json

from zmq import Socket

from py_types import ZeroMQMsg


def send_msg(socket: Socket, msg: ZeroMQMsg) -> None:
    try:
        client_msg_b = json.dumps(msg, default=str).encode()
        socket.send(client_msg_b)
        server_msg = socket.recv()
        print("Received reply {}".format(server_msg))
    except Exception as e:
        raise Exception("Socket Timeout: {}".format(str(e)))
