from depman.main import run_depman
from depman.config import depman_home
from subprocess import run, check_output
from shutil import copy, copytree, rmtree
from os import makedirs, remove
from os.path import expanduser
from configparser import ConfigParser
from glob import glob

name = 'log4cpp'
version = '1.0.0'

def clean():
    try:
        rmtree('package')
        remove('a.out')
        remove('log4cpp.o')
        remove('package_info.txt')
    except FileNotFoundError:
        pass

def build():
    run('g++ -c log4cpp.cpp', shell=True, check=True)

def build_test():
    run('g++ -I $PWD test/main.cpp -L $PWD log4cpp.o', shell=True, check=True)

def test():
    check_output('./a.out', shell=True) == 'Logged by my beautiful library ::Hello World!\n'

def package():
    makedirs('package/lib', exist_ok=True)
    makedirs('package/include', exist_ok=True)
    copy('log4cpp.o', 'package/lib/')
    copy('log4cpp.h', 'package/include/')

def generate_package_info():
    config = ConfigParser(allow_no_value=True)
    config['info'] = {
        'name': name,
        'version': version,
    }
    config['files'] = {}
    for path in glob('package/**/*'):
        config['files'][path] = None
        
    with open('package_info.txt', 'w') as _file:
        config.write(_file)

def install():
    install_path = expanduser(f'{depman_home}/{name}/{version}')
    makedirs(install_path, exist_ok=True)
    copytree('package/', f'{install_path}/package', dirs_exist_ok=True)
    copy('package_info.txt', install_path)
    copy(__file__, install_path)

phases = {
    'clean': clean,
    'build': build,
    'build_test': build_test,
    'test': test,
    'package': package,
    'generate_package_info': generate_package_info,
    'install': install,
}

run_depman(phases)