import sys
from console import Console

class Application(Console):
    
    config = []

    options = {
        'h': 'help',
    }

    def __init__(self, config = []):
        
        if len(sys.argv) > 1:
            self.processOptions()

        self.config = config

    def main(self):
        self.printTitle()
        self.printOptions()
        self.printCommands()

    def processOptions(self):
        sys.argv.pop(0)
        for option in sys.argv:
            if option in self.options:
                print()
            else:
                Console().sectionWithList('Problems:', [
                    f'Uknown option {option}'
                ])

