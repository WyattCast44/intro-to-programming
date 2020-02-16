from .Input import Input
from .Output import Output


class Console:

    options = {}
    commands = {}

    def __init__(self):
        return

    def input(self):
        return Input()

    def output(self):
        return Output()

    ##
    # Options
    ##

    def registerOption(self, key, handler):

        self.options[key] = handler

        return self

    def registerOptions(self, options):

        if type(options) == list or type(options) == set:

            # Given the list, use the class
            # to get the signature for the option
            for option in options:
                self.registerOption(option.signature, option)

        elif type(options) == dict:

            # Given the dict, use the provided key
            # and set the handler
            for key, option in options.items():
                self.registerOption(key, option)

        else:
            raise Exception(
                f'Uknown format used to register options. Type: {type(commands)}, Option(s): {options}')

        return self

    def runOption(self, option):

        # Ensure that option is registered
        if option in self.options:

            # Check if handler is a class
            if isinstance(self.options[option], type):
                self.options[option](self).handle()
                return

            # Check if handler is a function
            elif callable(self.options[option]):
                self.options[option](self)
                return

            # Unknown handler type
            else:
                raise Exception(
                    f'Unable to handle option with given handler. Option: {option}, Handler: {self.options[option]}')

        else:
            raise Exception(f'Unknown option: {option}')

    ##
    # Commands
    ##

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
                f'Uknown format used to register commands. Type: {type(commands)}, Command(s): {commands}')

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
