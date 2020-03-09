from .Enemy import Enemy


class Spirit(Enemy):

    def __init__(self, application):

        super().__init__(name="Evil Spirit", healthPoints=5,
                         attackPoints=30, application=application)

        return

    def activate(self):

        self.application.clearConsole()

        self.application.output().typed(
            'You opened the slot and a Evil Spirit comes rushing out!!', 0.065, 'red')

        return
