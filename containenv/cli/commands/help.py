'''
Usage: containenv help [--all] [ init | help ]

Options:
  -h, --help        Display this help message and exit.
  -a, --all         List available commands and exit.
'''
import os

class Command(object):
    def __init__(self, **args):
        self.args = args    
    def __call__(self):
        print(__doc__)
