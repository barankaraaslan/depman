from depman.main import run_depman
from subprocess import run, check_output
from shutil import copy, copytree, rmtree
from os import makedirs, remove

version = '1.0.0'
name = 'log4cpp'

def clean():
    try:
        rmtree('package')
        remove('a.out')
        remove('log4cpp.o')
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
    copy('log4cpp.o', 'package/lib/')

phases = {
    'clean': clean,
    'build': build,
    'build_test': build_test,
    'test': test,
    'package': package,
}

run_depman(phases)