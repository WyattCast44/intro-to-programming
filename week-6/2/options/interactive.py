class Interactive:
    
    signature = '--i'

    description = 'Run the application in an interactive mode'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.state().set('interactive', True)
