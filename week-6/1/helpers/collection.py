class Collection:
    items = []

    def __init__(self, items=[]):
        self.items = items

        return

    def unique(self):

        unique = set()

        repeats = []

        for item in self.items:
            if item in unique:
                # Item already seen
                repeats.append(item)
            else:
                # First time seeing item
                unique.add(item)

        return (len(repeats) == 0)


def collect(items=[]):
    col = Collection(items)
    return col
