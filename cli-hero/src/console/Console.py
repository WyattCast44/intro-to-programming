import sys
from .Input import Input
from .Output import Output


class Console:

    options = {}
    commands = {}
    optionsStack = []
    commandStack = []

    def __init__(self):
        super(Console, self).__init__()

        return

    def input(self):
        return Input()

    def output(self):
        return Output()

    ##
    # CLI
    ##

    def validateArguments(self, args=[]):

        for arg in args:

            if self.isOption(arg):

                # We can move onto next arg
                self.optionsStack.append(arg)

            elif self.isCommand(arg):

                # We need to get the args for the command and validate them
                if self.validateCommandArgs(arg, args[args.index(arg)+1:]):
                    # Args are valid for command
                    self.commandStack.append(arg)
                else:
                    # Args are invalid for command
                    print('\ncommand is invalid')

                break

            else:
                raise Exception(
                    f"Invalid command/option, please try again. Invalid item: {arg}")

    def validateCommandArgs(self, command, args):

        if hasattr(self.commands[command], 'args'):

            # command has args defined, we
            # need to validate that the required
            # args are present

            hasDefaultArg = False

            if len(self.commands[command].args) == 1:
                if not "?" in list(self.commands[command].args)[0]:
                    hasDefaultArg = True

            if hasDefaultArg:
                if "=" in list(self.commands[command].args)[0] and len(args) == 0:
                    # If there is only one arg and it
                    # has a default value, and the num of
                    # args is zero all good
                    return True
                elif len(args) == 1:
                    # if there is only one arg and the command has
                    # a default arg, all good to go!
                    return True

            if len(args) == 1 and hasDefaultArg:
                return True

            for key, desc in self.commands[command].args.items():

                isKeyRequired = (key[-1:] != '?')

        else:
            # command has no args, as long
            # as none were passed command is valid
            return (len(args) == 0)

    def processArguments(self, args=[]):

        self.validateArguments(args)

        for option in self.optionsStack:
            self.options[option](self).handle()

        for command in self.commandStack:
            if type(self.commands[command]) == type:
                self.commands[command](self).handle()
            elif callable(self.commands[command]):
                self.commands[command](self)

    ##
    # Options
    ##

    def isOption(self, option):
        return (option in self.options)

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

    def runOption(self, option, args=[]):

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

    def printOptionsMenu(self):

        options = []

        for key, option in self.options.items():

            options.append(self.output().formatLine(
                'green', option.signature) + f" {option.description}")

        self.output().sectionWithList('Options:', options, '')

    ##
    # Commands
    ##

    def isCommand(self, command):
        return (command in self.commands)

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

    def runCommand(self, command, args=[]):

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

    def printCommandMenu(self):

        commands = []

        for key, command in self.commands.items():

            commands.append(self.output().formatLine(
                'green', command.signature) + f" {command.description}")

        self.output().sectionWithList('Commands:', commands, '')
