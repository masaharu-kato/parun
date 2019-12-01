#!env/bin/python
import argparse
import json
import subprocess
from typing import Any, Dict, Iterator, List, Optional

import argsgen
import executor

def main():

    argp = argparse.ArgumentParser()
    argp.add_argument('settings_path', type=str, help="Path for settings file")
    argp.add_argument('pattern_name', type=str, nargs='?', help="Additional pattern name (Optional)")
    argp.add_argument('-q', '--quiet'  , action='store_true', help='Do not output messages to stdout')
    argp.add_argument('-p', '--preview', action='store_true', help='Preview commands to be run, but do not run.')
    args = argp.parse_args()

    with open(args.settings_path, mode='r') as f:
        settings = json.load(f)

    cmdargs_list = make_cmdargs_list(settings, args.pattern_name)

    if args.preview:
        for cmdargs in cmdargs_list:
            print(' '.join(cmdargs))
        return 0

    return executor.execute(cmdargs_list, quiet=args.quiet)



def make_cmdargs_list(settings:dict, pattern_name:Optional[str]) -> List[List[str]]:
    front_args = [settings['program']] if 'program' in settings else []
    pattern = make_pattern(settings, pattern_name)
    return [[*front_args, *cmdargs] for cmdargs in argsgen.pattern_to_cmdargs_iter(pattern)]


def make_pattern(settings:dict, pattern_name:Optional[str]) -> Dict[str, Any]:
    if 'patterns' in settings:
        if pattern_name is None:
            raise RuntimeError('Additional pattern name is not specified.')

        if not pattern_name in settings['patterns']:
            raise RuntimeError('Unknown pattern name: {}'.format(pattern_name))
        
        return settings['patterns'][pattern_name]

    if 'pattern' in settings:
        return settings['pattern']
    
    raise RuntimeError('Missing `pattern` or `patterns` in settings.')


if __name__ == '__main__':
    main()
