from src.filesystem import Filesystem


class MakeCommand:

    signature = "make:command"

    description = "Create a new application command"

    args = {
        'name': "The name of the class to make",
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

        self.path = self.application.state().get('cwd') + '/commands/'

        return

    def handle(self, args=[]):

        self.ensureCommandsDirExists()
        self.createCommand(args)
        self.ensureCommandInitFileExists()
        self.appendToInitFile()
        self.printSuccessMessage()

    def ensureCommandsDirExists(self):

        Filesystem.ensureDirExists(self.path)

    def ensureCommandInitFileExists(self):

        path = self.path + '__init__.py'

        Filesystem.ensureFileExists(path)

    def prepStub(self, args=[]):
        return self.stub.replace("[:command:]", 'MyCommand')

    def createCommand(self, args=[]):
        path = self.path + 'MyCommand.py'

        command = open(path, 'w')

        command.write(self.prepStub(args))

        command.close()

    def appendToInitFile(self):
        path = self.path + '__init__.py'

        init = open(path, 'a')
        init.write('from .MyCommand import MyCommand')
        init.close()

    def printSuccessMessage(self):
        self.application.output().success('\nSuccessfully created new command: MyCommand')
