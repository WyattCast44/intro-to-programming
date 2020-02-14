class Help:
    
    signature = '--h'

    description = 'Display the application help screen'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.console().line(f'\nRunning the help command')
