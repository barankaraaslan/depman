from depman.main import run_depman
from subprocess import run,check_output
from shutil import copy
from os import makedirs

def build():
    run('g++ -c logger.cpp', shell=True, check=True)

def build_test():
    run('g++ -I $PWD test/main.cpp -L $PWD logger.o', shell=True, check=True)

def test():
    check_output('./a.out', shell=True) == 'Logged by my beautiful library ::Hello World!\n'

def package():
    makedirs('package/lib', exist_ok=True)
    copy('logger.o', 'package/lib/')

phases = {
    'build': build,
    'build_test': build_test,
    'test': test,
    'package': package,
}

run_depman(phases)