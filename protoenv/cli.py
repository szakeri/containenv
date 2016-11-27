import docker
import jinja2
import os
import sys


HOME = os.environ['HOME']
CONTAINER_ENVS = os.path.abspath(
    os.path.join(HOME, '.protoenv', 'environments')
)
print(HOME)
PKG_ROOT = os.path.dirname(os.path.abspath(__file__))

DEFAULT_DICT = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}

def _init_config_dir(environment):
    print(CONTAINER_ENVS)
    print(environment)
    env_path = CONTAINER_ENVS + environment
    print(env_path)
    if not os.path.isdir(env_path):
        os.makedirs(env_path)
    return env_path

def set_python_config(environment, config_variables):
    basictemplate = open(
        os.path.join(PKG_ROOT, 'dockerfile_templates', 'basic')
    ).read()
    print(basictemplate)
    env_path = _init_config_dir(environment)
    rendered = jinja2.Template(basictemplate).render(**config_variables)
    outdfile = open(os.path.join(env_path, 'Dockerfile'), 'w').write(rendered)

#def launch_a_python_environment(config_directory_context, 

def main():
    TARG_DIR = os.path.abspath(os.curdir)
    print(PKG_ROOT)
    print(os.listdir(PKG_ROOT))
    set_python_config(TARG_DIR, DEFAULT_DICT)

if __name__ == '__main__':
    main()
