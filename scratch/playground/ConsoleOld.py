class Console:

    fluent = False
    message = ''

    formats = {
        'darkcyan': '\033[36m',
        'purple': '\033[95m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'bold': '\033[1m',
        'red': '\033[91m',
        'end': '\033[0m'
    }

    def format(self, message = ''):
        self.message = message
        self.fluent = True
        return self
    
    def formatLine(self, formats, message):

        if type(formats) == list:
            formatted = message
            for index in formats:
                formatted = f'{self.formats.get(index)}{formatted}{self.formats.get("end")}'
        else:
            formatted = f'{self.formats.get(formats)}{message}{self.formats.get("end")}' 

        return f'{formatted}'

    def bold(self, message):
        
        message = self.formatLine('bold', message)

        if self.fluent:
            return message
        else:
            print(message)

    def success(self, message):

        message = self.formatLine('green', message)

        if self.fluent:
            return message
        else:
            print(message)
    
    def info(self, message):

        message = self.formatLine('yellow', message)
        
        if self.fluent:
            return message
        else:
            print(message)

    def error(self, message = ''):

        if message == '':
            message = self.message

        message = self.formatLine('red', message)
        
        if self.fluent:
            return message
        else:
            print(message)

    def line(self, message):
        
        if self.fluent:
            return message
        else:
            print(message)

    def __del__(self):
        if self.fluent:
            print(self.message)
    
def main():
    Console().bold().color('red').print('Hello')

main()