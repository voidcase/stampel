#!env python3

from sys import argv
from os import system
import readline

def show_help():

if __name__ == '__main__':
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
