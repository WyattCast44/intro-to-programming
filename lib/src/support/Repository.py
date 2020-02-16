class Repository:

    store = {}

    def __init__(self):
        return

    # set() allows you to set a value in
    # the store, if the key already exists
    # an error is raised
    def set(self, key, value):

        # Dont overide store    
        if self.has(key):
            print('error')

            return self
        
        # Set the store
        self.store[key] = value

        return self

    # update() allows you to update a value
    # already in the store, if the key does not
    # exists an error is raised
    def update(self, key, value):

        if not self.has(key):
            print('error')

        self.store[key] = value

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

        return (key in self.store)

    # get() allows you to get the value of 
    # a key set in the store, or if no key
    # is provided, then the entire store 
    # is returned
    def get(self, key = None, defaultValue = None):

        if key == None:
            return self.store

        if '.' in key:
            keys = key.split('.')
            return self.store[keys[0]][keys[1]]

        if self.has(key):
            return self.store[key]

        return defaultValue

    def append(self, key, subkey, value):

        # Create the key if it doesn't exist
        if not self.has(key):
            self.set(key, {})
        
        current = self.get(key)

        current[subkey] = value

        self.update(key, current)

        return self
        