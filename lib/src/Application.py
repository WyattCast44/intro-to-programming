import os
import sys
from .support import Repository, Time, HasState
from .console import Console


class Application(Console, HasState):

    config = {
        'name': 'Console Application',
        'version': '1.0.0',
        'cwd': os.getcwd(),
        'description': 'Helping you build command line applications',
    }

    def __init__(self, config={}):

        super(HasState, self).__init__()

        # Update config w/users config
        self.config.update(config)

        # Set config in state
        self.state().set('config', self.config)
        self.state().append('config', 'start', Time.now())
        self.state().append('config', 'script', sys.argv[0])

        # Remove the filename from the args list
        # sys.argv.pop(0)

    def run(self):

        # When running the app, we need to
        # - check if any args were passed
        # - if they was
        #   - we need to check if it matches any user options
        #   - we need to check if it matches any internal options
        #   - we need to check if it matches any user commands
        #   - we need to check if it matches any internal commands
        # - else
        #   - we need to see if there is a default command

        print('\nrunning\n')

    def printMenu(self):
        print()

    def printOptions(self):
        print()

    def printCommands(self):
        print()

    def __del__(self):

        # Log script end time
        self.state().append('config', 'end', Time.now())

        # TODO: Compute execution time
        self.state().append('config', 'duration', Time.now())
