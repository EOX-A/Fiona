# (generated with --quick)

import fiona.collection
import fiona.env
import fiona.errors
import fiona.io
import fiona.model
import fiona.path
import glob
import logging
import os
import platform
import uuid
import warnings
from fiona import rfc3339
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union

BytesCollection: Type[fiona.collection.BytesCollection]
Collection: Type[fiona.collection.Collection]
Env: Type[fiona.env.Env]
FIELD_TYPES_MAP: Any
Feature: Type[fiona.model.Feature]
FionaDeprecationWarning: Type[fiona.errors.FionaDeprecationWarning]
Geometry: Type[fiona.model.Geometry]
MemoryFile: Type[fiona.io.MemoryFile]
ParsedPath: Type[fiona.path.ParsedPath]
Path: type
Properties: Type[fiona.model.Properties]
__all__: List[str]
__gdal_version__: Any
__version__: str
_bounds: Any
_err: Any
_geometry: Any
_listdir: Any
_listlayers: Any
_remove: Any
_remove_layer: Any
_whl_dir: str
calc_gdal_version_num: Any
collection: Callable
driver_count: Any
gdal_version: Any
get_gdal_release_name: Any
get_gdal_version_num: Any
get_gdal_version_tuple: Any
listlayers: Callable
log: logging.Logger
open: Callable
p: str
supported_drivers: Dict[str, str]

_T0 = TypeVar('_T0')

def bounds(ob) -> Any: ...
def drivers(*args, **kwargs) -> fiona.env.Env: ...
def ensure_env_with_credentials(f) -> Callable: ...
def listdir(path) -> Any: ...
def parse_path(path: _T0) -> Union[fiona.path.ParsedPath, fiona.path.UnparsedPath, _T0]: ...
def prop_type(text) -> Any: ...
def prop_width(val) -> Optional[int]: ...
def remove(path_or_collection, driver = ..., layer = ...) -> None: ...
def show_versions() -> None: ...
def vfs_parse_paths(uri, vfs = ...) -> Tuple[Any, Any, Any]: ...
def vsi_path(path) -> Any: ...
