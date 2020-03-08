class Mars:

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        print('mars')

        self.game.end()

        return
