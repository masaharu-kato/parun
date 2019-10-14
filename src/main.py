#!env/bin/python
import subprocess
import argparse
import argsgen
import executor

def main():

    argp = argparse.ArgumentParser()
    argp.add_argument('args_path', type=str, help="Path for params.json")
    argp.add_argument('args_name', type=str, help="Args name to run")
    args = argp.parse_args()

    return executor.execute(argsgen.generate_commands_from_setting_file(args.args_path, args.args_name))


if __name__ == '__main__':
    main()
