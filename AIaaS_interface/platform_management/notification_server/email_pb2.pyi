from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendEmailRequest(_message.Message):
    __slots__ = ["body_text", "email", "subject"]
    BODY_TEXT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    body_text: str
    email: str
    subject: str
    def __init__(self, email: _Optional[str] = ..., subject: _Optional[str] = ..., body_text: _Optional[str] = ...) -> None: ...

class SendEmailResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
