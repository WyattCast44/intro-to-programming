
class StartNewGame:

    signature = "new:game"

    description = "Start a new game"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.clearConsole()

        self.printFirstParagraph()

    def printFirstParagraph(self):

        from app.Spellbook import Spellbook

        Spellbook(self.application).read()
