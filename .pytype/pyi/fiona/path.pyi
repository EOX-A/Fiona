# (generated with --quick)

import attr
import re
import sys
import urllib.parse
from typing import Annotated, Any, Dict, Literal, Optional, Set, Tuple, Type, TypeVar, Union, overload

CURLSCHEMES: Set[str]
REMOTESCHEMES: Set[str]
SCHEMES: Dict[str, str]

_T0 = TypeVar('_T0')
_TParsedPath = TypeVar('_TParsedPath', bound=ParsedPath)

@attr.s
class ParsedPath(Path):
    path: Any
    archive: Any
    scheme: Any
    __attrs_attrs__: Tuple[attr.Attribute, ...]
    __doc__: str
    name: Annotated[Any, 'property']
    is_remote: Annotated[Any, 'property']
    is_local: Annotated[Any, 'property']
    def __init__(self, path, archive, scheme) -> None: ...
    @classmethod
    def from_uri(cls: Type[_TParsedPath], uri) -> _TParsedPath: ...

class Path:
    __doc__: str

@attr.s
class UnparsedPath(Path):
    path: Any
    __attrs_attrs__: Tuple[attr.Attribute, ...]
    __doc__: str
    name: Annotated[Any, 'property']
    def __init__(self, path) -> None: ...

def parse_path(path: _T0) -> Union[ParsedPath, UnparsedPath, _T0]: ...
@overload
def urlparse(url: str, scheme: str = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: bytes, scheme: Optional[bytes], allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
@overload
def urlparse(url: None, scheme: Optional[Union[bytes, Literal['']]] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
def vsi_path(path) -> Any: ...
