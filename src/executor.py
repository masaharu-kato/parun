import subprocess

def execute(commands:list, *, quiet:bool=False):
    for command in commands:
        if not quiet: print(' '.join(command))
        p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        for line in iter(p.stdout.readline,b''):
            print(line.decode("utf8"), end='')

