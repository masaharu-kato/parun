#!env/bin/python
import json
import sys
import os

def main():


    args = {}
    cname = ''
    cvalue = None

    for arg in sys.argv[1:]:
        if len(arg) and arg[0] == '-':
            args[cname] = cvalue
            cname = arg
            cvalue = None
        else:
            if type(cvalue) is list:
                cvalue.append(arg)
            elif cvalue is not None:
                cvalue = [cvalue, arg]
            else:
                cvalue = arg

    args[cname] = cvalue

    if '-o' in args:
        outpath = args['-o']
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        with open(outpath, mode='w') as f:
            json.dump(args, f)
    else:
        print(args)

    return


if __name__ == '__main__':
    main()
