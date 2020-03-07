import random
from time import time, sleep


class Game:

    def __init__(self, application):

        self.application = application

        return

    def start(self):

        self.application.state().upsert('game_start', time())

        self.application.clearConsole()

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

        other = """
        Humanity will once again leave Earth's gravity well.
        """

        self.application.output().success(banner)

        self.application.output().typed(intro, 0.06)

        sleep(5)

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

        quit()

        return
