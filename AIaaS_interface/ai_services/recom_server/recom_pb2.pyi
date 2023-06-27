from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColdstartItem(_message.Message):
    __slots__ = ["item_id", "movie_title", "rate"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    rate: int
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ..., rate: _Optional[int] = ...) -> None: ...

class ColdstartRequest(_message.Message):
    __slots__ = ["model", "n", "verbose"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    model: ModelProperties
    n: int
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ..., n: _Optional[int] = ...) -> None: ...

class ColdstartResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ColdstartItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ColdstartItem, _Mapping]]] = ...) -> None: ...

class CreateModelRequest(_message.Message):
    __slots__ = ["model", "verbose"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    model: ModelProperties
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ...) -> None: ...

class CreateModelResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ModelProperties(_message.Message):
    __slots__ = ["model_name", "user_id"]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    model_name: int
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., model_name: _Optional[int] = ...) -> None: ...

class SimilaritemsItem(_message.Message):
    __slots__ = ["item_id", "movie_title"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ...) -> None: ...

class SimilaritemsRequest(_message.Message):
    __slots__ = ["item_name", "model", "n", "verbose"]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    model: ModelProperties
    n: int
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ..., n: _Optional[int] = ..., item_name: _Optional[str] = ...) -> None: ...

class SimilaritemsResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SimilaritemsItem]
    def __init__(self, items: _Optional[_Iterable[_Union[SimilaritemsItem, _Mapping]]] = ...) -> None: ...

class StartColdstartRequest(_message.Message):
    __slots__ = ["data_dir", "model", "verbose"]
    DATA_DIR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    data_dir: str
    model: ModelProperties
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data_dir: _Optional[str] = ..., verbose: bool = ...) -> None: ...

class StartColdstartResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartSimilaritemsRequest(_message.Message):
    __slots__ = ["algo", "bsl_options", "data_dir", "k", "min_k", "model", "sim_options", "verbose"]
    ALGO_FIELD_NUMBER: _ClassVar[int]
    BSL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_DIR_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    MIN_K_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SIM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    algo: str
    bsl_options: _struct_pb2.Struct
    data_dir: str
    k: int
    min_k: int
    model: ModelProperties
    sim_options: _struct_pb2.Struct
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data_dir: _Optional[str] = ..., algo: _Optional[str] = ..., verbose: bool = ..., k: _Optional[int] = ..., min_k: _Optional[int] = ..., sim_options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., bsl_options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class StartSimilaritemsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartUserspecificRequest(_message.Message):
    __slots__ = ["data_dir", "k", "k_end", "k_start", "model", "verbose"]
    DATA_DIR_FIELD_NUMBER: _ClassVar[int]
    K_END_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    K_START_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    data_dir: str
    k: int
    k_end: int
    k_start: int
    model: ModelProperties
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data_dir: _Optional[str] = ..., verbose: bool = ..., k: _Optional[int] = ..., k_start: _Optional[int] = ..., k_end: _Optional[int] = ...) -> None: ...

class StartUserspecificResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserspecificItem(_message.Message):
    __slots__ = ["item_id", "movie_title", "rate"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    rate: int
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ..., rate: _Optional[int] = ...) -> None: ...

class UserspecificRequest(_message.Message):
    __slots__ = ["model", "n", "verbose"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    model: ModelProperties
    n: int
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ..., n: _Optional[int] = ...) -> None: ...

class UserspecificResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UserspecificItem]
    def __init__(self, items: _Optional[_Iterable[_Union[UserspecificItem, _Mapping]]] = ...) -> None: ...
