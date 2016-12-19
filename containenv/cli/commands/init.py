'''
Usage: containenv init [metasource]

Options:
  -h, --help        Display this help message and exit.
'''
import os


class Command(object):
    '''A createnv command that writes a container config and builds an image
    from it based on the current metasource directory.

        
    '''

    def __init__(self, metasource):
        self.metasource = os.path.abspath(metasource)

    def __call__(self):
        """Write container config and build container .

        Args:
            cli_args: The docopt arguments from the command line parsed from
                the module docstring using docopt. 

        Returns:
            The exit code for the command, or None, implying a successful run.
        """
        config = Configuration(
            cli_args['<config>'] or cli_args['--config'],
            type=cli_args['--type'],
            name=cli_args['--name'],
            requires=cli_args['--requires'],
            hosts=cli_args['--hosts'],
            vars=cli_args['--vars']
        )
        if cli_args['--output-dir']:
            output_dir = os.path.expanduser(cli_args['--output-dir'])
        else:
            output_dir = os.path.join(os.getcwd(), 'testenv_symbols')
        tasks = [(
            'Exporting all symbols...',
            lambda: backend.export(config, output_dir)
        )]
        return run_tasks(
            'Exporting {} test environment symbols'.format(config.name),
            tasks
