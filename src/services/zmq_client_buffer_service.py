from py_types import Buffer, ZeroMQMsg
from internal_queues import FFT_PROCESS_QUEUE

ZMQ_CLIENT_BUFFER = Buffer(
    dt=[],
    VA=[],
    VB=[],
    VC=[],
    IA=[],
    IB=[],
    IC=[],
)


def zmq_client_buffer_service(msg: ZeroMQMsg):
    ZMQ_CLIENT_BUFFER.dt.append(msg["msg_body"]["dt"])
    ZMQ_CLIENT_BUFFER.VA.append(msg["msg_body"]["VA"])
    ZMQ_CLIENT_BUFFER.VB.append(msg["msg_body"]["VB"])
    ZMQ_CLIENT_BUFFER.VC.append(msg["msg_body"]["VC"])
    ZMQ_CLIENT_BUFFER.IA.append(msg["msg_body"]["IA"])
    ZMQ_CLIENT_BUFFER.IB.append(msg["msg_body"]["IB"])
    ZMQ_CLIENT_BUFFER.IC.append(msg["msg_body"]["IC"])
    # freq: float

    if 32 <= len(ZMQ_CLIENT_BUFFER.VA):
        # Remove first value
        ZMQ_CLIENT_BUFFER.dt.pop(0)
        ZMQ_CLIENT_BUFFER.VA.pop(0)
        ZMQ_CLIENT_BUFFER.VB.pop(0)
        ZMQ_CLIENT_BUFFER.VC.pop(0)
        ZMQ_CLIENT_BUFFER.IA.pop(0)
        ZMQ_CLIENT_BUFFER.IB.pop(0)
        ZMQ_CLIENT_BUFFER.IC.pop(0)
        # Send buffer
        FFT_PROCESS_QUEUE.put(ZMQ_CLIENT_BUFFER)
