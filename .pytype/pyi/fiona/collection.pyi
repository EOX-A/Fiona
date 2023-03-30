# (generated with --quick)

import contextlib
import fiona.env
import fiona.errors
import fiona.logutils
import fiona.path
import logging
import os
import typing
import warnings
from fiona import compat
from fiona import vfs
from typing import Annotated, Any, Dict, Optional, OrderedDict, Tuple, Type, TypeVar, Union, overload

ALL_GEOMETRY_TYPES: set
CRS: Any
DriverError: Type[fiona.errors.DriverError]
DriverSupportError: Type[fiona.errors.DriverSupportError]
ExitStack: Type[contextlib.ExitStack]
FieldSkipLogFilter: Type[fiona.logutils.FieldSkipLogFilter]
FionaDeprecationWarning: Type[fiona.errors.FionaDeprecationWarning]
GDALVersionError: Type[fiona.errors.GDALVersionError]
GEOMETRY_TYPES: Any
ItemsIterator: Any
Iterator: Any
KeysIterator: Any
Path: Type[fiona.path.Path]
SchemaError: Type[fiona.errors.SchemaError]
Session: Any
UnsupportedGeometryTypeError: Type[fiona.errors.UnsupportedGeometryTypeError]
UnsupportedOperation: Type[fiona.errors.UnsupportedOperation]
WritingSession: Any
_GDAL_RELEASE_NAME: Any
_GDAL_VERSION_TUPLE: Any
buffer_to_virtual_file: Any
driver_mode_mingdal: Dict[str, Dict[str, Tuple[int, int, int]]]
get_gdal_release_name: Any
get_gdal_version_tuple: Any
log: logging.Logger
remove_virtual_file: Any
supported_drivers: Dict[str, str]

_T0 = TypeVar('_T0')
_TCollection = TypeVar('_TCollection', bound=Collection)

class BytesCollection(Collection):
    __doc__: str
    _allow_unsupported_drivers: bool
    _bounds: None
    _closed: bool
    _crs: None
    _crs_wkt: None
    _driver: None
    _env: Optional[contextlib.ExitStack]
    _len: int
    _schema: None
    _valid_geom_types: Any
    bytesbuf: Any
    enabled_drivers: None
    encoding: None
    field_skip_log_filter: fiona.logutils.FieldSkipLogFilter
    ignore_fields: None
    ignore_geometry: bool
    include_fields: None
    iterator: None
    mode: str
    name: Any
    path: Any
    session: Any
    virtual_file: Any
    def __init__(self, bytesbuf, **kwds) -> None: ...
    def __repr__(self) -> str: ...
    def close(self) -> None: ...

class Collection:
    __doc__: str
    _allow_unsupported_drivers: Any
    _bounds: Any
    _closed: bool
    _crs: Any
    _crs_wkt: Any
    _driver: Any
    _env: Optional[contextlib.ExitStack]
    _len: Any
    _schema: Any
    _valid_geom_types: set
    bounds: Annotated[Any, 'property']
    closed: Annotated[bool, 'property']
    crs: Annotated[Any, 'property']
    crs_wkt: Annotated[Any, 'property']
    driver: Annotated[Any, 'property']
    enabled_drivers: Any
    encoding: Any
    field_skip_log_filter: fiona.logutils.FieldSkipLogFilter
    ignore_fields: Any
    ignore_geometry: bool
    include_fields: Any
    iterator: Any
    meta: Annotated[Dict[str, Any], 'property']
    mode: Any
    name: Any
    path: Any
    profile: Annotated[Dict[str, Any], 'property']
    schema: Annotated[Any, 'property']
    session: Any
    def __contains__(self, fid) -> Any: ...
    def __del__(self) -> None: ...
    def __enter__(self: _TCollection) -> _TCollection: ...
    @overload
    def __exit__(self, type: Type[BaseException], value: BaseException, traceback) -> None: ...
    @overload
    def __exit__(self, type: None, value: BaseException, traceback) -> None: ...
    @overload
    def __exit__(self, type: Type[BaseException], value: None, traceback) -> None: ...
    @overload
    def __exit__(self, type: None, value: None, traceback) -> None: ...
    @overload
    def __exit__(self, type: Type[BaseException], value: BaseException, traceback: None) -> None: ...
    @overload
    def __exit__(self, type: None, value: BaseException, traceback: None) -> None: ...
    @overload
    def __exit__(self, type: Type[BaseException], value: None, traceback: None) -> None: ...
    @overload
    def __exit__(self, type: None, value: None, traceback: None) -> None: ...
    def __getitem__(self, item) -> Any: ...
    def __init__(self, path, mode = ..., driver = ..., schema = ..., crs = ..., encoding = ..., layer = ..., vsi = ..., archive = ..., enabled_drivers = ..., crs_wkt = ..., ignore_fields = ..., ignore_geometry = ..., include_fields = ..., wkt_version = ..., allow_unsupported_drivers = ..., **kwargs) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __repr__(self) -> str: ...
    def _check_schema_driver_support(self) -> None: ...
    def close(self) -> None: ...
    def filter(self, *args, **kwds) -> Any: ...
    def flush(self) -> None: ...
    def get(self, item) -> Any: ...
    def get_tag_item(self, key, ns = ...) -> Any: ...
    def guard_driver_mode(self) -> None: ...
    def items(self, *args, **kwds) -> Any: ...
    def keys(self, *args, **kwds) -> Any: ...
    def next(self) -> Any: ...
    def tags(self, ns = ...) -> Any: ...
    def update_tag_item(self, key, tag, ns = ...) -> Any: ...
    def update_tags(self, tags, ns = ...) -> Any: ...
    def validate_record(self, record) -> Any: ...
    def validate_record_geometry(self, record) -> Any: ...
    def values(self, *args, **kwds) -> Any: ...
    def write(self, record) -> None: ...
    def writerecords(self, records) -> None: ...

def _driver_converts_field_type_silently_to_str(driver, field_type) -> bool: ...
def _driver_supports_field(driver, field_type) -> bool: ...
def _get_valid_geom_types(schema, driver) -> set: ...
def driver_from_extension(path) -> str: ...
def env_ctx_if_needed() -> Union[fiona.env.Env, fiona.env.NullContextManager]: ...
def get_filetype(bytesbuf) -> str: ...
def parse_path(path: _T0) -> Union[fiona.path.ParsedPath, fiona.path.UnparsedPath, _T0]: ...
def vsi_path(path) -> Any: ...
