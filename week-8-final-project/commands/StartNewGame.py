from app import Game
from app import Foxx
from app import Puzzle


class StartNewGame:

    signature = "new:game"

    description = "Start a new game"

    def __init__(self, application):

        self.application = application

        return

    def handle(self):

        self.application.clearConsole()

        game = Game(self.application)

        player = Foxx(game)

        self.application.state().set('game', game)
        self.application.state().set('player', player)
        self.application.state().set('puzzle', Puzzle(game, self.application))

        game.run()

        return
