from . import config

def info():
    print('dependency resolution started')

def package():
    print('packaging')

def install():
    print('installing')

default_phases = {
    'info': info,
    'package': package,
    'install': install
}

def run_depman(phases=default_phases):
    for phase_action in phases.values():
        phase_action()