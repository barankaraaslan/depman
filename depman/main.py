from . import config

def info():
    print('dependency resolution started')

def package():
    print('packaging')

def install():
    print('installing')

class Phase:
    def __init__(self, action, next=None):
        self.action = action
        self.next = next

default_phases = {
    'info': Phase(info, 'package'),
    'package': Phase(package, 'install'),
    'install': Phase(install)
}
default_initial_phase = 'info'

def run_depman(phases=default_phases, initial_phase=default_initial_phase):
    key = initial_phase
    while key:
        phases[key].action()
        key = phases[key].next