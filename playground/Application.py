class ConsoleIO:

    formatters = {
        'underlined': '\033[4m',
        'darkcyan': '\033[36m',
        'purple': '\033[95m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'bold': '\033[1m',
        'red': '\033[91m',
        'end': '\033[0m',
    }

    def formatLine(self, formats, content):

        formatted = content 

        if type(formats) == list:
            for index in formats:
                formatted = f'{self.formatters.get(index)}{formatted}{self.formatters.get("end")}'
        else:
            formatted = f'{self.formatters.get(formats)}{formatted}{self.formatters.get("end")}' 

        return formatted

class ConsoleOutput(ConsoleIO):

    def success(self, message):
        print(self.formatLine('green', message))

    def error(self, message):
        print(self.formatLine('red', message))

    def info(self, message):
        print(self.formatLine('yellow', message))

    def title(self, message, formats = ['yellow']):

        if formats != []:
            message = self.formatLine(formats, message)
        
        length = len(message)

        underline = ''

        for index in range(length):
            underline = underline + '-'

        underline = self.formatLine(formats, underline)

        print(f'{message}\n{underline}')

    def line(self, message):
        print(message)

    def sectionWithOptions(self, title, options):
        self.title(f'\n{title}')

        for key, info in options.items():
            self.line(f'- {info}')

    def table(self, headers, rows):
        print('TODO')

class ConsoleInput(ConsoleOutput):

    def ask(self, message, options):
        
        self.sectionWithOptions(message, options)

        given = input('\n> ')

        while not given in options:
            self.line(f'\nUnknown option \'{given}\', please try again.')
            self.sectionWithOptions(message, options)
            given = input('\n> ')

        return given

ConsoleInput().ask('Would you like to hang out?', {
    'y': "Enter 'y' to hang out",
    'n': "Enter 'n' to chill later"
})
