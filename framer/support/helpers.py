def tap(payload):

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