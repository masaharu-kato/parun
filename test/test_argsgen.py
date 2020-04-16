import pytest #type:ignore
from src import argsgen
import json


with open('test/res/print_args.json', mode='r') as f:
    cfg_data = json.load(f)

with open('test/res/print_args_result.json', mode='r') as f:
    result_data = json.load(f)


inputs = cfg_data['patterns']
results = result_data['args_result']

test_patterns = {name:(_input, results[name]) for name, _input in inputs.items()}


@pytest.mark.parametrize(
    'pattern, ans_cmdargs_list',
    [*test_patterns.values()],
    ids = [*test_patterns.keys()]   
)
def test_argsgen(pattern, ans_cmdargs_list):
    cmdargs_iter = argsgen.pattern_to_cmdargs_iter(pattern)
    return all([*res] == ans for res, ans in zip(cmdargs_iter, ans_cmdargs_list))

