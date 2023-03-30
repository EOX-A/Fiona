# (generated with --quick)

import click
import cligj
import fiona
import functools
from fiona.fio import options
from typing import Any, Callable, Type

FIELD_TYPES_MAP_REV: Any
Feature: Type[fiona.model.Feature]
Geometry: Type[fiona.model.Geometry]
load: Any
partial: Type[functools.partial]

def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting = ..., antimeridian_offset = ..., precision = ...) -> Any: ...
def with_context_env(f) -> Callable: ...
