from time import time
from .Puzzle import Puzzle
from app.Steps import Intro


class Game:

    banner = """
    
    ████████╗███████╗███╗   ███╗██████╗ ██╗     ███████╗     ██████╗ ███████╗     █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝    ██╔═══██╗██╔════╝    ██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
       ██║   █████╗  ██╔████╔██║██████╔╝██║     █████╗      ██║   ██║█████╗      ███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗
       ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝      ██║   ██║██╔══╝      ██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
       ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗    ╚██████╔╝██║         ██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝

    """

    intro = """

    Your name is Foxx. You are on a quest to find the Lost Temple of Anubis!
    Deep in a underground canvern, you discovered a puzzle box that contains
    the last six pieces of the Lost Amulet. The Amulet is the key to unlocking
    the gates to the Temple of Anubis!

    The puzzle box had this note attached to it...
    """

    warningMessage = """
        "Be warned, brave adventurer in this box you will find what both what your 
        heart desires and horrors that will end your journey before it begins. Some 
        secrets are better left undiscovered, this is your last chance..."
    """

    outro = """
    
    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
        ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                        ░                   

    """

    def __init__(self, application):

        self.application = application

        # Clear the console
        self.application.clearConsole()

        # Capture the start time
        self.application.state().upsert('game_start', time())

        # Print the banner
        # self.application.output().success(self.banner)

        # # Print the intro
        # self.application.output().typed(self.intro, 0.04)

        # # Print the warning
        # self.application.output().typed(self.warningMessage, 0.04, 'red')

    def run(self):

        play = self.application.input().askWithOptions('Disregard the warning and search the box, danger be damned?', {
            'search': "Danger is my middle name, search it!",
            'leave': "Better play it safe"
        })

        if play == "search":

            while not self.application.state().get('game_over', False):

                self.application.state().get('puzzle').askWhichSlotToOpen()

        self.end()

    def end(self):

        self.application.state().upsert('game_end', time())

        self.application.state().upsert('game_over', True)

        self.application.output().error(self.outro)

        self.application.output().typed(
            f'\nYou collected {self.application.state().get("keys")} parts of the Lost Amulet.\n', 0.05)

        quit()

        return
