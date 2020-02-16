from .Input import Input
from .Output import Output


class Console(Input):

    options = {}
    commands = {}

    def output(self):
        return ConsoleOutput()

    def registerCommand(self, key, handler):

        self.commands[key] = handler

        return self

    def registerCommands(self, commands):

        if type(commands) == list or type(commands) == set:

            # Given the list, use the class
            # to get the signature for the command
            for command in commands:
                self.registerCommand(command.signature, command)

        elif type(commands) == dict:

            # Given the dict, use the provided key
            # and set the handler
            for key, command in commands.items():
                self.registerCommand(key, command)

        else:
            raise Exception(
                f'Uknown format used to register commands. Type: {type(commands)}')

        return self

    def runCommand(self, command):

        # Ensure that command is registered
        if command in self.commands:

            # Check if handler is a class
            if isinstance(self.commands[command], type):
                self.commands[command](self).handle()
                return

            # Check if handler is a function
            elif callable(self.commands[command]):
                self.commands[command](self)
                return

            # Unknown handler type
            else:
                raise Exception(
                    f'Unable to handle command with given handler. Command: {command}, Handler: {self.commands[command]}')

        else:
            raise Exception(f'Unknown command: {command}')
