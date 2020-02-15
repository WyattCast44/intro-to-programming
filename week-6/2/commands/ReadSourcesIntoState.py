from models import *

class ReadSourcesIntoState:
    
    signature = 'load:machines'

    description = 'Create machine models from the given data files'

    def __init__(self, application):
        self.application = application

    def handle(self):

        machines = []

        for path in self.application.state().get('sources'):

            machines.append(Machine().fromSource(path))
        
        self.application.state().set('machines', machines)