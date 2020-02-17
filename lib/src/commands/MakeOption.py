class MakeOption:

    signature = "make:option"

    description = "Create a new application option"

    args = {
        'default': 'The name of the file to create',
        '--f=False': "Force create the file"
    }

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.output().error('cool')
