from .input import ConsoleInput
from .output import ConsoleOutput

class Console(ConsoleInput, ConsoleOutput):
    pass

    def input(self):
        return ConsoleInput()

    def output(self):
        return ConsoleOutput()