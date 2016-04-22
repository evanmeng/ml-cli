#! /usr/bin/env python3


import cmd
import sys
from os import path
from session import MLSession


class MLCli(cmd.Cmd):
    def __init__(self, session):
        super(MLCli, self).__init__()
        self.session = session

    def do_EOF(self, args):
        return True

    def do_quit(self, args):
        return self.do_EOF(args)

    def do_filter(self, args):
        self.session.filter(args)

    def do_reset(self, args):
        self.session.reset()

    def do_it(self, args):
        print(self.session.str_it())

    def do_back(self, args):
        self.session.back()

    def do_stack(self, args):
        print(self.session.stack())


if __name__ == '__main__':
    args = sys.argv
    ds_path = path.abspath('.' if len(args) < 2 else args[1])
    cli = MLCli(MLSession(ds_path))
    cli.prompt = '>>> '
    cli.cmdloop()
