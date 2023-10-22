from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColdStartItem(_message.Message):
    __slots__ = ["item_id", "movie_title", "rate"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    rate: int
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ..., rate: _Optional[int] = ...) -> None: ...

class ColdStartRequest(_message.Message):
    __slots__ = ["model", "n", "verbose"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    model: ModelProperties
    n: int
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ..., n: _Optional[int] = ...) -> None: ...

class ColdStartResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ColdStartItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ColdStartItem, _Mapping]]] = ...) -> None: ...

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

class GetCounterRequest(_message.Message):
    __slots__ = ["model"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: ModelProperties
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ...) -> None: ...

class GetCounterResponse(_message.Message):
    __slots__ = ["counter"]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    counter: int
    def __init__(self, counter: _Optional[int] = ...) -> None: ...

class ModelProperties(_message.Message):
    __slots__ = ["model_name", "username"]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    username: str
    def __init__(self, username: _Optional[str] = ..., model_name: _Optional[str] = ...) -> None: ...

class SetCounterRequest(_message.Message):
    __slots__ = ["counter", "model"]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    counter: int
    model: ModelProperties
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., counter: _Optional[int] = ...) -> None: ...

class SetCounterResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SimilarItemsItem(_message.Message):
    __slots__ = ["item_id", "movie_title"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ...) -> None: ...

class SimilarItemsRequest(_message.Message):
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

class SimilarItemsResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SimilarItemsItem]
    def __init__(self, items: _Optional[_Iterable[_Union[SimilarItemsItem, _Mapping]]] = ...) -> None: ...

class StartColdStartRequest(_message.Message):
    __slots__ = ["data", "model", "verbose"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    data: dataProperties
    model: ModelProperties
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data: _Optional[_Union[dataProperties, _Mapping]] = ..., verbose: bool = ...) -> None: ...

class StartColdStartResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartSimilarItemsRequest(_message.Message):
    __slots__ = ["algo", "bsl_options", "data", "k", "min_k", "model", "n", "sim_options", "verbose"]
    ALGO_FIELD_NUMBER: _ClassVar[int]
    BSL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    MIN_K_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    SIM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    algo: str
    bsl_options: _struct_pb2.Struct
    data: dataProperties
    k: int
    min_k: int
    model: ModelProperties
    n: int
    sim_options: _struct_pb2.Struct
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data: _Optional[_Union[dataProperties, _Mapping]] = ..., verbose: bool = ..., algo: _Optional[str] = ..., k: _Optional[int] = ..., min_k: _Optional[int] = ..., sim_options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., bsl_options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., n: _Optional[int] = ...) -> None: ...

class StartSimilarItemsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartUserSpecificRequest(_message.Message):
    __slots__ = ["data", "k", "k_end", "k_start", "model", "verbose"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    K_END_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    K_START_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    data: dataProperties
    k: int
    k_end: int
    k_start: int
    model: ModelProperties
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., data: _Optional[_Union[dataProperties, _Mapping]] = ..., verbose: bool = ..., k: _Optional[int] = ..., k_start: _Optional[int] = ..., k_end: _Optional[int] = ...) -> None: ...

class StartUserSpecificResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserSpecificItem(_message.Message):
    __slots__ = ["item_id", "movie_title", "rate"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    movie_title: str
    rate: int
    def __init__(self, item_id: _Optional[int] = ..., movie_title: _Optional[str] = ..., rate: _Optional[int] = ...) -> None: ...

class UserSpecificRequest(_message.Message):
    __slots__ = ["dataset_userid", "model", "n", "verbose"]
    DATASET_USERID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    dataset_userid: int
    model: ModelProperties
    n: int
    verbose: bool
    def __init__(self, model: _Optional[_Union[ModelProperties, _Mapping]] = ..., verbose: bool = ..., dataset_userid: _Optional[int] = ..., n: _Optional[int] = ...) -> None: ...

class UserSpecificResponse(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[UserSpecificItem]
    def __init__(self, items: _Optional[_Iterable[_Union[UserSpecificItem, _Mapping]]] = ...) -> None: ...

class dataProperties(_message.Message):
    __slots__ = ["item_info_columns", "item_info_path", "item_sep", "user_info_columns", "user_info_path", "user_info_sep", "user_ratings_columns", "user_ratings_path", "user_ratings_sep"]
    ITEM_INFO_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ITEM_INFO_PATH_FIELD_NUMBER: _ClassVar[int]
    ITEM_SEP_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_SEP_FIELD_NUMBER: _ClassVar[int]
    USER_RATINGS_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    USER_RATINGS_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_RATINGS_SEP_FIELD_NUMBER: _ClassVar[int]
    item_info_columns: _containers.RepeatedScalarFieldContainer[str]
    item_info_path: str
    item_sep: str
    user_info_columns: _containers.RepeatedScalarFieldContainer[str]
    user_info_path: str
    user_info_sep: str
    user_ratings_columns: _containers.RepeatedScalarFieldContainer[str]
    user_ratings_path: str
    user_ratings_sep: str
    def __init__(self, user_info_path: _Optional[str] = ..., user_ratings_path: _Optional[str] = ..., item_info_path: _Optional[str] = ..., user_info_columns: _Optional[_Iterable[str]] = ..., user_ratings_columns: _Optional[_Iterable[str]] = ..., item_info_columns: _Optional[_Iterable[str]] = ..., user_info_sep: _Optional[str] = ..., user_ratings_sep: _Optional[str] = ..., item_sep: _Optional[str] = ...) -> None: ...
