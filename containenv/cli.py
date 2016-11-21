import docker
import jinja2
import os
import sys

PKG_ROOT = os.path.dirname(os.path.abspath(__file__))

DEFAULT_DICT = {'IMAGE': 'ubuntu',
                'TAG': 'latest',
                'RUNCOMMANDS': 
                    ['apt update && apt install -y python3\n       '+\
                     '&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*']}
def setup_target_as_python_environment(directory_name):
    basictemplate = open(
        os.path.join(PKG_ROOT, 'dockerfile_templates', 'basic')
    ).read()
    print(basictemplate)
    print(jinja2.Template(basictemplate).render(**DEFAULT_DICT))



def main():
    TARG_DIR = sys.argv[1]
    print(PKG_ROOT)
    print(os.listdir(PKG_ROOT))
    setup_target_as_python_environment(sys.argv[1])

if __name__ == '__main__':
    main()
