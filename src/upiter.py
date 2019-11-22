import itertools
from typing import Dict, Iterable, Iterator, Union

def union_product(vals) -> Union[Iterable, Dict]:

    if isinstance(vals, Dict):
        return dict(zip(vals.keys(), union_product(vals.values())))

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


def main():
    print(*product_union(['abc', 'puyo']))

    tdict = {'hoge':'abc', 'bar': ['piyo', ['puyo', 'puyo2'], 'fuga']}
    print(*product_union(tdict))
    # print(*product_union(tdict.values()))
    # print(dict(zip(tdict.keys(), product_union(tdict.values()))))


if __name__ == "__main__":
    main()
