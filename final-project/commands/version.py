from console import Console

class Version(Console):

    signature = {
        'v': 'Display the application version'
    }

    def __init__(self, application):
        self.application = application

    def handle(self):
        Console().line(f'\nRunning the version command\n{self.application.config["version"]}')
