# (generated with --quick)

import fiona.env
import os
from typing import Any, Dict, Optional, Tuple, Type

Env: Type[fiona.env.Env]
_GDAL_VERSION: Any
_driver_converts_to_str: Dict[str, Dict[str, Optional[Tuple[int, int, int]]]]
_driver_field_type_unsupported: Dict[str, Dict[str, Optional[Tuple[int, int, int]]]]
_drivers_not_supporting_milliseconds: Dict[str, None]
_drivers_not_supporting_timezones: Dict[str, Dict[str, Optional[Tuple[int, int, int]]]]
driver_mode_mingdal: Dict[str, Dict[str, Tuple[int, int, int]]]
get_gdal_version_tuple: Any
supported_drivers: Dict[str, str]

def _driver_converts_field_type_silently_to_str(driver, field_type) -> bool: ...
def _driver_supports_field(driver, field_type) -> bool: ...
def _driver_supports_milliseconds(driver) -> bool: ...
def _driver_supports_mode(driver, mode) -> bool: ...
def _driver_supports_timezones(driver, field_type) -> bool: ...
def _filter_supported_drivers() -> None: ...
def driver_from_extension(path) -> str: ...
def vector_driver_extensions() -> Dict[Any, str]: ...
