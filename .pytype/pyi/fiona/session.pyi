# (generated with --quick)

import fiona.path
import logging
import os
from typing import Annotated, Any, Dict, Optional, Type, TypeVar, Union

UnparsedPath: Type[fiona.path.UnparsedPath]
boto3: Optional[module]
log: logging.Logger

_T0 = TypeVar('_T0')

class AWSSession(Session):
    __doc__: str
    _creds: Any
    _session: Any
    credentials: Annotated[Dict[str, Any], 'property']
    endpoint_url: Any
    requester_pays: Any
    unsigned: bool
    def __init__(self, session = ..., aws_unsigned = ..., aws_access_key_id = ..., aws_secret_access_key = ..., aws_session_token = ..., region_name = ..., profile_name = ..., endpoint_url = ..., requester_pays = ...) -> None: ...
    def get_credential_options(self) -> Dict[str, Any]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

class AzureSession(Session):
    __doc__: str
    _creds: Dict[str, Any]
    credentials: Annotated[Dict[str, Any], 'property']
    storage_account: Any
    unsigned: bool
    def __init__(self, azure_storage_connection_string = ..., azure_storage_account = ..., azure_storage_access_key = ..., azure_unsigned = ...) -> None: ...
    def get_credential_options(self) -> Dict[str, Any]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

class DummySession(Session):
    __doc__: str
    _session: None
    credentials: Dict[nothing, nothing]
    def __init__(self, *args, **kwargs) -> None: ...
    def get_credential_options(self) -> Dict[nothing, nothing]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

class GSSession(Session):
    __doc__: str
    _creds: Dict[str, Any]
    credentials: Annotated[Dict[str, Any], 'property']
    def __init__(self, google_application_credentials = ...) -> None: ...
    def get_credential_options(self) -> Dict[str, Any]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

class OSSSession(Session):
    __doc__: str
    _creds: Dict[str, Any]
    credentials: Annotated[Dict[str, Any], 'property']
    def __init__(self, oss_access_key_id = ..., oss_secret_access_key = ..., oss_endpoint = ...) -> None: ...
    def get_credential_options(self) -> Dict[str, Any]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

class Session:
    __doc__: str
    @staticmethod
    def aws_or_dummy(*args, **kwargs) -> Union[AWSSession, DummySession]: ...
    @staticmethod
    def cls_from_path(path) -> Type[Union[AWSSession, AzureSession, DummySession, OSSSession, SwiftSession]]: ...
    @staticmethod
    def from_environ(*args, **kwargs) -> Union[AWSSession, DummySession]: ...
    @staticmethod
    def from_foreign_session(session, cls = ...) -> Any: ...
    @staticmethod
    def from_path(path, *args, **kwargs) -> Union[AWSSession, AzureSession, DummySession, OSSSession, SwiftSession]: ...
    def get_credential_options(self) -> _NotImplementedType: ...
    @classmethod
    def hascreds(cls, config) -> _NotImplementedType: ...

class SwiftSession(Session):
    __doc__: str
    _creds: Dict[str, Any]
    _session: Any
    credentials: Annotated[Dict[str, Any], 'property']
    def __init__(self, session = ..., swift_storage_url = ..., swift_auth_token = ..., swift_auth_v1_url = ..., swift_user = ..., swift_key = ...) -> None: ...
    def get_credential_options(self) -> Dict[str, Any]: ...
    @classmethod
    def hascreds(cls, config) -> bool: ...

def parse_path(path: _T0) -> Union[fiona.path.ParsedPath, fiona.path.UnparsedPath, _T0]: ...
