# (generated with --quick)

import builtins
import enum
import fiona.errors
import itertools
import json.encoder
import typing
from typing import Annotated, Any, Dict, List, Optional, OrderedDict, Type, TypeVar, overload

Enum: Type[enum.Enum]
FionaDeprecationWarning: Type[fiona.errors.FionaDeprecationWarning]
GEOMETRY_TYPES: Dict[Any, str]
JSONEncoder: Type[json.encoder.JSONEncoder]
MutableMapping: type

_TFeature = TypeVar('_TFeature', bound=Feature)
_TGeometry = TypeVar('_TGeometry', bound=Geometry)
_TProperties = TypeVar('_TProperties', bound=Properties)

class Feature(Object):
    __doc__: str
    __geo_interface__: Annotated[Dict[str, Any], 'property']
    _data: OrderedDict[nothing, nothing]
    _delegate: _Feature
    _delegated_properties: List[str]
    geometry: Annotated[Any, 'property']
    id: Annotated[Any, 'property']
    properties: Annotated[Any, 'property']
    type: Annotated[str, 'property']
    def __eq__(self, other) -> Any: ...
    def __init__(self, geometry = ..., id = ..., properties = ..., **data) -> None: ...
    @classmethod
    def from_dict(cls: builtins.type[_TFeature], ob = ..., **kwargs) -> _TFeature: ...

class Geometry(Object):
    __doc__: str
    __geo_interface__: Annotated[Any, 'property']
    _data: OrderedDict[nothing, nothing]
    _delegate: _Geometry
    _delegated_properties: List[str]
    coordinates: Annotated[Any, 'property']
    geometries: Annotated[Any, 'property']
    type: Annotated[Any, 'property']
    def __init__(self, coordinates = ..., type = ..., geometries = ..., **data) -> None: ...
    @classmethod
    def from_dict(cls: builtins.type[_TGeometry], ob = ..., **kwargs) -> _TGeometry: ...

class OGRGeometryType(enum.Enum):
    CircularString: int
    CircularStringM: int
    CircularStringZ: int
    CircularStringZM: int
    CompoundCurve: int
    CompoundCurveM: int
    CompoundCurveZ: int
    CompoundCurveZM: int
    Curve: int
    CurveM: int
    CurvePolygon: int
    CurvePolygonM: int
    CurvePolygonZ: int
    CurvePolygonZM: int
    CurveZ: int
    CurveZM: int
    GeometryCollection: int
    GeometryCollection25D: int
    GeometryCollectionM: int
    GeometryCollectionZM: int
    LineString: int
    LineString25D: int
    LineStringM: int
    LineStringZM: int
    LinearRing: int
    MultiCurve: int
    MultiCurveM: int
    MultiCurveZ: int
    MultiCurveZM: int
    MultiLineString: int
    MultiLineString25D: int
    MultiLineStringM: int
    MultiLineStringZM: int
    MultiPoint: int
    MultiPoint25D: int
    MultiPointM: int
    MultiPointZM: int
    MultiPolygon: int
    MultiPolygon25D: int
    MultiPolygonM: int
    MultiPolygonZM: int
    MultiSurface: int
    MultiSurfaceM: int
    MultiSurfaceZ: int
    MultiSurfaceZM: int
    NONE: int
    Point: int
    Point25D: int
    PointM: int
    PointZM: int
    Polygon: int
    Polygon25D: int
    PolygonM: int
    PolygonZM: int
    PolyhedralSurface: int
    PolyhedralSurfaceM: int
    PolyhedralSurfaceZ: int
    PolyhedralSurfaceZM: int
    Surface: int
    SurfaceM: int
    SurfaceZ: int
    SurfaceZM: int
    TIN: int
    TINM: int
    TINZ: int
    TINZM: int
    Triangle: int
    TriangleM: int
    TriangleZ: int
    TriangleZM: int
    Unknown: int

class Object(typing.MutableMapping):
    __doc__: str
    _data: OrderedDict
    _delegated_properties: List[nothing]
    def __delitem__(self, key) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __getitem__(self, item) -> Any: ...
    def __init__(self, **kwds) -> None: ...
    def __iter__(self) -> itertools.chain: ...
    def __len__(self) -> int: ...
    def __setitem__(self, key, value) -> None: ...
    def _props(self) -> Dict[nothing, Any]: ...

class ObjectEncoder(json.encoder.JSONEncoder):
    __doc__: str
    def default(self, o) -> Any: ...

class Properties(Object):
    __doc__: str
    _data: OrderedDict[nothing, nothing]
    def __init__(self, **kwds) -> None: ...
    @classmethod
    def from_dict(cls: Type[_TProperties], mapping = ..., **kwargs) -> _TProperties: ...

class _Feature:
    geometry: Any
    id: Any
    properties: Any
    def __init__(self, geometry = ..., id = ..., properties = ...) -> None: ...

class _Geometry:
    coordinates: Any
    geometries: Any
    type: Any
    def __init__(self, coordinates = ..., type = ..., geometries = ...) -> None: ...

def decode_object(obj) -> Any: ...
def to_dict(val) -> Any: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
