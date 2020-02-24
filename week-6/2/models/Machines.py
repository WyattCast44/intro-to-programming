class Machines:

    contents = None

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

        for path in self.sources:
            print(path)
