from depman.main import run_depman
from subprocess import run,check_output

def build():
    run('g++ -c logger.cpp', shell=True, check=True)

def build_test():
    run('g++ -I $PWD test/main.cpp -L $PWD logger.o', shell=True, check=True)

def test():
    check_output('./a.out', shell=True) == 'Logged by my beautiful library ::Hello World!\n'

phases = {
    'build': build,
    'build_test': build_test,
    'test': test,
}

run_depman(phases)