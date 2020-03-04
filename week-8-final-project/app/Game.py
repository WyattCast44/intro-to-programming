import random
from time import time, sleep


class Game:

    def __init__(self, application):

        self.application = application

        return

    def start(self):

        self.application.state().upsert('game_start', time())

        banner = """
                     _   _   _   _   _   _     _   _  
                    / \ / \ / \ / \ / \ / \   / \ / \ 
                   ( P | L | A | N | E | T ) ( 4 | 2 )
                    \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ 

        =========================================================
        """

        intro = """
        Planet 43, err... I mean 42 is a medium sized rocky planet, 
        orbiting proxima minor in the rishi maze quadrant of the Blue Moon 
        Galaxy. It's been said, 'If there was a bright center of the 
        universe, it's the furthest planet from it'. It is frequented by 
        smugglers and bounty hunters.
        """

        self.application.output().success(banner)
        self.application.output().typed(intro, 0.06)

        sleep(20)

        return self

    def run(self):

        while not self.application.state().get('game_over', False):

            if random.randint(0, 1):
                self.run()
            else:
                self.application.clearConsole()
                print('\n\tGame Over.\n')
                self.end()

        return

    def end(self):

        self.application.state().upsert('game_end', time())

        self.application.state().upsert('game_over', True)

        return

    # def printFirstParagraph(self):

    #     if random.randint(0, 1):
    #         print('\nI am still running\n')
    #     else:
    #         print('\nWe are in the endgame now\n')
    #         SpellBook(self.application).read()
    #         self.application.state().upsert('game_over', True)
