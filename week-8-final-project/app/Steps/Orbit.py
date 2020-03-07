from time import sleep


class Orbit:

    intro = """
        
        You are now in orbit

        """

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        self.application.output().typed(self.intro, 0.06)

        self.game.end()

        return
