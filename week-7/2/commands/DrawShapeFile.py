class DrawShapeFile:

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
