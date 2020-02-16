from .Repository import Repository


class HasState:

    store = None

    def __init__(self):
        self.store = Repository()

    def state(self):
        return self.store
