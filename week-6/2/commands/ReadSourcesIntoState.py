import json
from os import path
from models import *

class ReadSourcesIntoState:
    
    signature = 'load:machines
    '

    description = 'Read the data sources into app state'

    def __init__(self, application):
        self.application = application

    def handle(self):

        machines = []

        # For each source, parse the json 
        for filePath in self.application.state().get('sources'):

            machine = Machine().fromSource(filePath)

            machines.append(machine)
        
        self.application.state().set('machines', machines)