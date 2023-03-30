# (generated with --quick)

import click
import collections
from typing import Any, Type, TypeVar, Union

creation_opt: Any
defaultdict: Type[collections.defaultdict]
dst_crs_opt: Any
open_opt: Any
src_crs_opt: Any

_T2 = TypeVar('_T2')

def cb_key_val(ctx, param, value) -> dict: ...
def cb_layer(ctx, param, value: _T2) -> Union[int, _T2]: ...
def cb_multilayer(ctx, param, value) -> collections.defaultdict: ...
def validate_multilayer_file_index(files, layerdict) -> None: ...
