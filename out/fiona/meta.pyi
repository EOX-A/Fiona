from _typeshed import Incomplete
from fiona.env import require_gdal_version as require_gdal_version

log: Incomplete

class MetadataItem:
    CREATION_FIELD_DATA_TYPES: str
    CREATION_FIELD_DATA_SUB_TYPES: str
    CREATION_OPTION_LIST: str
    LAYER_CREATION_OPTION_LIST: str
    DATASET_OPEN_OPTIONS: str
    EXTENSIONS: str
    EXTENSION: str
    VIRTUAL_IO: str
    NOT_NULL_FIELDS: str
    NOT_NULL_GEOMETRY_FIELDS: str
    UNIQUE_FIELDS: str
    DEFAULT_FIELDS: str
    OPEN: str
    CREATE: str

def dataset_creation_options(driver): ...
def layer_creation_options(driver): ...
def dataset_open_options(driver): ...
def print_driver_options(driver) -> None: ...
def extensions(driver): ...
def extension(driver): ...
def supports_vsi(driver): ...
def supported_field_types(driver): ...
def supported_sub_field_types(driver): ...
