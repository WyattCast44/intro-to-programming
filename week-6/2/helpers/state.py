class State:

    state = {}

    def __init__(self):
        return

    # set() allows you to set a value in
    # the state, if the key already exists
    # an error is raised
    def set(self, key, value):

        # Dont overide state    
        if self.has(key):
            print('error')

            return self
        
        # Set the state
        self.state[key] = value

        return self

    # update() allows you to update a value
    # already in the state, if the key does not
    # exists an error is raised
    def update(self, key, value):

        if not self.has(key):
            print('error')

        self.state[key] = value

    # upsert() allows you to provide a key
    # and value, if the key is already defined
    # in the state, it will be updated, if 
    # it doesn't, it will be set
    def upsert(self, key, value):

        if self.has(key):
            self.update(key, value)
        else:
            self.set(key, value)

        return self

    # has() allows to check if a key is 
    # set in the state
    def has(self, key):

        return (key in self.state)

    # get() allows you to get the value of 
    # a key set in the state, or if no key
    # is provided, then the entire state 
    # is returned
    def get(self, key = None, defaultValue = None):
        
        if key == None:
            return self.state

        if self.has(key):
            return self.state[key]

        return defaultValue