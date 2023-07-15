from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AI_MODEL_COST: TransactionKind
DEPOSIT: TransactionKind
DESCRIPTOR: _descriptor.FileDescriptor
FAILED: TransactionStatus
PENDING: TransactionStatus
STORAGE_COST: TransactionKind
SUCCESSFUL: TransactionStatus
UNKNOWN_KIND: TransactionKind
UNKNOWN_STATUS: TransactionStatus
WITHDRAW: TransactionKind

class CreateNewWalletRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class CreateNewWalletResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTransactionsHistoryRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetTransactionsHistoryResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class GetWalletBalanceRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetWalletBalanceResponse(_message.Message):
    __slots__ = ["balance"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: int
    def __init__(self, balance: _Optional[int] = ...) -> None: ...

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

class Transaction(_message.Message):
    __slots__ = ["ai_model_name", "amount", "created_at", "kind", "status"]
    AI_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ai_model_name: str
    amount: int
    created_at: _timestamp_pb2.Timestamp
    kind: TransactionKind
    status: TransactionStatus
    def __init__(self, amount: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., kind: _Optional[_Union[TransactionKind, str]] = ..., status: _Optional[_Union[TransactionStatus, str]] = ..., ai_model_name: _Optional[str] = ...) -> None: ...

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

class TransactionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TransactionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
