from _typeshed import Incomplete

SCHEMES: Incomplete
CURLSCHEMES: Incomplete
REMOTESCHEMES: Incomplete

def valid_vsi(vsi): ...
def is_remote(scheme): ...
def vsi_path(path, vsi: Incomplete | None = ..., archive: Incomplete | None = ...): ...
def parse_paths(uri, vfs: Incomplete | None = ...): ...
