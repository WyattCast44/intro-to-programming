class ConsoleOutput:

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

    def line(self, message = ''):
        print(message)

    def sectionWithList(self, title, options):
        self.title(f'\n{title}')

        for option in options:
            self.line(f'- {option}')

    def table(self, headers, rows):
        print('TODO')
