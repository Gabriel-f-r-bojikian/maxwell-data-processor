# import time
from typing import Callable, Optional
import logging
import json

# from time import sleep

import zmq

from py_types import ZeroMQMsg, ZeroMQDsn

logger = logging.getLogger(__name__)


MSG_TYPES = {
    # "test": bytes("Test", "utf-8"),
}


class ZMQServer:
    def __init__(
        self,
        ipv4: str = "127.0.0.1",
        port: str = "5555",
        callback: Optional[Callable] = None,
        args: tuple = (),
        kwargs: dict = {},
    ):
        self.cnxn_str = ZeroMQDsn.build(ipv4, port)
        self.context = zmq.Context()
        self.keep_running = True
        self.socket = self.context.socket(zmq.REP)

        # Callback
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def _bind(self) -> None:
        try:
            self.socket.bind(self.cnxn_str)
        except Exception as e:
            logger.warning(str(e))

    def _send_client_response(self, msg: ZeroMQMsg):
        if msg["msg_origin"] == "client":
            client_response = MSG_TYPES.get(
                msg["msg_type"].lower(), bytes("Invalid Message", "utf-8")
            )
        else:
            logger.warning("Received unexpected message from server: {}".format(msg))
            client_response = bytes("Unexpected Message", "utf-8")

        self.socket.send(client_response)

    def _handle(self, client_request_b) -> None:
        try:
            client_request = json.loads(client_request_b)
            self._send_client_response(client_request)

            if self.callback is not None:
                self.callback(client_request, *self.args, **self.kwargs)
        except Exception as e:
            logger.warning(str(e))

    def run(self) -> None:
        self._bind()
        if not self.keep_running:
            client_request_b = self.socket.recv()
            self._handle(client_request_b)
            return

        while client_request_b := self.socket.recv():
            self._handle(client_request_b)
            # sleep(0.1)
