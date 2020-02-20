class Verbose:

    signature = "--v"

    description = "Set the output to verbose"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().success('Showing the verbose command')
