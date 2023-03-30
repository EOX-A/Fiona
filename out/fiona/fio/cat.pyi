from fiona.errors import AttributeFilterError as AttributeFilterError
from fiona.fio import options as options, with_context_env as with_context_env
from fiona.fio.helpers import recursive_round as recursive_round
from fiona.model import Feature as Feature, ObjectEncoder as ObjectEncoder
from fiona.transform import transform_geom as transform_geom

def cat(ctx, files, precision, indent, compact, ignore_errors, dst_crs, use_rs, bbox, where, cut_at_antimeridian, layer, open_options) -> None: ...
