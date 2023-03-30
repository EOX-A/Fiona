from _typeshed import Incomplete
from fiona import compat as compat, vfs as vfs
from fiona._env import get_gdal_release_name as get_gdal_release_name, get_gdal_version_tuple as get_gdal_version_tuple
from fiona.crs import CRS as CRS
from fiona.drvsupport import driver_from_extension as driver_from_extension, driver_mode_mingdal as driver_mode_mingdal, supported_drivers as supported_drivers
from fiona.env import env_ctx_if_needed as env_ctx_if_needed
from fiona.errors import DriverError as DriverError, DriverSupportError as DriverSupportError, FionaDeprecationWarning as FionaDeprecationWarning, GDALVersionError as GDALVersionError, SchemaError as SchemaError, UnsupportedGeometryTypeError as UnsupportedGeometryTypeError, UnsupportedOperation as UnsupportedOperation
from fiona.logutils import FieldSkipLogFilter as FieldSkipLogFilter
from fiona.ogrext import GEOMETRY_TYPES as GEOMETRY_TYPES, ItemsIterator as ItemsIterator, Iterator as Iterator, KeysIterator as KeysIterator, Session as Session, WritingSession as WritingSession, buffer_to_virtual_file as buffer_to_virtual_file, remove_virtual_file as remove_virtual_file
from fiona.path import Path as Path, parse_path as parse_path, vsi_path as vsi_path

log: Incomplete

class Collection:
    session: Incomplete
    iterator: Incomplete
    enabled_drivers: Incomplete
    include_fields: Incomplete
    ignore_fields: Incomplete
    ignore_geometry: Incomplete
    path: Incomplete
    name: str
    mode: Incomplete
    encoding: Incomplete
    field_skip_log_filter: Incomplete
    def __init__(self, path, mode: str = ..., driver: Incomplete | None = ..., schema: Incomplete | None = ..., crs: Incomplete | None = ..., encoding: Incomplete | None = ..., layer: Incomplete | None = ..., vsi: Incomplete | None = ..., archive: Incomplete | None = ..., enabled_drivers: Incomplete | None = ..., crs_wkt: Incomplete | None = ..., ignore_fields: Incomplete | None = ..., ignore_geometry: bool = ..., include_fields: Incomplete | None = ..., wkt_version: Incomplete | None = ..., allow_unsupported_drivers: bool = ..., **kwargs) -> None: ...
    def guard_driver_mode(self) -> None: ...
    @property
    def driver(self): ...
    @property
    def schema(self): ...
    @property
    def crs(self): ...
    @property
    def crs_wkt(self): ...
    def tags(self, ns: Incomplete | None = ...): ...
    def get_tag_item(self, key, ns: Incomplete | None = ...): ...
    def update_tags(self, tags, ns: Incomplete | None = ...): ...
    def update_tag_item(self, key, tag, ns: Incomplete | None = ...): ...
    @property
    def meta(self): ...
    profile = meta
    def filter(self, *args, **kwds): ...
    def items(self, *args, **kwds): ...
    def keys(self, *args, **kwds): ...
    def __contains__(self, fid) -> bool: ...
    values = filter
    def __iter__(self): ...
    def __next__(self): ...
    next = __next__
    def __getitem__(self, item): ...
    def get(self, item): ...
    def writerecords(self, records) -> None: ...
    def write(self, record) -> None: ...
    def validate_record(self, record): ...
    def validate_record_geometry(self, record): ...
    def __len__(self) -> int: ...
    @property
    def bounds(self): ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    @property
    def closed(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    def __del__(self) -> None: ...

ALL_GEOMETRY_TYPES: Incomplete

def get_filetype(bytesbuf): ...

class BytesCollection(Collection):
    bytesbuf: Incomplete
    virtual_file: Incomplete
    def __init__(self, bytesbuf, **kwds) -> None: ...
    def close(self) -> None: ...
