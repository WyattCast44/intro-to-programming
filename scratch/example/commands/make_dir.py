class MakeDir:

    signature = 'make:dir'

    description = 'Create a new directory'

    def __init__(self, application):
        self.application = application

    def handle(self):
        name = self.application.console().ask(f'What should the directory be named?')
        
