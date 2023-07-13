from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewWalletRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class CreateNewWalletResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class OnlinePaymentRequest(_message.Message):
    __slots__ = ["amount", "user_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    amount: int
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., amount: _Optional[int] = ...) -> None: ...

class OnlinePaymentResponse(_message.Message):
    __slots__ = ["online_payment_url"]
    ONLINE_PAYMENT_URL_FIELD_NUMBER: _ClassVar[int]
    online_payment_url: str
    def __init__(self, online_payment_url: _Optional[str] = ...) -> None: ...

class VerifyOnlinePaymentRequest(_message.Message):
    __slots__ = ["track_id"]
    TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    track_id: int
    def __init__(self, track_id: _Optional[int] = ...) -> None: ...

class VerifyOnlinePaymentResponse(_message.Message):
    __slots__ = ["was_successful"]
    WAS_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    was_successful: bool
    def __init__(self, was_successful: bool = ...) -> None: ...
