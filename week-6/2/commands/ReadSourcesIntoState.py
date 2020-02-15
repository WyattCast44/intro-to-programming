import json
from os import path

class ReadSourcesIntoState:
    
    signature = 'sources:read'

    description = 'Read the data sources into app state'

    def __init__(self, application):
        self.application = application

    def handle(self):

        data = []

        # For each source, parse the json 
        for filePath in self.application.state().get('sources'):
            data.append(json.loads(open(filePath, 'r').read()))

        # Put all the parsed json blobs into app state
        self.application.state().set('data', data)