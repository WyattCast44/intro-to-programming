class MakeCommand:

    args = {
        '-n': 'Filename',
        '-f': 'Force overwrite'
    }

    signature = 'make:command'

    description = 'Create a new application command'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.console().ask(f'What should the file be named?')
        
