import os
import sys
from .console import Console
from .support import Repository, Time, HasState, sleep


class Application(Console, HasState):

    config = {
        'name': 'Console Application',
        'version': '1.0.0',
        'description': 'Helping you build command line applications',
        'interactive': False,
    }

    def __init__(self, config={}):

        super(Application, self).__init__()

        # Update config w/users config
        self.config.update(config)

        # Set config in state
        self.state().set('cwd', os.getcwd())
        self.state().set('config', self.config)
        self.state().set('script', sys.argv[0])
        self.state().set('args', sys.argv[1:])
        self.state().append('config', 'start', Time.now())

    def printUsageMenu(self):

        self.output().sectionWithList(
            'Usage:', [f'python {self.state().get("script")} [option/command]'], ' ')

    def printMainMenu(self):

        self.printUsageMenu()

        self.printOptionsMenu()

        self.printCommandMenu()

    def run(self):

        if len(self.state().get('args')) > 0:

            # There is arguments to validate and process
            self.processArguments(self.state().get('args'))

        elif not self.defaultCommand == None:

            self.defaultCommand(self).handle()

        else:

            # Need to check for default command

            if self.state().get('config.interactive'):

                self.printMainMenu()

                command = self.input().ask('What command would you like to run?')

                self.runCommand(command, self.state().get('args'))

    def __del__(self):

        # Log script end time
        self.state().append('config', 'end', Time.now())

        # Compute execution time
        duration = self.state().get('config.end') - self.state().get('config.start')
        self.state().append('config', 'duration', duration)
