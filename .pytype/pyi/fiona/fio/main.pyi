# (generated with --quick)

import click
import fiona
import importlib.metadata
import itertools
import logging
import sys
from typing import Any, List, Type, overload

AWSSession: Type[fiona.session.AWSSession]
DummySession: Type[fiona.session.DummySession]
fio_version: str
main_group: Any
quiet_opt: Any
verbose_opt: Any
with_plugins: Any

def configure_logging(verbosity) -> None: ...
@overload
def entry_points() -> importlib.metadata.SelectableGroups: ...
@overload
def entry_points(*, name: str = ..., value: str = ..., group: str = ..., module: str = ..., attr: str = ..., extras: List[str] = ...) -> importlib.metadata.EntryPoints: ...
