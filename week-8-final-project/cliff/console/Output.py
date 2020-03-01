import sys
import time


class Output:

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

    def format(self, formats, content):

        formatted = content

        if type(formats) == list:
            for index in formats:
                formatted = f'{self.formatters.get(index)}{formatted}{self.formatters.get("end")}'
        else:
            formatted = f'{self.formatters.get(formats)}{formatted}{self.formatters.get("end")}'

        return formatted

    def success(self, message):
        print(self.format('green', message))

    def error(self, message):
        print(self.format('red', message))

    def info(self, message):
        print(self.format('yellow', message))

    def title(self, message, formats=['yellow']):

        if formats != []:
            message = self.format(formats, message)

        underline = self.format(formats, ('-' * len(message)))

        print(f'{message}\n{underline}')

    def line(self, message=''):
        print(message)

    def sectionWithList(self, title, options, prefix='- '):
        self.title(f'\n{title}')

        if type(options) == list:

            for option in options:
                self.line(f'{prefix}{option}')

        elif type(options) == dict:

            for key, desc in options.items():
                self.line(f'{prefix}{self.format("green", key)} {desc}')

    def typed(self, message, delay=0.1):
        for letter in message:
            time.sleep(delay)
            sys.stdout.write(letter)
            sys.stdout.flush()
