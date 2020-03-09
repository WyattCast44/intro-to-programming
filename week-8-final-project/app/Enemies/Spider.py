from .Enemy import Enemy


class Spider(Enemy):

    def __init__(self, application):

        super().__init__(name="Massive Spider", healthPoints=5,
                         attackPoints=20, application=application)

        return

    def activate(self):

        self.application.clearConsole()

        self.application.output().typed(
            'You opened the slot and a Massive Spider rears it\'s eight eyed head!!', 0.065, 'red')

        return
