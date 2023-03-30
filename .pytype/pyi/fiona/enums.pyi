# (generated with --quick)

import enum
from typing import Any, Type

Enum: Type[enum.Enum]

class WktVersion(enum.Enum):
    WKT1: str
    WKT1_ESRI: str
    WKT1_GDAL: str
    WKT2: str
    WKT2_2015: str
    WKT2_2019: str
    __doc__: str
    @classmethod
    def _missing_(cls, value) -> Any: ...
