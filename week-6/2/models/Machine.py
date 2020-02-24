import json


class Machine:

    MAX_ITEMS_PER_SLOT = 8

    def __init__(self):
        self.atts = {}

    def fromSource(self, path):

        self.source = path

        self.parseContents()

        return self

    def parseContents(self):

        fileObj = open(self.source, 'r')

        jsonContents = json.loads(fileObj.read())

        fileObj.close()

        # Grab the id
        self.atts['id'] = jsonContents['machine_id']

        # Grab the name
        self.atts['name'] = jsonContents['machine_label']

        # Grab the content
        self.atts['contents'] = jsonContents['contents']

        # Grab the rows
        rows = []

        for row in self.atts['contents']:

            rows.append(row)

        self.atts['rows'] = rows

        slots = []

        for row in rows:

            for slot in row['slots']:

                slots.append(slot)

        self.atts['slots'] = slots

        return self

    ###
    # Machine Details
    ###
    def getId(self):

        return self.atts['id']

    def getName(self):

        return self.atts['name']

    def getTotalCapacity(self):

        return self.getSlotsCount() * self.MAX_ITEMS_PER_SLOT

    ###
    # Contents
    ##
    def getContents(self):

        return self.atts['contents']

    ###
    # Rows
    ###
    def getRows(self):

        return self.atts['rows']

    def getRowsCount(self):

        return len(self.atts['rows'])

    ###
    # Slots
    ###
    def getSlots(self):

        return self.atts['slots']

    def getSlotsCount(self):

        return len(self.atts['slots'])

    ###
    # Analysis
    ###
    def getPercentSold(self):

        totalCapacity = self.getTotalCapacity()

        inStockCount = 0

        for slot in self.getSlots():

            inStockCount = inStockCount + slot['current_stock']

        return inStockCount

    def getTotalSales(self):
        return
