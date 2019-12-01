import subprocess
from typing import List

def execute(cmdargs_list:List[List[str]], *, quiet:bool=False):
    for cmdargs in cmdargs_list:
        if not quiet: print(' '.join(cmdargs))
        p = subprocess.Popen(cmdargs, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        for line in iter(p.stdout.readline,b''):
            print(line.decode("utf8"), end='')

