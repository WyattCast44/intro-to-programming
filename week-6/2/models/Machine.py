import json


class Machine:

    attributes = {}

    source, rawContents, jsonContents = None, None, None

    def fromSource(self, path):
        self.source = path

        self.loadSource().parseContents()

        return self

    def loadSource(self):
        # Read the file into memory
        self.rawContents = open(self.source, 'r').read()

        return self

    def parseContents(self):

        # Get the raw json
        self.jsonContents = json.loads(self.rawContents)

        # Grab the id
        self.attributes['id'] = self.jsonContents['machine_id']

        # Grab the name
        self.attributes['name'] = self.jsonContents['machine_label']

        # Grab the content
        self.attributes['contents'] = self.jsonContents['contents']

        return self

    def __del__(self):

        print(self.attributes["id"], self.attributes["name"])
