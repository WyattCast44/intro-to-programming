import random
from app.Items import AmuletPiece
from app.Enemies import Snake, Spider, Spirit


class Puzzle:

    items = [
        Snake,
        Spirit,
        Spider,
        AmuletPiece,
        AmuletPiece
    ]

    def __init__(self, game, application):

        self.game = game
        self.openedSlots = []
        self.application = application

        # Define a 4 row grid
        # Each row has 4 columns
        # Each slot can hold a enemy
        # or a amulet piece

        self.grid = [
            [[random.choice(self.items)], [random.choice(self.items)], [
                random.choice(self.items)], [random.choice(self.items)]],  # row 1
            [[random.choice(self.items)], [random.choice(self.items)], [
                random.choice(self.items)], [random.choice(self.items)]],  # row 2
            [[random.choice(self.items)], [random.choice(self.items)], [
                random.choice(self.items)], [random.choice(self.items)]],  # row 3
            [[random.choice(self.items)], [random.choice(self.items)], [
                random.choice(self.items)], [random.choice(self.items)]],  # row 4
        ]

        return

    def showGrid(self):

        gridDisplay = """

        ╔════╤════╤════╤════╤════╗
        ║    │ C1 │ C2 │ C3 │ C4 ║
        ╠════╪════╪════╪════╪════╣
        ║ R1 │ G0 │ G1 │ G2 │ G3 ║
        ╟────┼────┼────┼────┼────╢
        ║ R2 │ G4 │ G5 │ G6 │ G7 ║
        ╟────┼────┼────┼────┼────╢
        ║ R3 │ G8 │ G9 │ G10 │ G11 ║
        ╟────┼────┼────┼────┼────╢
        ║ R4 │ G12 │ G13 │ G14 │ G15 ║
        ╚════╧════╧════╧════╧════╝

        """

        for index in range(16):

            if index in self.application.state().get('opened_slots'):
                # Slot opened
                gridDisplay.replace(f'G{index}', '  ', 1)
            else:
                # Slot not opened
                gridDisplay = gridDisplay.replace(f'G{index}', '??', 1)

        print(gridDisplay)

    def openSlot(self, slotNumber):

        self.openedSlots.append(slotNumber)

        # TODO OPEN THE SLOT AND RUN ITEM IN IT

        return
