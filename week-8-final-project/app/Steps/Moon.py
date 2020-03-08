class Moon:

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        print('moon')

        self.game.end()

        return