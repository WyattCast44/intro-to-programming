class ResumeGame:

    signature = "resume:game"

    description = "Resume a saved game"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().error('\nTODO\n')
