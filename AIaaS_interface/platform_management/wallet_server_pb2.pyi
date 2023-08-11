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

class BuyAIModelReqPackageRequest(_message.Message):
    __slots__ = ["ai_model_name", "req_count", "user_id"]
    AI_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    REQ_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ai_model_name: str
    req_count: int
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., ai_model_name: _Optional[str] = ..., req_count: _Optional[int] = ...) -> None: ...

class BuyAIModelReqPackageResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateNewWalletRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class CreateNewWalletResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAIModelsCostPerReqRequest(_message.Message):
    __slots__ = ["ai_model_names"]
    AI_MODEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    ai_model_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ai_model_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAIModelsCostPerReqResponse(_message.Message):
    __slots__ = ["costs"]
    class CostsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    COSTS_FIELD_NUMBER: _ClassVar[int]
    costs: _containers.ScalarMap[str, int]
    def __init__(self, costs: _Optional[_Mapping[str, int]] = ...) -> None: ...

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

class HasUserWalletRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class HasUserWalletResponse(_message.Message):
    __slots__ = ["has_wallet"]
    HAS_WALLET_FIELD_NUMBER: _ClassVar[int]
    has_wallet: bool
    def __init__(self, has_wallet: bool = ...) -> None: ...

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

class SetAIModelCostPerReqRequest(_message.Message):
    __slots__ = ["ai_model_name", "cost_per_req"]
    AI_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    COST_PER_REQ_FIELD_NUMBER: _ClassVar[int]
    ai_model_name: str
    cost_per_req: int
    def __init__(self, ai_model_name: _Optional[str] = ..., cost_per_req: _Optional[int] = ...) -> None: ...

class SetAIModelCostPerReqResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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
