import random
from time import sleep


class Moon:

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        message = """

        You see the Moon growing larger and larger in your window. You see 
        the pockmarked surface and get ever closer.

        """

        self.application.output().typed(message, 0.055)

        astroids = random.randint(0, 1)

        if astroids:

            message = """

            WARNING. You have wandered into an uncharted asteroid belt!  
            Your ship is taking damage!

            """

            self.application.output().error(message)

            sleep(4)

        self.game.end()

        return
