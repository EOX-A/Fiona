from .helpers import eval_feature_expression as eval_feature_expression, obj_gen as obj_gen
from fiona.fio import with_context_env as with_context_env
from fiona.model import ObjectEncoder as ObjectEncoder

def calc(ctx, property_name, expression, overwrite, use_rs) -> None: ...
