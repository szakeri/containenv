
"""
Usage: containenv [--verbose] [--debug <LEVEL>] <command> [<args>...]
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
import importlib
import logging
import os
import pkgutil
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


def _run_command(argv):
    """Run the command with the the given CLI options and exit.

    Valid commands are modules in the containenv.cli.commands package. A command
    module *must* have the same name as the command it represents as the import
    system is used to retrieve the command module by the command name.

    Command modules are expected to have a __doc__ string that is parseable by
    docopt and contain a callable object named Command. If the the Command
    object has a schema attribute, the arguments passed to the command will be
    validated against the schema before the command is called.

    Args:
        argv: The list of command line arguments supplied for a command. The
            first argument is expected to be the name of the command to be run.
            Note that this is different than the full arguments parsed by
            docopt for the entire program.

    Raises:
        ValueError: Raised if the user attempted to run an invalid command.
    """
    command_name = argv[0]
    logger.info('Running command "%s" with args: %s', command_name, argv[1:])
    mod = _get_command_module(command_name)
    logger.debug('Parsing docstring:%s\nwith arguments %s.',
                 mod.__doc__, argv)
    args = docopt(mod.__doc__, argv=argv)
    try:
        logger.debug(
            'Attempting to create command with command line arguments: %s',
            args)
        command = mod.Command(**args)
    except TypeError:
        logger.debug('Command does not take arguments.')
        command = mod.Command()
    if hasattr(command, 'schema'):
        logger.debug('Validating command arguments against schema "%s".',
                     command.schema)
        args.update(command.schema.validate(args))
    sys.exit(command(**args) or 0)


def _get_command_module(command):
    """Return the command module for the specified CLI command.

    Args:
        command: The name of the CLI command to use in finding a module in the
            commands package.

    Returns:
        A module object for the given CLI command with a valid docopt __doc__
        and a main() function that takes a list containing the command line
        arguments.

    Raises:
        ValueError: Raised if no module with a name matching the command
            exists in the commands package.
    """
    mod_name = '{}.{}'.format(commands.__name__, command)
    try:
        return importlib.import_module(mod_name)
    except ImportError:
        logger.exception('Unable to import "%s".', mod_name)
        raise ValueError(
            '"{}" is not a containenv command. \'containenv help -a\' lists all '
            'available subcommands.'.format(command)
        )


def _help(command):
    """Print out a help message and exit the program.

    Args:
        command: If a command value is supplied then print the help message for
            the command module if available. If the command is '-a' or '--all',
            then print the standard help message but with a full list of
            available commands.

    Raises:
        ValueError: Raised if the help message is requested for an invalid
            command or an unrecognized option is passed to help.
    """
    if not command:
        doc = _DEFAULT_DOC
    elif command in ('-a', '--all'):
        available_commands = (command_name for _, command_name, _ in
                              pkgutil.iter_modules(commands.__path__))
        command_doc = 'Available commands:\n{}'.format(
            '\n'.join('   {}'.format(command) for command in available_commands))
        doc = __doc__.format(command_doc)
    elif command.startswith('-'):
        raise ValueError("Unrecognized option '{}'.".format(command))
    else:
        mod = _get_command_module(command)
        doc = mod.__doc__
    docopt(doc, argv=('--help',))
        
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
        args = docopt(_DEFAULT_DOC,
                      version='containenv {}'.format(VERSION),
                      options_first=True)
        pp(args)
        if args['--verbose']:
            debug_level = int(args['--debug']) # default == logging default
            handler = logging.StreamHandler(verbose_stream)
            handler.setLevel(debug_level)
            rl = logging.getLogger()
            rl.setLevel(debug_level)
            logger.info("debug level set to {}".format(debug_level))
            handler.setFormatter(LogColorFormatter())
            rl.addHandler(handler)
            logger.debug('Verbose logging activated')
        if args['<command>'] == 'help':
            subcommand = next(iter(args['<args>']), None)
            _help(subcommand)
        else:
            full_command = [args['<command>']] + args['<args>']
            _run_command(full_command)
    except (KeyboardInterrupt, EOFError):
        sys.exit("Cancelling at the User's request.")
    except Exception as e:
        logger.exception(e) 
        sys.exit(e)

if __name__ == '__main__':
    main()
