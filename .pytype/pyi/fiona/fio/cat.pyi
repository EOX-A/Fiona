# (generated with --quick)

import click
import cligj
import fiona
import json
import warnings
from fiona.fio import options
from typing import Any, Callable, Type, TypeVar, Union

AttributeFilterError: Type[fiona.errors.AttributeFilterError]
Feature: Type[fiona.model.Feature]
ObjectEncoder: Type[fiona.model.ObjectEncoder]
cat: Any

_T0 = TypeVar('_T0')

def recursive_round(obj: _T0, precision) -> Union[float, list, fiona.model.Geometry, _T0]: ...
def transform_geom(src_crs, dst_crs, geom, antimeridian_cutting = ..., antimeridian_offset = ..., precision = ...) -> Any: ...
def with_context_env(f) -> Callable: ...
