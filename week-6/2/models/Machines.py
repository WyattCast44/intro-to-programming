from models import Machine


class Machines:

    items = []

    def __init__(self, sources=None):

        self.sources = sources

        if not sources == None:

            self.loadSources()

    def loadSources(self, sources=None):

        if sources == None and self.sources == None:
            raise Exception(
                "You must pass the path(s) to the source files to create the machines object.")

            return

        self.sources = sources

        for source in sources:

            machine = Machine().fromSource(source)

            self.items.append(machine)

        return self

    def getMachines(self):

        return self.items
