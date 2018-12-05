
import argparse
import sys
from abc import ABCMeta

# --- begin "pretty"
#
# pretty - A miniature library that provides a Python print and stdout
# wrapper that makes colored terminal text easier to use (eg. without
# having to mess around with ANSI escape sequences). This code is public
# domain - there is no license except that you must leave this header.
#
# Copyright (C) 2008 Brian Nez <thedude at bri1 dot com>
#
# http://nezzen.net/2008/06/23/colored-text-in-python-using-ansi-escape-sequences/

def display(text, color='normal'):
    codes = {
        'black':     '0;30', 'bright gray':    '0;37',
        'blue':      '0;34', 'white':          '1;37',
        'green':     '0;32', 'bright blue':    '1;34',
        'cyan':      '0;36', 'bright green':   '1;32',
        'red':       '0;31', 'bright cyan':    '1;36',
        'purple':    '0;35', 'bright red':     '1;31',
        'yellow':    '0;33', 'bright purple':  '1;35',
        'dark gray': '1;30', 'bright yellow':  '1;33',
        'normal':    '0'
    }
    print("\033[" + codes[color]+"m" + text + "\033[0m")

class Args:
    def __init__(self, this, kwargs=None):
        self.this = this
        self.kwargs = kwargs

class Command:
    def __init__(self, name, position, description, args):
        """."""
        self.name = name
        self.position = position
        self.description = description
        self.args = args

    def __call__(self):
        """."""
        parser = argparse.ArgumentParser(
            description=self.description)
        for arg in self.args:
            parser.add_argument(arg.this, **arg.kwargs)

        # args = parser.parse_args(sys.argv[self.position:])
        text = " ".join(sys.argv[self.position - 1:])
        display(text, color="green")

    def __repr__(self):
        return self.name

class CollectorCLI:

    def __init__(self, description, usage):
        self.description = description
        self.usage = usage
        self.commands = []

    def run(self):
        """."""
        parser = argparse.ArgumentParser(
            description=self.description,
            usage=self.usage)
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        command = filter(lambda command: command.name == args.command, self.commands)
        if not command :
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        command = list(command)[0]
        command()

    def add_command(self, command):
        self.commands.append(command)


if __name__ == '__main__':
    cli = CollectorCLI(
            description='Pretends to be collector',
            usage=open('collector/figlet').read())
    putin = Command(
        name='putin',
        position=2,
        description='Record changes to the repository',
        args=[
            Args(
                this='--amend',
                kwargs={'action': 'store_true'}
            )
        ]
    )
    boast = Command(
        name='boast',
        position=2,
        description='Download objects and refs from another repository',
        args=[
            Args(
                this='repository',
                kwargs={}
            )
        ]
    )
    cli.add_command(putin)
    cli.add_command(boast)
    cli.run()


    # while True:
    #     color = input("Your color: ")
    #     text = open('collector/figlet').read()
    #     display(text, color=color)