from time import time
from .GameIntro import GameIntro


class Game:

    banner = """
                            
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

    def __init__(self, application):

        self.application = application

        return

    def run(self):

        # Note the start time
        self.application.state().upsert('game_start', time())

        # Clear the console
        self.application.clearConsole()

        # Print the banner
        self.application.output().success(self.banner)

        # Set the next step
        self.application.state().upsert('next_step', GameIntro)

        # Run the game until game over
        while not self.application.state().get('game_over', False):

            # Run the next step of the game
            self.application.state().get('next_step')(self.application, self).run()

        return

    def end(self):

        self.application.state().upsert('game_end', time())

        self.application.state().upsert('game_over', True)

        print('\n\tGame Over.\n')

        quit()

        return
