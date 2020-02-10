from ConsoleOutput import *

class ConsoleInput(ConsoleOutput):

    def ask(self, message, options):
        
        self.sectionWithOptions(message, options)

        given = input('\n> ')

        while not given in options:
            self.line(f'\nUnknown option \'{given}\', please try again.')
            self.sectionWithOptions(message, options)
            given = input('\n> ')

        return given

# ConsoleInput().ask('Would you like to hang out?', {
#     'y': "Enter 'y' to hang out",
#     'n': "Enter 'n' to chill later"
# })
