import random
from time import sleep
from .Mars import Mars
from .Moon import Moon
from .Diner import Diner
from .Neptune import Neptune


class Intro:

    intro = """

    The date is February 6, in the year 2018. Your mind is racing... you check your seat harness for 
    what seems like the hundredth time. You can't help but think no matter what happens today, history 
    is in the making. 

    All your training has lead to this point, this flight, this mission. The first ever flight of a 
    Space-X Falcon Heavy, with you and your Tesla Cybership on board.

    Mission Control: 
        "Falcon Heavy is configured for flight. T-Minus 25 seconds. Starman confirm go for launch."

    You: 
        "Starman is GO for launch."

    Mission Control:
        "Copy, Starman. Standby final countdown." 

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

        Launch!

    With a thunderous and ear-splitting roar, the 27 Merlins engines break the grip of gravity and 
    accelerate you onward to deep space...

    After a harrowing 3 minutes, the fairing surrounding you is jettisoned and you get your first look at
    Earth from outer space. You stare in awe at the beauty of the earth, the stars, and the universe... 

        """

    prompt = """
    Mission Control:
        "Starman, we show you established in a good orbit. Confirm all systems are green."
    
    You: 
        "Control, everything is green up here. It's all so beautiful..."

    Mission Control:
        "Copy Starman, you'll have to send me a postcard."

        "I suppose we will be seeing you in a few months then, where do you think you'll head to 
        first? Remember your mission is to collect as much Stardust as possible before 
        running out of energy."

    """

    response = """
    Mission Control:
        "Copy Starman, understand you'll be going to [DEST]. Godspeed, watch out for the 
        aliens, asteroids, and pirates! Mission Control out."

    You:
        "Thanks Control, see ya!" 
    """

    def __init__(self, application, game):

        self.game = game
        self.application = application

        return

    def run(self):

        # Print the intro
        # self.application.output().typed(self.intro, 0.055)

        # # Prompt for destination
        # self.application.output().typed(self.prompt, 0.055)

        # Get the destination
        destination = self.application.input().askWithOptions('Where to first?', {
            "mars": "Enter `mars` to go to Mars.",
            "moon": "Enter `moon` to go to Earth's Moon.",
            "neptune": "Enter `neptune` to go to Neptune",
            "random": "Enter `random` to let the autopilot choose."
        })

        # Print a response to destinatio
        self.application.output().typed(
            self.response.replace('[DEST]', destination.title()), 0.055)

        self.application.clearConsole()

        # Set the next step based on destination
        steps = {
            "mars": Mars,
            "moon": Moon,
            "neptune": Neptune,
            "random": random.choice([Mars, Moon, Neptune, Diner])
        }

        message = """
        You type the destination into the flight computer and off you go!
        """

        self.application.output().typed(message, 0.055)

        self.application.state().upsert('next_step', steps[destination])

        return
