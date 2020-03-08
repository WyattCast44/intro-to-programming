class Neptune:

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        print('neptune')

        self.game.end()

        return
