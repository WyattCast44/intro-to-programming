from .Output import Output


class Input(Output):

    def ask(self, question):
        self.info(f'\n{question}\n')

        return input(f'> ')

    def askWithOptions(self, question, options):

        self.sectionWithList(question, options)

        given = input('\n> ')

        while not given in options:
            self.line(f'\nUnknown option \'{given}\', please try again.')
            self.sectionWithList(question, options)
            given = input('\n> ')

        return given
