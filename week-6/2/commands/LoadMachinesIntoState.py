from models import Machines


class LoadMachinesIntoState:

    signature = 'load:machines'

    description = 'Create machine models from the given data files'

    def __init__(self, application):
        self.application = application

    def handle(self):

        machines = Machines().loadSources(self.application.state().get('sources'))

        self.application.state().set('machines', machines)
