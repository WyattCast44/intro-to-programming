import os, sys, time, inspect
from .state import State
from .console import Console

class Application:
    
    config = {
        'name': 'Console Application',
        'version': '0.1.0',
        'description': 'Helping you build simple and powerful, python command line applications!',
    }

    state = None

    options = {}

    commands = {}

    def __init__(self, config = {}):

        # Create the state
        self.store = State()

        # Update the application default config
        self.config.update(config)

        # Set some config values
        self.config["script"] = sys.argv[0]
        self.config["cwd"] = os.getcwd()
        self.config['start'] = time.time()

        # Remove the filename
        sys.argv.pop(0)

    def state(self):
        return self.store

    def console(self):
        return Console()

    def processOptions(self):
        
        # Tmp storage of unknown options
        unknownOptions = []

        # Process the passed args
        for option in sys.argv:

            # Check if the option is defined
            if option in self.options:

                # Option exists, need to call the handle method
                self.runOption(option)

                # Remove from the sys args
                sys.argv.pop(sys.argv.index(option))

            else:

                # Option does not exists, or was not registed
                unknownOptions.append(f'Uknown option {option}')

        if len(unknownOptions) > 0:
            self.processCommands()

        quit()

    def processCommands(self):
        
        # Tmp storage of unknown options
        unknownCommands = []

        # Process the passed args
        for command in sys.argv:

            # Check if the option is defined
            if command in self.commands:

                # Option exists, need to call the handle method
                self.runCommand(command)

                # Remove from the sys args
                sys.argv.pop(sys.argv.index(command))

            else:

                # Option does not exists, or was not registed
                unknownCommands.append(f'Uknown command/option {command}')

        if len(unknownCommands) > 0:
            self.console().sectionWithList('Problems:', unknownCommands)
    
    def registerOptions(self, options):

        if type(options) == list:
            for option in options:
                self.options[option.signature] = option
            return self
        elif type(options) == dict:
            for key, handler in options.items():
                self.options[key] = handler
            return self
        else:
            return self

    def registerCommands(self, commands):

        if type(commands) == list:
            for command in commands:
                self.commands[command.signature] = command
            return self
        else:
            return self

    def runOption(self, option):

        if option in self.options:
            # Check if handler is a class
            if isinstance(self.options[option], type):
                self.options[option](self).handle()
                return
            # Check if handler is a function
            elif callable(self.options[option]):
                self.options[option](self)
                return
            else:
                return

    def runCommand(self, command):

        if command in self.commands:
            # Check if handler is a class
            if isinstance(self.commands[command], type):
                self.commands[command](self).handle()
                return
            # Check if handler is a function
            elif callable(self.commands[command]):
                self.commands[command](self)
                return
            else:
                return

    def printMainMenu(self):
    
        # Print name and version
        self.console().title(f'\n{self.config["name"]}', 'green')

        # Print description
        self.console().line(self.config["description"])

        # Print usage section
        self.console().sectionWithList('Usage:', [
            f'python {self.config["script"]} [command/option]',
        ])

        # Print options menu
        self.printOptions()

        # Print commands section
        self.printCommands()

    def printOptions(self):

        options = []

        for key, option in self.options.items():
            if isinstance(option, type):
                options.append(self.console().formatLine('green', option.signature) +  f" {option.description}")
            else:
                options.append(self.console().formatLine('green', key))

        # Print options section
        self.console().sectionWithList('Options:', options, '')

    def printCommands(self):

        commands = []

        for key, command in self.commands.items():
            commands.append(self.console().formatLine('green', command.signature) +  f" {command.description}")

        # Print commands section
        if (len(commands) > 0):
            self.console().sectionWithList('Commands:', commands, '')

    def run(self):

        # Check if any args were passed
        if len(sys.argv) >= 1:

            # Process the args
            self.processOptions()

        self.printMainMenu()

    def __del__(self):

        # Log end time
        self.config['end'] = time.time()

        # Compute execution time
        self.config['time'] = round(self.config['end'] - self.config['start'], 2)