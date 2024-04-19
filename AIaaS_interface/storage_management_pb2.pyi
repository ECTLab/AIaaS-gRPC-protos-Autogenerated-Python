from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrowseDataRequest(_message.Message):
    __slots__ = ["path", "username"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class BrowseDataResponse(_message.Message):
    __slots__ = ["contents"]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contents: _Optional[_Iterable[str]] = ...) -> None: ...

class CopyRequest(_message.Message):
    __slots__ = ["destination_path", "source_path", "username"]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    destination_path: str
    source_path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., source_path: _Optional[str] = ..., destination_path: _Optional[str] = ...) -> None: ...

class CopyResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateFolderRequest(_message.Message):
    __slots__ = ["folder_name", "path", "username"]
    FOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    folder_name: str
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., folder_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CreateFolderResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CutRequest(_message.Message):
    __slots__ = ["destination_path", "source_path", "username"]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    destination_path: str
    source_path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., source_path: _Optional[str] = ..., destination_path: _Optional[str] = ...) -> None: ...

class CutResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeregisterUserRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class DeregisterUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DownloadFileRequest(_message.Message):
    __slots__ = ["path", "username"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class DownloadFileResponse(_message.Message):
    __slots__ = ["chunk_data"]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    chunk_data: bytes
    def __init__(self, chunk_data: _Optional[bytes] = ...) -> None: ...

class EmptyRecycleBinRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class EmptyRecycleBinResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ForceRemoveRequest(_message.Message):
    __slots__ = ["path", "username"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class ForceRemoveResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSystemicReportRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSystemicReportResponse(_message.Message):
    __slots__ = ["number_of_users", "over_subscription_rate", "total_volume", "volume_report"]
    NUMBER_OF_USERS_FIELD_NUMBER: _ClassVar[int]
    OVER_SUBSCRIPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_REPORT_FIELD_NUMBER: _ClassVar[int]
    number_of_users: int
    over_subscription_rate: float
    total_volume: int
    volume_report: VolumeReport
    def __init__(self, total_volume: _Optional[int] = ..., over_subscription_rate: _Optional[float] = ..., number_of_users: _Optional[int] = ..., volume_report: _Optional[_Union[VolumeReport, _Mapping]] = ...) -> None: ...

class GetVolumeRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class GetVolumeResponse(_message.Message):
    __slots__ = ["volume_report"]
    VOLUME_REPORT_FIELD_NUMBER: _ClassVar[int]
    volume_report: VolumeReport
    def __init__(self, volume_report: _Optional[_Union[VolumeReport, _Mapping]] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ["extension", "filename", "path", "username"]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    extension: str
    filename: str
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., path: _Optional[str] = ..., filename: _Optional[str] = ..., extension: _Optional[str] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ["initial_volume", "username"]
    INITIAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    initial_volume: int
    username: str
    def __init__(self, username: _Optional[str] = ..., initial_volume: _Optional[int] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveRequest(_message.Message):
    __slots__ = ["path", "username"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    username: str
    def __init__(self, username: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class RemoveResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ["content", "username"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    content: str
    username: str
    def __init__(self, username: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ["content_type", "path"]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    path: str
    def __init__(self, path: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...

class SetSystemVolumeRequest(_message.Message):
    __slots__ = ["over_subscription_rate", "total_volume"]
    OVER_SUBSCRIPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    over_subscription_rate: float
    total_volume: int
    def __init__(self, total_volume: _Optional[int] = ..., over_subscription_rate: _Optional[float] = ...) -> None: ...

class SetSystemVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetVolumeRequest(_message.Message):
    __slots__ = ["new_volume", "username"]
    NEW_VOLUME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    new_volume: int
    username: str
    def __init__(self, username: _Optional[str] = ..., new_volume: _Optional[int] = ...) -> None: ...

class SetVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ["chunk_data", "metadata"]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    chunk_data: bytes
    metadata: MetaData
    def __init__(self, metadata: _Optional[_Union[MetaData, _Mapping]] = ..., chunk_data: _Optional[bytes] = ...) -> None: ...

class UploadFileResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VolumeReport(_message.Message):
    __slots__ = ["remaining_volume", "total_allocated_volume", "total_used_volume"]
    REMAINING_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ALLOCATED_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_USED_VOLUME_FIELD_NUMBER: _ClassVar[int]
    remaining_volume: int
    total_allocated_volume: int
    total_used_volume: int
    def __init__(self, total_allocated_volume: _Optional[int] = ..., total_used_volume: _Optional[int] = ..., remaining_volume: _Optional[int] = ...) -> None: ...
