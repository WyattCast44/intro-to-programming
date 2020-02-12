import sys
import inspect
from console import Console

class Application(Console):
    
    config = {}

    options = {}

    commands = {}

    def __init__(self, config = []):

        # Set the application config
        self.config = config

    def processOptions(self):
        
        # Remove the file name
        sys.argv.pop(0)

        # Tmp storage of unknown options
        unknownOptions = []

        # Process the passed args
        for option in sys.argv:

            # Check if the option is defined
            if option in self.options:

                # Option exists, need to call the handle method
                self.runOption(option)

            else:

                # Option does not exists, or was not registed
                unknownOptions.append(f'Uknown option {option}')

        if len(unknownOptions) > 0:
            Console().sectionWithList('Problems:', unknownOptions)
    
    def registerOptions(self, options):

        if type(options) == dict:
            for key, desc in options.items():
                self.options[key] = desc
            return self
        else:
            return self

    def registerCommands(self, commands):
        
        if type(commands) == dict:
            for key, desc in commands.items():
                self.commands[key] = desc
            return self
        else:
            return self

    def runOption(self, option):

        if option in self.options:
            self.options[option](self).handle()

    def runCommand(self, command):

        if command in self.commands:
            self.commands[command](self).handle()

    def printMainMenu(self):
    
        # Print name and version
        Console().title(f'\n{self.config["name"]} - v{self.config["version"]}', 'green')

        # Print description
        Console().line(self.config["description"])

        # Print usage section
        Console().sectionWithList('Usage:', [
            f"python {sys.argv[0]} [option]",
        ])

        self.printOptions()

        # Print commands section
        Console().sectionWithList('Commands:', [
            "Enter 'resume' to resume a saved game",
            "Enter 'new' to start a new game",
        ])

    def printOptions(self):

        options = []

        for key, option in self.options.items():
            options.append(Console().formatLine('green', key) +  f" {option(self).signature[key]}")

        # Print options section
        Console().sectionWithList('Options:', options)

    def run(self):

        # Check if any args were passed
        if len(sys.argv) > 1:

            # Process the args
            self.processOptions()

            quit()

        self.printMainMenu()