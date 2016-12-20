"""
Usage: containenv [--verbose] [--debug <LEVEL>] ( init | help ) [<args>...]
       containenv (-V | --version)

Options:
  -V, --version     Display the version and exit.
  -v, --verbose     Print logging information to the console.
  -d <LEVEL>, --debug <LEVEL>  Set the sensitivity of loggers to [default: 30]

{}

See 'containenv help COMMAND' for more information on a specific COMMAND.
NOTE:  See also 'contain help' which is included in this package.

"""

_DEFAULT_DOC = __doc__.format("""Common containenv commands:
  init      Prepare a contained environment Dockerfile
  help      Print detailed usage information on a specific COMMAND.. or usage.
  """)
from ...utils import CommandContext
    
from . import commands

def main():
    CommandContext(commands, _DEFAULT_DOC, __doc__).execute()

if __name__ == '__main__':
    main()
