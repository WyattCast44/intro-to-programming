import sys
from .input import ConsoleInput
from .output import ConsoleOutput

class Console(ConsoleInput, ConsoleOutput):
    pass

    options = {}

    commands = {}
    
    def registerCommands(self):
        return
    
    def registerOptions(self):
        return