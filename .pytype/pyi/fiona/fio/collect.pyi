# (generated with --quick)

import click
import cligj
import fiona.model
import functools
import json
import logging
from fiona.fio import helpers
from fiona.fio import options
from typing import Any, Callable, Type

Geometry: Type[fiona.model.Geometry]
ObjectEncoder: Type[fiona.model.ObjectEncoder]
collect: Any
partial: Type[functools.partial]

def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting = ..., antimeridian_offset = ..., precision = ...) -> Any: ...
def with_context_env(f) -> Callable: ...
