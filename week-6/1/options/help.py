class Help:

    signature = '--h'

    description = 'Display the application help screen'

    def __init__(self, application):
        self.application = application

    def handle(self):

        message = """
    This program will ask you to input a list of
    items, and when you are finished entering items, 
    it will check the list and see if it contains 
    only unique items. If there is any repeated items
    it will tell you the list is not unique.
        """

        self.application.console().line(message)
