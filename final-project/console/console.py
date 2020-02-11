import sys
from .input import ConsoleInput
from .output import ConsoleOutput

class Console(ConsoleInput, ConsoleOutput):
    pass

    commands = {}

    def input(self):
        return ConsoleInput()

    def output(self):
        return ConsoleOutput()
    
    def registerCommands():
        return