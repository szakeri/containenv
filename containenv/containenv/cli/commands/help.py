'''
Usage: containenv help [--all] [ init | help ]

Options:
  -a, --all         Append available command list to usage and exit.
'''


class Command(object):

    def __init__(self, **args):
        self.args = args

    def __call__(self):
        print(__doc__)
