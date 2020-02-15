import json

class Machine:

    sourcePath = None

    rawContents = None

    jsonContents = None

    attributes = {}

    def fromSource(self, path):
        self.sourcePath = path

        self.loadSource()

        return self

    def loadSource(self):

        self.rawContents = open(self.sourcePath, 'r').read() 

        self.jsonContents = json.loads(self.rawContents)

        self.attributes['id'] = self.jsonContents['machine_id']

        self.attributes['name'] = self.jsonContents['machine_label']

        return self

    def get(self, key):
        return self.attributes[key]

    def dump(self):

        print(self.attributes)

        return self

# class MachineRow:
#     pass

# class RowSlot:
#     pass

# class MachineStatus:
#     pass

# Machine('source-file').id
# Machine('source-file').name
# Machine('source-file').slots
# Machine('source-file').slotsCount
# Machine('source-file').items
# Machine('source-file').itemsCount

"""
A machine has 
- rows
- slots
- items
"""