# (generated with --quick)

import logging
from typing import Any, Callable, Dict
from xml.etree import ElementTree as ET

_get_metadata_item: Any
dataset_creation_options: Any
dataset_open_options: Any
extensions: Any
layer_creation_options: Any
log: logging.Logger
print_driver_options: Any
supported_field_types: Any
supported_sub_field_types: Any
supports_vsi: Any

class MetadataItem:
    CREATE: str
    CREATION_FIELD_DATA_SUB_TYPES: str
    CREATION_FIELD_DATA_TYPES: str
    CREATION_OPTION_LIST: str
    DATASET_OPEN_OPTIONS: str
    DEFAULT_FIELDS: str
    EXTENSION: str
    EXTENSIONS: str
    LAYER_CREATION_OPTION_LIST: str
    NOT_NULL_FIELDS: str
    NOT_NULL_GEOMETRY_FIELDS: str
    OPEN: str
    UNIQUE_FIELDS: str
    VIRTUAL_IO: str

def _parse_options(xml) -> Dict[str, dict]: ...
def extension(driver) -> Any: ...
def require_gdal_version(version, param = ..., values = ..., is_max_version = ..., reason = ...) -> Callable[[Any], Any]: ...
