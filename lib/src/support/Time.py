import time

class Time:

    timestamp = None

    def __init__(self):
        self.timestamp = time.time()

    @staticmethod
    def now():
        return time.time()

    def make(self, timestamp):
        self.timestamp = timestamp

        return self