# (generated with --quick)

import logging
from typing import Any

class FieldSkipLogFilter(logging.Filter):
    __doc__: str
    seen_msgs: set
    def __init__(self, name = ...) -> None: ...
    def filter(self, record) -> int: ...

class LogFiltering:
    filter: Any
    logger: Any
    def __enter__(self) -> None: ...
    def __exit__(self, *args, **kwargs) -> None: ...
    def __init__(self, logger, filter) -> None: ...
