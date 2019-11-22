import itertools
from typing import Dict, Iterable, Iterator, Union

def union_product(vals) -> Union[Iterable, Dict]:
    if isinstance(vals, Dict):
        return {**zip(vals.keys(), union_product(vals.values()))}
    if isinstance(vals, Iterable):
        return itertools.chain(*(product_union(v) for v in vals))
    return [vals]


def product_union(vals) -> Union[Iterable, Dict]:
    if isinstance(vals, Dict):
        return {**zip(vals.keys(), product_union(vals.values()))}
    if isinstance(vals, Iterable):
        return itertools.product(*(union_product(v) for v in vals))
    return iter([vals])

