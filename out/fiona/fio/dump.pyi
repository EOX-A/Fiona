from fiona.fio import helpers as helpers, options as options, with_context_env as with_context_env
from fiona.model import Feature as Feature, ObjectEncoder as ObjectEncoder
from fiona.transform import transform_geom as transform_geom

def dump(ctx, input, encoding, precision, indent, compact, record_buffered, ignore_errors, with_ld_context, add_ld_context_item, layer, open_options): ...
