from infra.zmq import ZMQServer
from services import zmq_client_buffer_service


def zmq_process():
    zmq_server = ZMQServer(callback=zmq_client_buffer_service)
    zmq_server.run()
