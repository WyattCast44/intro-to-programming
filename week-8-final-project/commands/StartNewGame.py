from app import Game


class StartNewGame:

    signature = "new:game"

    description = "Start a new game"

    def __init__(self, application):

        self.application = application

        return

    def handle(self):

        # Let start by clearing the console
        self.application.clearConsole()

        # Lets now start and run the game
        game = Game(self.application).run()
