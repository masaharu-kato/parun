import subprocess

def execute(commands:list):
    for command in commands:
        print(' '.join(command))
        p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        for line in iter(p.stdout.readline,b''):
            print(line.decode("utf8"), end='')

