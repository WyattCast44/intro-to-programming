class Version:

    signature = '--v'

    description = 'Display application version'

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.output().info(
            f'\n{self.application.state().get("config.version")}')
