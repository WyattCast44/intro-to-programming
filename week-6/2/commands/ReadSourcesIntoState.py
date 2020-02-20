from models import Machine


class ReadSourcesIntoState:

    signature = 'load:machines'

    description = 'Create machine models from the given data files'

    def __init__(self, application):
        self.application = application

    def handle(self):

        # For each data file in state, create a machine model and
        # store models in state

        machines = []

        for path in self.application.state().get('sources'):

            machines.append(Machine().fromSource(path))

        self.application.state().set('machines', machines)
