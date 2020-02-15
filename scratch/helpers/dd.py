# dd() is my python equivilant
# of Laravel/symfony's dd()
# it takes a variable number of 
# items, prints them to the console
# then kills the script

def dd(*payloads):
    
    for payload in list(payloads):
        print(payload)
    quit()