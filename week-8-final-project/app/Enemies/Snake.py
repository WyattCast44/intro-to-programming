from .Enemy import Enemy


class Snake(Enemy):

    def __init__(self, application):

        super().__init__(name="Giant Snake", healthPoints=15,
                         attackPoints=30, application=application)

        return

    def activate(self):

        self.application.clearConsole()

        message = """

        You opened the slot and a seemingly never-ending Snake comes slithering out!!

        """

        art = """

                        /^\\/^\\
                _|__|  O|
        \\/     /~     \\_/ \\
        \____|__________/  \\
                \\_______      \\
                        `\\     \\                 \\
                        |     |                  \\
                        /      /                    \\
                        /     /                       \\
                    /      /                         \\ \\
                    /     /                            \\  \\
                /     /             _----_            \\   \\
                /     /           _-~      ~-_         |   |
                (      (        _-~    _--_    ~-_     _/   |
                \      ~-____-~    _-~    ~-_    ~-_-~    /
                    ~-_           _-~          ~-_       _-~
                    ~--______-~                ~-___-~
    
        """

        self.application.output().typed(message, 0.05, 'red')

        self.application.output().line(art)

        self.application.output().typed('It attacks you!!', 0.05, 'red')

        player = self.application.state().get('player')

        player.subtractHealth(self.attackPoints)

        healthPts = player.getHealth()

        self.application.output().typed(
            f'\nYour health has dropped to {healthPts}%!', 0.05, 'red')

        return
