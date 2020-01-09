#!/usr/bin/env python3

import readline
from sys import stderr
from os import system
from argparse import ArgumentParser, RawDescriptionHelpFormatter


EXAMPLE = 'Do like this: \n \
        $ stampel "echo and in that {} there was a {}"\n \
        > bog, hole\n \
        and in that bog there was a hole\n \
        > hole, tree\n \
        and in that hole there was a tree\n' \


def get_args():
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description='Execute multiple similar commands with minimal typing.',
        epilog=EXAMPLE,
    )
    parser.add_argument('pattern',
                        help='a shell command with {} at the insert positions'
                        )
    parser.add_argument('--delimeter', '-d', default=',')
    return parser.parse_args()


def run():
    args = get_args()
    try:
        while True:
            raw = input('> ')
            if not raw:
                break
            params = [p.strip() for p in raw.split(args.delimeter)]
            try:
                cmd = args.pattern.format(*params)
            except IndexError:
                print("Not enough arguments to fill all {}'s.", file=stderr)
                continue
            system(cmd)
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == '__main__':
    run()
