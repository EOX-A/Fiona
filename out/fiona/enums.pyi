from enum import Enum

class WktVersion(Enum):
    WKT2_2015: str
    WKT2: str
    WKT2_2019: str
    WKT1_GDAL: str
    WKT1: str
    WKT1_ESRI: str
