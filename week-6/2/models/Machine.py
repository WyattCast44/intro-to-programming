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

        # Set the initial row count
        self.attributes['rowCount'] = 0

        for row in self.attributes['contents']:

            self.incrementRowCount()

            for slot in row['slots']:
                # each row has 9 slots
                p = 1

        # Need to parse the rows
        # in the rows, need to parse the slots
        # in the slots, need to parse the
        # - item name
        # - last stock
        # - current stock
        # Machine need to know how many slots it has

        return self

    def incrementRowCount(self):

        self.attributes['rowCount'] = self.attributes['rowCount'] + 1

    # def __del__(self):

    #     print(self.attributes["id"], self.attributes["name"])
