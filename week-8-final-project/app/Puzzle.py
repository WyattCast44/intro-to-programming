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

            if index in self.openedSlots:
                # Slot opened
                gridDisplay.replace(f'G{index}', '  ', 1)
            else:
                # Slot not opened
                gridDisplay = gridDisplay.replace(f'G{index}', '??', 1)

        print(gridDisplay)

    def askWhichSlotToOpen(self):

        self.showGrid()

        row = self.application.input().askWithOptions('Select a row to open a slot:', [
            'R1',
            'R2',
            'R3',
            'R4'
        ])

        self.showGrid()

        column = self.application.input().askWithOptions('Select a column in the row to open:', [
            'C1',
            'C2',
            'C3',
            'C4'
        ])

        self.openSlot(row, column)

        return

    def openSlot(self, row, column):

        slotNumber = self.convertRowAndColumnToGridNumber(row, column)

        # Ensure a slot isnt opened more than once
        if slotNumber in self.openedSlots:

            self.application.output().error('\nYou have already opened that slot! Try again.')

            return

        # Mark that slot as opened
        self.openedSlots.append(slotNumber)

        # Convert selections to index accessible in the grid
        rowIndex = self.convertRowSelectionToRowIndex(row)
        columnIndex = self.convertColumnSelectionToColumnIndex(column)

        # Active the item in the slot
        print(f'opening {row}, {column}')

        contents = self.grid[rowIndex][columnIndex]

        print(contents)

        return

    def convertRowAndColumnToGridNumber(self, row, column):

        base = 0

        if row == "R1":
            base = 0
        elif row == "R2":
            base = 4
        elif row == "R3":
            base = 8
        elif row == "R4":
            base = 12

        if column == "C1":
            gridNumber = base
        elif column == "C2":
            gridNumber = base + 1
        elif column == "C3":
            gridNumber = base + 2
        elif column == "C4":
            gridNumber = base + 3

        return gridNumber

    def convertRowSelectionToRowIndex(self, row):

        if row == "R1":
            index = 0
        elif row == "R2":
            index = 1
        elif row == "R3":
            index = 2
        elif row == "R4":
            index = 3

        return index

    def convertColumnSelectionToColumnIndex(self, column):

        if column == "C1":
            index = 0
        elif column == "C2":
            index = 1
        elif column == "C3":
            index = 2
        elif column == "C4":
            index = 3

        return index
