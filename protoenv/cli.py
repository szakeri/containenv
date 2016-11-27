import argparse
import docker
import jinja2
import os
import sys


class ProtoEnvDockerfileDoesNotExist(Exception):
    pass

class ProtoEnvDockerfileAlreadyExists(Exception):
    pass

CURRENT = os.path.abspath(os.curdir)
PROTOENV = os.path.abspath(
    os.path.join(CURRENT, '.protoenv')
)
PKG_ROOT = os.path.dirname(os.path.abspath(__file__))

PYTHON3 = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}

def init_protoenv(config_variables):
    basictemplate = open(
        os.path.join(PKG_ROOT, 'dockerfile_templates', 'basic')
    ).read()
    rendered = jinja2.Template(basictemplate).render(**config_variables)
    os.makedirs(PROTOENV)
    outdfile = open(os.path.join(PROTOENV, 'Dockerfile'), 'w').write(rendered)

def run_protoenv():
    pass

def main():
    usage='Initialize or run a virtualenv-like prototyping environment.'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument( '--init',
                         help='Initialize a new prototyping environement',
                         action='store_true')
    args = parser.parse_args()
    if args.init:
        if os.path.isfile(os.path.join(PROTOENV, 'Dockerfile')):
            raise ProtoEnvDockerfileAlreadyExists
        init_protoenv(PYTHON3)
    else:
        if not os.path.isfile(os.path.join(PROTOENV, 'Dockerfile')):
            raise ProtoEnvDockerfileDoesNotExist
        run_protoenv()
        

if __name__ == '__main__':
    main()
