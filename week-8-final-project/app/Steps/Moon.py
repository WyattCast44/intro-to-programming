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

        astroids = False  # random.randint(0, 1)

        if astroids:

            message = """

            WARNING. You have wandered into an uncharted asteroid belt!  
            Your ship is taking damage!

            """

            self.application.output().error(message)

            option = self.application.input().askWithOptions('Quick, what are you going to do?!', [
                'turn-around',
                'push-thru',
            ])

        else:

            amount = random.randint(0, 10)

            self.application.state().upsert(
                'stardust_amount', self.application.state().get('stardust_amount') + amount)

            totalAmount = self.application.state().get('stardust_amount')

            message = """
            As you get closer you see a hazy belt hovering around the moon. STARDUST! 
            You gathered [AMT] units of STARDUST! Great job, you now have 
            [TOTAL] units! Let's keep searching...
            """.replace('[AMT]', str(amount)).replace('[TOTAL]', str(totalAmount))

            self.application.output().success(message)

        self.game.end()

        return
