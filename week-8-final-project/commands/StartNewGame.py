class StartNewGame:

    signature = "new:game"

    description = "Start a new game"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().error('\nTODO\n')
