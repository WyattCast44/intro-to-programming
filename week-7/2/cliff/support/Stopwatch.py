from time import time


class Stopwatch:

    start = None

    end = None

    def __init__(self):

        self.start = time()
        self.marks = {}

    def mark(self, event, context=None):

        timestamp = time()

        self.marks[timestamp] = {
            'event': event,
            'context': context,
        }

        return self

    def dump(self):

        return self.marks

    def __del__(self):

        self.end = time()
