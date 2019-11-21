import itertools

from typing import Any, Dict, Iterable, Iterator, List, Optional, Union as UnionType
ArgVal = UnionType[str, Iterable[str]] # Optional[Union[int, float, str]]
IArgVal = UnionType[ArgVal, List[ArgVal]]


class Args:
    def __init__(self, pargs:list, kwargs:dict):
        self.pargs = pargs
        self.kwargs = kwargs


    def command_args(self) -> Iterator[str]:
        yield from self.pargs
        yield from itertools.chain.from_iterable(map(self.keyvalue_to_cmd_args, self.kwargs.items()))


    @staticmethod
    def keyvalue_to_cmd_args(keyvalue:Tuple[ArgName, ArgVal]) -> Iterator[str]:
        key, v = keyvalue
        yield key
        if v is not None:
            if hasattr(v, '__iter__'):
                yield from v
            else:
                yield v



class Union():
    def __init__(self, *vals):
        self.vals = vals


    def __iter__(self):
        return self.vals


class Product:
    def __init__(self, *vals):
        self.vals = vals


    def __iter__(self):
        #TODO: Correct Implementation
        return itertools.product(*self.vals)



class Format():
    def __init__(self, text:str):
        self.text = text


    def format(self, args:Args):
        # TODO: Corresponds to positional arguments
        return self.text.format(*args.kwargs)



class ArgsPattern:
    def __init__(self, iargs:Dict[ArgName, IArgVal]):
        self.iargs = iargs


    def args(self) -> Iterator[Dict[str, str]]:
        return self.dict_product_with_kv(
            self.iargs.keys(),
            map(self.iargval_to_argval, self.iargs.values())
        )


    @staticmethod
    def iargval_to_argval(v:ArgValueEx) -> Iterator[ArgVal]:
        if hasattr(v, '__iter__'):
            yield from v
        else:
            yield v


    @staticmethod
    def dict_product_with_kv(keys:Iterable, values:Iterable) -> Iterator[Dict]:
        return (dict(zip(keys, values)) for values in itertools.product(values))

