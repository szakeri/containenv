import argparse
import docker
import jinja2
import os
import sys


class ProtoEnvDirDoesNotExist(Exception):
    pass

CURRENT = os.path.abspath(os.curdir)
PROTOENV = os.path.abspath(
    os.path.join(CURRENT, '.protoenv')
)
PKG_ROOT = os.path.dirname(os.path.abspath(__file__))

DEFAULT_DICT = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}

def _init_config_dir():
    if not os.path.isdir(PROTOENV):
        raise ProtoEnvDirDoesNotExist

def set_python_config(config_variables):
    basictemplate = open(
        os.path.join(PKG_ROOT, 'dockerfile_templates', 'basic')
    ).read()
    print(basictemplate)
    _init_config_dir()
    rendered = jinja2.Template(basictemplate).render(**config_variables)
    outdfile = open(os.path.join(PROTOENV, 'Dockerfile'), 'w').write(rendered)

#def launch_a_python_environment(config_directory_context, 

def main():
    usage='Initialize or run a virtualenv-like prototyping environment.'
    parser = argparse.ArgumentParser(usage=usage)
    print(CURRENT)
    print(PROTOENV)
    set_python_config(DEFAULT_DICT)

if __name__ == '__main__':
    main()
