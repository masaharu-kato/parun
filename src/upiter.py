import functools
import itertools
from typing import Dict, Iterable, Iterator, Union

def union_product(vals) -> Union[Iterable, Dict]:

    if isinstance(vals, Dict):
        return (dict(zip(vals.keys(), union_product(vals.values()))), )

    if _is_iterable(vals):
        return itertools.chain(*(product_union(v) for v in vals))
            
    return (vals,)


def product_union(vals) -> Union[Iterable, Dict]:
    if isinstance(vals, Dict):
        return (dict(zip(vals.keys(), res)) for res in product_union(vals.values()))

    if _is_iterable(vals):
        return itertools.product(*(union_product(v) for v in vals))

    return (vals,)


def _is_iterable(vals) -> bool:
    return isinstance(vals, Iterable) and not isinstance(vals, (str, bytes))


def dict_flatten(dicts:Iterable[Dict]) -> Dict:
    return functools.reduce(lambda a, b:{**a, **b}, dicts)
    


# def main():

#     lst1 = [1, ('2a', '2b'), 3]
#     print(*union_product(lst1))
#     print(*product_union(lst1))

#     tdict1 = {'hoge':1, 'fuga':('2a', '2b'), 'piyo':3}
#     print(*union_product(tdict1))
#     print(*product_union(tdict1))

#     tdict2 = (
#         {'hoge':1, 'fuga':('2a', '2b'), 'piyo':3},
#         {'hoge':1, 'poyo':('A', 'B', 'C'), 'fuga':40},
#     )
#     print(*union_product(tdict2))
#     print(*product_union(tdict2))


# if __name__ == "__main__":
#     main()
