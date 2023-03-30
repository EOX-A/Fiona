from _typeshed import Incomplete
from collections.abc import MutableMapping
from enum import Enum
from fiona.errors import FionaDeprecationWarning as FionaDeprecationWarning
from json import JSONEncoder

class OGRGeometryType(Enum):
    Unknown: int
    Point: int
    LineString: int
    Polygon: int
    MultiPoint: int
    MultiLineString: int
    MultiPolygon: int
    GeometryCollection: int
    CircularString: int
    CompoundCurve: int
    CurvePolygon: int
    MultiCurve: int
    MultiSurface: int
    Curve: int
    Surface: int
    PolyhedralSurface: int
    TIN: int
    Triangle: int
    NONE: int
    LinearRing: int
    CircularStringZ: int
    CompoundCurveZ: int
    CurvePolygonZ: int
    MultiCurveZ: int
    MultiSurfaceZ: int
    CurveZ: int
    SurfaceZ: int
    PolyhedralSurfaceZ: int
    TINZ: int
    TriangleZ: int
    PointM: int
    LineStringM: int
    PolygonM: int
    MultiPointM: int
    MultiLineStringM: int
    MultiPolygonM: int
    GeometryCollectionM: int
    CircularStringM: int
    CompoundCurveM: int
    CurvePolygonM: int
    MultiCurveM: int
    MultiSurfaceM: int
    CurveM: int
    SurfaceM: int
    PolyhedralSurfaceM: int
    TINM: int
    TriangleM: int
    PointZM: int
    LineStringZM: int
    PolygonZM: int
    MultiPointZM: int
    MultiLineStringZM: int
    MultiPolygonZM: int
    GeometryCollectionZM: int
    CircularStringZM: int
    CompoundCurveZM: int
    CurvePolygonZM: int
    MultiCurveZM: int
    MultiSurfaceZM: int
    CurveZM: int
    SurfaceZM: int
    PolyhedralSurfaceZM: int
    TINZM: int
    TriangleZM: int
    Point25D: int
    LineString25D: int
    Polygon25D: int
    MultiPoint25D: int
    MultiLineString25D: int
    MultiPolygon25D: int
    GeometryCollection25D: int

GEOMETRY_TYPES: Incomplete

class Object(MutableMapping):
    def __init__(self, **kwds) -> None: ...
    def __getitem__(self, item): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __eq__(self, other): ...

class _Geometry:
    coordinates: Incomplete
    type: Incomplete
    geometries: Incomplete
    def __init__(self, coordinates: Incomplete | None = ..., type: Incomplete | None = ..., geometries: Incomplete | None = ...) -> None: ...

class Geometry(Object):
    def __init__(self, coordinates: Incomplete | None = ..., type: Incomplete | None = ..., geometries: Incomplete | None = ..., **data) -> None: ...
    @classmethod
    def from_dict(cls, ob: Incomplete | None = ..., **kwargs): ...
    @property
    def coordinates(self): ...
    @property
    def type(self): ...
    @property
    def geometries(self): ...
    @property
    def __geo_interface__(self): ...

class _Feature:
    geometry: Incomplete
    id: Incomplete
    properties: Incomplete
    def __init__(self, geometry: Incomplete | None = ..., id: Incomplete | None = ..., properties: Incomplete | None = ...) -> None: ...

class Feature(Object):
    def __init__(self, geometry: Incomplete | None = ..., id: Incomplete | None = ..., properties: Incomplete | None = ..., **data) -> None: ...
    @classmethod
    def from_dict(cls, ob: Incomplete | None = ..., **kwargs): ...
    def __eq__(self, other): ...
    @property
    def geometry(self): ...
    @property
    def id(self): ...
    @property
    def properties(self): ...
    @property
    def type(self): ...
    @property
    def __geo_interface__(self): ...

class Properties(Object):
    def __init__(self, **kwds) -> None: ...
    @classmethod
    def from_dict(cls, mapping: Incomplete | None = ..., **kwargs): ...

class ObjectEncoder(JSONEncoder):
    def default(self, o): ...

def decode_object(obj): ...
def to_dict(val): ...
