import os, sys, time, inspect
from console import Console

class Application():
    
    config = {
        'name': 'Console Application',
        'version': '0.1.0',
        'description': 'Helping you build simple and powerful, python command line applications!',
    }

    options = {}

    commands = {}

    def __init__(self, config = {}):

        # Update the application default config
        self.config.update(config)

        # Set some config values
        self.config["cwd"] = os.getcwd()
        self.config['start'] = time.time()

    def console(self):
        return Console()

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
            self.console().sectionWithList('Problems:', unknownOptions)
    
    def registerOptions(self, options):

        if type(options) == list:
            for option in options:
                self.options[option.signature] = option
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
        self.console().title(f'\n{self.config["name"]}', 'green')

        # Print description
        self.console().line(self.config["description"])

        # Print usage section
        self.console().sectionWithList('Usage:', [
            f"python {sys.argv[0]} [command/option]",
        ])

        # Print options menu
        self.printOptions()

        # Print commands section
        # self.console().sectionWithList('Commands:', [
        #     "Enter 'resume' to resume a saved game",
        #     "Enter 'new' to start a new game",
        # ])

    def printOptions(self):

        options = []

        for key, option in self.options.items():
            options.append(self.console().formatLine('green', option.signature) +  f" {option.description}")

        # Print options section
        self.console().sectionWithList('Options:', options, '')

    def run(self):

        # Check if any args were passed
        if len(sys.argv) > 1:

            # Process the args
            self.processOptions()

            # print(self.options)

            quit()

        self.printMainMenu()
    
    def __del__(self):

        # Log end time
        self.config['end'] = time.time()

        # Compute execution time
        self.config['time'] = round(self.config['end'] - self.config['start'], 2)