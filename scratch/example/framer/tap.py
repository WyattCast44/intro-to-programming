def tap(payload):
    # tap() is used to return an instance of a class via
    # a class name, instance, or function. 
    # This object then can have method called on it 
    # w/o the need for a temporary variable 
    
    # Class reference
    if type(payload) == type:

        # Init the class
        tmp = payload()

        return tmp

    # Function
    if callable(payload):

        # Call the function and get return value
        returned = payload()

        # Return value is class reference
        if type(returned) == type:

            # Init the class
            tmp = returned()

            return tmp

        # Return value is an object
        return returned

    # Payload is object, return it
    return payload