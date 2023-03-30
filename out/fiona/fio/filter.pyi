from _typeshed import Incomplete
from fiona.fio import with_context_env as with_context_env
from fiona.fio.helpers import eval_feature_expression as eval_feature_expression, obj_gen as obj_gen

logger: Incomplete

def filter(ctx, filter_expression, use_rs) -> None: ...
