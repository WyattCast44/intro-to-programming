import sys
import inspect
from console import Console

class Application(Console):
    
    config = []

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
            return
        else:
            return

    def registerCommands(self, commands):
        
        if type(commands) == dict:
            for key, desc in commands.items():
                self.commands[key] = desc
            return
        else:
            return

    def runOption(self, option):

        if option in self.options:
            self.options[option]().handle()

    def run(self):

        # Check if any args were passed
        if len(sys.argv) > 1:

            # Process the args
            self.processOptions()

            quit()