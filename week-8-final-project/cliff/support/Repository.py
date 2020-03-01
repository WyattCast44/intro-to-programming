import functools


class Repository:

    store = None

    def __init__(self):

        self.store = {}

        return

    # set() allows you to set a value in
    # the store, if the key already exists
    # an error is raised
    def set(self, key, value, override=False):

        # Dont overide store
        if self.has(key) and not override:
            raise Exception(
                f"Attempted to set a value already set in state. Key: {key}")
            return self

        # Set the store
        self.store[key] = value

        return self

    # update() allows you to update a value
    # already in the store, if the key does not
    # exists an error is raised
    def update(self, key, value):

        if not self.has(key):
            raise Exception(
                f"Attempted to update a value not set in state. Key: {key}")
            return self

        if '.' in key:
            # TODO: implement
            raise Exception('TODO: Make work')
        else:
            self.store[key] = value

        return self

    # upsert() allows you to provide a key
    # and value, if the key is already defined
    # in the store, it will be updated, if
    # it doesn't, it will be set
    def upsert(self, key, value):

        if self.has(key):
            self.update(key, value)
        else:
            self.set(key, value)

        return self

    # has() allows to check if a key is
    # set in the store
    def has(self, key):

        if "." in key:

            keys = key.split('.')

            value = functools.reduce(lambda d, key: d.get(
                key) if d else None, keys, self.store)

            return (value != None)

        else:
            return (key in self.store)

    # get() allows you to get the value of
    # a key set in the store, or if no key
    # is provided, then the entire store
    # is returned
    def get(self, key=None, defaultValue=None):

        if key == None:
            return self.store

        if not self.has(key):
            return defaultValue

        if '.' in key:
            return functools.reduce(lambda d, key: d.get(
                key) if d else None, key.split('.'), self.store)
        else:
            return self.store[key]

    def append(self, key, subkey, value):

        # Create the key if it doesn't exist
        if not self.has(key):
            self.set(key, {})

        current = self.get(key)

        current[subkey] = value

        self.update(key, current)

        return self
