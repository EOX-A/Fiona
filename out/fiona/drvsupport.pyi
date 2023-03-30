from _typeshed import Incomplete
from fiona._env import get_gdal_version_tuple as get_gdal_version_tuple
from fiona.env import Env as Env

supported_drivers: Incomplete
driver_mode_mingdal: Incomplete

def vector_driver_extensions(): ...
def driver_from_extension(path): ...
