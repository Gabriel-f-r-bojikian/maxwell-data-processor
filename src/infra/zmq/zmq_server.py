# import time
from typing import Callable, Optional
import logging
import json
from time import sleep

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

    def _client_response(self, msg: ZeroMQMsg) -> bytes:
        if msg["msg_origin"] == "client":
            return MSG_TYPES.get(
                msg["msg_type"].lower(), bytes("Invalid Message", "utf-8")
            )
        else:
            logger.warning("Received unexpected message from server: {}".format(msg))
            return bytes("Unexpected Message", "utf-8")

    def _handle(self) -> None:
        try:
            client_request_b = self.socket.recv()
            client_response = self._client_response(json.loads(client_request_b))
            self.socket.send(client_response)

            if self.callback is not None:
                self.callback(client_response, *self.args, **self.kwargs)
        except Exception as e:
            logger.warning(str(e))

    def run(self) -> None:
        self._bind()
        if not self.keep_running:
            self._handle()
            return

        while True:
            self._handle()
            sleep(0.1)
