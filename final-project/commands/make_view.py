class MakeView:

    signature = 'make:view'

    description = 'Create a new view file'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.console().ask(f'What should the file be named?')
        
