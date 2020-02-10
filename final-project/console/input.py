from .output import ConsoleOutput

class ConsoleInput(ConsoleOutput):

    def ask(self, question):
        self.info(f'\n{question}\n')

        return input(f'> ')        
    
    def askWithOptions(self, question, options):
        
        self.sectionWithOptions(question, options)

        given = input('\n> ')

        while not given in options:
            self.line(f'\nUnknown option \'{given}\', please try again.')
            self.sectionWithOptions(question, options)
            given = input('\n> ')

        return given