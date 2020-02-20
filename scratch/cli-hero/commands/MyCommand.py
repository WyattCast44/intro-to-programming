class MyCommand:

    signature = "my:command"

    description = "My command description"

    args = {
        'default': "The default command argument",
    }

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        pass
    