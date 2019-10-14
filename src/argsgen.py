import json
import itertools


def generate_commands_from_setting_file(filepath:str, args_name:str):

    with open(filepath, mode='r') as f:
        settings = json.load(f)

    return generate_commands_from_settings(settings, args_name)


def generate_commands_from_settings(settings:dict, args_name:str):
    return [[
        settings['target'],
        *itertools.chain.from_iterable([get_string_keyvalue_pair(key, value) for key, value in args.items()])
    ] for args in generate_args_from_settings(settings, args_name)]


def get_string_keyvalue_pair(key, value):
    if value is None: return (str(key),)
    return (str(key), str(value))


def generate_args_from_settings(settings:dict, args_name:str):

    if args_name not in settings['args']:
        raise RuntimeError('Specified args name not found.')

    c_args = settings['args'][args_name]

    return generate_args(
        constant    = c_args.get('constant'   ),
        additionals = c_args.get('additionals'),
        patterns    = c_args.get('patterns'   ),
        formatted   = c_args.get('formatted'  ),
    )


def generate_args(*, constant:dict, additionals:list, patterns:dict, formatted:dict) -> list:

    if constant is None: constant = {}
    if additionals is None or not len(additionals): additionals = [{}]
    if patterns is None: patterns = {}
    if formatted is None: formatted = {}

    base_args_list = [dict(itertools.chain(constant.items(), additional.items())) for additional in additionals]

    return [
        dict(itertools.chain(
            args.items(),
            {key:value.format(**args) for key, value in formatted.items()}.items()
        ))
        for args in [
            dict(itertools.chain(pair[0].items(), pair[1].items()))
            for pair in itertools.product(base_args_list, dict_product(patterns))
        ]
    ]


def dict_product(i_dict:dict) -> list:
    return _dict_product({key:elm if type(elm) is list else [elm] for key, elm in i_dict.items()})


def _dict_product(i_dict:dict) -> list:
    return (dict(zip(i_dict.keys(), values)) for values in itertools.product(*i_dict.values()))
