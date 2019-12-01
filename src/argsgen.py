import itertools
import upiter
from typing import Any, cast, Dict, Iterable, Iterator, List, Optional, Tuple, Union


class Format:
    """ Formatted argument value obejct
    """
    def __init__(self, text:str, args:Dict[str, Any]):
        self.text = text # format text
        self.args = args # (Reference to) arguments


    def __str__(self) -> str:
        """ get formatted string with arguments """
        return self.text.format(**self.args)


# Scalar = Union[None, bool, int, float, str]
ArgVal = Any #Union[Scalar, Iterable[Any], Format]
Args = Dict[str, ArgVal] # (All-) Arguments dictionary

_PArgs_ = '' # Key name of positional arguments in all-arguments dictionary 


def pattern_to_cmdargs_iter(pattern) -> Iterator[Iterator[str]]:
    """ Generate iterators of commandline arguments from pattern """
    return map(args_to_cmdargs, pattern_to_args_iter(pattern))


def pattern_to_args_iter(pattern) -> Iterator[Args]:
    """ Generate iterators of argument objects from pattern """
    return map(rawargs_to_args, pattern_to_rawargs_iter(pattern))


def pattern_to_rawargs_iter(pattern) -> Iterator[Args]:
    """ Generate iterators of raw argument values from pattern """
    return map(upiter.to_dict, upiter.product_union(pattern))


def rawargs_to_args(rawargs:Args) -> Args:
    """ Convert raw argument values to final values
        (Create `Format` object in specified value) 
    """

    args_for_format:Args = {}

    def make_value(v):
        if isinstance(v, dict):
            if '__format__' in v:
                return Format(v['__format__'], args_for_format)
            return {_k:make_value(_v) for _k, _v in v.items()}
        if upiter.is_iterable(v):
            return [make_value(_v) for _v in v]
        return v

    args = {k:make_value(v) for k, v in rawargs.items()}

    args_for_format.update(make_args_for_format(args))

    return args


def args_to_cmdargs(args:Args) -> Iterator[str]:
    """ Iterate final command argument strings """
    yield from map(str, args_to_cmdargobjs(args))


def args_to_cmdargobjs(args:Args) -> Iterator:
    """ Iterate command arguments (as string or other object) """
    yield from get_pargs(args)
    yield from itertools.chain.from_iterable(keyvalue_to_cmdargs(k, v) for k, v in get_kwargs(args))


def keyvalue_to_cmdargs(k:str, v:ArgVal) -> Iterator[str]:
    """ Iterate key-value pair (yield key and value)
        If value is None, yield only key
        If value is iterable, yield from the value
    """
    yield k
    if v is not None: yield from upiter.as_iterable(v)


def make_args_for_format(args:Args) -> Args:
    """ Make dictionary for formatting
        Assign positional arguments as key '$(number)' in addition to keyword arguments (except Format object)
    """
    return {
        **{'$'+str(i):v for i, v in enumerate(get_pargs(args), 1) if not isinstance(v, Format)},
        **{k:v for k, v in get_kwargs(args) if not isinstance(v, Format)}
    }


def get_pargs(args:Args) -> Iterable[ArgVal]:
    """ Get positional arguments from all-arguments dictionary """
    return upiter.as_iterable(args.get(_PArgs_))


def get_kwargs(args:Args) -> Iterator[Tuple[str, ArgVal]]:
    """ Get keyword arguments from all-arguments dictionary """
    return ((k, v) for k, v in args.items() if k != _PArgs_)
