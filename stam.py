#!/usr/bin/env python3

from sys import argv, exit
from os import system
import readline

def show_help():
    print('Do like this: \n \
        $ stam.py "echo and in that {} there was a {}"\n \
        > bog, hole\n \
        and in that bog there was a hole\n \
        > hole, tree\n \
        and in that hole there was a tree\n' \
        )

if __name__ == '__main__':
    if len(argv) != 2:
        show_help()
        exit(1)
        
    pattern = argv[1]
    try:
        while True:
            raw = input('> ')
            if not raw:
                break
            params = [p.strip() for p in raw.split(',')]
            cmd = pattern.format(*params)
            system(cmd)
    except (EOFError, KeyboardInterrupt):
        pass
