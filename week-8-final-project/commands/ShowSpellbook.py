import random
from app.Spellbook import SpellBook


class ShowSpellbook:

    signature = "read:spellbook"

    description = "Read up and study your spellbook"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.clearConsole()

        SpellBook(self.application).read()
