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

        # Process the passed args
        for option in sys.argv:

            # Check if the option is defined
            if option in self.options:

                # Option exists, need to call the handle method
                self.runOption(option)

            else:

                # Option does not exists, or was not registed
                Console().sectionWithList('Problems:', [
                    f'Uknown option {option}'
                ])
    
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
            self.options[option]().handle()

    def runCommand(self, command):

        if command in self.commands:
            self.commands[command]().handle()

    def printMainMenu(self):
    
        # Print name and version
        Console().title(f'\n{self.config["name"]} - v{self.config["version"]}', 'green')

        # Print description
        Console().line(self.config["description"])

        # Print usage section
        Console().sectionWithList('Usage:', [
            f"python {sys.argv[0]} [option]",
        ])

        # Print options section
        Console().sectionWithList('Options:', [
            "Pass 'h' for application help",
        ])

        # Print commands section
        Console().sectionWithList('Commands:', [
            "Enter 'resume' to resume a saved game",
            "Enter 'new' to start a new game",
        ])

    def run(self):

        # Check if any args were passed
        if len(sys.argv) > 1:

            # Process the args
            self.processOptions()

            quit()

        self.printMainMenu()