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

        jsonContents = json.loads(open(self.source, 'r').read())

        self.atts['json'] = jsonContents

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
    # Items
    ###
    def getUniqueItems(self):

        items = []

        for slot in self.getSlots():

            name = slot['item_name']

            if not name in items:

                items.append(name)

        return items

    def getItemInStockCount(self, itemName):

        stock = 0

        for slot in self.getSlots():

            if itemName == slot['item_name']:

                stock = stock + slot['current_stock']

        return stock

    def getItemLastStockCount(self, itemName):

        stock = 0

        for slot in self.getSlots():

            if itemName == slot['item_name']:

                stock = stock + slot['last_stock']

        return stock

    def getItemTotalCapacity(self, itemName):

        capacity = 0

        for slot in self.getSlots():

            if itemName == slot['item_name']:

                capacity = capacity + self.MAX_ITEMS_PER_SLOT

        return capacity

    def containsItem(self, itemName):

        status = False

        for slot in self.getSlots():

            if itemName == slot['item_name']:

                status = True

        return status

    ###
    # Analysis
    ###
    def getPercentSold(self):

        totalCapacity = self.getTotalCapacity()

        inStockCount = 0

        for slot in self.getSlots():

            inStockCount = inStockCount + slot['current_stock']

        return round((inStockCount/totalCapacity * 100), 2)

    def getTotalSales(self):

        total = 0

        for slot in self.getSlots():

            numberSoldInSlot = slot['last_stock'] - slot['current_stock']

            total = total + (numberSoldInSlot * slot['item_price'])

        return round(total, 2)
