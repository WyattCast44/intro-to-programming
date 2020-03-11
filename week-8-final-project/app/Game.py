from time import time
from .Puzzle import Puzzle


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
    the missing pieces of the Lost Amulet. The Amulet is the key to unlocking
    the gates to the Temple of Anubis!

    The puzzle box had this note attached to it...
    """

    warningMessage = """
        "Be warned, brave adventurer in this box you will find both what your 
        heart desires and horrors that will end your journey before it begins. Some 
        secrets are better left undiscovered, this is your last chance..."
    """

    def __init__(self, application):

        self.application = application

        # Clear the console
        self.application.clearConsole()

        # Capture the start time
        self.application.state().upsert('game_start', time())

        # Print the banner
        self.application.output().success(self.banner)

        # Print the intro
        self.application.output().typed(self.intro, 0.04)

        # Print the warning
        self.application.output().typed(self.warningMessage, 0.04, 'red')

    def run(self):

        play = self.application.input().askWithOptions('Disregard the warning and search the box, danger be damned?', {
            'search': "Danger is my middle name, search it!",
            'leave': "Better play it safe"
        })

        if play == "search":

            while not self.application.state().get('game_over', False):

                self.application.state().get('puzzle').askWhichSlotToOpen()

        self.end()

    def end(self, didWin=False):

        self.application.state().upsert('game_end', time())
        self.application.state().upsert('game_over', True)

        self.application.clearConsole()

        if didWin:

            message = """
                                               _
                                             ,d8b,
                                     _,,aadd8888888bbaa,,_
                                _,ad88P+++8,  I8I, 8+++Y88ba,_
                             ,ad88P" `Ya  `8, `8' ,8'  aP' "Y88ba,
                           ,d8"' "Yb   "b, `b  8  d' ,d"   dP" `"8b,
                          dP"Yb,  `Yb,  `8, 8  8  8 ,8'  ,dP'  ,dP"Yb
                     ,88888888Yb, `Yb,`Yb,`8 8 8 8 8',dP',dP' ,dY88888888,
                     dP     `Yb`Yb, Yb,`8b 8 8 8 8 8 d8',dP ,dP'dP'     Yb
                    ,8888888888b "8, Yba888888888888888adP ,8" d8888888888,
                    dP        `Yb,`Y8P""'             `""Y8P',dP'        Yb
                   ,88888888888P"Y8P'_.---.._     _..---._`Y8P"Y88888888888,
                   dP         d'  8 '  ____  `. .'  ____  ` 8  `b         Yb
                  ,888888888888   8   <(@@)>  | |  <(@@)>   8   888888888888,
                  dP          8   8    `"""         """'    8   8          Yb
                 ,8888888888888,  8          ,   ,          8  ,8888888888888,
                 dP           `b  8,        (.-_-.)        ,8  d'           Yb
                ,88888888888888Yaa8b      .'       `.      d8aaP88888888888888,
                dP               ""8b     _,gd888bg,_     d8""               Yb
               ,888888888888888888888b,    ""Y888P""    ,d888888888888888888888,
               dP                   "8"b,             ,d"8"                   Yb
              ,888888888888888888888888,"Ya,_,ggg,_,aP",888888888888888888888888,
              dP                      "8,  "8"\\w/"8"  ,8"                      Yb
             ,88888888888888888888888888b   8\\\w//8   d88888888888888888888888888,
             8888bgg,_                  8   8\\\w//8   8                  _,ggd8888
              `"Yb, ""8888888888888888888   Y\\\w//P   8888888888888888888"" ,dP"'
                _d8bg,_"8,              8   `b\\w/d'   8              ,8"_,gd8b_
              ,iP"   "Yb,8888888888888888    8\\w/8    8888888888888888,dP"  `"Yi,
             ,P"    __,888              8    8\\w/8    8              888,__    "Y,
            ,8baaad8P"":Y8888888888888888 aaa8\\w/8aaa 8888888888888888P:""Y8baaad8,
            dP"':::::::::8              8 8::8\\w/8::8 8              8:::::::::`"Yb
            8::::::::::::8888888888888888 8::88888::8 8888888888888888::::::::::::8
            8::::::::::::8,             8 8:::::::::8 8             ,8::::::::::::8
            8:::::::::::::Ya            8 8:::::::::8 8            aP:::::::::::::8
            Ya:::::::::::::88888888888888 8:::::::::8 88888888888888:::::::::::::aP
            `8;:::::::::::::Ya,         8 8:::::::::8 8         ,aP:::::::::::::;8'
             Ya:::::::::::::::"Y888888888 8:::::::::8 888888888P":::::::::::::::aP
             `8;::::::::::::::::::::""""Y8888888888888P""""::::::::::::::::::::;8'
              Ya:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::aP

                    Congratulations brave adventurer! You have retrieved all
                    the missing pieces of the Lost Amulet! Go forth explore the
                    Lost Temple of Anubis!

            """

            self.application.output().success(message)

        else:
            message = """
                _.---._\n             .\'       `.\n             :)       (:\n             \\ (@) (@) /\n              \A   /\n               )     (\n               \\\"\"\"\"\"/\n                `._.\'\n                \n         .---._.-.=.-._.---.\n        / \':-(_.-: :-._)-:` \\\n       / /\' (__.-: :-.__) `\\ \\\n    /  (___.-` \'-.___)  \\ \\\n     / /   (___.-\'^`-.___)   \\ \\\n    / /    (___.-\'=`-.___)    \\ \\\n /     (____.\'=`.____)     \\ \\\n  / /       (___.\'=`.___)       \\ \\\n (_.;       `---\'.=.`---\'    ._)\n ;||        __  _.=._  __        ||;\n ;||       (  `.-.=.-.\'  )       ||;\n ;||       \\    `.=.\'/       ||;


        Better luck next time!
                           
            """
            self.application.output().error(message)

        quit()

        return
