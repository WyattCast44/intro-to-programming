from .Tile import Tile


class Start(Tile):

    def __init__(self):

        super().__init__(0, 0)

    def message(self):

        return "You have started..."
