import itertools

from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple, Union as UnionType
ArgVal = UnionType[str, Iterable[str]] # Optional[Union[int, float, str]]
IArgVal = UnionType[ArgVal, List[ArgVal]]


class Args:
    def __init__(self, pargs:list, kwargs:dict):
        self.pargs = pargs
        self.kwargs = kwargs
        self.args_for_format = {
            **{'$'+str(i):v for i, v in enumerate(self.pargs, 1)},
            **self.kwargs
        }


    def cmdargs(self) -> Iterator[str]:
        yield from map(str, self.raw_cmdargs())


    def raw_cmdargs(self) -> Iterator:
        yield from self.pargs
        yield from itertools.chain.from_iterable(map(self.keyvalue_to_cmd_args, self.kwargs.items()))


    @staticmethod
    def keyvalue_to_cmdargs(keyvalue:Tuple[str, ArgVal]) -> Iterator[str]:
        key, v = keyvalue
        yield key
        if v is not None:
            if isinstance(v, Iterable):
                yield from v
            else:
                yield v


class Format:
    def __init__(self, text:str, args:Dict[str, ArgVal]):
        self.text = text
        self.args = args


    def __str__(self) -> str:
        return self.text.format(**self.args)



class ArgsPattern:
    def __init__(self, iargs:Dict[str, IArgVal]):
        self.iargs = iargs


    def args(self) -> Iterator[Dict[str, str]]:
        return self.dict_product_with_kv(
            self.iargs.keys(),
            map(self.iargval_to_argval, self.iargs.values())
        )


    @staticmethod
    def iargval_to_argval(v) -> Iterator[ArgVal]:
        if isinstance(v, Iterable):
            yield from v
        else:
            yield v

