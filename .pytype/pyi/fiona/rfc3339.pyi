# (generated with --quick)

import logging
import re
from typing import Any, Optional, Tuple, Union

log: logging.Logger
pattern_date: re.Pattern[str]
pattern_datetime: re.Pattern[str]
pattern_time: re.Pattern[str]

class FionaDateTimeType(str):
    __doc__: str

class FionaDateType(str):
    __doc__: str

class FionaTimeType(str):
    __doc__: str

class group_accessor:
    match: Any
    def __init__(self, m) -> None: ...
    def group(self, i) -> Any: ...

def parse_date(text) -> Tuple[int, int, int, int, int, int, int, None]: ...
def parse_datetime(text) -> Tuple[int, int, int, int, int, int, int, Optional[Union[float, int]]]: ...
def parse_time(text) -> Tuple[int, int, int, int, int, int, int, Optional[Union[float, int]]]: ...
