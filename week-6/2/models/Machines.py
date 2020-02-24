from models import Machine


class Machines:

    def __init__(self):

        self.items = []

        return

    def loadSources(self, sources=None):

        if sources == None:
            raise Exception(
                "You must pass the path(s) to the source files to create the machines object.")

            return

        for source in sources:

            machine = Machine().fromSource(source)

            self.items.append(machine)

        return self.items
