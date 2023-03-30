from fiona.fio import helpers as helpers, options as options, with_context_env as with_context_env
from fiona.model import Geometry as Geometry, ObjectEncoder as ObjectEncoder
from fiona.transform import transform_geom as transform_geom

def collect(ctx, precision, indent, compact, record_buffered, ignore_errors, src_crs, with_ld_context, add_ld_context_item, parse): ...
