from typing import TypedDict


class ZeroMQMsgBody(TypedDict):
    pass


class ZeroMQMsg(TypedDict):
    msg_origin: str
    msg_type: str
    msg_body: ZeroMQMsgBody
