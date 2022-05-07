from depman.main import run_depman, Phase
from subprocess import run

def build():
    run('g++ -c logger.cpp', shell=True, check=True)

phases = {
    'build': Phase(build)
}

run_depman(phases, 'build')