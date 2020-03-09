from .Enemy import Enemy


class Spider(Enemy):

    def __init__(self, application):

        super().__init__(name="Massive Spider", healthPoints=5,
                         attackPoints=25, application=application)

        return

    def activate(self):

        message = "You opened the slot and a Massive Spider rears it\'s eight eyed head!!"

        art = """

            (\n               )\n              (\n        /\\  .-\"\"\"-.  /\\\n       //\\\\/  ,,,  \\//\\\\\n       |/\\| ,;;;;   |/\\|\n       //\\\\\\;-\"\"\"-;///\\\\\n      //  \\/   .   \\/  \\\\\n     (| ,-_| \\ | / |_-, |)\n       //`__\\.-  /__`\\\\\n      // /.-(() ())-.\\ \\\\\n     (\\ |)   \'---\'   (| /)\n      ` (|           |) `\n        \\)         (/

        """

        self.application.clearConsole()

        self.application.output().typed(message, 0.05, 'red')

        self.application.output().line(art)

        self.application.output().typed('It attacks you!!', 0.05, 'red')

        player = self.application.state().get('player')

        player.subtractHealth(self.attackPoints)

        healthPts = player.getHealth()

        self.application.output().typed(
            f'\nYour health has dropped to {healthPts}%!', 0.05, 'red')

        return
