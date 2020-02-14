class MakeFile:

    signature = 'make:file'

    description = 'Create a new file'

    def __init__(self, application):
        self.application = application

    def handle(self):
        name = self.application.console().ask(f'What should the file be named?')
        
