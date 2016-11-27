from setuptools import setup, find_packages

import protoenv

print(protoenv.__version__)
setup(
    name='protoenv',
    version=protoenv.__version__,
    author='Za Wilgustus',
    author_email='wilcoxjg@gmail.com',
    license='Apache 2.0',
    url='https://github.com/zancas/protoenv.git',
    packages=find_packages(),
    install_requires=['docker-py >= 1.10.6, < 1.11',
                      'jinja2 >= 2.8, < 3'],
    entry_points={'console_scripts': [
        'protoenv=protoenv.cli:main']},
    package_data={'protoenv':['dockerfile_templates/*']}
)
