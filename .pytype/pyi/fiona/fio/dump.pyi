# (generated with --quick)

import click
import cligj
import fiona
import functools
import json
import logging
from fiona.fio import helpers
from fiona.fio import options
from typing import Any, Callable, Type

Feature: Type[fiona.model.Feature]
ObjectEncoder: Type[fiona.model.ObjectEncoder]
dump: Any
partial: Type[functools.partial]

def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting = ..., antimeridian_offset = ..., precision = ...) -> Any: ...
def with_context_env(f) -> Callable: ...
