class DrawShapeFile:

    signature = "draw:shapefile"

    description = "Allows you to specify a shape file and we will draw the shapes in that file"

    def __init__(self, application):
        self.application = application
        return

    def handle(self):

        self.filename = self.application.input().ask(
            'What shapefile would you like to use?')
