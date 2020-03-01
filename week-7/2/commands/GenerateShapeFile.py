from cliff.filesystem import Filesystem
from src.ShapeGenerator import ShapeGenerator


class GenerateShapeFile:

    signature = "make:shapefile"

    description = "Allows you to generate a shapefile with given name and number of shapes"

    def __init__(self, application):
        self.application = application
        return

    def ensureFileExists(self):

        Filesystem.ensureFileExists(self.filename)

        return self

    def generateShapes(self):

        lines = []
        current = 1

        while current <= self.shapeCount:

            shape = ShapeGenerator().random()

            lines.append(shape)

            current = current + 1

        self.shapes = lines

        return self

    def handle(self):

        self.filename = self.application.input().ask(
            'What would you like the shape file to be named?')

        self.shapeCount = int(self.application.input().ask(
            'How many shapes shoud we generate?'))

        self.ensureFileExists().generateShapes()

        Filesystem.writeLines(self.filename, self.shapes)

        self.application.output().success('\nShape file created successfully!')

        status = self.application.input().askWithOptions(
            'Would you like to run the `draw:shapefile` command now?', {
                'y': 'Enter `y` to run the command',
                'n': 'Or `n` to quit'
            })

        if status == 'y':
            self.application.runCommand('draw:shapefile')
        else:
            return
