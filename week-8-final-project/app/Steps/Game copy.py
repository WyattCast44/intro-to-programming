from time import time
from app.Steps import Intro


class Game:

    intro = """
                        
    ████████╗██╗  ██╗███████╗                                                                                     
    ╚══██╔══╝██║  ██║██╔════╝                                                                                     
       ██║   ███████║█████╗                                                                                       
       ██║   ██╔══██║██╔══╝                                                                                       
       ██║   ██║  ██║███████╗                                                                                     
       ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                     
     █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗███████╗     ██████╗ ███████╗    
    ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔════╝    ██╔═══██╗██╔════╝    
    ███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  ███████╗    ██║   ██║█████╗      
    ██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  ╚════██║    ██║   ██║██╔══╝      
    ██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗███████║    ╚██████╔╝██║         
    ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝         
    ███████╗████████╗ █████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗                                                
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║                                                
    ███████╗   ██║   ███████║██████╔╝██╔████╔██║███████║██╔██╗ ██║                                                
    ╚════██║   ██║   ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║                                                
    ███████║   ██║   ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║                                                
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                
            
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

        # Capture the start time
        self.application.state().upsert('game_start', time())

        # Set the base stardust amount
        self.application.state().set('stardust_amount', 0)

        # Set the base ship health
        self.application.state().set('health', 100)

        # Clear the console
        self.application.clearConsole()

        # Print the banner
        self.application.output().success(self.intro)

        return

    def run(self):

        # Set the first step
        self.application.state().upsert('next_step', Intro)

        # Run the game until game over
        while not self.application.state().get('game_over', False):

            self.application.state().get('next_step')(self.application, self).run()

        return

    def end(self):

        self.application.state().upsert('game_end', time())

        self.application.state().upsert('game_over', True)

        self.application.output().error(self.outro)

        self.application.output().typed(
            f'\nYou collected {self.application.state().get("stardust_amount")} units of STARDUST. Well done, Starman!\nYour ship health is {self.application.state().get("health")}%\n')

        quit()

        return
