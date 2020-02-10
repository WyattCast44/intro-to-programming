class Console:

    """
    Console is a helper class to print styled lines in the console
    """

    decorators = {
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

    def __init__(self):
        self.message = ''
        self.formatters = []

    def message(self, message):
        self.message = message
        
        return self
    
    def section(self, message):
        self.message = message
        self.formatters.append('bold')
        self.formatters.append('green')

        print(self.getFormattedOutput())

    def bold(self):
        self.formatters.append('bold')

        return self

    def success(self):
        self.formatters.append('green')

        return self

    def underlined(self):
        self.formatters.append('underlined')
        
        return self

    def getFormattedOutput(self):
        
        formatted = self.message

        for formatter in self.formatters:
            formatted = f'{self.decorators.get(formatter)}{formatted}{self.decorators.get("end")}'

        return f'{formatted}'
    
    def print(self, message = ''):

        if message != '':
            self.message = message

        print(self.getFormattedOutput())