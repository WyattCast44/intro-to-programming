class ShowCredits:

    signature = "credits"

    description = "Show the game credits"

    creditsText = """

            STAR WARS
            ORDER 66

    Battles rage across known space.
    The Galactic Republic is crumbling
    under the continuous attacks by
    the Separatist droid army.

    The Jedi council is in turmoil.
    The Dark side has clouded a 
    plot to destroy the Jedi.

    In his hunt for the evil General 
    Grevious, General Kenobi and the
    501st Legion find themselves on 
    the bare planet of Utapau.

    Commander Cody of the 501st has 
    found himself facing his own 
    battle within the war...

    """

    def __init__(self, application):
        self.application = application
        return

    def handle(self):
        self.application.clearConsole()
        self.application.output().typed(self.creditsText, 0.06)
