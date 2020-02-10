import .ConsoleInput
import .ConsoleOutput

class ConsoleIO(ConsoleInput, ConsoleOutput):
    pass

    def input(self):
        return ConsoleInput()

    def output(self):
        return ConsoleOutput()