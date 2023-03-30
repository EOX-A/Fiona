# (generated with --quick)

import fiona.collection
import fiona.errors
import logging
from typing import Any, Type, TypeVar

Collection: Type[fiona.collection.Collection]
DriverError: Type[fiona.errors.DriverError]
MemoryFileBase: Any
_listdir: Any
_listlayers: Any
log: logging.Logger
supports_vsi: Any

_TMemoryFile = TypeVar('_TMemoryFile', bound=MemoryFile)

class MemoryFile(Any):
    __doc__: str
    def __enter__(self: _TMemoryFile) -> _TMemoryFile: ...
    def __exit__(self, *args, **kwargs) -> None: ...
    def __init__(self, file_or_bytes = ..., filename = ..., ext = ...) -> None: ...
    def listdir(self, path = ...) -> Any: ...
    def listlayers(self, path = ...) -> Any: ...
    def open(self, mode = ..., driver = ..., schema = ..., crs = ..., encoding = ..., layer = ..., vfs = ..., enabled_drivers = ..., crs_wkt = ..., allow_unsupported_drivers = ..., **kwargs) -> fiona.collection.Collection: ...

class ZipMemoryFile(MemoryFile):
    __doc__: str
    name: str
    def __init__(self, file_or_bytes = ..., filename = ..., ext = ...) -> None: ...
    def open(self, path = ..., driver = ..., encoding = ..., layer = ..., enabled_drivers = ..., allow_unsupported_drivers = ..., **kwargs) -> fiona.collection.Collection: ...
