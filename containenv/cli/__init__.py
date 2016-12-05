
"""
Usage: containenv [--verbose] [--debug <LEVEL>] <command>
       containenv (-h | --help)
       containenv (-V | --version)

Options:
  -h, --help        Build or run a virtualenv-like contained environment.
  -V, --version     Display the version and exit.
  -v, --verbose     Print logging information to the console.
  -d <LEVEL>, --debug <LEVEL>  Set the sensitivity of loggers to [default: 30]

{}

See 'containenv help <command>' for more information on a specific command.

"""

from __future__ import print_function

from cStringIO import StringIO
import atexit
import logging
import os
import sys

from colorama import Fore
from colorama import Style
from colorama.ansi import clear_line
import docker
from docopt import docopt
import jinja2

from .. import VERSION
from . import commands

_DEFAULT_DOC = __doc__.format("""Common containenv commands:
  build Prepare a contained environment Dockerfile
  run  Run a container environment with a context and Dockerfile as input.""")

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stderr))


class ContainEnvDockerfileDoesNotExist(Exception):
    pass


class ContainEnvDockerfileAlreadyExists(Exception):
    pass


class LogColorFormatter(logging.Formatter):
    """A colored logging.Formatter implementation."""

    def format(self, record):
        """Format the log record with timestamps and level based colors."""
        if record.levelno >= logging.ERROR:
            color = Fore.RED
        elif record.levelno >= logging.WARNING:
            color = Fore.YELLOW
        elif record.levelno >= logging.INFO:
            color = Fore.RESET
        else:
            color = Fore.CYAN
        self._fmt = (
            '{}{}%(levelname)s{} [%(asctime)s][%(name)s]{} %(message)s'.format(
                Style.BRIGHT, color, Fore.RESET, Style.RESET_ALL))
        return super(LogColorFormatter, self).format(record)


'''
CURRENT = os.path.abspath(os.curdir)
CONTAINENV = os.path.abspath(
    os.path.join(CURRENT, '.containenv')
)
PKG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PYTHON3 = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}
'''

def main():
    """Parse the command line options and launch the requested command.

    If the command is 'help' then print the help message for the subcommand; if
    no subcommand is given, print the standard help message.

    Note:
        This is the entry point method for the containenv command defined in
        setup.py.
    """
    from pprint import pprint as pp
    verbose_stream = StringIO()
    atexit.register(lambda: print(
        clear_line() + verbose_stream.getvalue(), file=sys.stderr, end='')
    )
    try:
        print('before docopt')
        args = {'--debug': 10}
        args = docopt(_DEFAULT_DOC,
                      version='containenv {}'.format(VERSION),
                      options_first=True)
        print('after docopt')
        pp(args)
        if args['--verbose']:
            handler = logging.StreamHandler(verbose_stream)
            rl = logging.getLogger()
            if args['--debug']:
                debug_level = int(args['--debug'])
                rl.setLevel(debug_level)
                handler.setLevel(debug_level)
                logger.info("debug level set to {}".format(debug_level))
            handler.setFormatter(LogColorFormatter())
            rl.addHandler(handler)
            logger.debug('Verbose logging activated')
    except (KeyboardInterrupt, EOFError):
        sys.exit("Cancelling at the User's request.")
    except Exception as e:
        logger.exception(e) 
        sys.exit(e)
    '''
    if args.build:
        if os.path.isfile(os.path.join(CONTAINENV, 'Dockerfile')):
            raise ContainEnvDockerfileAlreadyExists
        build_containenv(PYTHON3)
    else:
        if not os.path.isfile(os.path.join(CONTAINENV, 'Dockerfile')):
            raise ContainEnvDockerfileDoesNotExist
        run_containenv()
    ''' 

if __name__ == '__main__':
    main()
