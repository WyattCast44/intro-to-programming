from .Repository import Repository


class HasState:

    store = None

    def __init__(self):
        super(HasState, self).__init__()

        self.store = Repository()

        return

    def state(self):
        return self.store
