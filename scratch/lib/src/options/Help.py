class Help:

    signature = "--h"

    description = "Display the application help screen"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().success('Showing the help command')
