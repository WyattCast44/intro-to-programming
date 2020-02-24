class ReportChooser:

    signature = 'reports:choose'

    description = 'Allows you to choose a report to view.'

    def __init__(self, application):
        self.application = application

    def handle(self):

        options = {
            'm': 'Enter `m` for the machines report',
            'i': 'Enter `i` for the inventory report',
        }

        choice = self.application.input().askWithOptions(
            'Please choose which report you would like to view:', options)

        # choice = self.application.input().ask(
        #     'Which you like to view the (m)achine report or the (i)nventory report?')

        while not choice in options:

            choice = self.application.input().askWithOptions(
                'Please choose which report you would like to view:', options)

        print('\n')
