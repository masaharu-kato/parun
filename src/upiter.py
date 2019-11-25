import functools
import itertools
from typing import Any, Callable, Dict, Iterable, Iterator, Union

def union_product(vals) -> Union[Iterable, Dict]:

    if isinstance(vals, Dict):
        return (dict(zip(vals.keys(), union_product(vals.values()))), )

    if is_iterable(vals):
        return itertools.chain(*(product_union(v) for v in vals))
            
    return (vals,)


def product_union(vals) -> Union[Iterable, dict]:

    if isinstance(vals, dict):
        return (dict(zip(vals.keys(), res)) for res in product_union(vals.values()))

    if is_iterable(vals):
        return itertools.product(*(union_product(v) for v in vals))

    return (vals,)


def is_iterable(v) -> bool:
    return isinstance(v, Iterable) and not isinstance(v, (str, bytes))


def as_iterable(v) -> Iterable:
    if v is None: return tuple()
    if not is_iterable(v): return (v,)
    return v


def any_map(func:Callable[[Any], Any], v):

    _any_map = lambda v: any_map(func, v)
    
    if isinstance(v, dict):
        return dict(zip(v.keys(), _any_map(v.values())))

    if isinstance(v, list):
        return [*map(lambda v: _any_map(v), v)]

    if is_iterable(v):
        return (*map(lambda v: _any_map(v), v),)

    return func(v)


def dict_union(dicts:Iterable[dict]) -> dict:
    return functools.reduce(merge_dicts, dicts)


def merge_dicts(d1:dict, d2:dict) -> dict:
    return {**d1, **d2}
#   return {k: merge_dict_values(d1, k, d2, k) for k in dict.fromkeys([*d1.keys(), *d2.keys()])}


# def merge_dict_values(d1:dict, key1, d2:dict, key2):
#     """
#     merge values (in dictionary)
#     At least one of keys (key1, key2) must be existed in dictionary.
#     If only one of keys exists, return its value as it is.
#     If the value of key1 is iterable, return its value merged the value of key2.
#     If the value of key1 is not iterable, return only key2 as it is.
#     """

#     if not key1 in d1:
#         if not key2 in d2:
#             raise RuntimeError('Both keys do not exist in target dictionary.')
#         return d2[key2]
#     if not key2 in d2:
#         return d1[key1]

#     val1 = d1[key1]
#     val2 = d2[key2]
#     if is_iterable(val1):
#         if is_iterable(val2):
#             return (*val1, *val2)
#         return (*val1, val2)
#     return val2
