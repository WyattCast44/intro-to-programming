from time import sleep


class GameIntro:

    intro = """
        The date is February 6, in the year 2018. Your mind is racing... you check your seat harness for 
        what seems like the hundredth time. You can't help but think that either way history is in the making.

        Mission Control: 
            Falcon Heavy is configured for flight. T-Minus 25 seconds. Starman confirm go for launch.

        You: 
            Starman is GO for launch. 

        Mission Control:
            Copy, Starman. Standby final countdown. 

        Mission Control:

            10...
            9...
            8...
            7...
            6...
            5...
            4...
            3...
            2...
            1...

        """

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        self.application.output().typed(self.intro, 0.06)

        self.application.state().upsert('next_step')

        sleep(5)

        self.game.end()

        return
