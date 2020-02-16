class MakeOption:

    signature = "make:option"

    description = "Create a new application option"

    args = {
        'default': "The name of the class to make",
        '--f': "Overwrite any file with same name"
    }

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        path = self.application.state().get('config.cwd') + 'options'
