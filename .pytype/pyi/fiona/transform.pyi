# (generated with --quick)

import fiona.errors
import fiona.model
from typing import Any, Optional, Tuple, Type, overload

DICT_TYPES: Tuple[Type[dict], Any, Any]
FionaDeprecationWarning: Type[fiona.errors.FionaDeprecationWarning]
Geometry: Type[fiona.model.Geometry]
_transform: Any
_transform_geom: Any

def decode_object(obj) -> Any: ...
def transform(src_crs, dst_crs, xs, ys) -> Any: ...
def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting = ..., antimeridian_offset = ..., precision = ...) -> Any: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
