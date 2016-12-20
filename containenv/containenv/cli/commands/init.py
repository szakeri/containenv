'''
Usage: containenv init [metasource]

Options:
  -h, --help        Display this help message and exit.
'''
import os
import time
from ....display import run_tasks


class Command(object):
    '''A containenv command that writes a container config and builds an image
    from it based on the current metasource directory.

        
    '''

    def __init__(self, metasource=os.curdir):
        self.metasource = os.path.abspath(metasource)
        self.tasks = [
            ('first thing', lambda: None),
            ('second thing', lambda: None),
            ('third thing', lambda: None),
            ]

    def __call__(self):
        """Write container config and build container .

        Returns:
            The exit code for the command, or None, implying a successful run.
        """
        return run_tasks(
            'running some tasks',
            self.tasks)
