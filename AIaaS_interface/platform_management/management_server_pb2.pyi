from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetOnlinePaymentCallbackUrlRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetOnlinePaymentCallbackUrlResponse(_message.Message):
    __slots__ = ["callback_url"]
    CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    callback_url: str
    def __init__(self, callback_url: _Optional[str] = ...) -> None: ...
