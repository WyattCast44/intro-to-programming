from .Enemy import Enemy


class Spirit(Enemy):

    def __init__(self, application):

        super().__init__(name="Evil Spirit", healthPoints=5,
                         attackPoints=5, application=application)

        return

    def activate(self):

        self.application.clearConsole()

        message = """
            You opened the slot and a Evil Spirit comes rushing out!! 
        """

        self.application.output().typed(message, 0.065, 'red')

        art = """
            _.--\"\"-._\n  .                  .\"         \".\n / \\    ,^.         /(     Y             |      )\\\n/   `---. |--\'\\    (  \\__..\'--   -   -- -\'\"\"-.-\'  )\n|        :|    `>   \'.     l_..-------.._l      .\'\n|      __l;__ .\'      \"-.__.||_.-\'v\'-._||`\"----\"\n \\  .-\' | |  `              l._       _.\'\n  \\/    | |                   l`^^\'^^\'j\n        | |                _   \\_____/     _\n        j |               l `--__)-\'(__.--\' |\n        | |               | /`---``-----\'\"1 |  ,-----.\n        | |               )/  `--\' \'---\'   \\\'-\'  ___  `-.\n        | |              //  `-\'  \'`----\'  /  ,-\'   I`.  \\\n      _ L |_            //  `-.-.\'`-----\' /  /  |   |  `. \\\n     \'._\' / \\         _/(   `/   )- ---\' ;  /__.J   L.__.\\ :\n      `._;/7(-.......\'  /        ) (     |  |            | |\n      `._;l _\'--------_/        )-\'/     :  |___.    _._./ ;\n        | |                 .__ )-\'\\  __  \\  \\  I   1   / /\n        `-\'                /   `-\\-(-\'   \\ \\  `.|   | ,\' /\n                           \\__  `-\'    __/  `-. `---\'\',-\'
        """

        self.application.output().line(art)

        message = """
            "LEAVE NOW IF YOU WANT TO LIVE!!"
        """

        self.application.output().typed(message, 0.065, 'red')

        return
