#!env python3

from sys import argv
from os import system

if __name__ == '__main__':
    pattern = argv[1]
    while True:
        raw = input()
        if not raw:
            break
        params = [p.strip() for p in raw.split(',')]
        cmd = pattern.format(*params)
        system(cmd)
