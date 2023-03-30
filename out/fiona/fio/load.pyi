from fiona.fio import options as options, with_context_env as with_context_env
from fiona.model import Feature as Feature, Geometry as Geometry
from fiona.schema import FIELD_TYPES_MAP_REV as FIELD_TYPES_MAP_REV
from fiona.transform import transform_geom as transform_geom

def load(ctx, output, driver, src_crs, dst_crs, features, layer, creation_options): ...
