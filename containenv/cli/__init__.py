import argparse
import docker
import jinja2
import os
import sys


class ContainEnvDockerfileDoesNotExist(Exception):
    pass

class ContainEnvDockerfileAlreadyExists(Exception):
    pass

CURRENT = os.path.abspath(os.curdir)
CONTAINENV = os.path.abspath(
    os.path.join(CURRENT, '.containenv')
)
PKG_ROOT = os.path.dirname(os.path.abspath(__file__))

PYTHON3 = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}


def init_containenv(config_variables):
    basictemplate = open(
        os.path.join(PKG_ROOT, 'dockerfile_templates', 'basic')
    ).read()
    rendered = jinja2.Template(basictemplate).render(**config_variables)
    os.makedirs(CONTAINENV)
    outdfile = open(os.path.join(CONTAINENV, 'Dockerfile'), 'w').write(rendered)


def run_containenv():
    pass


def main():
    usage='Initialize or run a virtualenv-like contained environment.'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument( '--init',
                         help='Initialize a new contained environment',
                         action='store_true')
    args = parser.parse_args()
    if args.init:
        if os.path.isfile(os.path.join(CONTAINENV, 'Dockerfile')):
            raise ContainEnvDockerfileAlreadyExists
        init_containenv(PYTHON3)
    else:
        if not os.path.isfile(os.path.join(CONTAINENV, 'Dockerfile')):
            raise ContainEnvDockerfileDoesNotExist
        run_containenv()
        

if __name__ == '__main__':
    main()
