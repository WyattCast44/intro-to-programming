from .ReadSourcesIntoState import ReadSourcesIntoState


class PrintMachinesList:

    signature = 'print:machines-list'

    description = 'Print a list of all your machines and thier information'

    def __init__(self, application):
        self.application = application

    def handle(self):

        s = ReadSourcesIntoState(self.application).handle()

        self.application.output().error('\nTODO\n')
