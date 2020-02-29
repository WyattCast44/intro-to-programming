class MakeOption:

    signature = "make:option"

    description = "Create a new application option"

    args = {
        'name': 'The name of the file to create',
    }

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().error('cool')
