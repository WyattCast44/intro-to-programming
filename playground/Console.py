class Console:
    
    output = ''

    message = ''

    formatters = []

    decorators = {
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

    def print(self, message = ''):

        if message != '':
            self.message = message

        print(self.getFormattedOutput())

    def message(self, message):
        self.message = message
        
        return self

    def bold(self):
        self.formatters.append('bold')

        return self

    def getFormattedOutput(self):
        
        formatted = self.message

        for formatter in self.formatters:
            formatted = f'{self.decorators.get(formatter)}{formatted}{self.decorators.get("end")}'

        self.output = f'{formatted}'

        return self.output

    def sectionTitle(self, message):

        self.message = f'{message}\n--------------------------\n'

        return self
    
def main():
    # Valid
    Console().print('Hello')
    
    # Valid
    Console().message('Hello World').print()

    # Valid
    Console().bold().print('Bold')

    Console().sectionTitle('Welcome to the Jungle!').print()

main()