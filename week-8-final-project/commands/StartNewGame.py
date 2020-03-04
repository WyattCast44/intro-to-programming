import random


class StartNewGame:

    signature = "new:game"

    description = "Start a new game"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.clearConsole()

        self.printFirstParagraph()

    def printFirstParagraph(self):

        if random.randint(0, 1):
            print('I am still running')
        else:
            print('We are in the endgame now')
            self.application.state().upsert('game_over', True)
