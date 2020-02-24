class Help:

    signature = '--h'

    description = 'Display application help screen'

    def __init__(self, application):
        self.application = application

    def handle(self):

        self.application.printMainMenu()
