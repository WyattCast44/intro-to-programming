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
            print('\nI am still running\n')
        else:
            print('\nWe are in the endgame now\n')
            self.application.state().upsert('game_over', True)
