class MakeCommand:

    args = {
        '-n': 'Filename',
        '-f': 'Force overwrite'
    }

    signature = 'make:command'

    description = 'Create a new application command'

    helpText = """
    Description:
        [:description:]

    Usage:
        [:usage:] [:signature:] CommandName

    Arguments:
        -i: interactive, will prompt you to enter a command name
        -f: force overwrite, will overwrite any file with the same name
    
    Examples:
        [:usage:] [:signature:] MyCommand

        This is will create a python class named `MyCommand` in the default commands folder.
        It will also update the `__init__` file in the commands folder to import the new command.
    """

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.console().ask(f'What should the file be named?')
        
