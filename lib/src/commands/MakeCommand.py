from src.filesystem import Filesystem


class MakeCommand:

    signature = "make:command"

    description = "Create a new application command"

    args = {
        'default': "The name of the class to make",
        '--f': "Overwrite any file with same name"
    }

    stub = """class [:command:]:

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
    """

    def __init__(self, application):
        self.application = application
        return

    def handle(self, args=[]):

        stub = self.stub.replace("[:command:]", 'MyCommand')

        path = self.application.state().get('config.cwd') + '/commands/'

        Filesystem.ensureDirExists(path)

        path = path + 'MyCommand.py'

        command = open(path, 'w')
        command.write(stub)
        command.close()
