
import argparse
import sys
from abc import ABCMeta
from .style import display

class Args:
    def __init__(self, this, kwargs=None):
        self.this = this
        self.kwargs = kwargs


class Command:

    def __init__(self, name, description, usage, pos=1):
        self.name = name
        self.description = description
        self.usage = usage
        self.pos = pos
        self.subcommands = []
        self.parser = argparse.ArgumentParser(
            description=self.description,
            usage=self.usage)
        self.parser.add_argument('command', help='Subcommand to run')


    def run(self):
        """."""
        args = self.parser.parse_args(sys.argv[self.pos:self.pos + 1])
        command = list(filter(lambda command: command.name == args.command,
                         self.subcommands))
        if not command :
            display('Unrecognized command', color='red')
            self.parser.print_help()
            exit(1)

        command = command[0]
        command()

    def add_command(self, command):
        self.subcommands.append(command)

    def __call__(self):
        if self.subcommands:
            self.run()
        elif sys.argv[self.pos] in ['-h', '--help', '-help']:
            self.parser.print_help()
        else:
            display(self.name + sys.argv[self.pos], color='green')
