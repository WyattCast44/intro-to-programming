class AmuletPiece:

    def __init__(self, application):
        self.application = application

        return

    def activate(self):

        message = """
            Success! You have found another piece of the Lost Amulet!
        """

        art = """

                                      /^\\
                   L L               /   \\               L L
                __/|/|_             /  .  \\             _|\\|\\__
               /_| [_[_\\           /     .-\\           /_]_] |_\\
              /__\\  __`-\\_____    /    .    \\    _____/-`__  /__\\
             /___] /=@>  _   {>  /-.         \\  <}   _  <@=\\ [___\\
            /____/     /` `--/  /      .      \\  \--` `\     \\____\\
           /____/  \\____/`-._> /               \\ <_.-`\____/ \\____\\
          /____/    /__/      /-._     .   _.-  \\      \__\    \\____\\
         /____/    /__/      /         .         \\      \__\    \\____\\
        |____/_  _/__/      /          .          \\      \__\_  _\\____|
         \__/_ ``_|_/      /      -._  .        _.-\\      \_|_`` _\\___/
           /__`-`__\      <_         `-;           _>      /__`-`__\\
              `-`           `-._       ;       _.-`           `-`
                                `-._   ;   _.-`
                                    `-._.-`

        """

        self.application.output().typed(message, 0.065, 'green')

        self.application.output().line(art)

        player = self.application.state().get('player')

        player.addAmuletPart()

        count = player.getAmuletCount()

        self.application.output().typed(
            f'You have collected {count} Amulet pieces so far!', 0.05, 'green')

        return
